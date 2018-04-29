from flask import Flask, render_template,request,redirect,url_for # Implémentation Flask
from pymongo import MongoClient # Pour la connexion à la base de données
from bson.objectid import ObjectId # Permet l'utilisation d'ObjectId

client = MongoClient('localhost', 27017)    #Configuration de la connexion à la base de données
db = client.ouap2018    #On choisit la database
posts = db.post #On choisit la collection

app = Flask(__name__)
title = "Annonces Flask"
heading = "Annonces Logic immo"

def redirect_url():
    return request.args.get('next') or \
           request.referrer or \
           url_for('index')

@app.route("/")
def lists ():
	#Affiche les annonces
	posts_l = posts.find()
	a1="active"
	return render_template('index.html',a1=a1,posts=posts_l,t=title,h=heading)


@app.route("/action", methods=['POST'])
def action ():
	#Poster une annonce
   url=request.values.get("url") 
   location=request.values.get("location") 
   name=request.values.get("name")
   desc=request.values.get("desc")
   typ=request.values.get("typ")
   pr=request.values.get("pr")
   posts.insert({"url":url, "location":location, "name":name, "desc":desc, "typ":typ, "pr":pr})
   return redirect("/")

@app.route("/remove")
def remove ():
	#Supprimer une annonce
	key=request.values.get("_id")
	posts.remove({"_id":ObjectId(key)})
	return redirect("/")

@app.route("/update")
def update ():
   #Modifier une annonce : redirige vers la page de modification
	id=request.values.get("_id")
	task=posts.find({"_id":ObjectId(id)})
	return render_template('update.html',tasks=task,h=heading,t=title)

@app.route("/action3", methods=['POST'])
def action3 ():
   #Modifier une annonce
   url=request.values.get("url") 
   location=request.values.get("location")
   name=request.values.get("name")
   desc=request.values.get("desc")
   typ=request.values.get("typ")
   pr=request.values.get("pr")
   id=request.values.get("_id")
   posts.update({"_id":ObjectId(id)}, {'$set':{ "url":url, "location":location, "name":name, "desc":desc, "typ":typ, "pr":pr }})
   return redirect("/")

@app.route("/search", methods=['GET'])
def search():
	#Rechercher une annonce : redirige vers la page de recherche

	key=request.values.get("key")
	refer=request.values.get("refer")
	if(key=="_id"):
		posts_l = posts.find({refer:ObjectId(key)})
	else:
		posts_l = posts.find({refer:key})
	return render_template('searchlist.html',posts=posts_l,t=title,h=heading)

@app.route("/about")
def about():
	return render_template('credits.html',t=title,h=heading)

if __name__ == "__main__":
    app.run(debug=True)
# Debug mode


