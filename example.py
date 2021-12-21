from pybpjs import bpjs

# Host BPJS 
# Host Development VClaim : https://apijkn-dev.bpjs-kesehatan.go.id/vclaim-rest-dev/
# Host Production VClaim : https://apijkn-dev.bpjs-kesehatan.go.id/vclaim-rest/
# Host Development API JKN : https://apijkn-dev.bpjs-kesehatan.go.id/antreanrs_dev/
# Host Production API JKN : -

credential = {
    "host": "https://apijkn-dev.bpjs-kesehatan.go.id/vclaim-rest-dev/",
    "consid": "",
    "secret": "",
    "user_key": "",
    "is_encrypt": "1"
}

endpoint = "referensi/poli/ana"
method = "get"
payload = ""

data = bpjs.bridging(credential, endpoint, method, payload)
print(data)