# google-image-scrapping
a project for scrapping data and images from google image 

**you can run this codes by two way:**

**1) run codes currently with pyton command**

**2) run with Docker**

--------
**this project based on three phase and you can write each one of them at the same time**

**first phase is taking title and quantities from restAPI server and save it in the postgresql database** 

**in second phase scrapping process is start and image with specified title  will scrap from images.google.com and save image url in mongodb database**

**and in the Third phase data will show user by a graphql server**
______

first way 
---
**run codes currently with pyton command**
first you need to have install git in your system 

after that you can make a new dir and in that start git with this cmd 
```
git init
```

after that you can run this cmd in your dir to achieve the files and apps 
```
git clone https://github.com/hosseinhj1380/google-image-scrapping.git
```
and now files must be in your dir 
you should now install requirements and dependencies in your device 

!!! it recommend to use virtualenv in your dir !!!
you can do that  by read this url  : 
https://docs.python.org/3/library/venv.html

now you need to install requirements in your device :

!!! if you dont need all three phase you can use just requirements in any phase you want !!!

run this command :

```
pip install -r requirements.txt
```

now you had to sure that postgresql and mongodb is install in your device or you can download it from these links:

https://www.postgresql.org/download/

https://www.mongodb.com/atlas/database

create a new database in your postgresql and a new collection in mongodb and put the correct info of your db in the files 
_______
**First phase**
for run this phase you need to just run these command :
for make migrations of  django model run this 
```
python manage.py makemigrations
```
for migrate changes of  model in your Databse run 
```
python manage.py migrate
```
and for run the apps run 
```
python manage.py runserver
```
now you can check this link in your browser or postman 
```
127.0.0.1:8000/api/request/
```
if everything run correctly you can send json aith POST method to this url by this format :
```
{
    "title":"<any title >",
    "quantity":<quantity of image you want >
}
```
_______

** second phase **
before run the second phase you had to downloas webdriver for your browser and give the path of that and import it 
!!! default brower is firefox !!!

after add database info to its file you can make some change in main.py code :
<pre>
	
	obj.download_image("/", urls, req.title)

</pre>
ypu need to make a dir for save images i that and put the correct path instead of "/"

you can start scrapping process by running the main.py :

```
python main.py
```
_____
**Third phase**

at the end you can run this phase to acces images with graphql server 

put the correct info about your mongodb and run :

```
python manage.py runserver 127.0.0.1:8001
```
now you can write query in graphql mode in this url :
```
127.0.0.1:8001/graphql/
```


----------------------------------

**Second way(use docker)**
-----------------------

first make sure to do everything about database in the top 

then make sure to have install docker in your device 
you can download it from this url :

https://www.docker.com/

then you can run docker file and make containner for each phase with this cmd :

```
docker build -t <project-name> .

```
after run correctly this cmd you can run this cmd for run container :
```
docker run -p <real port of device >:<expose port in docker file > <containter name >
```

now its available in url that noticed on the first-phase 


:heart: :heart::star: :star:




