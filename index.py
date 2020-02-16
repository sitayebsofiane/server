#coding:utf-8
import cgi
import http.cookies
import datetime
import os
import sys,codecs
#gestion encodage
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a,%d-%b-%Y %H:%M:%S")
my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["expires"] = True

 
print(my_cookie.output())
print("Content-type: text/html; charset=utf-8\n")

var="str"
html_head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style> 
            p{
            background-color: rgb(8, 184, 52);;
                }
    </style>
    <title>Page test python html</title>
</head>"""
html_body = """
<body>
    <h1>hello tout le monde</h1>
    <h2>si voulez gerer les conference taper <a href="conferences.py">ici</a></h2>
    <h2>si voulez gerer les conferencier taper <a href="speakers.py">ici</a><h2p>
"""
html_footer = """
</body>
</html>

"""
print(my_cookie["pref_lang"])
