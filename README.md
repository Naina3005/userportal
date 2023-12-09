# userportal 

User Portal:
Create a sleek, secure website with seamless login, effortless file uploads, and an organized view of uploaded files.

User Interaction:
Enable users to explore peer profiles with a robust search, share files effortlessly, and enhance user experience by displaying shared files.   

#creating virtual Environment 
step-by-step process along with the relevant commands for creating and activating a virtual environment  

Open your terminal or command prompt and run the following command to install virtualenv  
pip install virtualenv 

Navigate to your project directory using the terminal and run the following command to create a virtual environment (replace venv with the desired name of your virtual environment) 

virtualenv env  

Activate the Virtual Environment 

/env/Scripts/activate.ps1 

After that process Virtual Environment has created  

Install Django  

pip  install django   

for starting the project 

django-admin startproject file_upload_project 
cd file_upload_project 
python manage.py startapp file_upload_app 

If your project involves authentication and you want to access the Django admin interface, create a superuser 
python manage.py createsuperuser  

If your app includes database models, run the following command to apply migrations and create the necessary database tables   

python manage.py makemigrations 
python manage.py migrate  

Start the Django development server 

python manage.py runserver 

http://127.0.0.1:8000/  #give result like this   

for Registration 
http://127.0.0.1:8000/register/ 
for Login 
http://127.0.0.1:8000/login/ 
for Upload File 
http://127.0.0.1:8000/upload/ 
for File List  
http://127.0.0.1:8000/file_list/   











