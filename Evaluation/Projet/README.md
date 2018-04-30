Sujet 4 : Logic Immo

Equipe : TANON KOUADIO Astrid et HO Tay-Son

Pour cloner le projet : 

'git clone https://github.com/Taysonho/OUAP-4314.git'

## Set up requis pour le projet:

	Install Python
		`sudo apt-get install python`
		
	Install Flask 
		`pip install flask`
		
	Install MongoDB 
		`sudo apt-get install -y mongodb-org`
			
	Import bson pour manipuler ObjectId et Pymongo pour la connexion à la base de données
		`pip install bson`
		`pip install pymongo'
		

## Exécution :
		
	Run MongoDB
		`sudo service mongod start` pour linux
		'cd ~\MongoDB\Server\3.6\bin' sous windows
		'mongod'
	
	Run le fichier flask(mongo_flask.py)
		'cd ~\OUAP-4314\Evaluation\Projet'
		`python mongo_flask.py`
		
	Run Scrapy
		'cd ~\OUAP-4314\Evaluation\Projet\projetlogic'
		'scrapy crawl logic_immo -o logicimmo.json'	

	Ouvrir un navigateur avec l'adresse:
		`http://localhost:5000'
		





