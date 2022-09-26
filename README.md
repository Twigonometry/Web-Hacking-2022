# Web-Hacking-2022
Web Hacking demo for SESH, 2022 edition!

## Run

### Windows

```
PS > cd .\web\
PS > $env:FLASK_APP = "app"
PS > $env:FLASK_DEBUG = "true"
PS > python -m flask run
```

OR run app.py

## Solutions

### XSS 1

`/xss1?flavour=chocolate&quantity=%3Cscript%3Ealert(%27ello%27)%3C/script%3E`