from Crypto.Cipher import AES
from datetime import datetime
import lzstring
import requests
import hashlib
import base64
import hmac
import json

def decrypt_data(keys, encrypts):
    decompress = None

    if encrypts != None:
        x = lzstring.LZString()
        key_hash = hashlib.sha256(keys.encode('utf-8')).digest()

        decryptor = AES.new(key_hash[0:32], AES.MODE_CBC, IV=key_hash[0:16])
        plain = decryptor.decrypt(base64.b64decode(encrypts))
        decompress = json.loads(x.decompressFromEncodedURIComponent(plain.decode('utf-8')))
        
    return decompress

def check_json(str_json):
    try:
        json_object = json.loads(str_json)

    except ValueError as e:
        return False
        
    return True

def fixed_url(url):
    if url.startswith('/') == True:
        return url[1:]

    if url.endswith('/') == True:
        return url[:-1]

    else:
        return url

def rest_bpjs(consid, secret, user_key, url, method, payload, timestamp):
    message = consid+"&"+timestamp
    signature = hmac.new(bytes(secret,'UTF-8'),bytes(message,'UTF-8'), hashlib.sha256).digest()
    encodeSignature = base64.b64encode(signature)

    headers = {'X-cons-id': consid, 'X-timestamp': timestamp, 'X-signature': encodeSignature.decode('UTF-8'), 'user_key': user_key, 'Content-Type': 'Application/x-www-form-urlencoded','Accept': '*/*'}

    if payload == '' or payload == None:
        payload = 0
    else:
        payload = json.dumps(payload)

    try:
        if method.lower() == 'post':
            if payload == 0:
                res = requests.post(url, headers=headers)
            else:
                res = requests.post(url, data=payload, headers=headers)

        elif method.lower() == 'put':
            if payload == 0:
                res = requests.put(url, headers=headers)
            else:
                res = requests.put(url, data=payload, headers=headers)
        elif method.lower() == 'delete':
            if payload == 0:
                res = requests.delete(url, headers=headers)
            else:
                res = requests.delete(url, data=payload, headers=headers)
        else:
            if payload == 0:
                res = requests.get(url, headers=headers)
            else:
                res = requests.get(url, data=payload, headers=headers)

    except:
        res = {
            'metaData': {
                'code': "400",
                'message': "Ada kesalahan request data, cek kembali",
            },
            'response': None
        }

    return res

def bridging(credential, endpoint, method = 'get', payload = {}):
    host = credential['host']
    consid = credential['consid']
    secret = credential['secret']
    user_key = credential['user_key']
    is_encrypt = credential['is_encrypt']

    url = fixed_url(host) + "/" + fixed_url(endpoint)
    timestamp = str(int(datetime.today().timestamp()))

    res = rest_bpjs(consid, secret, user_key, url, method, payload, timestamp)

    if not hasattr(res, 'status_code'):
        return res

    if res.status_code != 404:
        if check_json(res.text) == True:

            keys = consid + secret + timestamp
            res = res.json()

            metadata = 'metaData'
            if metadata not in res:
                metadata = 'metadata'

            code = 'code'
            if code not in res[metadata]:
                code = 'Code'

            if res[metadata][code] == 0:
                data = {
                    'metaData': {
                        'code': 400,
                        'message': res[metadata]['message'],
                    },
                    'response': None
                }

                return data

            if 'response' not in res:
                data = {
                    'metaData': {
                        'code': res[metadata][code],
                        'message': res[metadata]['message'],
                    },
                    'response': None
                }

                return data

            if int(is_encrypt) == 1:
                url_not_encrypt = ["SEP/2.0/delete", "SEP/2.0/update"]
                status_encrypt = True

                for unc in url_not_encrypt:
                    if unc in url:
                        status_encrypt = False

                if status_encrypt == True:
                    response = decrypt_data(keys, res['response'])

                else:
                    response = res['response']

            else:
                response = res['response']

            data = {
                'metaData': {
                    'code': res[metadata][code],
                    'message': res[metadata]['message'],
                },
                'response': response
            }

            status_code = res[metadata][code]

            if res[metadata][code] == 1:
                status_code = 200
                
            return data

        else:
            data = {
                'metaData': {
                    'code': res.status_code,
                    'message': res.text,
                },
                'response': None
            }

            return data

    else:
        data = {
            'metaData': {
                'code': 404,
                'message': "URL tidak ditemukan",
            },
            'response': None
        }

        return data