# ⚽Soccer Apparel⚽ (Football Shop Assignment 2 PBP)

**Name:** Sultanadika Shidqi M  
**NPM:** 2406365326  
**Class:** KKI  

🔗 **Link to Pacil Web Service (PWS):**  
(https://sultanadika-shidqi-footballshop.pbp.cs.ui.ac.id/)


# Step by Step on building the Website

1. Create new Django Project
  - created football-shop as its project directory
  - run django-admin startproject football_shop . (to create and start the project)

2. Set up Virtual Environment and add depedencies on requirements.txt
  - set up the virtual environment by doing " python -m venv env "
  - activate the script by doing " env\Scripts\activate ".
  - create requirements.txt file and write its components on it, after that install it 

3. ENV and project configurations
  - create .env file in the root project directory and open the file and fill it with "PRODUCTION=False"
  - fill in the database for the project (this doesnt show at repo)
  - modify the settings.py to set allowed_host for development purposes
  - add database configurations in settings.py

4. Create Main Application
  - create main by doing "python manage.py startapp main"
  - register 'main' in 'settings.py' file

5. Create a template in the templates directory within main
  - Create a new directory named templates inside the main application directory.
  - Inside the templates directory, create a new file named main.html and fill the main.html with mainly (Store title, Name, NPM, and Class)

6. Created Model in models.py:
      name = models.CharField(max_length=120, help_text="Item Name")                                                                    # item name
      description = models.TextField(help_text="Item Description")                                                                      # description of item
      thumbnail = models.URLField(max_length=330, help_text="Image URL")                                                                # image of the item
      price = models.IntegerField(help_text="Price(rupiah)")                                                                            # Price of item in Rp. currency
      category = models.CharField(max_length=50, help_text="Item category (ex: Ball, Boots, Shirt, etc)")                               # category of items
      is_featured = models.BooleanField(default=False, help_text="a Featured Item?")                                                    # featured item 
      rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)],help_text="Drop a rating (0-10)") # for ratings, 0 is min and 10 is max
      brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand name(ex: Puma, Under Armour, Nike)")             # brands in my football store
      stock = models.IntegerField(default=0, help_text="Available stock")                                                               # available stock of items

7. Create function in views.py that consist of Name,NPM,Class

8. Create and apply Model Migrations
   - do python manage.py makemigrations to create model migrations
   - do python manage.py migrate to apply migrations to local database
     
9. Deploying the website:
   - Push the repositories into Github
   - Push the repositories into PWS and deploy it at PWS
   
10. After deployment:
    - After deployment is success copy the website link from PWS and paste it into google
    - if its not success yet then finding the bug to fix it would be the best to do :D

