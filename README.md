# Constcollection

A Django Hackathon project.

[Link to deployed site](https://hackathon-constcollection-e94b800f4c67.herokuapp.com/)

[Link to the project GitHub](https://github.com/users/SourTarte/projects/7/views/1)

[Link to project KanBan](https://github.com/users/SourTarte/projects/7)

Constcollection is a student Hackathon project who's premise is to create a response, accessible website for the artist Cecilia Kristoffersson.


<images>


# Table of Contents

- [User Experience and Design](#user-experience-and-design)
    - [Agile Methodology](#agile-methodology)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Wireframes](#wireframes)
    - [Colour](#colour)
    - [Fonts](#fonts)
- [Features](#features)
    - [Admin](#admin)
    - [Navbar](#navbar)
    - [Footer](#footer)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
    - [Manual Testing against User Stories](#manual-testing-against-user-stories)
    - [Code Validation](#code-validation)
    - [Lighthouse Testing](#lighthouse-testing)
- [Bugs](#bugs)
- [Use of AI](#use-of-ai)
- [References and Credits](#references-and-credits)


# User Experience and Design

The site goal is to create a responsive, accessible website that showcases the art of Swedish artist Cecilia Kristoffersson. This minimalist site is intended to focus the users' attention on the works created by Cecilia, while also offering additional pages to learn more about the artist, their collections and exhibitions.

The site allows the artist to upload, modify, and delete works through the front end of the site without needing access to the Django admin panel.

Future versions of the site would include avenues for direct sale of available works by the artist, thought that functionality is not intended for the initial version of the site.

## Agile Methodology ##

Development follows the principle of Agile development. The project KanBan board can be found here:

[Link to project KanBan](https://github.com/users/SourTarte/projects/7)

## Entity Relationship Diagram (ERD) ##

![ERD](documentation/ERD.png)

Here we have a Media model, which holds any images or videos the artist wants to display on the site. For the MVP we focused on displaying images foremost, but wanted to have the capability of storing videos later. The Media model had a clean method that only allowed either a video or an image, but not both and not neither. This is so one Media object only references one piece of media. 

The Category model stores information about the 'types' of art the artist paints. She had several different categories with explanations of this, stored in the information field. One category could be linked to many pieces of media.

The AboutSection model stores information on exhibitions, the artist's biography, and any press information - essentially information that is not directly linked to pieces of art. The AboutSection has a many to many relationship with media, so that for example, a section on an exhibition can inlude art pieces, photos, or videos of the event. 

The ERD needed no reference to the User model none of the objects were linked to a user. We only have one or two users - the artist or curator who wants to update the site.

## Wireframes ##

Mobile:

![Mobile Wireframes](documentation/artistwireframesmobile.webp.png)

![Desktop Wireframes](documentation/artist_wireframes.webp)


## Colour ##


## Fonts ##


# Features #

Admin panel to add, edit or delete Media, Art Categories, Exhibitions, or About sections.

This has tabs for each form, and the forms are scrollable with buttons to edit or delete existing objects.

There is no functionality to register a user so this is only avaliable to the artist/curator who is given a log in. 

![Admin Panel Add](documentation/Admin-panel1.png)

![Admin Panel Edit/Delete](documentation/Admin-panel2.png)

A navigation bar accessible through a toggle on the right, so as to not ditract from the art:

![Admin Panel](documentation/Navigation.png.png)

Welcome page:

![Welcome](documentation/Welcome.png)

Gallery to display all art pieces:

![Gallery](documentation/Gallery1.png)

About the artist:

![About](documentation/About.png)

Exhibitions:

![Exhibitions](documentation/Exhibitions.png)


# Technologies Used #

## Languages
- **Python 3** – Main backend language (Django framework)
- **HTML5** – Markup for templates
- **CSS3** – Styling, including Bootstrap classes
- **JavaScript** – For interactive elements (if used)

## Frameworks & Libraries
- **Django** – Main web framework for backend and templating
- **Bootstrap 5** – Responsive front-end framework for layout and components
- **Cloudinary** – Image hosting and management for media files
- **Gunicorn** – WSGI HTTP server for deploying Django on Heroku
- **psycopg2** – PostgreSQL database adapter for Django
- **dj-database-url** – For parsing database URLs from environment variables
- **whitenoise** – For serving static files in production

## Database
- **PostgreSQL** – Production database (hosted on Neon.tech)

## Deployment & Hosting
- **Heroku** – Cloud platform for deployment
- **GitHub** – Version control and project management

## Tools & Services
- **Git** – Version control
- **GitHub Projects** – Kanban board for Agile workflow
- **VS Code** – Main code editor
- **Cloudinary** – Media storage and delivery
- **Django Admin** – For backend content management

## Other
- **pip** – Python package manager
- **venv** – Virtual environment for dependency management

# Deployment #

This project was deployed on Heroku, pulling from GitHub.

#### To enable deployment:  

Ensure all sensitive information, such as your SECRET_KEY and DATABASE_URL, are stored as environment variables and not visible in your project code. Set DEBUG in settings.py to 'False'.

Install requirements.txt - the important installations for deployment are gunicorn for serving the application, and whitenoise for handling static files.  

Add a Procfile at the root of your project, with the content: "web: gunicorn {project_name}.wsgi".  
Add a .python-version file specifying your version of Python.

Add '.herokuapp.com' to ALLOWED_HOSTS within your project's settings.py.  
Add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS within your project's settings.  

Commit and push your code to GitHub, on the branch you want to deploy from.   

#### To deploy:
Navigate to your Heroku dashboard.  
Create a new Heroku app.  
Select the region closest to you for deployment. 

Generate a secret key to be used with Heroku. This should be a different key to the one used in your project code.    
Go to the settings tab and select Config Vars.  
Add these two keys:  
-- DATABASE_URL : {your_project's_database_url}  
-- SECRET_KEY : {your_secret_key}  

Navigate to the deploy tab.  
Connect to GitHub and select your project repository.  
Select 'Manual Deploy' and choose the branch you want to deploy from.  
Click 'Deploy Branch'.    

# Testing #

All colour contrast meets WCAG AAA 

## Manual Testing against User Stories ##

## Code Validation ##

## Lighthouse testing ##

# Bugs #

# Use of AI #

AI in the form of Copilot and GitHub Copilot has been used throughout the development of this project. Uses have primarily been:

- Generation and refinement of User Stories for the project KanBan
- Searching for answers in documentation
- Code generation, including code using Bootstrap and Django Template Language
- Accellerated debugging of code


# References and Credits #


This project is inspired in large part from the "I Think Therefore I Blog" project that is a key part of Code Institutes full-stack web development course.

Copilot uses the collective knowledge of hundreds of millions, and has helped created code for this project. 