## Creating Github Repository
### Cloning Repository
After creating Github repository, in somewhere of your computers

	$ git clone github.com-Mujirin:Mujirin/ml_service_using_django.git

## Creating project
### Virtual environment
In this tutorial we are using conda environment, please create one for the poject!.
### Django
#### Installing Django
	$ conda install -c anaconda django
#### Checking its version
	$ python -m django --version
#### Starting the project
	$ django-admin startproject ml_service
	$ cd ml_service
#### Running the development server
	$ python manage.py runserver
See the welcoming site in **localhost:8000/**
### Secret key
- Buat file setara dengan manage.py dengan nama setingan_rahasia.py
- Cut SECRET_KEY di ml_service/setting.py dan taruh di setingan_rahasia.py
- Tambahakan

	from setingan_rahasia import *

di bagian paling atas ml_service/setting.py

## Gitignore
- Buat file .gitignore setara dengan README.md
- Tambahkan di file tersebut

	(Secret key)

	setingan_rahasia.py

	(Ignore Mac system files)
	
	.DS_Store

### Commit to the repo
	$ git status
	$ git add .
	$ git status

Make sure the setingan_rahasia.py did not included in the list file that added to the this commit.

	$ git commit -m "Initial commit."
	$ git push
## Migrations
	$ python manage.py migrate
## Creating superuser
Please adjust to your own information
	$ python manage.py createsuperuser
	$ Username (leave blank to use 'thomas'): mujirin
	$ Email address: mujirin@ui.ac.id             
	$ Password: 
	$ Password (again): 
Superuser created successfully.
Then start the development server

	$ python manage.py runserver

go to the development server in the browser by

	http://localhost:8000/admin/

Enter the username and password
And now, you are in the admin page.