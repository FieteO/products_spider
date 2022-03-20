# Scrapy webspider

## Getting started
Install the python env using `pipenv`.
``` bash
pipenv install
```
Activate the environment.
``` bash
source .venv/bin/activate
```
Start scrapy splash (the javascript rendering engine)
``` bash
docker-compose up
```

## Goals
- save screenshots of the rendered page
- save the complete html source
- save the extracted text from the html source
- [stretch] save statistics for structure of DOM 