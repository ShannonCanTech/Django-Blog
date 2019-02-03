# Django Blog

Django blog with Bootstrap 4. Utlizes SQlite3 and default admin function.

*__Note: For CRUD implementation, download and run the branch design-testing.__*

![screenshot](https://github.com/ShannonCanTech/Django-Blog/blob/master/blog/static/images/home_page_screenshot.png)

![screenshot](https://github.com/ShannonCanTech/Django-Blog/blob/master/blog/static/images/post_details_screenshot.png)

## Getting Started

You can follow along to [DjangoGirl's Blog tutorial](https://tutorial.djangogirls.org/en/) and add your own touches, properies, and actions.

### Prerequisites

Install [Git](https://git-scm.com/downloads).

Check whether Python is installed:
```
$ python --version
```
Check for pip installation:
```
$ pip3 --version
```
#### If no installation found:
Recommened to have either Homebrew (for Mac and Linux users) oor Chocolately (for Windows users) installed. You will use either of these to install Python 3. Follow the installation instructions for installing either Homebrew or Chocolately. For Chocolately, I recommend using __Windows PowerShell__.

*Note that you may need to [change the execution policy in Windows PowerShell to bypass](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-6)*.

Once chocolately or homebrew is installed, install Python 3 as an administrator by running either commands

Windows

```
choco install python3
```

Mac or Linux

```
brew install python3
```

This will install Python 3 at C://Python37.

Open Git Bash and run:
```
$ python --version
$ pip3 --version
```

#### Upgrade pip in bash:
```
$ python -m pip install --upgrade pip
```

I used VS Code as my editor of choice and installed pylint:
```
$ pipenv shell
$ pipenv install pylint --dev
```

### Installing

Create a directory to store your project in:
```
$ mkdir myprojectfolder
$ cd myprojectfolder
```
Install pipenv:
```
$ pip3 install --user pipenv
```
Install Django:
```
$ pipenv install django
```
Start shell:
```
$ pipenv shell
```

## The Database

### Create tables for models in the database
```
$ python manage.py makemigrations blog
$ python manage.py migrate blog
```

Create your own superuser login credentials to access the admin features.

http://127.0.0.1:8000/admin shows Django administrator page.

To start it, you must run:
```
$ python manage.py migrate
$ python manage.py runserver
```
While the virtual enviroment is active, press CRTL+C (or CMD+C) and enter the following command:
```
$ python manage.py createsuperuser
```
Input a username and password. You can choose a default username by pressing enter.

Once completed, run:
```
$ python manage.py runserver
```
Log into the admin portal.

### Creating a queryset with default SQLite3

You can either add posts object models through the admin page (easier) or via the terminal. Run:
```
$ python manage.py shell
```
This will start the Django interactive console, where you can add and modify posts.

Import Post:
```
>>> from blog.models import Post
```
Import user:
```
>>> from django.contrib.auth.Models import User
```
Show all querysets:
```
>>> Post.objects.all()
```
To add a new queryset:
```
>>> me = User.objects.get(username="my.username")
>>> Post.objects.create(author=me, title='The Post Title', text='This is my post's text')
```
To exit:
```
>>> exit()
```

#### Posts created via admin portal
![screenshot](https://github.com/ShannonCanTech/Django-Blog/blob/master/blog/static/images/admin_page_screenshot.png)

## Deployment

Ensure the virtual enviroment is active, migrate, and runserver. You may need to log into the admin portal again but should have no issue viewing your post list and individual post details.

## Built With

* [Python](https://docs.python.org/)
* [Django](https://docs.djangoproject.com/en/2.1/) - Web framework
* [Bootstrap](https://getbootstrap.com/docs/4.2/getting-started/introduction/) - Front end framework, great tool to get UI/UX friendly basic designs and animations

#### Before Bootstrap
![screenshot](https://github.com/ShannonCanTech/Django-Blog/blob/master/blog/static/images/home_page_progess_screenshot.png)

## Authors

* **Shannon Foster** - [@SheCanTech](https://twitter.com/@SheCanTech) - [LinkedIn](https://Linkedin.com/in/SheCanTech)


## Acknowledgments

* Thanks Django Girls for the amazing tutorial
* And WSVincent for the alternative "Getting Started" suggestions
