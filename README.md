# getVet
Job hunt made easy for veterans

## Run it locally

### For Windows-

First, clone the repository to your local machine:  

`$ git clone https://github.com/kev5/getVet.git`

Install the requirements:  

`$ pip install -r requirements.txt`

Apply the migrations:  

`$ python manage.py migrate`

Finally, run the development server:  

`$ python manage.py runserver`

The project will be available at 127.0.0.1:8000.

### For macOS-

First, clone the repository to your local machine:  

`$ git clone https://github.com/kev5/getVet.git`

Install the requirements (You might get an error here; don't worry, carry on to the next steps):  

`$ pip install -r requirements.txt`

Install Virtual Environment:  

`$ python3 -m pip install virtualenv`

Run your Virtual Env:  

`$ virtualenv -p python3 env`

Activate your Virtual Env:  

`$ source env/bin/activate`

Install Dependencies:

```
$ pip install django
$ pip install django-crispy-forms
```

Apply the migrations:  

`$ python manage.py migrate`

Finally, run the development server:  

`$ python manage.py runserver`

The project will be available at 127.0.0.1:8000.
