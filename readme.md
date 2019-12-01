# Milestone Project 4 - Auction E-Commerce App
wireframes [here](https://drive.google.com/open?id=1eMpOrnaVDADfW-CZU_iwkKvDAcTaU4fH) and please download free [Adobe XD](https://www.adobe.com/lu_de/products/xd.html) to view these frames properly!
[![Build Status](https://travis-ci.org/dano5342/Milestone4V2.svg?branch=master)](https://travis-ci.org/dano5342/Milestone4V2)
## Overview
This website is inspired by Ebay as an e-commerce website - with a twist. This project is going to be built purely upon historical artifacts of myth and legend, with maybe a few actual items thrown in as well. This website will be intended for collectors and sellers as will be storied upon below in my UX section. Think of these items as an offshoot of the old Catholic way of buying into heaven by way of [Indulgences](https://en.wikipedia.org/wiki/Indulgence).

## UX
The website will be focussed on a few different users which shall be expanded upon below.
1. `New User` On happenstance has found the website through a search engine via optimised keywords - This new user wants to know what the site is for, what they can achieve via registering to the site and what is on offer. Nothing too obtrusive and they can browse at their leisure and be walked through the auctions through categories and tags.
2. `Previous User` Has been on the site for a while now, has an account and han't yet made any sales or purchases, and via luck has come accross a Splinter from the Lance of St. George - Thus he would like to make some money via an auction. Understanding this he places the item for sale with a time limit of 2 weeks and also a `Buy it!` limit of £1500. Starting the auction at £499 to entice people to go above and beyond the `Buy it!` price.
3. `Collector` This user is the main Target audience for the website, this user wants to be able to review all things within certain categories and then make purchases from within them. Storing things as they go along in their cart until ready for order. They also arent sure how trustworthy some sellers are as they had a bad experience with one previously! So they would like the ability to view reviews of the person/shop they may be buying from and also leave a review for an item that they purchased from this seller.

## Features
The premise of the website was originally to be an Ecommerce/Auction website for user to user interaction with sales ran by users kind of like an Ebay application. However throughout the course of development and for the purpose of marking the website I cut down the scope and decided to go for a simpler approach with the same kind of ideas as before.

The site was therefore changed into a more conventional project along the lines of etsy or an Asos store, with login/logout functionality, the ability to peruse and purchase items securely using Stripe integrated into the app with JS and on the backend. 

Some base features:
+ Account CRUD functionality
+ Browsing and filtering products by category, filter by search and by details
+ Storing products in the session for return users and for new users.
+ Authentication required for purchasing products from the site.

## Technologies
This project will make use of a collection of tech's that I've used so far through my course.
+ [HTML](https://www.w3schools.com/html/html5_intro.asp) - For writing the templates in which each view will be written HTML the language of the web will be utilised.
+ [SCSS / CSS](https://sass-lang.com/) - Compiling my stles from Sassy CSS into CSS will help to minimise the amount of coding necessary in the styling of the website.
+ [Bootstrap](https://getbootstrap.com/) - For minimising the amount of custom coding necessary within the project this will be used for the grid and layout.
+ [jQuery](https://jquery.com/) - This will be used for making the website more interactive for the user and making it more appealing to the eye via DOM manipulation.
+ [Python Django](https://www.djangoproject.com/) - Python highend language will be used for writing tests, views, urls and linking the backend up to the front end. This will be achieved with Django templating framework.
+ [PostgreSQL](https://www.postgresql.org/) / [SQLite](https://www.sqlite.org/index.html) - Will be used for my database in the back end. Postgres will be used for the heroku hosting and SQLite will be used for testing the site before deployment.
+ [Travis CI](https://travis-ci.org/) Travis is a tool for Continuous Integration and helped with a large part of developing the project, used to help test functionality.
+ [Heroku](https://www.heroku.com/) Is a cloud hosting platform for hosting projects and web applications. I have used Heroku to display and host my project.
+ [AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) I've used Amazons Web Services to hsot my static and my media files. The S3 Buckets allows a user to create a storage elsewhere and call it from the site from environment variables.

## Testing
All unit testing was completed using the built in `python manage.py test` command working through each app for the django project, you can find
the tests written for each app under the 'appname'/'testing' folders, each test suite is written for the views, forms and models of each section. Further testing information can be 
[found here](https://docs.djangoproject.com/en/2.2/topics/testing/advanced/)
Coverage was also used to help attain near 100% completion. If there was anything particularly 
challenging on something that required a lot of testing it will be written up below however if nothing out of the ordinary
comes up then the unit tests passed correctly and didnt require any further testing for the purposes of the project.

Unit Testing the products section was one of the more typical TDD testing I have written, creating the test for the detailed view for the product was very typical, writing the minimal amount of code per run to try and make it pass each time, until it does. Here is a detailed write up:
+ I began this particular test trying to just access the product itself whilst writing it up
``` python
class TestProductPages(TestCase):
    
    def setUp(self):
        self.client = Client()
        ....
def test_detail_prod_view(self):
        product = Product(title = 'TestProd')
        product.save()
        page = self.client.get('/products/more_info/{0}'.format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prod_detail.html')
```

+ This resulted in the following problem: `self.assertEqual(page.status_code, 200) AssertionError: 404 != 200`
+ So through this I figured that the 404 was due to the ID not being formatted correctly and amended my code like so:
``` python
def test_detail_prod_view(self):
        product = Product(title = 'TestProd',
                          pk = id)
        product.save()
        page = self.client.get('/products/more_info/{0}'.format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prod_detail.html')
``` 
+ The eagle eyed viewer may realise this resulted in a syntax error.
Next I tried to create the product while calling the id:
```python
def test_detail_prod_view(self):
        product = Product(title = 'TestProd')
        product.save()
        id = product.id
        page = self.client.get('/products/more_info/{0}'.format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prod_detail.html')
```
+ This then resulted in the following error: `django.db.utils.IntegrityError: NOT NULL constraint failed: products_product.price`
+ So this got me thinking that in my DB There was another relational object that needed calling for this test to pass: the category so this resulted in the following code:
```python
def test_detail_prod_view(self):
    #Creating the category object before calling it from the product.
        cat = Category(category="testCat")
        cat.save()

        product = Product(title = 'TestProd',
                          price = 24,
                          category = cat)
        product.save()
        id = product.id
        page = self.client.get('/products/more_info/{0}'.format(id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'prod_detail.html')
```
##### Checkout Issues
During my struggles to write the stripe code into the project I utilised the builtin Python DeBugger (PDB) tool to help print to the console what was being held in the app at the time, this helped to differentiate between bools and functions whilst getting lost in the code. The PDB tool can be used whilst running the application by using the `set_trace()` function on an object to see whats going on. More info on [PDB can be found here](https://docs.python.org/3/library/pdb.html)
##### Continuous Integration
Throughout the development of the project after setting up Heroku 

+ User Stories Testing Manually testing.
+ Am i responsive?

##### Additional Testing Notes
During Development the creation of models allows for declaring these as `__str__` objects, allowing the administrators to access these through the database backend. This was also used for testing that products and categories. etc were working.
#### Deployment
+ Will be done on Heroku
+ Mention AWS for static/media hosting


#### Credits
A lot of the imagery and photos received inspiration from the posters at [reddits artefact subreddit](https://www.reddit.com/r/ArtefactPorn/)
##### Content
##### Media
Disclaimer: I Do not own any of the images and or photos mentioned herein below, with all certainty have I tried to credit the author/owner where required and free to use/public domain images have been credited where possible too. 



+ Compass & Atlas credit: Ylanite Kloppens: https://www.pexels.com/photo/beige-analog-gauge-697662/ 
+ Books image (BOOKS) credit: Suzy Hazelwood: https://www.pexels.com/photo/low-light-photography-of-books-1301585/
+ Other image credit: Paula (Pexels): https://www.pexels.com/photo/brown-wooden-drumstick-beside-brown-wooden-case-179959/
+ Medieval armor image credit: Ott Maidre: https://www.pexels.com/photo/medieval-armor-2046779/
+ Roman Coin medallion image credit: Wikimedia/Walters art museum: https://commons.wikimedia.org/wiki/File:Roman_-_Medallion_with_Alexander_the_Great_-_Walters_591_-_Obverse.jpg
+ Jewellery image Staatliche Antikensammlungen [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/)
+ Furniture image credit: Freddy: pexels.com/photo/brown-wooden-armchair-2168227/
###### Jewellery Credits
+ [Scythian Golden Comb](https://commons.wikimedia.org/wiki/File:Scythian_comb.jpg) Public Domain
+ [Byzantine Marriage Ring](https://upload.wikimedia.org/wikipedia/commons/a/a3/Byzantine_-_Marriage_Ring_-_Walters_571715_-_Top.jpg) Public Domain
+ [Norse Spurs](https://www.khm.uio.no/english/visit-us/historical-museum/exhibitions/viking-age/) C5905 in Oldsaksamlingen at Kulturhistorisk Museum,  Museum of Cultural History / UiO
+ [Pendant](https://www.metmuseum.org/art/collection/search/39461?&searchField=All&sortBy=Relevance&what=Gold&ft=*&offset=0&rpp=20&amp;pos=11) Public Domain
+ [Pectoral Necklace](https://www.metmuseum.org/art/collection/search/464070?&searchField=All&sortBy=Relevance&what=Gold&ft=Coin&offset=0&rpp=20&amp;pos=6) Public Domain
+ [Hairnet](https://www.metmuseum.org/art/collection/search/255890?&searchField=All&sortBy=Relevance&what=Gold&ft=Medallion&offset=0&rpp=20&amp;pos=8) Public Domain
###### Arms & Armor Credits
+ [Iron War Mask](https://www.metmuseum.org/art/collection/search/35152), Public Domain
+ [Closed Burgeonet](https://www.metmuseum.org/art/collection/search/27103) Public Domain
+ [Gold Burgeonet](https://www.metmuseum.org/art/collection/search/22859) Public Domain
+ [Powder Flask](https://www.metmuseum.org/art/collection/search/22391) Public Domain
+ [Steel Shield](https://www.metmuseum.org/art/collection/search/25415) Public Domain
+ [Saber & Scabbard](https://www.metmuseum.org/art/collection/search/22871?&searchField=All&sortBy=Relevance&what=Gold&ft=Sword&offset=20&rpp=20&amp;pos=24) Public Domain
+ [Rapier](https://www.metmuseum.org/art/collection/search/24860?&searchField=All&sortBy=Relevance&what=Gold&ft=Rapier&offset=0&rpp=20&amp;pos=11)
###### Furniture Credits
+ [Ornamental Jade Disk](https://www.harvardartmuseums.org/collections/object/204830) Public Domain (Educational Purposes)
+ [Commode](https://www.metmuseum.org/art/collection/search/206990?&searchField=All&sortBy=Relevance&what=Engraving&ft=*&offset=0&rpp=20&amp;pos=4) Public Domain
+ [Standing Clock](https://www.metmuseum.org/art/collection/search/202114) Public Domain
+ [Continued Furniture](https://www.metmuseum.org/art/collection/search#!?material=Gold&perPage=20&offset=0&q=Furniture&pageSize=0&sortBy=Relevance&sortOrder=asc&searchField=All) All public domain
###### Other Credits
+ [Arhat Statue](https://upload.wikimedia.org/wikipedia/commons/c/c3/%E9%81%BC_%E4%B8%89%E5%BD%A9%E7%BE%85%E6%BC%A2%E5%83%8F-Arhat_%28Luohan%29_MET_DP163966.jpg) Public Domain
+ [Rosetta Stone](https://en.wikipedia.org/wiki/File:Rosetta_Stone.JPG) Credit: © Hans Hillewaert
+ [Ptah Statue](https://www.metmuseum.org/art/collection/search/587598?&searchField=All&sortBy=Relevance&what=Gold&ft=statue&offset=0&rpp=20&amp;pos=1) Public Domain
###### Books Credits
+ [Dead Sea Scrolls](https://en.wikipedia.org/wiki/Dead_Sea_Scrolls#/media/File:Psalms_Scroll.jpg) Public Domain
+ [Leather Bible](https://www.metmuseum.org/art/collection/search/466569) Public Domain
+ [Illuminated Gospel](https://www.metmuseum.org/art/collection/search/317618) Public Domain
+ [Album of Tourneys](https://www.metmuseum.org/art/collection/search/25111) Public Domain
+ [Kitano Legends](https://www.metmuseum.org/art/collection/search/45428?&searchField=All&sortBy=Relevance&what=Gold&ft=*&offset=0&rpp=20&amp;pos=19) Public Domain
+ [Aizen Myoo](https://www.metmuseum.org/art/collection/search/44910) Public Domain
######  Coins Credits
+ [All Coins](https://www.metmuseum.org/art/collection/search#!?material=Gold&perPage=20&offset=0&q=Coin&pageSize=0&sortBy=Relevance&sortOrder=asc&searchField=All) Fully Public Domain
##### Honourable Mentions