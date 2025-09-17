# ⚽Soccer Apparel⚽ (Football Shop Assignment PBP)

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
<img width="1416" height="1154" alt="image" src="https://github.com/user-attachments/assets/187d94dc-03a0-4811-b766-6b102dcbfc9a" />

Extra Explanation: 
1. User sents a request with internet and received it by django
2. Django sends the rquest to its internal and it went to urls.py first
3. urls.py received the request and handle the requent based on its URL pattern
4. After being handled by urls.py, sents the request to view.py
5. View.py work the request with the help of models.py and templates (main.html)
6. models.py work on its database mainly and main.html works more on its structure and context data
7. after view.py got the result with the help of 2, view.py gonna insert the data to placeholder
8. After its inserted, the response is sent to the user


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



# Assignment 3 

__Why do we need data delivery in implementing a platform?__

Data Delivery is Important when implementing a platform because with data delivery it allows information to move between the frontend (what user usually sees) and the backend (mostfully to store data), without the help of data delivery the web will just become a static site without any interactions available

Without a proper data delivery on the website it can cause:
- Delays and failures when it comes to users accessing the website
- Its components cant communicate effectively


__In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?__

In my opinion JSON is more efficient because JSON offers a more clear structure which is easier to learn for beginners, not like XML which is more complex. This reason is what makes JSON more popular than XML


__What is the purpose of the is_valid() method in Django forms, and why do we need it?__ 

The is_valid() method in Django forms is used to check whether the data submitted through the form is valid according to the form’s rules and constraints. 

is_valid() is needed because :

- Prevents invalid data from being saved to the database.
- Ensures data integrity by checking constraints (like field types, min/max values, required fields).
- Provides user feedback by showing errors when the input doesn’t meet the rules.

__Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?__

CSRF (Cross-Site Request Forgery token) is a security feature in Django that protects your forms from malicious requests made by attackers from outside your site.

Why CSRF is needed:

- It ensures that form submissions come only from trusted sources (your own site).
- It prevents attackers from tricking users into unknowingly submitting malicious requests.

How attackers exploit the website:

- The user is logged into site in one browser tab.
- The attacker sends the user a malicious link or page in another tab.
- That page submits a form request to the site (since the user is logged in, their cookies are still valid).
- Without CSRF protection, the server would accept the request as if it came from the real user.


# Step-by-Step Implementation for Assignment 3

**Added 4 new views functions to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.** (Implemented these functions in main/views.py)

__show_xml__

<pre> ```python def show_xml(request): data = FootballItem.objects.all() xml_data = serializers.serialize("xml", data) return HttpResponse(xml_data, content_type="application/xml") ``` </pre>

- takes all FootballProducts object from the database
- To return HTTPS respond with XML type of content
