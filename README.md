# kytchentable

Kytchen Table: Come Home to the Table

Welcome to Kytchen Table, your newest farm to table restaurant, serving food from the heart, and sourced and supported by local famers and suppliers and run by Head Chef Kyran Becker. Kytchen Table's wesite is designed with users at its heart, allowing them to see the menu with ease, as well as signing up to the restaurant to allow them to make and amend bookings and join their mailing list to recieve up to date information about the restaurants seasonal menu changes. The website also has backend functionality, allowing Super Admins to add, modify and make changes to menu options on the live site, as well as control and amend bookings. 

The target audience for Kytchen Table is middle class and wealthy food lovers, who are keen on knowing the stories of their food and the journey the ingredients took to reach their plate. It is directly inspired by restaurants such as Simon Rogan's Henrock and Raymond Blanc's Le Manoir aux Quat’Saisons.

Welcome to our table. Welcome home.

# Table of Contents 
[UX]
[Five Planes of UX Design](#five-planes-of-ux-design)
[Strategy](#strategy)
[Scope](#scope)
[Structure](#structure)
[Skeleton](#skeleton)
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

Content Requirements
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

## Skeleton
I used Balsamiq to create mobile and desktop wireframes for Kytchen Table:

### Mobile Wireframes
WOW THIS IS WEIRD




# Tools & Technologies Used
* Balsamiq for wireframes
* Mermaid for ERD's
* Canva & Photoshop for favicon, logo and watermark creation
* Gemini AI as a prompt to create content for menus
* Google Fonts for web fonts
* Coolors for colour palette generation