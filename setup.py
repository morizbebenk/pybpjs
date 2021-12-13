import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	name="pybpjs",
	version="0.0.3",
	author="Moriz",
	author_email="morizbebenk@gmail.com",
	description="Aplikasi Python yang digunakan untuk menangani proses dekripsi respon data dari bridging BPJS VCLAIM REST 2.0 (Encrypted Version). Support VCLAIM v1 dan API JKN (Antrean RS).",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/morizbebenk/pybpjs",
    project_urls={
        "Bug Tracker": "https://github.com/morizbebenk/pybpjs/issues",
    },
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    license="MIT",
    keywords="bpjs vclaim vclaim-rest vclaim-encrypted ",
    install_requires=["lzstring", "requests", "pycryptodome"]
)