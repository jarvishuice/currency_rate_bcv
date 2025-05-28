from setuptools import setup, find_packages

setup(
    name="currency_rate_bcv",                # Nombre del paquete
    version="0.1.0",                   # Versión inicial
    author="Jarvis Gabriel Huice Padron",
    author_email="jarvis.realg@gmail.com",
    description="Una breve descripción de tu librería",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tuusuario/mi_libreria ",  # Repo público
    packages=find_packages(),          # Encuentra automáticamente los paquetes
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)