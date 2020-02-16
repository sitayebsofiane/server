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

form = cgi.FieldStorage()
if form.getvalue("nom"):
    n=int(form.getvalue("nom"))
else:
    n=2
print(my_cookie.output())
print("Content-type: text/html; charset=utf-8\n")
print("""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <style> 
            body{
                background-color:rgb(0, 0, 0);
                color:rgb(8, 184, 52);
            }
           
    </style>
    <title>Page test python html</title>
</head><body>""")
#------------------------------------------work--------------------------------------------------
for i in range(n+1):
    print("<span>"+i*"*"+"</span><br>")
    
print("""
    <form method="post">
 
        <fieldset>
            <legend>Ajouter un nombre de star</legend> 
     
            <label for="nom">Quel est le nombre ?</label>
            <input type="number" name="nom" id="nom" />
        <input type="submit" value="Envoyer" />
        </fieldset>
   </form>""")
#-----------------------------------------end work-----------------------------------------------
print("""</body>
</html>""")
