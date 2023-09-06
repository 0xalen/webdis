# WebDis

## DESCRIPTION
Web Disassembler is a simple application designed to connect to websites and extract some of their
key components, such as urls, src, files, etc. It aims to simplify the process of information gathering
during security risk assesments.

## DEPLOYMENT

### Docker
The app can be built as a Docker container using the following command:
`docker build -t webdis .`

Afterwards it can by ran with:
`docker run -p 8501:8501 webdis`

Run in the brackground:
`docker run --rm -ti -p 8501:8501 --name webdis-dev webdis`

It uses python 3.11 and it runs by default on port 8501.

### Standalon executable
The recommended way to run it is as a standalone executable, which can be generated using the
follogwing command:
`nuitka3 --standalone --onefile webdis.py`


