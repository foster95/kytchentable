# Kytchen Table

Kytchen Table: Come Home to the Table

Welcome to Kytchen Table, your newest farm to table restaurant, serving food from the heart, and sourced and supported by local famers and suppliers and run by Head Chef Kyran Becker. Kytchen Table's wesite is designed with users at its heart, allowing them to see the menu with ease, as well as signing up to the restaurant to allow them to make and amend bookings and join their mailing list to recieve up to date information about the restaurants seasonal menu changes. The website also has backend functionality, allowing Super Admins to add, modify and make changes to menu options on the live site, as well as control and amend bookings. 

The target audience for Kytchen Table is middle class and wealthy food lovers, who are keen on knowing the stories of their food and the journey the ingredients took to reach their plate. It is directly inspired by restaurants such as Simon Rogan's Henrock and Raymond Blanc's Le Manoir aux Quat’Saisons.

Welcome to our table. Welcome home.

# Table of Contents 
1. [UX](#ux)
2. [Five Planes of UX Design](#five-planes-of-ux-design)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
3. [Development Using Agile Methodology](#development-using-agile-methodology)

[Tools & Technologies Used](#tools--technologies-used)

# UX
## Five Planes of UX Design
To build out Kytchen Table, I used the theory of the 5 planes of UX, going through them one by one to help flesh out the project needs and requirements. The theory of the 5 planes of UX design is the following: Strategy, Scope, Structure, Skeleton and Surface.

## Strategy
### Purpose
* To provide the restaurant management team with a website that can monitor and manage restaurant reservations and menus
* To provide potential customers with a holistic and intuitve website which allows the user to find out about the website, including the menu available at the time of year, and make a reservation, as well as give them the tools to amend the booking if required.

### Primary User Needs
* Restaurant management need to be able to see an overview of the reservations by day
* Restaurant management need to be able to amend any booking via an admin system in case of last minute bookings/cancellations etc
* Restaurant management need to be able to amend the menu to update every season
* Users need to be able to create their own reservation and modify or cancel the reservation after the fact
* Guests, Users and Management need to be able to see the seasonal menu at the time, including allergens. 

### Business Goals
* To provide a website that provides an upscale, sleek experience, mirroring the experience they will be recieving at the restaurant.
* The website should include a management portal for restaurant managers to be able to add, remove or amend all menus, as well as update allergens. 
* The website mangement portal should also make life as easy for staff as possible, with an immediate overview as to not just bookings by day but the available tables by day and time slot as well

## Scope
### Functional Specifications
* Users will be able to create an account that they can use to make reservations
* Users will be able to see all their upcoming reservations
* Users will be able amend those reservations (ie time, date, guest number), and cancel the reservation if required
* Users will be able to see browse restaurant philosophy
* Users will be able to browse the current restaurant menu and allergens associated with each item
* Users will be able to browse the restaurants contact information
* Users will be able to browse the restaurants social media details
* Management teams will be able to add or delete any user - but will have to complete additional validation to delete the user
* Management teams will be able to see all of the upcoming reservations by date and time slot
* Management teams will be able to amend any and all upcoming reservations, and cancel the reservation if required
* Mangement will be able to amend the information seen by the users, including menus and allergens

### Content Requirements
* A favicon must be visible on desktop use
* The header must include the logo and a navigation bar (this will collapse for mobile users)
* The footer must include restaurant details and social media details
* The main home page will have a hero image
* The main home page should also have a carousel of images of the food created at the restaurant
* There must be a menu page
* The menu page must include allergens
* There must be a ethos/philosophy page
* Users must be identified once they have logged in 
* Users must be able to immediately see a log in / log out option

Please see below for future design features to be implemented

## Structure
### Information Architecture
The Navigation menu should show the following options: Home, Our Philosophy, Menu, Make a Reservation, My Reservations (only for users logged in) and Login (or Log Out dependent on status)

### User Flow
Role | Function/Aim | Path
--- | --- | ---
User | Wishes to make a reservation | Home -> Make a Reservation -> Provide Reservation Details -> Confirm -> Confirmation Screen
User | Wishes to view menu | Home -> Menu
User | Wishes to see restaurant philosophy | Home -> Our Philosophy
User | Needs to register for an account | Home -> Login -> Sign Up -> Provide Sign Up Reservations -> Submit
User | Wants to see confirmed reservations | Home -> Login -> User provides login information -> My Reservations
User | Wants to ammend reservation | Home -> Login -> User provides login information -> My Reservations -> Amend
User | Wants to cancel reservation | Home -> Login -> User provides login information -> My Reservations -> Cancel
Site Managers | Want to see current bookings | Home -> Login
Site Managers | Want to update menu | Home -> Login

## Skeleton
I used Balsamiq to create mobile and desktop wireframes for Kytchen Table:

### Mobile Wireframes
![Mobile Wireframes One](https://github.com/foster95/kytchentable/blob/main/static/images/readme/mobile-wireframes-set-one.png)

![Mobile Wireframes Two](https://github.com/foster95/kytchentable/blob/main/static/images/readme/mobile-wireframes-set-two.png)

### Desktop Wireframes
![Desktop Wireframes One](https://github.com/foster95/kytchentable/blob/main/static/images/readme/desktop-wireframes-set-one.png)

![Desktop Wireframes Two](https://github.com/foster95/kytchentable/blob/main/static/images/readme/desktop-wireframes-set-two.png)

![Desktop Wireframes Three](https://github.com/foster95/kytchentable/blob/main/static/images/readme/desktop-wireframes-set-three.png)

![Desktop Wireframes Four](https://github.com/foster95/kytchentable/blob/main/static/images/readme/desktop-wireframes-set-four.png)

## Surface
Kytchen Table is a luxury restaurant, modelled after the typical website of a Michelin starred restaurant, which I looked into prior to beginning the project as a form of research. The website therefore, should mirror this as a luxury, sleek website which is not litered with images, and has a consistent colour palette across the website which is mirrored in the logo design and tied together with a cohesive set of fonts. 

### Kytchen Table Colour Palette
![Ktychen Table Colour Palette](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-colour-palette.png)

### Kytchen Table Logo
![Kytchen Table Logo/Watermark](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-wordmark.png)

### Kytchen Table Branded Fonts
To figure out the best font pairings I used the Our Own Thing font pairing website, which allowed me to look through all of the fonts available through Google Fonts and choose. As a result, the following fonts were chosen:

* [Aboreto Regular](https://fonts.google.com/specimen/Aboreto?preview.text=Kytchen%20Table) is used as the primary font for headings and is also the font used for the logo and for the favicon. The font was chosen as it was a readable font whilst still providing a statement that fitted with the sleek, upmarket feel of the website
* [Abyssinica SIL](https://fonts.google.com/specimen/Abyssinica+SIL?preview.text=Kytchen%20Table) is used for all secondary font and body text. I chose this font as I felt it paired nicely, providing a warmth and softness to give the website a bit more of a comforting feel
* [Font Awesome](https://fontawesome.com/) was used for the social media icons used in the footer

## Development using Agile Methodology
### User Stories
Using the Agile Methodology, I first created a series of user stories to help break down the requirements of the website. These user stories were all writen in the following formation: As a *Role* I can *Capability* so that *Recieve Benefit*. I then used the GitHub issues section to create these user stories. These can be found below:

* As a Site Admin I can create and amend menu items so that I can add or remove food options as new dishes are created in the restaurant
* As a Site Admin I can create times and days of the week slots the restaurant is open so that I can monitor booking availability throughout the week
* As a Site Admin I can book tables in the booking slots so that I can book tables on behalf of guests
* As a Site Admin I can see all of the bookings currently made so that I can be informed about how many covers are required at the restaurant at any given day and make any changes to bookings if needed
* As a Site Admin I can be blocked from any more bookings that slots available per time slot so that I do not overbook any tables
* As a Site Admin I can delete any account so that I can control access to the user panel
* As a User I can register for an account with Kytchen Table so that I can log into the user portal
* As a User I can delete my account so that *I no longer have an account with Kytchen Table
* As a User I can see the availability of tables at any given day and time slot so that I can decide what day and time to book a table
* As a User I can book a table in a slot so that I can reserve my table at the restaurant
* As a User I can amend an upcoming booking so that I can change the details provided to the restaurant
* As a User I can log out of the user portal so that I can know that I am no longer in my account
* As a User I can see a home page which provides an overview of the restaurant so that I can know more about the restaurant
* As a User I can see the contact details of the restaurant so that I know where to go and what number to call
* As a User I can find out about the ethos of the restaurant so that I can decide if it is my sort of place to visit
* As a User I can view the menu so that I can decide what I would like to have
* As a User I can sign up to the restaurants mailing list so that I can recieve up to date information about changing menus at the restuarant
* As a User I can see a 404 error page so that I can know I've gone to the wrong page
* As a User  I can filter the menu by allergen so that I can easily see what items contain food I am allergic to

Each story was then broken down with a series of acceptance criteria that must be fulfilled before the user story can be considered complete.

After this I used the MoSCoW Prioritisation method to break these user stories down even further. MoSCow stands for the following:
* Must Have - should be no more than 60% of the project
* Should Have
* Could Have
* Won't Have

With this in mind the stories were then grouped in the issues board before being transferred to the project board

### Must Have
* As a Site Admin I can create and amend menu items so that I can add or remove food options as new dishes are created in the restaurant
* As a Site Admin I can create times and days of the week slots the restaurant is open so that I can monitor booking availability throughout the week
* As a Site Admin I can book tables in the booking slots so that I can book tables on behalf of guests
* As a Site Admin I can see all of the bookings currently made so that I can be informed about how many covers are required at the restaurant at any given day and make any changes to bookings if needed
* As a User I can register for an account with Kytchen Table so that I can log into the user portal
* As a Site Admin I can delete any account so that I can control access to the user panel
* As a User I can delete my account so that *I no longer have an account with Kytchen Table
* As a User I can book a table in a slot so that I can reserve my table at the restaurant
* As a User I can amend an upcoming booking so that I can change the details provided to the restaurant
* As a User I can log out of the user portal so that I can know that I am no longer in my account
* As a user I can view the menu so that I can decide what I would like to have

### Should Have
* As a Site Admin I can be blocked from any more bookings that slots available per time slot so that I do not overbook any tables
* As a User I can see the availability of tables at any given day and time slot so that I can decide what day and time to book a table
* As a User I can see a home page which provides an overview of the restaurant so that I can know more about the restaurant
* As a User I can see the contact details of the restaurant so that I know where to go and what number to call
* As a user I can find out about the ethos of the restaurant so that I can decide if it is my sort of place to visit

### Could Have
* As a user I can sign up to the restaurants mailing list so that I can recieve up to date information about changing menus at the restuarant
* As a User I can see a 404 error page so that I can know I've gone to the wrong page

### Won't Have
* As a User I can filter the menu by allergen so that I can easily see what items contain food I am allergic to



# Tools & Technologies Used
* Balsamiq for wireframes
* Mermaid for ERD's
* Canva & Photoshop for favicon, logo and watermark creation
* Gemini AI as a prompt to create content for menus
* Google Fonts for web fonts
* Coolors for colour palette generation
* Our Own Thing's Font Pairing website for typography