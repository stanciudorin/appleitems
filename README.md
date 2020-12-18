# MILESTONE PROJECT 4: [Apple Items](https://appleitems.herokuapp.com/)

## SOURCE: [Project Repository](https://github.com/stanciudorin/appleitems)

## ABOUT THE PROJECT
<p>This is the website for APPLE ITEMS, and e-commerce fictional website for a start-up that wants to promote their business and sell their products online.

The business if based on selling the well known Apple braded products, from iphones, macbooks, smartwatches to ipads, minis and more, this potential business could bring generous revenues if it is taken to the next level.

Users can purchase Apple product with or without having an account on the website, however having an account brings extra features as showing past orders information and having delivey addresses saved to their account.

</p>

## USER STORIES

 ### Business Goals
The following are the user stories this e-commerce website has been built on:
* A user that wants to see all categories and all products the website offers without having to register as a customer.
* A user that wants to see all categories and all products the website offers even if he/she is a current customer.
* A user wants to look around the shop and search for the products they want in order to compare different options of the item they are looking for, especially how the product looks like and its description.
* A user that wants to access a single product page and see individual products
* A registered user that wants to store their personal details so they are available as default for future orders from the shop.
* A registered user that wants to check what items they have purchased from the shop in previous orders and have a summary of all of them.
* A user/registered user that wants to purchase the products in an easy and seamless way.
* Having a professional design the business desires to attract customers from all over the world, being able, at checkout, to despatch everywhere on the globe.

## FEATURES

### Existing features

#### Shop

* A user, authenticated or not, can peruse the different products available at the shop. They can search for items using the search bar, filter their search selecting any of the categories and subcategories narrowing down the options to those they are looking for, and also sort the items by category, price, product name or brand name.
* Users can view more details of the desire item by clicking on the prodcut image.
* Once the user has chosen their desire size, when applicable, and number of items wanted, they can add then to the shopping bag. After doing so, they can either go back to the shop to look for other products, or review the items they have in their shopping bag before procceding to the checkout page. User can update the number of items or remove the items completely directly from the shopping bag.
* If they user is happy with the items in their bag, they can finish the purchase filling up the checkout form, inclusive of some personal details to be included in the order and the credit or debit card they want to use for the payment. Once the payment is accepted, they can see a summary of their order. At this same time, an email is sent to the email address provided.

#### Logging in
* Members that have finished the sign up process can log in from the home page using either their email address or username selected during the registration and their password. If they have forgotten the password, they can reset this by clicking the link on the log in page.
* After a successful log in, the user is redirected to their profile page, where they can review their personal details and any previous orders from the shop, if any.
* The member can update their personal details directly from the link on the profile page, which will display a form pre-filled with their current information.

### Features left to implement
* As we gain more business and more customers, we can add extra functionality on the products. i.e we can implement a color function for the customers to be able to select different product colours.
* We can also implement a sorting functionality so that only products of a certain colour to be desplayed.
* A pre ordering functionality for the products that are soon to be released by Apple so that the customers can pre order them.

---

## TECHNOLOGIES USED

### Languages, libraries and frameworks
* [HTML5](https://en.wikipedia.org/wiki/HTML5): The project uses HTML5 to provide the content and structure.
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets): The project uses CSS3 for styling.
* [jQuery](https://jquery.com) and [JavaScript](https://www.javascript.com): The project uses them for interactive elements.
* [Python](https://www.python.org): The project uses Python to run the application, for build control and management of applications.
* [Bootstrap](https://https://getbootstrap.com/): The project uses Bootstrap for layout, responsiveness and elements.
* [Font Awesome](https://fontawesome.com/): The project uses Fontawesome Icons for icons.
* [Django](https://https://www.djangoproject.com/): The project uses Django as the framework.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/): The project uses Jinja as the templating language.
* [Stripe](https://stripe.com): The project uses Stripe for payment processing.
* [GitHub](https://github.com/stanciudorin?tab=repositories): The project uses GitHub to host the repository.
* [Heroku](https://www.heroku.com/): The project is hosted on Heroku.
* [Gunicorn](https://docs.gunicorn.org/en/stable/): Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
* [Pillow](https://pillow.readthedocs.io/en/stable/handbook/overview.html): The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
* [Psycopg2](https://pypi.org/project/psycopg2/): Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety. 
* Werkzeug Web Server Gateway Interface for debugging and structured error logs.

### Code Editors
* [GitPod](https://www.gitpod.io/): The project was developed in GitPod.

### Additional tools used
* Balsamiq: for developing my wireframes.
* Adobe Lightroom: for developing the logo.  
_No links provided due to both softwares being installed directly on my laptop_

---

## TESTING

### Testing tools

The website has been tested with different tools and on different devices to check its responsiveness, functionality and overall structure.
The following tools and devices have been used to test the website in several different scenarios.

*  Google Chrome Developer Tools: The project used Google Chrome Developer Tools to test responsiveness, styles, and different layouts throughout development. This also allowed the site to be tested on several other mobile devices.

### Devices used for testing

* [Apple MacBook Air](https://www.amazon.co.uk/Apple-dual-core-10th-generation-Intel-Core-i3-processor/dp/B08633F581/ref=sr_1_3?crid=Y6V4SM2K3QKH&dchild=1&keywords=macbook+air+2018&qid=1597952568&sprefix=macbook+air+2018%2Caps%2C202&sr=8-3): the entire project was developed on a 2018 MacBook Air that runs on macOS Catalina.
* [Apple iPad Air 2nd Generation](https://www.amazon.co.uk/Apple-iPad-Air-10-5-inch-Wi-Fi-64GB/dp/B07NHQQ27K/ref=sr_1_16?crid=26JWMWRCVIBDE&dchild=1&keywords=ipad+air+2nd+generation&qid=1597952866&sprefix=ipad+air+2nd%2Caps%2C212&sr=8-16): for testing it's responsivenes on iPads and screens smaller than a regula laptop, I used my iPad Air connected to my lapop wirelesslly. The results were positive as all its functiones worked as normal.
* [Apple iPhone 7](https://www.amazon.co.uk/Apple-iPhone-SIM-Free-Smartphone-Refurbished/dp/B01MUEA4PM/ref=sr_1_5?dchild=1&keywords=Apple+iphone+7&qid=1608274525&sr=8-5): havig all three Apple devices connected to my iCloud Account, I managed to phisically test my website on my iPhone 7 without any issues. The website was responsive and all its functions worked as normal.

### Devices Used For Simulated Testing Within Chrome Dev Tools.

* Samsung Galaxy S9/S9+
* iPhone 6/7/8
* iPhone X
* iPad

I used the following web browsers on both desktop (macOS) and mobile (iOS) where available.
* Google Chrome: Version 84.0.4147.125 (Official Build) (64-bit)
* Safari: Version 13.1.2 (15609.3.5.1.3)

The project was run through both [HTML Validation](https://validator.w3.org) and [CSS Validation](https://jigsaw.w3.org/css-validator/) with no errors found.

---

## DEPLOYMENT

I created my project on GitHub and used GitPod's development environment to write my code. Use the following link to view my live project: [Apple Items](https://appleitems.herokuapp.com/).

### Connecting to GitHub

* I logged into Github, and created a repository, named appleitems.
* I have connected to Gitpod by clicking the green button beside the repo in Github
* Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

### Creation of app in Heroku, and connection

* Log in to Heroku (account is required), within the dashboard, click the "new" button featured in the top right of the page.
* Pick the closest region to you
* Using the CLI, add the heroku app as the remote master branch | heroku git: remote a [app name]

### Deployment to Heroku

* In the created Heroku app, I installed Heroku Postgres (Free Plan) as an add-on in the Resources tab
* To use Postgres, I installed two packages in my project, dj_database_url and psycopg2 and added them to my requirements
* In the Heroku app, I set Config Vars, so any secret information was kept out of version control, the django secret key has been changed from the one that was exposed.
* In the settings.py file, I imported dj_database_url, and set it to be used in production environment
* I used loaddata to import the data from my fixture files into the data models used in production
* I created a superuser for use in production via the command line
* I installed gunicorn, for use as the web server, added it to requirements.txt
* Created a Procfile
* The deployed sites hostname was added to "ALLOWED_HOSTS"
* Before pushing to heroku, DISABLE_COLLECTSTATIC was set to 1, to stop static files being collected during deployment
* Before pushing to Heroku, I pushed my commits to Github
* I then procceded to push to heroku
* After the successful deploy set up Heroku to automatically deploy whenever I push the my project on github.
* I set the SECRET_KEY in settings.py to get it from the environment
* Debug is set to false when not in development environment

---

## CREDITS

### Content
* For this project I have manually created avery single product in the admin panel. All products have been researched by myself and images, titles, descriptions and current prices have been extracted from Currys/PC World website, so every details is current to December 2020 statistics.

### Media
* The Logo was created by myself using Adobe Lightroom.

### Acknowledgements
* My Mentor __Owonikoko Oluwaseun__ for helping me through the project with her advice and guidance.
* Slack Community for their replies and good advices.
* Tutor Support for answering my questions and explaining a few things step by step. A special THANK YOU to Miklos, Haley, Cormac who have also tested my Heroku App and it's functionality and confirmed that it functions corectly.