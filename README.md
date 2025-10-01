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

<pre> 
  def show_xml(request): 
    data = FootballItem.objects.all() 
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml") 
</pre>

- takes all FootballProducts object from the database
- To return HTTPS respond with XML type of content


__show_json__

<pre>
  def show_json(request):
    data = FootballProducts.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")
</pre>

- return HTTPS respond with json type of content
- and takes all FootballProducts object from the database

__show_xml_by_id__

<pre>
def show_xml_by_id(request, id):
    try:
        data = FootballProducts.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", data)
        return HttpResponse(xml_data, content_type="application/xml")
    except FootballProducts.DoesNotExist:
        return HttpResponse(status=404)
</pre>

- Include error handling when FootballProduct items does not exist
- Accepts ID as a parameter

__show_json_by_id__

<pre>
  def show_json_by_id(request, id):
    try:
        data = FootballProducts.objects.filter(pk=id)
        json_data = serializers.serialize("json", data)
        return HttpResponse(json_data, content_type="application/json")
    except FootballProducts.DoesNotExist:
        return HttpResponse(status=404)
</pre>

- Include error handling when FootballProduct items does not exist
- Accepts ID as a parameter

**Created URL routings for all 4 new views** (Implemented these functions in main/urls.py)

<pre>
  from django.urls import path
from main.views import show_main, create_football_product, product_details, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_football_product, name='create_football_product'),
    path('product/<str:id>/', product_details, name='product_details'),
    path('product/xml/', show_xml, name='show_xml'),
    path('product/json/', show_json, name='show_json'),
    path('product/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('product/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
</pre>

__small addition__
- create-product/ : create product purposes
- product/str:id : product details by ID
- product/xml/ : show items in xml format
- product/json/ : show items in json format
- product/xml/int:id/ : returns specific xml format item based on its ID
- product/json/int:id/ : returns specific json format item based on its ID

**Created Main webpage with features in main.html**

__Features Added__

- View Product Detail button
- Display item image based on its URL
- shows brand, name price of the product
- Add product button below name,npm,class details

**Created Details in product_details.html**

__product_details_page_info__

- Displayed when the product is created in website
- Displayed the price of the product
- Displayed the thumbnail of the product
- Displayed the Product name in big font
- Displayed the short details of product
- Displayed tags of the product for easier search

__Created a file "create_football_product.html"__

#  Feedback for the teaching assistant for Tutorial 2
No Feedback from me as the tutorial already helped me alot :D

# Postman IMG

JSON 
<img width="1457" height="939" alt="Screenshot 2025-09-17 113534" src="https://github.com/user-attachments/assets/27cb3f99-e740-4e63-88d0-557911e77c26" />

XML 
<img width="1456" height="928" alt="Screenshot 2025-09-17 113618" src="https://github.com/user-attachments/assets/757c9cf6-00e4-4d8b-8653-4571b8e2088e" />

JSON BY ID
<img width="1463" height="957" alt="Json by ID" src="https://github.com/user-attachments/assets/ef4e01ed-e498-4efa-a541-e878cb0c15e5" />

XML BY ID
<img width="1460" height="965" alt="product xml by id" src="https://github.com/user-attachments/assets/2b6dc502-4fdc-4e07-b70a-16b368080b85" />


# Assignment 4

__What is Django's AuthenticationForm? Explain its advantages and disadvantages__

AuthenticationForm is a built-in form from django.contrib.auth.forms and it’s used for handling user login.
Under the hood, it has two fields:
- username
- password

__Advantages of AuthenticationForm__

1. Well Secured
Handles password validation securely (using Django’s hashing).
Protects against timing attacks and common security flaws.

2. Ready to use
No need to build own login form

3. Integration with Django’s auth system
Works seamlessly with login() and authenticate().
Supports features like is_active, user permissions, etc.

__Disadvantages of AuthenticationForm__

1. Rigid fields
Only supports username + password by default.
Must be extend inorder to login with email/phone number

2. Basic UI
No styling — it just provides form fields. You must customize the HTML rendering.

 3. Limited error messages
Default messages are generic (“Please enter a correct username and password”). 

4. Coupled to Django’s built-in User model
Doesnt fit well with heavy authentication system


# What is the difference between authentication and authorization? How does Django implement the two concepts?

Authentication = Verifying who the user is. (Login process)
Authorization = Controlling what the authenticated user is allowed to do. (Permissions & access control)

How Django Implements the Two Concept (Authentication and Authorization):

__Authentication in Django__

- Django has the Authentication System inside django.contrib.auth.
  It provides: User model (with fields: username, password, email, etc.).

- Built-in functions:
   - authenticate(request, username, password) 
   - login(request, user) 
   - logout(request)

__Authorization in Django__

Once authenticated, Django enforces permissions & groups:
  -  is_authenticated → simple check if user is logged in.
Decorators:
  -  @login_required (User needs to be logged in inorder to do stuff in the website)
  -  

# What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?

__Cookies__

Benefits:
- Stored on client side → no server storage needed.
- Lightweight & fast → small key-value pairs (like theme=dark, lang=en).
- Persistent → can survive browser restarts (if not expired).
- Cross-request availability → automatically sent with each HTTP request to the same domain.

Drawbacks:
- Security risks → vulnerable to theft via XSS if not secured (e.g., stolen cookies can hijack sessions).
- Size limit → usually max 4KB per cookie.
- Can be disabled by users in browsers.
- Visible to client → not good for sensitive data (like passwords).

__Sessions__

Benefits:
- Secure → sensitive data is stored server-side (client only gets a session ID cookie).
- Flexible storage → can be stored in DB, cache, or files.
- Scalable → can store larger data than cookies (not limited to 4KB).
- Built-in expiration → can automatically log users out after inactivity.

Drawbacks:
- Requires server storage → increases memory/DB usage as users grow.
- Session management overhead → need cleanup of expired sessions.
- Not shared across domains → sessions are tied to one app/server.
- Slightly slower → extra DB/cache lookup for every request.

# in web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?

No. By default, cookies are not inherently secure — they’re just small text stored in the browser. If not configured properly, they can be stolen, modified, or misused.

__Risks of cookies:__
- XSS (Cross-Site Scripting) → attacker injects JavaScript to steal cookies.
- CSRF (Cross-Site Request Forgery) → attacker tricks browser into sending cookies to perform actions.
- Man-in-the-Middle (MITM) attacks → if cookies are sent over HTTP (not HTTPS), they can be intercepted.
- Session Hijacking → if a session cookie (sessionid) is stolen, attacker can impersonate the user.

__How Django Handles Cookie Security:__
- HttpOnly flag → prevents JavaScript from accessing cookies (mitigates XSS).
- Django sets HttpOnly=True for session cookies by default.
- Secure flag → ensures cookies are only sent over HTTPS.
- CSRF protection → Django includes the {% csrf_token %} system to ensure cookies can’t be abused in CSRF attacks.


# Step by Step Implementation:

__Create User Registration__:
- Added Imports to views.py
<pre> 
  from django.shortcuts import render, redirect, get_object_or_404 
  from main.forms import FootballProductsForm 
  from main.models import FootballProducts from django.core import serializers 
  from django.http import HttpResponse from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
  from django.contrib import messages from django.contrib.auth import authenticate, login, logout 
  from django.contrib.auth.decorators import login_required import datetime 
  from django.http import HttpResponseRedirect     
  from django.urls import reverse 
</pre>

- Created login_user Function in views.py
<pre>
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
</pre>

- Created function to logout in views.py
<pre>
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
</pre>

- Created function to register in views.py
<pre>
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
</pre>

- Created file named register.html to link it to the register function
- Created login.html for users to login

- configurate the path in urls.py
<pre>
from django.urls import path
from main.views import show_main, create_football_product, product_details, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
app_name = 'main'

  urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_football_product, name='create_football_product'),
    path('product/<str:id>/', product_details, name='product_details'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('product/xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('product/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]   
</pre>

__connect product model with user model__:

- configured the models.py
<pre>
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator # for rating

class FootballProducts(models.Model):
    name = models.CharField(max_length=120, help_text="Item Name")
    description = models.TextField(help_text="Item Description")
    thumbnail = models.URLField(max_length=330, help_text="Image URL")
    price = models.IntegerField(help_text="Price(rupiah)")
    category = models.CharField(max_length=50, help_text="Item category (ex: Ball, Boots, Shirt, etc)")
    is_featured = models.BooleanField(default=False, help_text="a Featured Item?")
    rating = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)],help_text="Drop a rating (0-10)")
    brand = models.CharField(max_length=100, blank=True, null=True, help_text="Brand name(ex: Puma, Under Armour, Nike)")
    stock = models.IntegerField(default=0, help_text="Available stock")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
</pre>
Added: user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

- Make migrations
  do python manage.py makemigration and python manage.py migrate

- Updated show_main function in views.py
<pre>
  @login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        football_products = FootballProducts.objects.all()
    else:
        football_products = FootballProducts.objects.filter(user=request.user)

    context = {
        'npm' : '2406365326',
        'name': request.user.username,
        'class': 'PBP KKI',
        'football_products' : football_products,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

</pre>
  - updated create_football_product function in views.py
<pre>
    @login_required(login_url='/login')
def create_football_product(request):
    form = FootballProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        football_product = form.save(commit=False)   
        football_product.user = request.user         
        football_product.save()                      
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_football_product.html", context)
</pre>

__Pushed the website to github and Pacil Web Service__
- pushed to github branch master
- pushed to pacil web service

__Created Dummy User and Password for website__

User     : testuserwebsite1
Password : Password123keren

User     : testuserwebsite2
Password : Password123keren

# ASSIGNMENT 5

# CSS Selector Priority: If multiple CSS selectors target an HTML element, explain the priority order for CSS selector selection

CSS Selector Priority Order:

- 1. Inline styles
     
  Example: <div style="color:red;">
  Inline styles have the highest priority .
  IDs (#id)
  Example: #main { color: blue; }
  

- 2. Classes, Attributes, and Pseudo-classes
     
  Examples:
  Class: .button{ ... },
  Attribute: [type="text"]{ ... },
  Pseudo-class: :hover, :first-child,
  

- 3. Elements and Pseudo-elements
     
  Examples:
  div { ... },
   h1 { ... }, 
   ::before, ::after.

Special Rules:

!important

Overrides normal specificity rules. But if two !important rules conflict, then specificity decides. If two selectors have the exact same specificity, the one written later in the CSS file takes precedence.

# Why is responsive design important in web application development?

1. Adaptive to any Device 

Users access websites from desktops, laptops, tablets, and smartphones — all with different screen sizes and resolutions. Responsive design ensures the site adapts automatically so it looks and works well on any device.
  
2. Better User Experience (UX)

A non-responsive site may force users to zoom, scroll horizontally, or struggle with navigation. Responsive design improves readability, usability, and accessibility, leading to happier users.

3. Mobile-First Era

The majority of internet traffic now comes from mobile devices. If a website isn’t mobile-friendly, users often leave immediately.

4. Able to adapt with future devices 

New devices with varying screen sizes keep emerging (foldable phones, smart TVs, etc.). A responsive approach ensures the design can adapt to future devices without starting from scratch.

# Examples of applications that have and haven't implemented responsive design (Explain the reasons behind your examples)

Applications with Responsive Design:

1. Twitter 

Desktop mode, theres a three-column layout (sidebar, feed, trends). Mobile mode, it collapses into a single scroll feed, with the menu hidden behind a hamburger icon.

Reason:
Because twitter is heavily mobile-driven. A responsive design ensures consistent user experience across devices, keeping users engaged without needing a separate mobile app for browsing.

2. YouTube

Desktop mode, YouTube shows grid thumbnails + sidebar navigation. Mobile mode, the sidebar becomes a bottom tab bar, and videos take full width.

Reason:
YouTube’s massive mobile audience means responsive design is key to ensuring videos remain the focus, no matter the screen size.


Applications without Responsive Design: 

1. Old Government Websites (Usually built with HTML only (1990-2000s)

Many older sites were built only for desktop screens, showing fixed-width layouts that require horizontal scrolling on mobile.

Reason:
They were created before mobile became dominant and never updated. They rely on outdated frameworks, so poor UX persists on smaller devices

2. Some University/College Portals

Course registration systems often don’t resize properly, with small buttons and forms that break on mobile.

Reason:
These portals are usually developed for internal use with a desktop-first mindset, prioritizing functionality over accessibility. Maintenance budgets are limited, so responsiveness is often ignored.

# Differences between margin, border, and padding, and how to implement them
1. Margin

What it is:
The outer space outside the element’s border.

Purpose:
Creates spacing between elements.

Doesn’t affect:
The element’s size or background color (margin is always transparent).

2. Border

What it is:
The edge line surrounding the padding and content.

Purpose:
Visually outlines the element.

Affects size:
Borders add to the total element width/height.

3. Padding

What it is:
The inner space between the content and the border.

Purpose:
Creates breathing room inside the box.

Affects background:
Padding inherits the element’s background color or image.

Implementation Example of them:

<pre>
  .box {
  margin: 20px;             /* gives space around the box */
  border: 5px solid white;  /* this border around padding & content */
  padding: 10px;            /* create a space between text and border */
}
</pre>

# Explain the concepts of flexbox and grid layout along with their uses # 

-Flexbox:

Flexbox is a one-dimensional layout system that arranges items in a row or column. It’s best for aligning and distributing space between elements, like navbars, buttons, or lists.
Example:

<img width="577" height="554" alt="image" src="https://github.com/user-attachments/assets/59585726-b566-484f-8e7e-e6ad12d60879" />

- Grid:
Grid is a two-dimensional layout system that works with rows and columns simultaneously. It’s ideal for building full web page layouts, dashboards, or galleries where precise placement is needed.
Example:

<img width="725" height="523" alt="image" src="https://github.com/user-attachments/assets/dbecb05a-fcdf-4b11-84ea-82a8dd829cfb" />


Implementation Steps:  Checklist step-by-step

- SET UP TAILWIND ON BASE.HTML

- MADE FILES THAT HAS A FUNCTION FOR (CONSISTS OF VIEWS.PY, MODELS.PY, HTML FILES, URLS.PY)
  1. edit_product
  2. create_product
  3. navigation bar
  4. login
  5. logout
  6. about (without model cause only consist extra info)
  7. contact (without model cause only consist extra info)
  8. product_detail

- DESIGNED THE WEBSITES WITH TAILWIND CSS (ON ITS HTML FILES)
- RENDERED THE WEBSITE ON VIEWS.PY AND SHOWED THE PATH WITH URLS.PY
- APPLIED CARD DESIGN ON EACH PRODUCT ALSO APPLIED EDIT OR DELETE FUNCTION
- APPLIED IMAGE WHEN NO PRODUCT IS AVAILABLE
- ADDED NAVIGATION BAR FOR MOBILE AND DESKTOP
- DEPLOYED WEBSITE TO PWS AND PUSHED CODE TO GITHUB AND MADE README.MD
  
     
  











