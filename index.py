#coding:utf-8
import cgi
import datetime,time
import os,sys,codecs
#-----------------------------------------------------------
"""gestion encodage"""
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#-----------------------------------------------------------

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
form = cgi.FieldStorage()
if form.getvalue("nombre"):
    n=int(form.getvalue("nombre"))
else:
    n=2
for i in range(n+1):
    print("<span>"+i*"*"+"</span><br>")

print("""
    <form method="post">
 
        <fieldset>
            <legend>Ajouter un nombre de star</legend> 
     
            <label for="nombre">Quel est le nombre ?</label>
            <input type="number" name="nombre" id="nombre" />
        <input type="submit" value="Envoyer" />
        </fieldset>
   </form>""")
#-----------------------------------------end work-----------------------------------------------
print("""</body>
</html>""")
