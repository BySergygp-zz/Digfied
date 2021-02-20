from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = 'digfied' ,
    version = '0.0.1' ,
    descripcion = 'Certificados digitales' ,
    author = 'BySergygp' ,
    author_email = 'bysergygp@gmail.com' ,
    packages = ['digfied','test']
)