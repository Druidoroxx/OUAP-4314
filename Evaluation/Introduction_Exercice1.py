<<<<<<< HEAD
import requests 

class Requete:
    
        def request(self):
               url = "http://www.google.fr"
               headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
               response = requests.get(url, headers = headers , timeout = 10)
               return response.text
           
               r = Requete()
               print(r.request())
         


              


=======
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:33:18 2018

@author: hot
"""

class testhttp:
    "Permet des requêtes HTTP"
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    def get(self, url, timeout=10):
        self.response = requests.get(url, headers=headers, timeout = timeout)
        if self.response != "<Response [200]>":
            self.response = requests.get(url, headers=headers, timeout = timeout)
        return self.response.text
    

        
            
            
    
        
        
>>>>>>> fb52f117373d0947a5a71f8e96b6346bd4ba841d
