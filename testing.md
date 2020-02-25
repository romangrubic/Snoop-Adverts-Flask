## Summary
* [Responsivnes](#responsivnes)
* [CRUD](#crud)
    * [Create](#create-advert)
    * [Read](#read-advert)
    * [Update](#update-advert)
    * [Delete](#delete-advert)
* [Overall](#overall)
    * [Navigation](#navigation)
    * [Search and Filter](#search-and-filter)
    * [Top Advert section](#top-advert-section)
    * [Button "Go to top"](#button-"go-to-top")
    * [Pagination](#pagination)
    * [Footer](#footer)
---

## Responsivnes
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Viewing on mobile device | Images adapted, no side adverts visible | As Expected | Pass |
| Viewing on tablet device | Side adverts visible, adverts not breaking out | As expected | Pass |
| Viewing on laptop device | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 2k | All in order, no distortion | As expected | Pass |
| Viewing on desktop device up to 4k | All in order, no distortion | Home page distorted in carousel section, Marketplace page adverts are too big, on pages Add and Edit, footer is not covering bottom enough  | Fail |

[Back to top](#summary)

---

## CRUD

### Create Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Submit` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking on `Submit` button after filling all the forms | Redirect to the home page and the advert is added | As expected | Pass |
| Clicking on `Cancel` button | Redirect to the home page | As expected | Pass |

[Back to top](#summary)

### Read Advert
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on advert cards | Displays advert in View advert page | As Expected | Pass |

[Back to top](#summary)

### Update Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Save` button without filling all the forms | Displays Validation to tell the user to enter all the forms | As Expected | Pass |
| Clicking `Save` button after changing some of the forms | Redirect to the view advert page and the advert is edited | As expected | Pass |
| Click on `Cancel` button | Cancel all changes and redirects to view advert page | As expected | Pass | 

[Back to top](#summary)

### Delete Advert

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Delete` button | Opens a modal to confirm deletion | As Expected | Pass |
| Clicking on `Delete` button inside modal | Deletes advert and redirects to Home page | As Expected | Pass |
| Clicking on `Close` button inside modal | Closes modal and cancels deletion | As Expected | Pass |

[Back to top](#summary)

---

## Overall

### Navigation 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on Logo button | Opens "Home" page | As Expected | Pass |
| Clicking on `Marketplace` link | Opens "Marketplace" page | As expected | Pass |
| Clicking on `Add advert` link | Open "Add advert" page | As expected | Pass |

[Back to top](#summary)


### Search and Filter

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Searching for a word or part of a word | Shows all adverts with searched word in the name | As Expected | Pass |
| Clicking on filter button when choosing Motors | Displays all the adverts with category of "Motors" | As Expected | Pass |
| Clicking on filter button when choosing Home | Displays all the adverts with category of "Home" | As Expected | Pass |
| Clicking on filter button when choosing Electronics | Displays all the adverts with category of "Electronics" | As Expected | Pass |

[Back to top](#summary)


### Top Advert section

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on an advert | Open that advert in view advert page | As Expected | Pass |

[Back to top](#summary)


### Button "Go to top" 

| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `Go to top` button | Scrolls up to top of the page | As Expected | Pass |

[Back to top](#summary)


## Pagination
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on `<< Previous` button | Open the previous page (if on page 3, open page 2) | As Expected | Pass |
| Clicking on button with page number | Opens that page (if clicked on `3`, opens third page)  | As Expected | Pass |
| Clicking on `Next >>` button | Open the next page (if on page 2, open page 3) | As Expected | Pass |

[Back to top](#summary)

## Footer 
| Functionality | Expected Outcome | Actual Outcome | Pass/Fail |
| :-------------: |:----------------:| :--------------: | :---------: |
| Clicking on My projects `Weather 360°` icon | Opens "Weather 360°" project in new tab | As Expected | Pass |
| Clicking on My projects `Memory game` icon  | Opens "Memory game" project in new tab | As expected | Pass |
| Clicking on `Github` icon | Opens "Github" profile in new tab | As expected | Pass |
| Clicking on `LinkedIn` icon | Opens "LinkedIn" profile in new tab | As expected | Pass |
| Clicking on `E-mail` icon | Opens contact modal for user to contact me | As expected | Pass |
| Clicking on `Submit` button without filling e-mail modal form | User is not able to send | As expected | Pass |
| Clicking on `Submit` button after filling e-mail modal form | Changes `Submit` button from red to green and modal closes itself  | As expected | Pass |

[Back to top](#summary)


