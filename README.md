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
* [Information Architecture](#information-architecture)
* [Technology used](#technology-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

---
## Features
### Existing Features
* View counter

  - View counter is implemented in footer section and is only visible on medium and bigger screen sizes. It increments the counter by +1 every time Home page is visited.

* Social icons

  - In the footer are three social icons with links, one leading to my GitHub page, one for my LinkedIn profile (both of them open in a new tab because of 
  `target="_blank"` attribute) and last one opens a contact modal from which user can contact me.

* Contact modal

  - When user click on contact icon, it opens a new modal. User has to input all the requested information in order for e-mail to be sent. When the e-mail has been submitted, 
  the text in the submit button will go from red background color and `Submit` to green background color and `E-mail submitted! Closing...` and modal will close itself after 2seconds using `setTimeout` function. 
  If it was unsuccessful, it will turn gray background color with `Failed to submit. Refresh page` text.

* My projects icons

  - In the footer are two project icons with links, one leading to my **Weather 360°** JS project and one for my **Memory game** project (both of them open in a new tab because of 
  `target="_blank"` attribute). Only visible on medium and bigger screen sizes.

[Back to top](#summary)

### Future Features
  - A login systems for users on the page would've provided another level of security to adverts on this page. This could be performed in the back end using conditional statements to check if the current user is logged in or not with the current user being gotten from the session. Only if these criteria were satisfied then the user would be allowed to edit, delete or add adverts etc.

[Back to top](#summary)

---
## Information Architecture

### Database
As this is the MS3 of the course a NoSQL database is used, this project employs the NoSQL database MongoDB. Inner arrays were utilised in the data structure in order to iterate through the items in a list with relative ease.

[Back to top](#summary)

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

## Testing
### Validating code
HTML
 - code is validated through [W3 validator](https://validator.w3.org/).

CSS
 - code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

JavaScript
 - code is validated through [JS Hint](https://jshint.com/).

Python
 - code is validated through [PEP8](http://pep8online.com/).

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

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/romangrubic/database-project.git` into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.  

Further help with cloning can be found on this GitHub Help [page](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

[Back to top](#summary)

---

## Credits
### Content
+ All content was written by myself and by users.

### Media
+ Background photo used in this web-site was obtained from [Komana](http://komana.amcworks.co/color-background/).

### Acknowledgement
* I would like to thank my mentor for help during project and great ideas.
* Videos on [CodeInstitute](https://codeinstitute.net/).
* Big thanks to [W3 Schools](https://www.w3schools.com/) for all the content and clarification of different methods.
* Other advertisement site like [DoneDeal](https://www.donedeal.ie/), [Advert](https://www.adverts.ie/), [Gumtree](https://www.gumtree.ie/) etc.

#### This is for educational use.
[Back to top](#summary)