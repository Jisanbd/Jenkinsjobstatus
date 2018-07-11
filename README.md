
Teststatus Tool
================

Purpose of the tool to get the buildstatus from jenkins job of various project and show the result to the dashboard


Description
===========

jenkindata.py : It extracts data from jenkins by using jenkinsapi and upload the data to mysql server.It needed to be set in the linux crontab so that file can be run automatically in fixed time interval.

model.py : It creates the mysql table(ex.Projectname,Jenkinsjobsname and Jenkinsjobsinformation).In order to populate the table in mysql server, please use following commands.

```sh
   python manage.py makemigrations
   python manage.py migrate
```
 
admin.py : It creates default admin page.Run below command to create superuser/admin

```sh
  python manage.py createsuperuser
```


Installation and Run
====================

1. Install requirements.txt by command 

```sh
  pip install -r requirements.txt
```

2. Install and run mysql server. Please see the instructions https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04


3. Create database "firstdatabase" in mysql server

4. In order the extract data from jenkins and upload the data to mysql execute the script jenkindata.py by following command.
  
```sh
  py jenkindata.py
```

5. Run the default server by command

```sh 
  python manage.py runserver
```

6. Launch the browser with the url : http://127.0.0.1:8000/buildstatus/

7. Open the admin page with url : http://127.0.0.1:8000/admin/
  


