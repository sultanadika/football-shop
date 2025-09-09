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
  - created requirements.txt file and write its components on it, after that install it 

3. ENV and project configurations
  - created .env file in the root project directory and open the file and fill it with "PRODUCTION=False"
  - fill in the database for the project (this doesnt show at repo)
  - modify the settings.py to set allowed_host for development purposes
  - add database configurations in settings.py

4. Create Main Application
  - created 'main' application by doing "python manage.py startapp main"
  - register 'main' in 'settings.py' file

5. Create a template in the templates directory within main
  - Created a new directory named templates inside the main application directory.
  - Inside the templates directory, createa a new file named main.html and fill the main.html with mainly (Store title, Name, NPM, and Class)

6. Created model with the required models in models.py

7. Created a function in views.py that consist of Name,NPM,Class

8. Creating and apply Model Migrations
- do python manage.py makemigrations to create model migrations
- do python manage.py migrate to apply migrations to local database
     
9. Deploying the website:
- Push the repositories into Github
- Push the repositories into PWS and deploy it at PWS
   
10. After deployment:
- After deployment is success copy the website link from PWS and paste it into github and scele 
- if its not success yet then finding the bug to fix it would be the best to do :D

Website is done and well finished :D 🥇💯

# Diagram showing the client request to the Django-based web application and its response
On development 

# Role of Settings.py in a Django Project

🔑 1. Project Configuration

Defines key configurations such as: 
- INSTALLED_APPS → active apps in the project (e.g., main, django.contrib.admin).

- MIDDLEWARE → layers that process requests and responses

- ROOT_URLCONF → tells Django which urls.py file to use. (in this case i used 'football_shop.urls')

2. Database Settings

- Located in the DATABASES dictionary.
- Defines which database you’re using (SQLite, PostgreSQL, MySQL, etc.).

3. Internationalization & Localization
Settings for time zones, language, and date formats.
<pre>   LANGUAGE_CODE = 'en-us' 
  TIME_ZONE = 'UTC' 
  USE_I18N = True 
  USE_TZ = True  
</pre>

4. Security

- DEBUG = if True, errors are shown (only in development).

- ALLOWED_HOSTS = defines which hosts can access your site (important for deployment).


# How does database migration work in Django

Database Migration:
In Django, migrations are the way Django translates changes in your models.py into actual database schema changes (tables, columns, constraints).

Process of database migration:
- Creating a Migration
  <pre> python manage.py makemigrations </pre>
  - Creates new Migration files 
  - This also will make Django compare the current models with the last migration ever did

- Running Migration
  <pre> python manage.py migrate </pre>
  - Django executes the instructions in the migration files.
  - Easy to use because it will automatically update to the newest models when migrating
  - Can be modified in anytime and simple to use


# Why is the Django framework chosen as the starting point for learning software development?

1. Large Community & Documentation
- Django has excellent official documentation and a huge global community. Beginners can easily find tutorials, guides, and answers to common problems.

2. Fast Development
- Django was designed to help developers build applications quickly. For beginners, this means you can see results fast (like building a blog or store in just a few steps), which keeps learning motivating and fun.

3. Clear Project Structure
- Provides an organized folder and file layout making it easier to maintain code and follow good development practices.
- Model View Template which it is really easy to learn.

4. Ready to use Framework
- Used by famous companies (ex: Instagram, Mozilla, etc)
- Teaches the best practice that are applicable on industries
- Great Production features

5. Friendly Learning Framework:
- Has a very high and detailed documentation which it helps new developers on studying django
- Very good for debugging code as the error notice are mostly easy to understand
  
#  Feedback for the teaching assistant for Tutorial 1

No feedback from me, The tutorial is so easy to understand and i could say is fun to learn from it!

