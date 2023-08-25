# I Care
Welcome to the "I Care" repository!

"I Care" is a static web application of a hospital management system that has been developed using HTML, CSS, and Django. The project contains three modules: admin, client, and doctor, which have been designed to provide a comprehensive solution for managing a hospital."I Care" has been developed to provide a comprehensive solution for managing a hospital. It is a user-friendly system that is easy to navigate and helps hospital staff to manage their tasks more efficiently. The project can be customized to meet the specific needs of any hospital and can be easily integrated into existing systems. Overall, "I Care" is a reliable and efficient hospital management system that can help hospitals to provide better care to their patients.
 

![Screenshot (20)](https://github.com/PurnaChandar26/iCare/assets/97793147/30d61368-114b-4794-9cd6-e48deab77612)

## Getting Started
Steps for executing iCare program: 

1. Make sure your pc has all the required python modules. (Requirements attached below)
2. Extract the zip folder.
3. Open a terminal or command prompt and navigate to the project folder of the iCare program. This can typically be done using the "cd" command followed by the path to the project folder. For example:

    cd path/to/iCare-project-folder

4. Then run following Commands:

--> py manage.py makemigrations

{This command prepares the database migrations based on the changes made to the models in the iCare program.}

--> py manage.py migrate

{This command applies the prepared migrations to the database, creating the necessary tables and relationships.}

--> py manage.py runserver

{This command starts the development server, allowing you to access the iCare program through a browser.}

5. Now enter the following URL in Your Browser: http://127.0.0.1:8000/



Requirements:
- python latest version
- django 
	- to install, type 'pip install django' (without quotes) in the windows terminal 
	  also install 'pip install django-widget-tweaks' in the windows terminal
-xhtml
	- to install, type 'pip install xhtml2pdf' (without quotes) in the windows terminal 

## Modules
The "I Care" project contains three modules:

### Admin Module
The admin module is responsible for managing the hospital's operations, such as adding new doctors, creating patient records, and managing appointments. The admin module also allows for the management of hospital staff, including nurses and other medical professionals.

### Client Module
The client module is designed for patients who wish to book appointments with the hospital's doctors. Patients can create an account, view their medical history, and schedule appointments through this module. The client module also allows for patients to receive notifications for upcoming appointments and receive reminders for medication or treatment.

### Doctor Module
The doctor module is designed for hospital staff, including doctors, nurses, and other medical professionals. Through this module, doctors can view their schedules, communicate with patients, and manage their patient records. The doctor module also allows for doctors to receive notifications for appointments, prescriptions, and other important updates.
