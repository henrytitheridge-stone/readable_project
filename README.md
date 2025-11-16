# READABLE project
Readable is a social book cataloguing website, built using Django, which could be tailored for children, students and adults alike looking for a clean, simple book-browsing experience. Users can explore a catalogue of novels, read synopses and reviews, create an account to leave their own reviews and get in touch to recommend additions.

## User stories
[Kanban board](https://github.com/users/henrytitheridge-stone/projects/5/views/1)
## Database

## Design

## Features

## Testing

### Validation

## Future developments



## Development & Deployment
- The site was built using Visual Studio Code connected to GitHub via the steps below:
    - Created a local project folder in VS Code and a GitHub repository with the same name
    - Copied the GitHub commands to 'create a new repository on the command line'
    - Pasted and ran these through a new terminal in VS Code
        - This initialised git, made a readme file and pushed a first commit to GitHub

- A virtual environment, Django project and app were created and activated via the steps below:
    - Chose ‘Python: Create environment...’ from the VS Code command palette
    - Selected ‘Venv’, ‘Python 3.12’ and ‘requirements.txt’ to install dependencies
    - Added ‘.venv’ to the ‘.gitignore’ file to exclude it from version control
    - Ran the following commands to install Django, list dependencies, and start a new project:
        - pip3 install Django~=4.2.1
        - pip3 freeze local > requirements.txt
        - django-admin startproject readable .
    - Started the new app by running: python manage.py startapp catalogue
    - Added this to the INSTALLED_APPS in settings.py

- Throughout the project, changes made in VS Code were regularly saved and shared by:
    - Entering 'git add .' into a terminal to stage all changes
    - Entering 'git commit -m' with a succinct summary message to commit the changes
    - Entering 'git push' to push all local changes to the project's remote GitHub repository

### Initial deployment
- The site was initially deployed to Heroku via the steps below:
    - Set DEBUG to False in settings.py and committed changes (repeated for every deployment)
    - Created a new app with the project name from the Heroku dashboard
    - Opened the Settings tab in the new app
    - Added a single config var with a key set to ‘DISABLE_COLLECTSTATIC’ and value of '1'

    - VS CODE: ensured a deployment-compatible server and both local and production hosting by:
        - Installing gunicorn by running: pip3 install gunicorn~=20.1
        - Adding a Procfile to the root directory and the code: web gunicorn readable.wsgi
        - Adding '.herokuapp.com' and '127.0.0.1' to the ALLOWED_HOSTS in settings.py

    - HEROKU: Selected the ‘Connect to GitHub’ deployment method in the Deploy tab
    - Searched for and selected the project repository name to establish the connection
    - Scrolled to 'Manual deploy' and selected 'Deploy branch' to build the live app
    - Above the tabs bar an 'Open app' link was provided to the hosted site

### Final deployment
- To maintain deployment-ready status as the project grew, a series of adjustments were needed:
#### Database
- The following steps were taken to connect to a new database and access the admin panel:
    - Created a PostgreSQL instance using the Code Institute login, emailed as a link
    - Pasted the url into a new env.py file as a setdefault("DATABASE_URL", ...)
    - Added env.py to the .gitignore to keep secure data from being pushed to GitHub
    - Connected the database by running:
        - pip3 install dj-database-url~=0.5 psycopg2~=2.9
        - pip3 freeze --local > requirements.txt
    - Imported env into the settings.py file to access the database url
    - Commented out the local sqlite3 database connection
    - Ran 'python manage.py migrate' to add default apps to the database
    - Ran 'python manage.py createsuperuser' and added details to login to the admin dashboard
- DEPLOYMENT: Added a DATABASE_URL config var to the Heroku app
#### Secret keys
- To secure the database, secret keys were generated and activated via the steps below:
    - Generated a random key and added it to a "SECRET_KEY" environment variable in env.py
    - Replaced the insecure SECRET_KEY in settings.py with the environment variable
- DEPLOYMENT: Added a SECRET_KEY config var to the Heroku app with a newly-generated key
#### Static files
- The following steps were taken to ensure static files loaded correctly on deployment:
    - Added a STATIC_ROOT path to 'staticfiles' underneath the STATIC_DIRS in settings.py
    - Installed whitenoise (to enable Heroku to run 'collectstatic' automatically) by:
        - Running 'pip3 install whitenoise~=5.3.0' and 'pip3 freeze --local > requirements.txt'
        - Adding the whitehoise MIDDLEWARE and backend STORAGES to settings.py
    - Ran 'python manage.py collectstatic' to create staticfiles directory and initial cache
    - Added 3.12 to .python-version file
- DEPLOYMENT: Remove DISABLE_COLLECTSTATIC config var from the Heroku app before re-deploying
#### Forms and HTTP methods
- Finally, the site was protected against Cross-Site Request Forgery by: 
    - Adding //localhost and //*.herokuapp.com domains to CSRF_TRUSTED_ORIGINS in settings.py
- DEPLOYMENT: This ensured that malicious sites would be prevented from tricking users' browsers into submitting unauthorised data to either the local or hosted site

## Credits
- Example code from the Code Institute 'I Think Therefore I Blog' walkthrough project
- Book information from [Penguin](https://www.penguin.co.uk/discover/articles/100-must-read-classic-books) and [Amazon](https://www.amazon.co.uk/books) 
- Preview screens from [Am I Responsive?](https://ui.dev/amiresponsive)
- PEP8 validation run through the [CI Python Linter](https://pep8ci.herokuapp.com/)