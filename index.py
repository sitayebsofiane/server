#coding:utf-8
import cgi,http.cookies
import datetime,time
import os,sys,codecs

"""gestion encodage"""
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a,%d-%b-%Y %H:%M:%S")
my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
#my_cookie["pref_lang"]["expires"] = True

 
print(my_cookie.output())
print("Content-type: text/html; charset=utf-8\n")
print("""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <style> 
            span{
            background-color:rgb(8, 184, 52);;
                }
    </style>
    <title>Page test python html</title>
</head><body>""")
#------------------------------------------work--------------------------------------------------
for i in range(1,50):
  
    print("<span>"+i*"*"+"</span><br>")
#-----------------------------------------end work-----------------------------------------------
print("""</body>
</html>""")
