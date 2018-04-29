import requests 

class Requete:
    
        def request(self):
               url = "http://www.google.fr"
               headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
               response = requests.get(url, headers = headers , timeout = 10)
               return response.text
           
               r = Requete()
               print(r.request())
         


              


