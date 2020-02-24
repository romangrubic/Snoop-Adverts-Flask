## Data Centric Development Project - Code Institute
---
# Snoop
Tired or signing up just to place your toaster or TV for sell? Tired of unwanted spam mail in your e-mail about adverts that don't interest you?
With **Snoop** you don't have to give your e-mail or phone number! No more long sign-up process and you have more time to snoop for a good deal on that car you like!

#### A live demo is hosted [here](https://adverts-project.herokuapp.com/home)

---
## Summary
* [Project Background](#project-background)
* [User Experience](#ux)
    * [User Stories](#user-stories)
    * [Five planes](#strategy)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Technology used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

---

## Technology used

* HTML5 & CCS3: Essential languages used to build a websites foundations.
 
    - https://en.wikipedia.org/wiki/HTML5
    - https://en.wikipedia.org/wiki/Cascading_Style_Sheets
* Bootstrap: An easy to use, responsive framework. Bootstrap was used to allow easy implementation of the overall responsivness and contact modal. Bootstrap's 
grid system was also used for simplicity and efficiency.
    
    - https://getbootstrap.com/
* Font Awesome: A vast and free library of responsive icons. This library was used for the social link icons found in the footer.
    
    - https://fontawesome.com/
* JavaScript and jQuery: These technologies were essential for the functioning of Email.js in order for user to contact me.
    
    - https://jquery.com/
* EmailJS: Service that helps sending emails using client side technologies only. It only requires to connect EmailJS to one of the supported email services, 
create an email template, and use their Javascript library to trigger an email. This was used for contact modal so that user's can get in contact with me. 
    
    - https://www.emailjs.com/
* Python: Python is an interpreted, high-level, general-purpose programming language. In this project it was used to manage the back end development of the project.

    - https://www.python.org/
* Flask: Lightweight WSGI web application framework. It is designed to make getting
 started quick and easy, with the ability to scale up to complex applications.

    - https://palletsprojects.com/p/flask/
* MongoDB: NoSQL document-oriented database program that uses JSON like documents with schema used by the site to store user adverts.

    - https://www.mongodb.com/
* Github: Provides hosting for software development version control using Git and is used to store this projects repository.

    - https://github.com/
* Heroku: Cloud platform as a service supporting several programming languages and is used to deploy this project
    
[Back to top](#summary)

---

## Deployment
The project was written and developed in the Gitpod IDE.

A local repository was intialized using Git. Regular changes were commited to the local repository.

The process for deployment on Heroku was:

  - Create a new unique app name in Heroku with “Europe” as the server.
  - In the workspace, log into Heroku with command Line and the set of commands provided to create a connection between the application and Heroku.
  - Create a new Git repository and add the files, then associate the Heroku application and push to Heroku once the requirements.txt file and Procfile have been created.
  - Configuration variables had to be set in order to get the project running. These had to be set in both the Gitpod IDE and on Heroku. These included, PORT, IP and Mongo URL.
  - Open the app to test successful deployment.


[Back to top](#summary)