# Milestone Project 4 - Auction E-Commerce App
wireframes [here](https://drive.google.com/open?id=1eMpOrnaVDADfW-CZU_iwkKvDAcTaU4fH) and please download free [Adobe XD](https://www.adobe.com/lu_de/products/xd.html) to view these frames properly!
[![Build Status](https://travis-ci.org/dano5342/Milestone4V2.svg?branch=master)](https://travis-ci.org/dano5342/Milestone4V2)
#### Overview
This website is inspired by Ebay as an e-commerce website - with a twist. This project is going to be built purely upon historical artifacts of myth and legend, with maybe a few actual items thrown in as well. This website will be intended for collectors and sellers as will be storied upon below in my UX section. Think of these items as an offshoot of the old Catholic way of buying into heaven by way of [Indulgences](https://en.wikipedia.org/wiki/Indulgence). 

#### UX
The website will be focussed on a few different users which shall be expanded upon below.
1. `New User` On happenstance has found the website through a search engine via optimised keywords - This new user wants to know what the site is for, what they can achieve via registering to the site and what is on offer. Nothing too obtrusive and they can browse at their leisure and be walked through the auctions through categories and tags.
2. `Previous User` Has been on the site for a while now, has an account and han't yet made any sales or purchases, and via luck has come accross a Splinter from the Lance of St. George - Thus he would like to make some money via an auction. Understanding this he places the item for sale with a time limit of 2 weeks and also a `Buy it!` limit of £1500. Starting the auction at £499 to entice people to go above and beyond the `Buy it!` price.
3. `Shop User (seller)` This is an experienced user and they may be a business of their own with employees for finding these treasures and the person who runs the online shop. They have recently found a trove of treasures from the Spanish Treasure Fleet. As such they have many items that are of similar look and size and dont want to auction them however sell them off individually with only `Buy it!` options, some of their customers would like to access these and store them in a cart for reviewing until they are ready to purchase. This allows them to keep a tight inventory on what they have left over etc.
4. `Collector` This user is the main Target audience for the website, this user wants to be able to review all things within certain categories and then make purchases from within them. Storing things as they go along in their cart until ready for order. They also arent sure how trustworthy some sellers are as they had a bad experience with one previously! So they would like the ability to view reviews of the person/shop they may be buying from and also leave a review for an item that they purchased from this seller.

#### Features
+ Registration - `New User` Wants to be able to register to the site to be able to make purchases and read reviews on items
+ Log In - `Previous User` Wants to be able to log in as they didnt complete their sale when going through last time, the site has saved some of the details that they added before but they'd like to complete this to make some money.
+ Create Auction - `Previous User` Will also need to use this function to complete their sales. They can achieve this buy going through to their account page and finding the create auction area button.
+ Leave a review - `Collector` - Has had a good experience buying from a particular shop and is exstatic about the quality of a Piece of Eight coin they purchased. This can be done via their "Previous Orders" section within their account.
+ Remove Auction - `Shop User` Has had a private offer on one of their items with limited availability and would like to remove the item from sale to the public. 
+ Watch this Product - `Collector` has had their eye on a portrait of Medusa before she became a gorgon and is quite certain he wants to purchase it, however he doesn't want to go too high too quickly and is watching to see how the auction will unfold.

#### Technologies
This project will make use of a collection of tech's that I've used so far through my course.
+ HTML - For writing the templates in which each view will be written HTML the language of the web will be utilised.
+ SCSS / CSS - Compiling my stles from Sassy CSS into CSS will help to minimise the amount of coding necessary in the styling of the website.
+ Bootstrap - For minimising the amount of custom coding necessary within the project this will be used for the grid and layout.
+ jQuery - This will be used for making the website more interactive for the user and making it more appealing to the eye via DOM manipulation.
+ Python Django - Python highend language will be used for writing tests, views, urls and linking the backend up to the front end. This will be achieved with Django templating framework.
+ PostgreSQL / SQLite - Will be used for my database in the back end. Postgres will be used for the heroku hosting and SQLite will be used for testing the site before deployment.

#### Testing
+ To be written
+ PDB - using it to debug stripe payments in the console.
+ Travis write up
+ Unit Testing
+ User Stories Testing Manually testing.
+ Am i responsive?

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
###### Other Credits
+ [Arhat Statue](https://upload.wikimedia.org/wikipedia/commons/c/c3/%E9%81%BC_%E4%B8%89%E5%BD%A9%E7%BE%85%E6%BC%A2%E5%83%8F-Arhat_%28Luohan%29_MET_DP163966.jpg) Public Domain
+ [Rosetta Stone](https://en.wikipedia.org/wiki/File:Rosetta_Stone.JPG) Credit: © Hans Hillewaert
###### Books Credits
+ [Dead Sea Scrolls](https://en.wikipedia.org/wiki/Dead_Sea_Scrolls#/media/File:Psalms_Scroll.jpg) Public Domain
+ [Leather Bible](https://www.metmuseum.org/art/collection/search/466569) Public Domain
+ [Illuminated Gospel](https://www.metmuseum.org/art/collection/search/317618) Public Domain
+ [Album of Tourneys](https://www.metmuseum.org/art/collection/search/25111) Public Domain
+ [Kitano Legends](https://www.metmuseum.org/art/collection/search/45428?&searchField=All&sortBy=Relevance&what=Gold&ft=*&offset=0&rpp=20&amp;pos=19) Public Domain
+ [Aizen Myoo](https://www.metmuseum.org/art/collection/search/44910) Public Domain
######  Coins Credits

##### Honourable Mentions