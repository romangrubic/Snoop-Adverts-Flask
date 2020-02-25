## Data Centric Development Project - Code Institute
---
# Snoop
Tired or signing up just to place your toaster or TV in order to get few bobs? Tired of unwanted spam mail in your e-mail about adverts that don't interest you?
With **Snoop** you don't have to give your e-mail or phone number! No more long sign-up process and you have more time to snoop for a good deal on that car you like!

#### A live demo is hosted [here](https://adverts-project.herokuapp.com/home)
![Snoop Demo](https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/responsive.png "Snoop Demo")

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
## Project Background

Welcome to my Data Centric Milestone Project for Code Institute. The goal of this project was to allow the user to make simple operations where it could create, retrieve, update and delete data. Database used is a noSQL database MongoDB.
The project is a web-site where user can post their adverts (similar to DoneDeal, Adverts, Gumtree...).
I choose the name Snoop as in "to snoop around" and all similarities with Snoop Dog is accidental.

 [Back to top](#summary)

---

## UX
### User Stories
As a new user of the web-site, I would like to be able to:

* **see all the ads**
  - user can see all adverts by clicking on `Marketplace` button. 

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/all-ads.png" width="500" height="300" alt="Marketplace image">
</p>

* **search for a specific advert**
  - user can use the search bar for specific word or part of the word. 

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/search-bar.png" width="500" height="300" alt="Seacr by part of the word">
</p>

* **search by category**
  - user can search by specific category such as Motors, Home or Electronic by pressing button.

<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/filter-buttons.png" width="500" height="300" alt="Filter buttons">
</p>

* **view advert that I'm interested in**
  - user can view advert in full view by clicking anywhere on the advert. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/view-ad.png" width="500" height="300" alt="View advert">
</p>

* **place my own advert**
  - user can place their own advert just by going to Add advert in the navigation bar. 
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/add-advert.png" width="500" height="300" alt="Add advert">
</p>

* **change my advert**
  - user can edit adverts if something changed by pressing `Edit` button.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/edit-advert.png" width="500" height="300" alt="Edit advert">
</p>

* **delete my advert**
  - user can delete adverts if the advert is no longer valid.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/delete-advert.png" width="500" height="300" alt="Delete advert">
</p>

As a company, I would like to:
* **promote my product**
  - companies can promote their product or buy space to promote themselves by contacting me. Every page has dedicated `Your AD here!` spaces which can be rented by anyone.
<p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/place-ad.png" width="500" height="300" alt="Place your ad!">
</p>

[Back to top](#summary)

### Strategy

**Snoop** web-site purpose is to be a marketplace where users can put their things to sell and earn money and companies to promote their bussines by renting advertisement space.

### Scope

In designing this page, I wanted for the user to have a positive experience and for the web-site to be simple to use. So I wanted to make a page like that. 
User can easily search with one click (by pressing Marketplace in navbar or by pressing one of the filter buttons to search for adverts in a certain category).



### Structure

When the user arrives on site, it will see buttons and search bar as a call to action. Navigation is centered and is always on top of the screen and has a logo which acts as a link to Home page,
Marketplace button where he can see all the adverts sorted by number of views and Add advert where new advert can be added with ease. There is also "Top Ad" section where adverts with highest number of views are displayed on a carousel.

When user goes to Marketplace page, adverts will show up ranked by number of views they have. Also, there are only 12 adverts visible per page and a `Go to top` button at the end of the page. Adverts are presented as cards with a decent size picture and below their name, number of views, location and price. 
Adverts are clickable on all of their size so user can easily see the whole advert. If user clicks on advert, a new page will open where information will be presented in a bigger format and advert description will also be visible. 
There are buttons on the end of the page where user can delete the advert or edit it if neccessary. If user presses `Delete` button, a modal will show up asking the user are they sure they want to delete it. If they press `Edit` button, an edit page will open 
containing all the data of the advert in database and user can change anty part of it.

User can click on filter button that are visible on all main pages, where he can fast search a specific category of adverts. If he wants to see `Motors`, all adverts in category of Motors will show. Same 
for the rest of the categories.

There is also an `Add advert` link in the navigation where user can put things to sale.

Footer is visible on any page and icons themselves are clickable and leading to my projects, different pages or opening a 
contact modal. 

As an addition, I have implemented a designated space on all of the pages where companies or anyone can rent and promote themselves and me as an owner can earn some money on the side.

#### Further description of buttons, icons and elements used is in the next section (Features).

### Wireframes

* **Home page**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe-home.jpg" width="500" height="300" alt="Home page">
</p>

* **Marketplace page**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe-market.jpg" width="400" height="500" alt="Marketplace page">
</p>

* **View advert**
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/romangrubic/database-project/master/static/images/readme/wireframe-view.jpg" width="500" height="300" alt="View advert">
</p>

### Surface 
Using light color scheme I'm creating an environment where user will stay as long as possible because there are not bright colors which will tired users eyes.
By making all the elements stand out correctly and are simple to use, I'm creating environment where 
user can see what it wants, look at adverts that interest it. Users experience of **Snoop** will be that it is simple and easy to use.

[Back to top](#summary)

---
## Features
### Existing Features
* Navigation bar
  - Navigation bar is visible on all pages and on all sizes. It contains a link to home page presented by logo, a link for marketplace where user can see all the ads sorted by views and an add advert page where user can place an advert. 

* Advert section
  - On each page, on medium screens and bigger sizes, there are parts where owner of the
   page can promote his own adverts or rent that space to companies for advertisement and earn money that way.

* Filter buttons and search bar
  - They are visible on all pages and are used to filter ads. User can filter by category or by searching names. In search bar user can search by whole word or by letter.

* Top Ad section 
  - Top Ad section is a carousel which is showing 4 most viewed adverts on site. Each image in carousel is clickable and if user clicks on it will open that advert in View_advert.html

* Add advert 
  - User can add advert by typing all the required information that are neccssary to present the advert.
   All fields are required and have to filled by the requirements. By pressing submit button, advert will be saved to database and presented in Marketplace.

* Adverts cards
  - Once the user searches or visits Marketplace, adverts will be presented in cards. User can see image of the advert and bellow it
  are tittle, number of views, location and price. The cards themselves are clickable and once clicked they 
  will open in a new page where user can see rest of information such as description and contact information.

* View advert
  - Once user clicks on an advert, a big page opens where user can see all the information about an advert and also can delete the advert or edit the advert if the information is not correct or have changed

* Edit advert
  - Edit advert is similar to add advert page except it already shows all the data of the advert that is in database. User can then either save the changes that were made or cancel the edit if it was misclicked or no changes added.

* Pagination 
  - I have added pagination to Marketplace.html and Search.html so that user can only see 12 adverts at a time. 

* "Go to top" button
  - Instead of user scrolling back to the top of the page when he reaches the bottom, I have put a button that will return to top once pressed.

* "No results" page
  - I've implemented a 404page in case user types something that is not in database. Upon that, a picture will be shown that the search is not in database and instruc user to search again or filter through categories. The image itself is clickable and once clicked, it will open Home page.
* View counter
  - View counter is implemented in footer section and is only visible on medium and bigger screen sizes. It increments the counter by +1 every time Home page is visited.

* Social icons
  - In the footer are three social icons with links, one leading to my GitHub page, one for my LinkedIn profile (both of them open in a new tab because of 
  `target="_blank"` attribute) and last one opens a contact modal from which user can contact me.

* My projects icons
  - In the footer are two project icons with links, one leading to my **Weather 360°** project and one for my **Memory game** project (both of them open in a new tab because of 
  `target="_blank"` attribute). Only visible on medium and bigger screen sizes.

* Contact modal
  - When user click on contact icon, it opens a new modal. User has to input all the requested information in order for e-mail to be sent. When the e-mail has been submitted, 
  the text in the submit button will go from red background color and `Submit` to green background color and `E-mail submitted! Closing...` and modal will close itself after 2seconds using `setTimeout` function. 
  If it was unsuccessful, it will turn gray background color with `Failed to submit. Refresh page` text.

[Back to top](#summary)

### Future Features
  - A login systems for users on the page would've provided another level of security to adverts on this page. This could be performed in the back end using conditional statements to check if the current user is logged in or not with the current user being gotten from the session. Only if these criteria were satisfied then the user would be allowed to edit, delete or add adverts etc.

[Back to top](#summary)

---
## Information Architecture

### Database
This project employs the NoSQL database [MongoDB](https://www.mongodb.com/). 

### Data Types

Below are the different data types in the MongoDB that I'm using:

- ObjectId
- String
- Integer

### Data Structure 

Below is the data base collection:

Adverts Collection

| Title              | DB Key       | Form Validation                           | Data type |
| ------------------ | ------------ | ----------------------------------------- | --------- |
| Advert Id          | _id          | None                                      | ObjectId  |
| Category name      | category_name| user chooses from a list of choices       | string    |
| Advert Name        | advert_name  | text, maxlength="9"                       | string    |
| Advert Description | advert_description | text/number , maxlength="300"       | string    |
| Price              | price        | number , min="0" max="99999"              | string    |
| Contact info       | contact_info | text/number/email, maxlength="25"         | string    |
| Location           | location     |  user chooses from a list of choices      | string    |
| Upload Image       | imageURL     | image, image/*                            | string    |
| Views              | views        | number                                    | integer   |


[JSON file showing adverts collection structure](https://github.com/romangrubic/database-project/tree/master/data/database/adverts.json) 


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
    
    - https://www.heroku.com

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