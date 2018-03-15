Votre premier projet
====================

Dans un premier temps vous devez créer un projet Scrapy avec la commande : 

.. code-block:: bash

    scrapy startproject monprojet
    
Cette commande va créer un dossier ``monprojet`` contenant les éléments suivants correspondant au squelette ::

    monprojet/
        scrapy.cfg            # Options de déploiement

        monprojet/             # Le module Python contenant les informations
            __init__.py

            items.py          # Fichier contenant les items
            
            middlewares.py    # Fichier contenant les middlewares

            pipelines.py      # Fichier contenant les pipelines

            settings.py       # Fichier contenant les paramètres du projet

            spiders/          # Dossier contenant toutes les spiders
                __init__.py


Votre première Spider
=====================

Une Spider est une classe Scrapy qui permet de mettre en place toute l'architecture complexe vu dans l'introduction. Pour définir une spider, il vous faut hériter de la classe :class:`scrapy.Spider`. La seule chose à faire est de définir la première requête à effectuer et comment suivre les liens. La Spider s'arrêtera lorsqu'elle aura parcouru tous les liens qu'on lui a demandé de suivre. 

Pour créer une Spider on utilise la syntaxe: 

.. code-block:: bash

    scrapy genspider <SPIDER_NAME> <DOMAIN_NAME>

Par exemple, 

.. code-block:: bash

    cd monprojet
    scrapy genspider leboncoin leboncoin.fr
    
Cette commande permet de créer une spider appelée ``leboncoin`` pour scraper le domaine ``leboncoin.fr``. Cela créé le fichier Python ``leboncoin.py`` suivant :

.. code-block:: Python

    import scrapy


    class LeboncoinSpider(scrapy.Spider):
        name = "leboncoin"
        allowed_domains = ["leboncoin.fr"]
        start_urls = ['http://leboncoin.fr/']

        def parse(self, response):
            pass
            

Une bonne pratique pour commencer à développer une Spider est de passer par l'interface Shell proposée par Scrapy. Elle permet de récupérer un objet ``Response`` et de tester les méthodes de récupération des données.
 
 
.. code-block:: bash
    
    scrapy shell 'http://leboncoin.fr'
    
Scrapy lance un kernel Python 

.. code-block:: bash

    2018-02-08 11:28:47 [scrapy.utils.log] INFO: Scrapy 1.3.3 started (bot: monprojet)
    2018-02-08 11:28:47 [scrapy.utils.log] INFO: Overridden settings: {'BOT_NAME': 'monprojet', 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0, 'NEWSPIDER_MODULE': 'monprojet.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['monprojet.spiders']}
    2018-02-08 11:28:47 [scrapy.middleware] INFO: Enabled extensions:
    ['scrapy.extensions.corestats.CoreStats',
     'scrapy.extensions.telnet.TelnetConsole']
    2018-02-08 11:28:47 [scrapy.middleware] INFO: Enabled downloader middlewares:
    ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
     'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
     'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
     'scrapy.downloadermiddlewares.retry.RetryMiddleware',
     'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
     'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
     'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
     'scrapy.downloadermiddlewares.stats.DownloaderStats']
    2018-02-08 11:28:47 [scrapy.middleware] INFO: Enabled spider middlewares:
    ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
     'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
     'scrapy.spidermiddlewares.referer.RefererMiddleware',
     'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
     'scrapy.spidermiddlewares.depth.DepthMiddleware']
    2018-02-08 11:28:47 [scrapy.middleware] INFO: Enabled item pipelines:
    []
    2018-02-08 11:28:47 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
    2018-02-08 11:28:47 [scrapy.core.engine] INFO: Spider opened
    2018-02-08 11:28:47 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.leboncoin.fr/robots.txt> from <GET https://leboncoin.fr/robots.txt>
    2018-02-08 11:28:47 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.leboncoin.fr/robots.txt> (referer: None)
    2018-02-08 11:28:47 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.leboncoin.fr/> from <GET https://leboncoin.fr>
    2018-02-08 11:28:47 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.leboncoin.fr/robots.txt> (referer: None)
    2018-02-08 11:28:47 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.leboncoin.fr/> (referer: None)
    2018-02-08 11:28:49 [traitlets] DEBUG: Using default logger
    2018-02-08 11:28:49 [traitlets] DEBUG: Using default logger
    [s] Available Scrapy objects:
    [s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
    [s]   crawler    <scrapy.crawler.Crawler object at 0x11035dc50>
    [s]   item       {}
    [s]   request    <GET https://leboncoin.fr>
    [s]   response   <200 https://www.leboncoin.fr/>
    [s]   settings   <scrapy.settings.Settings object at 0x1148e4ef0>
    [s]   spider     <LeboncoinSpider 'leboncoin' at 0x114b83080>
    [s] Useful shortcuts:
    [s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
    [s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
    [s]   shelp()           Shell help (print this help)
    [s]   view(response)    View response in a browser
    
Grâce à cette interface, vous avez accès à plusieurs objets comme la ``Response``, la ``Request``,  la ``Spider`` par exemple. Vous pouvez aussi exécuter ``view(response)`` pour afficher ce que Scrapy récupère dans un navigateur.


.. code-block:: Python

    In [1]: response
    Out[1]: <200 https://www.leboncoin.fr/>
    
    In [3]: request
    Out[3]: <GET http://leboncoin.fr>

    In [4]: type(request)
    Out[4]: scrapy.http.request.Request
    
    In [5]: spider
    Out[5]: <LeboncoinSpider 'leboncoin' at 0x111e61b38>

    In [6]: type(spider)
    Out[6]: monprojet.spiders.leboncoin.LeboncoinSpider
   
   
Vos premières requêtes
----------------------

On peut commencer à regarder comment extraire les données de la page web en utilisant le langage de requêtes proposé par Scrapy. Il existe deux types de requêtes : les requêtes ``css`` et ``xpath``. Les requêtes ``xpath`` sont plus complexes mais plus puissantes que les requêtes ``css``. Dans le cadre de ce tutorial, nous allons uniquement aborder les requêtes ``css``, elles nous suffiront pour extraire les données dont nous avons besoin (en interne, Scrapy transforme les requêtes ``css``en requêtes ``xpath``. 

Que ce soit les requêtes ``css`` ou ``xpath``, elles crééent des sélecteurs de différents types.
Quelques exemples :

Pour récupérer le titre d'une page : 

.. code-block:: Python

    In [1]: response.css('title')
    Out[1]: [<Selector xpath='descendant-or-self::title' data='<title>\n\n\t\tleboncoin, site de petites an'>]
    
On récupère une liste de sélecteurs correspondant à la requête ``css`` appelée. La requête précédante était unique, d'autre requêtes moins restrictives permettent de récupérer plusieurs résultats. 
Par exemple pour rechercher l'ensemble des liens présents sur la page, on va rechercher les balises HTML ``<a></a>``

.. code-block:: Python

    In [2]: response.css('a')
    Out[2]: 
    [<Selector xpath='descendant-or-self::a' data='<a href="" title="Fermer le menu" class='>,
     <Selector xpath='descendant-or-self::a' data='<a id="appRedirect" target="_blank" clas'>,
     <Selector xpath='descendant-or-self::a' data='<a class="displayMenu button-white-mobil'>,
     <Selector xpath='descendant-or-self::a' data='<a href="//www.leboncoin.fr/" class="log'>,
     <Selector xpath='descendant-or-self::a' data='<a href="" class="logo-site trackable cu'>,
     <Selector xpath='descendant-or-self::a' data='<a href="//www.leboncoin.fr/" title="Acc'>,
     <Selector xpath='descendant-or-self::a' data='<a href="//www.leboncoin.fr/ai?ca=12_s" '>, ... ]
    
Pour récupérer le texte contenu dans les balises, on passe le paramêtre ``<TAG>::text``. Par exemple : 
    
.. code-block:: Python

    In [3]: response.css('title::text')
    Out[3]: [<Selector xpath='descendant-or-self::title/text()' data='\n\n\t\tleboncoin, site de petites annonces '>]
    
    
.. note:: Exercice 

    Comparer les résultats des deux requêtes ``response.css('title')`` et ``response.css('title::text')``.
    
Maintenant pour extraire les données des selecteurs on utilise l'une des deux méthodes suivantes :
- ``extract()`` permet de récupérer une liste des données extraites de tous les sélecteurs
- ``extract_first()`` permet de récupérer une ``String`` provenant du premier sélecteur de la liste.

.. code-block:: Python

    In [4]: response.css('title::text').extract_first()
    Out[4]: '\n\n\t\tleboncoin, site de petites annonces gratuites\n\n'
    
On peut récupérer un attribut d'une balise avec la syntaxe ``<TAG>::attr(<ATTRIBUTE_NAME>)``:

Par exemple, les liens sont contenus dans un attribut ``href``.

.. code-block:: Python

    In [5]: response.css('a::attr(href)')
    Out[5]: 
    [<Selector xpath='descendant-or-self::a/@href' data=''>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/'>,
     <Selector xpath='descendant-or-self::a/@href' data=''>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/ai?ca=12_s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/annonces/offres'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/annonces/demandes'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/aw?ca=12_s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/aw?ca=12_s&selected=b'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/aw?ca=12_s&selected=s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/boutiques/tout_secteu'>,
     <Selector xpath='descendant-or-self::a/@href' data=''>,
     <Selector xpath='descendant-or-self::a/@href' data=''>,
     <Selector xpath='descendant-or-self::a/@href' data='https://corporate.leboncoin.fr/'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/recrutement.htm?ca=12'>,
     <Selector xpath='descendant-or-self::a/@href' data='http://secondhandeffect.leboncoin.fr/'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/legal.htm?ca=12_s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/regles.htm?ca=12_s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/cgv_general.htm?ca=12'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/cookies/'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www2.leboncoin.fr/pub/form/?ca=12_s'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www2.leboncoin.fr/dc/vos_droits_et_obl'>,
     <Selector xpath='descendant-or-self::a/@href' data='https://comptepro.leboncoin.fr/immobilie'>,
     <Selector xpath='descendant-or-self::a/@href' data='//www.leboncoin.fr/vos-recrutements'>,...]
     
Comme vu précédemment, si on veut récupérer la liste des liens de la page on applique la méthode `extract()`
     
.. code-block:: Python

    In [18]: response.css('a::attr(href)').extract()
    Out[18]: 
    ['',
     '//www.leboncoin.fr/',
     '',
     '//www.leboncoin.fr/',
     '//www.leboncoin.fr/ai?ca=12_s',
     '//www.leboncoin.fr/annonces/offres',
     '//www.leboncoin.fr/annonces/demandes',
     '//www.leboncoin.fr/aw?ca=12_s',
     '//www.leboncoin.fr/aw?ca=12_s&selected=backup',
     '//www.leboncoin.fr/aw?ca=12_s&selected=search',
     '//www.leboncoin.fr/boutiques/tout_secteur_d_activite/toutes_categories/ile_de_france/',
     '',
     '',
     'https://corporate.leboncoin.fr/',
     '//www.leboncoin.fr/recrutement.htm?ca=12_s&c=0&w=3',
     'http://secondhandeffect.leboncoin.fr/',
     '//www.leboncoin.fr/legal.htm?ca=12_s',
     '//www.leboncoin.fr/regles.htm?ca=12_s',
     '//www.leboncoin.fr/cgv_general.htm?ca=12_s',
     '//www.leboncoin.fr/cookies/',...]
     
Les liens dans une page HTML sont souvent codés de manière relative par rapport à la page courante. La méthode de l'objet ``Response`` peut être utilisée pour recréer l'url complet. 

Un exemple sur le 4e élément : 

.. code-block:: Python

    In [22]: response.urljoin(response.css('a::attr(href)').extract()[3])
    Out[22]: 'https://www.leboncoin.fr/'
    
Exercice :    

Utiliser une liste compréhension pour transformer les liens relatifs récupérés par la méthode ``extract()`` en liens absolus.
    
Le résultat doit ressembler à : 

.. code-block:: Python

    Out[23]: 
    ['https://www.leboncoin.fr/',
     'https://www.leboncoin.fr/',
     'https://www.leboncoin.fr/',
     'https://www.leboncoin.fr/',
     'https://www.leboncoin.fr/ai?ca=12_s',
     'https://www.leboncoin.fr/annonces/offres',
     'https://www.leboncoin.fr/annonces/demandes',
     'https://www.leboncoin.fr/aw?ca=12_s',
     'https://www.leboncoin.fr/aw?ca=12_s&selected=backup',
     'https://www.leboncoin.fr/aw?ca=12_s&selected=search',
     'https://www.leboncoin.fr/boutiques/tout_secteur_d_activite/toutes_categories/ile_de_france/',
     'https://www.leboncoin.fr/',...]
     
..  [response.urljoin(url) for url in response.css('a::attr(href)').extract()]

Des requêtes plus complexes
---------------------------

On peut créer des requêtes plus complexes en utilisant à la fois la structuration HTML du document mais également la couche de présentation CSS. On utilise l'inspecteur de ``Google Chrome`` pour identifier le type et l'identifiant de la balise contenant les informations.  

Il y a au moins deux choses à savoir en ``css`` :  

- Les ``.`` représentent les classes 
- Les ``#`` représentent les id


On se propose de récupérer le texte ou les liens associés aux noms des régions disposées à droite de la page d'accueil de ``leboncoin.fr``. Elles sont situées dans une balise mère ``<section>`` de classe ``mapNav`` et ensuite dans chaque balise fille ``li``.

.. code-block:: HTML

    <section class="mapNav tiny-hidden small-hidden medium-hidden">
            <ul>
                <li class="">
                        <a href="//www.leboncoin.fr/annonces/offres/alsace/" title="Alsace" data-map="alsace" id="region_0" class="trackable" data-info="{&quot;event_name&quot; : &quot;accueil::selection_region::lien_textuel::alsace&quot;, &quot;event_type&quot; : &quot;click&quot;, &quot;event_s2&quot; : &quot;1&quot;, &quot;click_type&quot; : &quot;N&quot;}">Alsace</a>
                    </li>
                <li class="">
                        <a href="//www.leboncoin.fr/annonces/offres/aquitaine/" title="Aquitaine" data-map="aquitaine" id="region_1" class="trackable" data-info="{&quot;event_name&quot; : &quot;accueil::selection_region::lien_textuel::aquitaine&quot;, &quot;event_type&quot; : &quot;click&quot;, &quot;event_s2&quot; : &quot;1&quot;, &quot;click_type&quot; : &quot;N&quot;}">Aquitaine</a>
                    </li>
                <li class="">
                        <a href="//www.leboncoin.fr/annonces/offres/auvergne/" title="Auvergne" data-map="auvergne" id="region_2" class="trackable" data-info="{&quot;event_name&quot; : &quot;accueil::selection_region::lien_textuel::auvergne&quot;, &quot;event_type&quot; : &quot;click&quot;, &quot;event_s2&quot; : &quot;1&quot;, &quot;click_type&quot; : &quot;N&quot;}">Auvergne</a>
                    </li>
                    
                    ...
                    
            </ul>
        </section>
        
        
A partir de cette structure HTML on peut construire la requête suivante pour récupérer tous les liens : 

.. code-block:: Python

    In [30]: response.css(".mapNav li a::attr(href)").extract()
    Out[30]: 
    ['//www.leboncoin.fr/annonces/offres/alsace/',
     '//www.leboncoin.fr/annonces/offres/aquitaine/',
     '//www.leboncoin.fr/annonces/offres/auvergne/',
     '//www.leboncoin.fr/annonces/offres/basse_normandie/',
     '//www.leboncoin.fr/annonces/offres/bourgogne/',
     '//www.leboncoin.fr/annonces/offres/bretagne/',
     '//www.leboncoin.fr/annonces/offres/centre/',
     '//www.leboncoin.fr/annonces/offres/champagne_ardenne/',...]
     
Le shell Scrapy permet de définir la structure des requêtes et de s'assurer de la pertinence du résultat retourné.
Pour automatiser le processus, il faut intégrer cette syntaxe au code Python des modules de spider définis dans la structure du projet.

Intégration des requêtes
------------------------

Le squelette de la classe ``LeboncoinSpider`` généré lors de la création du projet doit maintenant être enrichi. Par défaut 3 attributs et une méthode ``parse()`` ont été créés :

- ``name`` permet d'identifier sans ambiguïté la spider dans le code.
- ``allowed_domain`` permet de filtrer les requêtes et forcer la spider à rester sur une liste de domaines.
- ``starts_urls`` est la liste des urls d'où la spider va partir pour commencer son scraping.
- ``parse()`` est une méthode héritée de la classe ``scrapy.Spider``. Elle doit être redéfinie selon les requêtes que l'on doit effectuer et sera appelée sur l'ensemble des urls contenus dans la liste ``starts_urls``.

``parse()`` est une fonction ``callback`` qui sera appelée automatiquement sur chaque objet ``Response`` retourné par la requête. Cette fonction est appelée de manière asynchrone. Plusieurs requêtes peuvent ainsi être lancées en parallèles sans bloquer le thread principal.
L'objet ``Response`` passé en paramètre est le même que celui mis à disposition lors de l'exécution du Scrapy Shell.

.. code-block:: Python

    def parse(self, response):
        title = response.css('title::text').extract_first()
        all_links = [response.urljoin(url) for url in response.css(".mapNav li a::attr(href)").extract()]
        yield {
            "title":title,
            "all_links":all_links
        }
        
La fonction est un générateur (``yield``) et retourne un dictionnaire composé de deux éléments : 

- Le titre de la page; 
- La liste des liens sortants sous forme de String.

Pour le moment cette spider ne parcourt que la page d'accueil, ce qui n'est pas très productif.


Votre premier scraper
---------------------

Récupérer les données sur un ensemble de pages webs nécessite d'explorer en profondeur la structure du site en suivant tout ou partie des liens rencontrés.

La spider peut se ``balader`` sur un site assez efficacement. Il suffit de lui indiquer comment faire. Il faut spécifier à Scrapy de générer une requête vers une nouvelle page en construisant l'objet ``Request`` correspondant. Ce nouvel objet ``Request`` est alors inséré dans le scheduler de Scrapy. On peut évidemment générer plusieurs ``Request`` simultanément, correspondant par exemple, à différents liens sur la page courante. Ils sont insérés séquentiellement dans le scheduler.

Pour cela on modifie la méthode ``parse()`` de façon à ce qu'elle retourne un objet ``Request`` pour chaque nouveau lien rencontré. On associe également à cet objet une fonction de callback qui déterminera la manière dont cette nouvelle page doit être extraite.

Par exemple, pour que la spider continue dans les liens des différentes régions (pour l'instant la fonction de callback ne fait rien) : 

.. code-block:: Python

    import scrapy
    from scrapy import Request


    class LeboncoinSpider(scrapy.Spider):
        name = "leboncoin"
        allowed_domains = ["leboncoin.fr"]
        start_urls = ['http://leboncoin.fr/']

        def parse(self, response):
            all_links = [response.urljoin(url) for url in response.css(".mapNav li a::attr(href)").extract()]
            for link in all_links:
                yield Request(link, callback=self.parse_region)

        def parse_region(self, response):
            pass
            
La méthode ``parse_region()`` prend en argument un objet ``Response`` qui sera la réponse correspondant aux liens des regions. On peut comme ceci traverser un site en définissant des méthodes différentes en fonction du type de contenu.

Si la structure du site est plus profonde, on peut empiler autant de couches que souhaité. Imaginons que la structure du site leboncoin.fr inclue des pages correspondant aux départements de chacune des régions et aux villes de chacun des départements, nous modifirions la classe ``LeboncoinSpider`` comme ci-dessous.

.. code-block:: Python

    import scrapy
    from scrapy import Request


    class LeboncoinSpider(scrapy.Spider):
        name = "leboncoin"
        allowed_domains = ["leboncoin.fr"]
        start_urls = ['http://leboncoin.fr/']

        def parse(self, response):
            all_links = [response.urljoin(url) for url in response.css(".mapNav li a::attr(href)").extract()]
            for link in all_links:
                yield Request(link, callback=self.parse_region)

        def parse_region(self, response):
            for link in all_links_departments :
                yield Request(link, callback=self.parse_department)
                
        def parse_department(self, response):
            for link in all_links_cities :
                yield Request(link, callback=self.parse_cities)
                
        def parse_cities(self, response):
            pass
            
Quand on arrive sur une page région, on peut vouloir récupérer tous les éléments de la page. Pour cela, on réutilise le scrapy Shell pour commencer le développement de la nouvelle méthode d'extraction.

Par exemple pour la page ``https://www.leboncoin.fr/annonces/offres/alsace/`` : 

.. code-block:: bash

    scrapy shell 'https://www.leboncoin.fr/annonces/offres/alsace/'
    
Toutes les offres sont stockées dans une balise mère ``<div></div>`` de classe ``tabsContent``. On récupère alors le selecteur de cette classe et donc de cet objet. 

.. code-block:: Python

    In [1]: response.css(".tabsContent")
    Out[1]: [<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' tabsContent ')]" data='<section class="tabsContent block-white '>]
    
Pour récupérer chacun des éléments, il faut adresser les balises ``<li>`` contenues dans le sélecteur: 
    
.. code-block:: Python

    In [2]: response.css(".tabsContent li")
    Out[2]: 
    [<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' tabsContent ')]/descendant-or-self::*/li" data='<li itemscope itemtype="http://schema.or'>,
     <Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' tabsContent ')]/descendant-or-self::*/li" data='<li itemscope itemtype="http://schema.or'>,...]
     
On peut empiler les sélecteurs ``css`` pour créer des requêtes plus complexes.

Par exemple, pour récupérer tous les titres des différentes annonces :

.. code-block:: Python

    In [7]: response.css(".tabsContent li .item_infos .item_title::text").extract()
    Out[7]: 
    ['\n                            \tMeuble de jukboxe\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tVolkswagen golf 5 1.9 tdi 105 cv \n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tPoulailler xxl\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tVitre côté passager twingo\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tPoupée porcelaine\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \ttuiles\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tDrone racer 250 eachine carbone\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tChaise de douche \n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tLot de 4 chaises de salle à manger\n                                \n                            \t\n\t\t\t\t\t\t\t',
     '\n                            \tLot de tee-shirt garçon 12 mois\n                                \n                            \t\n\t\t\t\t\t\t\t',
     "\n                            \tVerre/gobelet d'apprentissage\n                                \n                            \t\n\t\t\t\t\t\t\t", ...]

En HTML les données sont souvent de très mauvaise qualité. Il faut définir des méthodes permettant de les nettoyer pour être intégrées dans des bases de données.

Par exemple, pour supprimer tous les espaces superflus : 

.. code-block:: Python

    In [13]: def clean_spaces(string_):
    ...:        if string_ is not None: 
    ...:            return " ".join(string_.split())
        

Pour l'appliquer à tous les titres récupérés, on peut faire une list comprehension : 
.. code-block:: Python

    In [8]:  [clean_spaces(elt) for elt in response.css(".tabsContent li .item_infos .item_title::text").extract()]
    Out [8]: 
    ['Meuble de jukboxe',
     'Volkswagen golf 5 1.9 tdi 105 cv',
     'Poulailler xxl',
     'Vitre côté passager twingo',
     'Poupée porcelaine',
     'tuiles',
     'Drone racer 250 eachine carbone',
     'Chaise de douche',...]
     
La méthode précédente est intéressante si l'on ne recherche qu'une seule information par offre.
     
Par contre si l'on veut récupérer d'autres caractéristiques comme le prix par exemple, il est plus intéressant et plus efficace de récupérer l'objet et d'effectuer plusieurs traitements sur ce dernier.

Chaque objet retourné par les requêtes ``css`` est un selecteur avec lequel on peut interagir.

Par exemple pour récupérer le titre et le prix 

.. code-block:: Python

    In [3]: for item in response.css(".tabsContent li .item_infos"):
   ...:     print(clean_spaces(item.css(".item_title::text").extract_first()))
   ...:     print(clean_spaces(item.css(".item_price::text").extract_first()))
   ...:     
    Housse pour clic clac
    20 €
    Masque a gaz d’époque avec etui en acier
    20 €
    Boite neuve lego Chima 70231crocodile
    9 €
    Renault Mégane modèle 2004 version sport dynamique
    3 300 €
    Iveco 8x4 plateaux grue jib +treuil
    10 €
    Gigoteuse fille
    10 €
    2 chaises formicas années 60
    20 €
    
Persistence des données
-----------------------
    
Pour pouvoir stocker les informations que l'on récupère en parcourant un site il faut pouvoir les stocker. On utilise soit de simples dictionnaires Python, ou mieux des ``scrapy.Item`` qui sont des dictionnaire améliorés. 

Nous allons voir les deux façons de faire. On peut réécrire la méthode ``parse_region()`` pour lui faire retourner un dictionnaire correspondant à chaque offre rencontrée.

.. code-block:: Python

    def parse_region(self, response):
        for item in response.css(".tabsContent li .item_infos"):
            title = self.clean_spaces(item.css(".item_title::text").extract_first())
            price = self.clean_spaces(item.css(".item_price::text").extract_first())
            yield {
                "price":price,
                "title":title
            }
            
Si on combine tout dans la spider : 

.. code-block:: Python

    import scrapy
    from scrapy import Request


    class LeboncoinSpider(scrapy.Spider):
        name = "leboncoin"
        allowed_domains = ["leboncoin.fr"]
        start_urls = ['http://leboncoin.fr/']

        def parse(self, response):
            title = response.css('title::text').extract_first()
            all_links = [response.urljoin(url) for url in response.css(".mapNav li a::attr(href)").extract()]
            for link in all_links:
                yield Request(link, callback=self.parse_region)

        def parse_region(self, response):
            for item in response.css(".tabsContent li .item_infos"):
                title = self.clean_spaces(item.css(".item_title::text").extract_first())
                price = self.clean_spaces(item.css(".item_price::text").extract_first())
                yield {
                    "price":price,
                    "title":title
                }

        def clean_spaces(self, string):
            if string:
                return " ".join(string.split())
                
On peut maintenant lancer notre spider avec la commande suivante : 

.. code-block:: bash

    scrapy crawl <NAME>
    
``scrapy crawl`` permet de démarrer le processus en allant chercher la classe ``scrapy.Spider`` dont l'attribut ``name``  = <NAME>.

Par exemple, pour la spider ``LeboncoinSpider`` : 

.. code-block:: bash

    scrapy crawl leboncoin
    
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': '25 €', 'title': 'Maillot de bain Desigual'}
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': '400 €', 'title': 'Kit Embrayage sachs + volant moteur bi masse'}
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': '3 €', 'title': 'Chemisette bébé garçon'}
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': '5 €', 'title': 'Téléphone fixe'}
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': None, 'title': 'Échange Chaise volcane td'}
    2018-02-09 10:26:04 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.leboncoin.fr/annonces/offres/reunion/>
    {'price': '170 €', 'title': 'samsung j5 pro 2017'}
    
On peut exporter les résultats de ces retours dans différents formats de fichiers. 

- CSV : `scrapy crawl leboncoin -o lbc.csv`
- JSON : `scrapy crawl leboncoin -o lbc.json`
- JSONLINE : `scrapy crawl leboncoin -o lbc.jl`
- XML : `scrapy crawl leboncoin -o lbc.xml`

.. note:: Exercice 

Exécuter la spider avec les différents formats de stockage. Explorer ensuite le contenu des fichiers ainsi créés.

Votre premier Item
------------------

La classe ``Item`` permet de structurer les données que l'on souhaite récupérer sous la forme d'un modèle. Les items doivent être définis dans le fichier ``items.py`` créé par la commande ``scrapy startproject``. Les ``Item`` héritent de la class ``scrapy.Item``.

On veut structurer les données avec deux champs : le titre et le prix de l'annonce. Scrapy utilise une classe ``scrapy.Field`` permettant de 'déclarer' ces champs. Dans notre cas : 

.. code-block:: Python

    import scrapy

    class LeboncoinItem(scrapy.Item):
        title = scrapy.Field()
        price = scrapy.Field()
        
    
        
Utiliser la classe ``scrapy.Item`` plutôt qu'un simple dictionnaire permet plus de contrôle sur la structure des données. En effet, on ne peut insérer dans les items que des données avec des clés 'déclarées'. Ce qui assure une plus grande cohérence au sein d'un projet. 

On peut instancier un item de plusieurs façons : 

.. code-block:: Python

    lbc_item = LeboncoinItem(title="Drone DJI", price="100€")
    print(lbc_item)
    
    {'price': '100€', 'title': 'Drone DJI'}

    
.. code-block:: Python

    lbc_item = LeboncoinItem()
    lbc_item["title"] = "Drone Parrot"
    lbc_item["price"] = "120 €"
    print(lbc_item)
    
    {'price': '120 €', 'title': 'Drone Parrot'}

    
La définition d'un item permet de palier toutes les erreurs de typo dans les champs.

.. code-block:: Python

    lbc_item = LeboncoinItem()
    lbc_item["titel"] = "Drone Parrot"

    
     Traceback (most recent call last):
      File "/Users/raphael/PycharmProjects/scrapy_course/monprojet/monprojet/items.py", line 17, in <module>
        lbc_item["titel"] = "Drone Parrot"
      File "/Users/raphael/anaconda3/lib/python3.6/site-packages/Scrapy-1.3.3-py3.6.egg/scrapy/item.py", line 66, in __setitem__
        (self.__class__.__name__, key))
    KeyError: 'LeboncoinItem does not support field: titel'
    
Les items héritent des dictionnaires Python, et possèdent donc toutes les méthodes de ceux-ci: 

.. code-block:: Python

    lbc_item = LeboncoinItem(title="Drone DJI")
    print(lbc_item["title"]) # Méthode __getitem__() 
    print(lbc_item.get("price", "price is not set")) # Méthode get() 
    
    
On peut transformer un ``Item`` en dictionnaire très facilement, en le passant au constructeur:

.. code-block:: Python

    lbc_item = LeboncoinItem(title="Drone DJI", price="100€")
    print(type(lbc_item))
    dict_item = dict(lbc_item)
    print(type(dict_item))
    print(dict_item)
    
    <class '__main__.LeboncoinItem'>
    <class 'dict'>
    {'title': 'Drone DJI', 'price': '100€'}
    
On intègre maintenant cet item dans notre spider.

.. code-block:: Python

    import scrapy
    from scrapy import Request

    from ..items import LeboncoinItem # Import relatif Cf. Structure du projet Scrapy


    class LeboncoinSpider(scrapy.Spider):
        name = "leboncoin"
        allowed_domains = ["leboncoin.fr"]
        start_urls = ['http://leboncoin.fr/']

        def parse(self, response):
            title = response.css('title::text').extract_first()
            all_links = [response.urljoin(url) for url in response.css(".mapNav li a::attr(href)").extract()]
            for link in all_links:
                yield Request(link, callback=self.parse_region)

        def parse_region(self, response):
            for item in response.css(".tabsContent li .item_infos"):
                title = item.css(".item_title::text").extract_first()
                price = item.css(".item_price::text").extract_first()
                yield LeboncoinItem(price=price, title=title)
                
 On voit bien que le générateur retourne maintenant un ``Item``.
 
 .. note:: Exercice : 
 
 Relancer la spider pour vérifier le bon déroulement de l'extraction.
 

Postprocessing
--------------

Si l'on se réfère au diagramme d'architecture de Scrapy, on voit qu'il est possible d'insérer des composants suplémentaires dans le flux de traitement. Ces composants s'appellent ``Pipelines``. 

Par défaut, tous les ``Item`` générés au sein d'un projet Scrapy passent par les ``Pipelines``. Les pipelines sont utilisées la plupart du temps pour : 

- Nettoyer du contenu HTML ;
- Valider les données scrapées ; 
- Supprimer les items qu'on ne souhaite pas stocker ;
- Stocker ces objets dans des bases de données.

Les pipelines doivent être définis dans le fichier ``pipelines.py``.

Dans notre cas on peut vouloir nettoyer les champs ``price`` et ``title`` pour enlever les caractères supperflus.
Par exemple, le champ ``price`` on peut vouloir supprimer le caractère ``€``. Une bonne pratique est de passer toutes les méthodes de nettoyage dans les pipelines. 

Pour cela, nous allons en définir deux différentes. 

PricePipeline permet d'enlever le signe € et de transformer le prix en entier.

.. code-block:: Python

    from scrapy.exceptions import DropItem


    class PricePipeline(object):

        def process_item(self, item, spider):
            if item['price']:
                item["price"] = int(item["price"].replace("€", "").strip())
                return item
            else:
                raise DropItem("Missing price in %s" % item)
                
                
Nous allons aussi transferer la fonction de nettoyage du code html dans une Pipeline. 

.. code-block:: Python

    class TextPipeline(object):

        def process_item(self, item, spider):
            if item['title']:
                item["title"] = clean_spaces(item["title"])
            if item['price']:
                item["price"] = clean_spaces(item["price"])
                return item
            else:
                raise DropItem("Missing title in %s" % item)


    def clean_spaces(string):
        if string:
            return " ".join(string.split())


Pour dire au process Scrapy de faire transiter les items par ces pipelines. Il faut le spécifier dans le fichier de paramétrage ``settings.py``.

.. code-block:: Python

    ITEM_PIPELINES = {
        'monprojet.pipelines.TextPipeline': 100,
        'monprojet.pipelines.PricePipeline': 200,
    }
    
La valeur entière définie permet de déterminer l'ordre dans lequel les pipelines vont être appelées. Ces entiers peuvent être entre compris 0 et 1000.

On relance notre spider : 

.. code-block:: bash

    scrapy crawl leboncoin -o lbc.json
    
    
On peut aussi utiliser les Pipelines pour stocker les données récupérées dans une base de données. Pour stocker les items dans des documents mongo. 

.. code-block:: Python

    import pymongo

    class MongoPipeline(object):

        collection_name = 'scrapy_items'

        def open_spider(self, spider):
            self.client = pymongo.MongoClient()
            self.db = self.client["leboncoin"]

        def close_spider(self, spider):
            self.client.close()

        def process_item(self, item, spider):
            self.db[self.collection_name].insert_one(dict(item))
            return item
            
Ici redéfini deux autres méthodes:  ``open_spider()``et ``close_spider()``, ces méthode sont appelés comme leurs noms l'indiquent elles sont appelées lorsque la Spider est instanciée et fermée. 

Ces méthodes nous permettent d'ouvrir la connexion Mongo et de la fermer lorsque le scraping se termine. La méthode ``process_item()`` est appelé à chaque fois qu'un item passe dans le mécanisme interne de scrapy. Ici, la méthode permet d'insérer l'item en tant que document mongo. 

Pour que cette pipeline soit appelé il faut l'ajouter dans les settings du projet.

ITEM_PIPELINES = {
        'monprojet.pipelines.TextPipeline': 100,
        'monprojet.pipelines.PricePipeline': 200,
        'monprojet.pipelines.MongoPipeline': 300,

    }
    
La pipeline est ajoutée à la fin du process pour profiter des deux précédantes.
    
Settings
--------

Scrapy permet de gérer le comportement des spiders avec certains paramètres. Comme expliqué dans le premier cours, il est important de suivre des règles en respectant les différents site. Il existe énormément de paramètres mais nous allons (dans le cadre de ce cours) aborder les plus utilisés : 

- DOWNLOAD_DELAY : Le temps de téléchrgement entre chaque requête sur le même domaine ;
- CONCURRENT_REQUESTS_PER_DOMAIN : Nombre de requêtes simultanées par domaine ;
- CONCURRENT_REQUESTS_PER_IP : Nombre de requêtes simultanées par IP ;
- DEFAULT_REQUEST_HEADERS : Headers HTTP utilisé pour les requêtes ;
- ROBOTSTXT_OBEY : Scrapy récupère le robots.txt et adapte le scraping en fonction des règles trouvées ;
- USER_AGENT : UserAgent utilisé pour faire les requêtes ;
- BOT_NAME : Nom du bot annoncé lors des requêtes
- HTTPCACHE_ENABLED : Utilisation du cache HTTP, utile lors du parcours multiple de la même page.


Le fichiers settings.py permet de définir les paramètres globaux d'un projet. Si votre projet contient un grand nombre de spiders il peut être intéressant d'avoir des paramètres distincts pour chaque spider. Un moyen simple est d'ajouter un attribut ``custom_settings``à votre spider :

.. code-block:: Python

    class LeboncoinSpider(scrapy.Spider):
            name = "leboncoin"
            allowed_domains = ["leboncoin.fr"]
            start_urls = ['http://leboncoin.fr/']
            custom_settings = {
                "HTTPCACHE_ENABLED":True, 
                "CONCURRENT_REQUESTS_PER_DOMAIN":100
            }

