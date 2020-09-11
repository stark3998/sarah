

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/stark3998/sarah.git
```
Create a virtual environment and Install Dependencies 

```
python -m venv env
env\Scripts\Activate
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 

#### That's it! Happy Coding!
