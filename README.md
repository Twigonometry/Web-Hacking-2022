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

### Docker on Linux

```
$ sudo docker build -t web-hacking .
$ sudo docker run -p 5000:5000 webhacking
```

## Solutions

### XSS 1

This is a reflected XSS attack, but the trick is that only one of the URL parameters is vulnerable. While the web form only allows numbers to be inputted into the quantity field, anything can be inserted within the URL bar:

`/xss1?flavour=chocolate&quantity=%3Cscript%3Ealert(%27ello%27)%3C/script%3E`

### XSS 2

This is a stored XSS attack, as inputs are saved to the database. Just post a comment with the contents `<script>alert('xss')</script>`.

You should only be able to see your own comments :)

### SQL 1

Classic payload: simply login with `' OR 1=1;--` in the username field, and anything in the password field. This is a very simple SQL injection login bypass technique, but some systems may require slightly different syntax.

Unintended solution involved modifying the URL parameter `allowed` to say login was successful (`allowed=True`), which was also the solution to our Activity Fair challenge.

### SQL 2

`http://localhost:5000/sqli2/getuserdata?userid=71PEO4MZZ145ICYR%27%20OR%201=1;--`

Note: this challenge is also technically an IDOR, as if you know the admin's username (admin) you can view their profile:

`http://localhost:5000/sqli2/getuserdata?userid=admin`

### Cookies

Simply modify the value of the isAdmin cookie to `isAdmin=True` using your developer tools or another method such as the cookie editor browser plugin, then reload the page.
