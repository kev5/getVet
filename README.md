[Devpost BostonHacks 2018 Submission](https://devpost.com/software/vetme-us-fqkplv)

# getVet
Job hunt made easy for veterans

## Run it locally

### For Windows-

1. First, clone the repository to your local machine:  

    `$ git clone https://github.com/kev5/getVet.git`

2. Install the requirements:  

    `$ pip install -r requirements.txt`

3. Install Virtual Environment:  

    `$ pip install virtualenv`

4. Run your Virtual Env inside the main directory:  

    `$ python -m virtualenv .`

5. Activate your Virtual Env:  

    `$ Scripts\activate`

6. Apply the migrations:  

    `$ python manage.py migrate`

7. Finally, run the development server:  

    `$ python manage.py runserver`

The project will be available at 127.0.0.1:8000.

### For macOS-

1. First, clone the repository to your local machine:  

    `$ git clone https://github.com/kev5/getVet.git`

2. Install the requirements (You might get an error here; don't worry, carry on to the next steps):  

    `$ pip install -r requirements.txt`

3. Install Virtual Environment:  

    `$ python3 -m pip install virtualenv`

4. Run your Virtual Env inside the main directory:  

    `$ virtualenv -p python3 env`

5. Activate your Virtual Env:  

    `$ source env/bin/activate`

6. Install Dependencies:

    ```
    $ pip install django
    $ pip install django-crispy-forms
    ```

7. Apply the migrations:  

    `$ python3 manage.py migrate`

8. Finally, run the development server:  

    `$ python3 manage.py runserver`

The project will be available at 127.0.0.1:8000.
