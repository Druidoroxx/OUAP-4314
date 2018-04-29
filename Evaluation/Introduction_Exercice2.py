<<<<<<< HEAD
import requests 
import re
from urlparse import urlparse


class Requete:
    
        def request(self):
               url = "http://www.google.fr"
               headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
               response = requests.get(url, headers = headers , timeout = 10)
               return response.text


        def supSuperflus():
                r = Requete()
                doc = r.request() 
                doc1 = doc.replace(" ", "")
                print(doc1)
        
        
        def strIntelligible():
                r = Requete()
                doc = r.request() 
                doc1 = re.sub('[^A-Za-z0-9]+', '', doc)
                print(doc1)
                
        def domUrl(self):
             
                parsed_uri = urlparse("http://www.google.fr" )
                domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                print domain
                

=======
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 09:22:07 2018

@author: hot
"""

def suppr_space(self):
    self.response.replace(" ","")
        
def suppr_car(self):
    self.response.replace()
>>>>>>> fb52f117373d0947a5a71f8e96b6346bd4ba841d
