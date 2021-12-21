## pybpjs

Aplikasi Python yang digunakan untuk menangani proses dekripsi respon data dari bridging BPJS VClaim v2.0 (Encrypted Version). Support VClaim v1 / v1.1 dan Antrean RS.

## Kebutuhan

**Utama**

- Python

**Package**

- lzstring
- requests
- pycryptodome 

## Virtual Environment

Bagian ini opsional tetapi sangat disarankan untuk membuat virtual environment supaya ketika ada update package yang tidak support / bermasalah tidak akan mengganggu aplikasi lain.

### Membuat Virtual Environment

```bash
python -m venv virtualenv
```

atau

```bash
python3 -m venv virtualenv
```

### Aktivasi Virtual Environment

- **Windows**

    ```bash
    virtualenv\Scripts\activate
    ```

- **Bash**

    ```bash
    source virtualenv/bin/activate
    ```

### Instalasi

```bash
pip install pybpjs
```

## Sumber Daya
- https://dvlp.bpjs-kesehatan.go.id:8888/trust-mark/portal.html

## Lisensi
- Aplikasi ini open source dengan lisensi [MIT](LICENSE).