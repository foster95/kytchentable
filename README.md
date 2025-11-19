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
    * [User Stories](#user-stories)
    * [GitHub Issues](#github-issues)
    * [GitHub Projects](#github-projects)
4. [Database Design](#database-design)
5. [Features](#features)
6. [Future Features](#future-features)
7. [Testing](#testing)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [Accessibility Testing](#accessibility-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [JShint Validation](#jshint-validation)
    * [PEP8 Validation](#pep8-validation)
    * [Device Testing](#device-testing)
    * [Automated Testing](#automated-testing)
    * [Manual Testing](#manual-testing)


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
#### Original Palette
![Ktychen Table Colour Palette](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-colour-palette.png)

#### Refined Palette upon website build
![Kytchen Table Revised Palette]()

### Kytchen Table Logo
![Kytchen Table Wordmark](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-watermark.png)

### Kytchen Table Branded Fonts
To figure out the best font pairings I used the Our Own Thing font pairing website, which allowed me to look through all of the fonts available through Google Fonts and choose. As a result, the following fonts were chosen:

* [Aboreto Regular](https://fonts.google.com/specimen/Aboreto?preview.text=Kytchen%20Table) is used as the primary font for headings and is also the font used for the logo and for the favicon. The font was chosen as it was a readable font whilst still providing a statement that fitted with the sleek, upmarket feel of the website
* [Abyssinica SIL](https://fonts.google.com/specimen/Abyssinica+SIL?preview.text=Kytchen%20Table) is used for all secondary font and body text. I chose this font as I felt it paired nicely, providing a warmth and softness to give the website a bit more of a comforting feel
* [Font Awesome](https://fontawesome.com/) was used for the social media icons used in the footer

# Development using Agile Methodology
## User Stories
Using the Agile Methodology, I first created a series of user stories to help break down the requirements of the website. These user stories were all writen in the following formation: As a *Role* I can *Capability* so that *Recieve Benefit*.

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

With this in mind the stories were then grouped in the issues board before being transferred to the GitHub Projects kanban board which were then tracked across the remainder of the project

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

## GitHub Issues
From the beginning of development, I used GitHub Issues as means to manage and create EPICS with user stories inside them, as well as build out the acceptance criteria for each user story. In the later stages of development, I used GitHub issues to manage and track bugs that had developed throughout the project

### GitHub Issues - Start of Project Prior to Coding
![GitHub Issues - Start of Project Prior to Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghi-start-of-project.png)

## GitHub Projects
In the later stages of development I used GitHub Projects kanban board as a tracker. EPICS with user stories inside them, were placed in the Todo section and were steadily moved over as they were completed.

### GitHub Projects Board - Start of Project Prior to Coding
![GitHub Projects - Start of Project Prior to Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghp-start-of-project.png)

# Database Design
## Data Models
Prior to beginning the actual build of the website, I created an Entity Relationship Diagram to help me visualise the relationships between the different databases that would run through the project. To create this I used Mermaid.

![Kytchen Table ERD](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-erd.png)

# Features
## Header
The header uses the base.html template, and has been designed to be minimalistic in keeping with the rest of the website. The header has the restaurant name which is a hyperlink to the home page and a simple navigation bar. The navigation bar comes from Bootstrap and therefore is responsive to screen sizes, stretching to a full bar only on desktops and wider. At all other times the navigation bar is accessible via the burger icon.

## Footer
The footer also uses the base.html website, and again has been designed with minimalism in mind. The footer features three columns, one for the website address (meeting the user story requirements), one for the opening and closing times of the restaurant and one for the social media handles of the website. All of the social media links apply the "rel=noopeener" rule and open to a new page as per best practise. All of the links also have aria labels associated with them for screen readers. The footer was also created with Bootstrap and therefore on devices other than desktop, the footer stacks on top of each other. On a desktop the footer stretches out into one row with three columns. 

## Home Page
The home page utiltises a hero image, a small amount of copy, a reservation button and a carousel of images. The hero image is a small model that uses a Cloudinary field to reduce storage on the site itself. 

        class HeroImage(models.Model):
            """
            Model to store hero images for the home page.
            """
            title = models.CharField(max_length=200)
            image = CloudinaryField('image', default='placeholder')

            def __str__(self):
                return self.title

Likewise, the carousel is also a small model using Cloudinary fields. This means that administrative Superusers can update both the hero image and the carousel of images depending on the seasonl, new dishes etc. 

        class ImageGallery(models.Model):
            """
            Model to store images for the image gallery.
            """
            title = models.CharField(max_length=200)
            image = CloudinaryField('image', default='placeholder')

            def __str__(self):
                return self.title

The reservation button automatically redirects users to the reservation form page and if the user isn't logged in, to the sign in page. 

## Our Philosophy
Our Philosophy is the simplest app of all of the apps, and doesn't utilise any models. The page is comprised of copy and a series of images. These images have been hardcoded to the website rather than running through models as these photos will not change like the hero and carousel could. The page has been designed with Bootstrap assistance, and uses columns to show the information responsively. On mobiles and tablets the information displays stacked in a column but on desktops the page stretches out to display the information more dynamically, showing information then a photo in alternating rows:

Rooted in the land: 

        <div class="row align-items-center mb-4">
            <div class="col-12 col-md-6">

Rhythm of the Season:

        <div class="row align-items-center mb-4 flex-md-row-reverse">
            <div class="col-12 col-md-6">

Refined, Not Restricted:

        <div class="row align-items-center mb-4">
            <div class="col-12 col-md-6">

## Menu
The Menu app is compromised of two models - one for the menu item itself and one for the allergens in each item. The menu has been split across two different options - an Ala Carte and a Tasting Menu which have been created as categories within the model. Along with this, the admin panel has been coded to ensure that the menu items can be displayed and edited along with their title, description and category filter. The allergies have been set so that the Superadmin can create the menus in the back administrative system and these can then be applied to each individual item. Each item can be edited, removed and deleted by the Superadmin but not by a general user. Equally, allergens can also be added, deleted and ammended. 

The menus have been styled using Bootstraps pills system, to give users the opportunity to flick between the full Tasting Menu and the A La Carte. Within the A La Carte pills users are given the further option to choose between Starts, Mains, Sides and Deserts breaking down the information in a clear, readable fashion and avoiding information overload. Users can also see the allergens for each food, as this has been pulled through from the model and admin panel and these are organised by alphabetical order, along with the titles of each dish. As the Tasting Menu operates on a different ordering system and cannot be alphabetised, the Superadmin can number each item on a 1-7 numbering system which categorises the dishes to show accordingly. 

            CATEGORY_CHOICES = [
                ('Entree', 'Entree'),
                ('Main', 'Main Course'),
                 ('Side', 'Side Dish'),
                ('Dessert', 'Dessert'),
                ('Tasting', 'Tasting Menu'),
            ]


            class Allergen(models.Model):
                name = models.CharField(max_length=50)

                class Meta:
                    ordering = ['name']

                def __str__(self):
                    return self.name


            class MenuItem(models.Model):

                """
                Stores information about a menu item.
                """

                category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
                name = models.CharField(max_length=200)
                description = models.TextField()
                allergen = models.ManyToManyField(Allergen, blank=True)
                tasting_order = models.PositiveIntegerField(
                    null=True,
                    blank=True,
                    help_text="Order for tasting menu (1 = first course)"
                )

                class Meta:
                    ordering = ['category', 'name']

                def __str__(self):
                    return self.name

## Reservation Form 
The reservation form can only be accessed by registered users and upon a user clicking on "Make a Reservation" they are redirected to the account sign in page. Upon signing into their account, the full form is then shown. The form is built off one main model which includes time slots for the booking, and requires users to provide a guest name, a guest phone number, a guest email and their reservation details - the date they wish to make the reservation for and the timeslot they wish to book. Registered users are then given the option to complete the optional 'Allergies' section and 'Special Requests' sections. Upon confirming their reservation, the registered user is shown a green alert stating "Your reservation has been submitted succesfully!" informing the user that the reservation form has been sent to the website admin. To avoid overbooking, the model also includes a maximum figure so that once 15 tables have been booked in each slot, a registered user cannot book anymore in that slot.

Regarding CRUD functionality, this ensures that the website meets the Create requirements. 

To ensure that the validation is watertight, the model and form include validation. Unfortunately this seems to have unearthed a minor bug where the HTML tooltip does not show - details of this can be found below in the unsolved bugs section. 

            class Reservation(models.Model):

                # Options for number of guests from 1 to 7
                NO_GUESTS = [(i, str(i)) for i in range(1, 7)]

                TIME_SLOTS = [
                    ('10:00', '10:00'),
                    ('10:15', '10:15'),
                    ('10:30', '10:30'),
                    ('10:45', '10:45'),
                    ('11:00', '11:00'),
                    ('11:15', '11:15'),
                    ('11:30', '11:30'),
                    ('11:45', '11:45'),
                    ('12:00', '12:00'),
                    ('12:15', '12:15'),
                    ('12:30', '12:30'),
                    ('12:45', '12:45'),
                    ('13:00', '13:00'),
                    ('13:15', '13:15'),
                    ('13:30', '13:30'),
                    ('13:45', '13:45'),
                    ('14:00', '14:00'),
                    ('14:15', '14:15'),
                    ('14:30', '14:30'),
                    ('14:45', '14:45'),
                    ('15:00', '15:00'),
                    ('15:15', '15:15'),
                    ('15:30', '15:30'),
                    ('15:45', '15:45'),
                    ('16:00', '16:00'),
                    ('16:15', '16:15'),
                    ('16:30', '16:30'),
                    ('16:45', '16:45'),
                    ('17:00', '17:00'),
                    ('17:15', '17:15'),
                    ('17:30', '17:30'),
                    ('17:45', '17:45'),
                    ('18:00', '18:00'),
                    ('18:15', '18:15'),
                    ('18:30', '18:30'),
                    ('18:45', '18:45'),
                    ('19:00', '19:00'),
                    ('19:15', '19:15'),
                    ('19:30', '19:30'),
                    ('19:45', '19:45'),
                    ('20:00', '20:00'),
                    ('20:15', '20:15'),
                    ('20:30', '20:30'),
                    ('20:45', '20:45'),
                    ('21:00', '21:00'),
                    ('21:00', '21:00'),
                    ('21:30', '21:00'),
                    ('21:45', '21:45'),
                    ('22:00', '22:00'),
                    ('22:15', '22:15'),
                ]

                MAXIMUM_TABLES = 15

                user = models.ForeignKey(User, on_delete=models.CASCADE)
                guest_name = models.CharField(max_length=100)
                guest_phone = models.CharField(
                    max_length=20,
                    validators=[
                        RegexValidator(
                            r'^\+?[0-9\s\-\(\)]{7,20}$',
                            "Please enter a valid phone number"
                            ),
                        ],
                    )

                guest_email = models.EmailField(max_length=254,)
                reservation_date = models.DateField()
                time_slot = models.CharField(max_length=10, choices=TIME_SLOTS)
                number_of_guests = models.PositiveIntegerField(choices=NO_GUESTS)
                allergies = models.ManyToManyField(Allergen, blank=True)
                special_requests = models.TextField(blank=True, null=True)
                created_at = models.DateTimeField(default=timezone.now)

                class Meta:
                    ordering = ['reservation_date', 'time_slot']

                def __str__(self):
                    return (
                        f"Reservation for {self.user} on"
                        f"{self.reservation_date} for {self.number_of_guests} guests"
                    )

                def clean(self):
                     """Prevent saving or editing reservations
                        in the past or overbooking."""
                        super().clean()

                    if self.reservation_date and self.time_slot:
                        try:
                            reservation_time = datetime.strptime(
                                self.time_slot, "%H:%M").time()
                            reservation_datetime = datetime.combine(
                                self.reservation_date, reservation_time)
                            reservation_datetime = timezone.make_aware(
                                reservation_datetime,
                                timezone.get_current_timezone()
                            )

                            if reservation_datetime < timezone.now():
                                raise ValidationError(
                                    "Reservations cannot be set in the past.")
                        except ValueError:
                            raise ValidationError("Invalid time format for reservation.")

                    # Prevent overbooking more than MAXIMUM_TABLES
                        existing_count = Reservation.objects.filter(
                            reservation_date=self.reservation_date,
                            time_slot=self.time_slot
                        ).exclude(id=self.id).count()

                        if existing_count >= self.MAXIMUM_TABLES:
                            raise ValidationError(
                                "Sorry, all tables are booked for this time slot.")

                def save(self, *args, **kwargs):
                     """Ensure validation always runs when saving the model."""
                    self.full_clean()
                    super().save(*args, **kwargs)

## View My Reservations
The 'View My Reservations' page has gone through a fair few iterations and for the purposes of the MVP this is the simplest version of the page. A future version of the page would turn this from simply displaying future bookings to a full account page, including a profile picture and more details about the user including birthdays so that the restaurant can reach out and offer birthday discounts etc and a section for the user to update their details, and password, as well as display past bookings up to a certain point. For the purposes of this project however, I decided to simply keep the page as a 'My Reservations' page, showing a registered user their upcoming reservations by date. 

If a user wishes to make any ammendments to their booking they can either 'Edit Reservation' or 'Delete Reservation', providing the registered user CRUD functionality. Depending on what the user wants to do, this will launch a modal (details of these features can be found below). If any amendments are made to the reservation, all changes also show in the admin panel in real time, and the Superadmin can make changes to the reservation which are reflected in the users reservations details.  

## Edit Upcoming Reservations Modal
The edit reservation modal uses Javascript and HTML to trigger. If a registered user chooses to Edit their reservation, the modal will pull up all the details of the booking, which the JavaScript script prepopulates with all of the information from the reservation request. If the user updates any of the details within the reservation this is updated on the Django Administrative panel. Equally, if the Superadmin updates something in the admin panel, this will show in the updated modal information. This serves as part of CRUD functionality - Read and Update

            <div class="modal fade" id="editReservationModal" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                    <div class="modal-content">

                        <form id="edit-reservation-form" method="post" action="{% url 'update_reservation' %}">
                            {% csrf_token %}

                            <input type="hidden" name="booking_id" id="booking_id">

                            <div class="modal-header">
                                <h5 class="modal-title">Edit Reservation</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                            </div>

                            <div class="modal-body">

                                <div id="modal-errors" class="mb-3"></div>

                                <label>Name</label>
                                <input type="text" class="form-control mb-3" id="id_guest_name" name="guest_name" required>

                                <div class="row">
                                    <div class="col-md-6 mb-3">
                                        <label>Email</label>
                                        <input type="email" class="form-control" id="id_guest_email" name="guest_email" required>
                                </div>

                                <div class="col-md-6 mb-3">
                                    <label>Phone</label>
                                    <input type="tel" 
                                        class="form-control"
                                        id="id_guest_phone"
                                        name="guest_phone"
                                        required
                                        pattern="^\+?[0-9\s\-\(\)]{7,20}$"
                                        title="Please enter a valid phone number.">
                                </div>
                            </div>

                            <label>Date</label>
                            <input type="date" class="form-control mb-3" id="id_date" name="reservation_date" required>

                            <label>Time Slot</label>
                            <select class="form-select mb-3" id="id_time_slot" name="time_slot">
                                {% for time, label in TIME_SLOTS %}
                                    <option value="{{ time }}">{{ label }}</option>
                                {% endfor %}
                            </select>

                            <label>Guests</label>
                            <select class="form-select mb-3" id="id_guests" name="number_of_guests">
                                {% for count, label in NO_GUESTS %}
                                    <option value="{{ count }}">{{ label }}</option>
                                {% endfor %}
                            </select>

                            <label class="mt-3 d-block">Allergies</label>
                            <div class="row row-cols-2" id="id_allergens">
                                {% for allergen in allergens %}
                                <div class="col form-check">
                                    <input type="checkbox"
                                        class="form-check-input allergy-checkbox"
                                        name="allergies"
                                        id="allergen_{{ allergen.id }}"
                                        value="{{ allergen.id }}">
                                    <label class="form-check-label" for="allergen_{{ allergen.id }}">{{ allergen.name }}</label>
                                </div>
                            {% endfor %}
                        </div>

                        <div class="text-end mt-2">
                            <button type="button" id="clear-allergies-button" class="btn btn-sm btn-outline-secondary">
                                Clear all
                            </button>
                        </div>

                        <label class="mt-3">Special Requests</label>
                            <textarea class="form-control" id="id_special_requests" name="special_requests"></textarea>

                    </div>

                    <div class="modal-footer">
                        <button type="submit" class="btn btn-dark">Save changes</button>
                    </div>

                </form>

            </div>
        </div>
    </div>


## Delete Upcoming Reservations Modal
The delete reservation modal is even simpler, launching a modal which asks the user to confirm a second time that they absolutely want to delete the reservation. Upon the reservation being deleted, the reservation is removed from the Django Administrative panel and no longer appears in the registered user's upcoming reservations. This serves the second half of CRUD functionality - delete. 

            <!-- DELETE MODAL -->
                <div class="modal fade" id="deleteReservationModal" tabindex="-1">
                    <div class="modal-dialog">
                         <div class="modal-content">
                            <form id="delete-form" method="post">
                                {% csrf_token %}
                                <div class="modal-body text-center">
                                    <p>Are you sure you want to delete this reservation?</p>
                                </div>
                                <div class="modal-footer justify-content-center">
                                    <button type="submit" class="btn btn-danger">Yes, delete</button>
                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>

## Sign Up
Kytchen Table uses standard Allauth authentication though the sign up page itself has been stylised to match the rest of the website's aesthetic. The form uses standard CSRF protection and once signed up the user is redirected back to the homepage.

## Sign In
Allauth authentication is also used on the login page, and once the user has logged in they are also redirected to the home page. To show the user that they have logged in, a green Bootstrap alert appears at the top of the website stating the user has logged in, however this disappears when the user reloads the page. To ensure that the user knows that they are logged in the entire time, there is a small login indicator that sits underneath the navigation bar which states "You are signed in as (username)". 

## Sign Out
If the user wishes to log out of the website, they can click the Sign Out button in the navigation bar. Upon clicking this, they will be taken to a page that will ask the user to reconfirm that they would like to sign out to avoid accidentally signing out of the account without further confirmation. If the user clicks this, they will be taken to a succesful sign out page, where the user will be told they have signed out and a green Bootstrap alert will also indicate the user has been logged out. 

# Future Features
A future version of this website would include functionality on the reservation form to warn and bar users from being able to make a booking when the restaurant is closed. Additionally, the future version of this website would build out the 'My Reservations' page further, turning it into a 'My Account' page where users could provide a profile picture, their birthday, their allergy preferences, and provide reviews. 

## Developmental Bugs - Solved
### Base.html
During development I noticed an issue where the logo font size directly impacted the alignment of the navigation bar, sending it slightly out of alignment with the other items in the bar. To fix this issue I updated my personal CSS overriding the Bootstrap styling that was originally in place. 

        .navbar-nav .nav-link {
            font-family: var(--font-body);
            font-size: 1.1rem;
            color: var(--tertiary-color) !important;
            padding: 0 !important;          
            margin: 0 1rem;                 
            line-height: 1;                 
            display: flex;
            align-items: center;            
            height: 40px;        
            }

### Menu
#### Allergen picker in Django Administration
Whilst creating the model for the menu to show on the website, I incorporated the allergens into the model so that side admins could update this information regularly.

Initially I found that despite adding the allergens as a seperate model into the menu panel, the allergens were duplicating and showing as the same set of allergens on every item.

        ALLERGEN_CHOICES = [
            ('Celery', 'Celery'),
            ('Cereals', 'Cereals containing gluten'),
            ('Crustaceans', 'Crustaceans'),
            ('Eggs', 'Eggs'),
            ('Fish', 'Fish'),
            ('Lupin', 'Lupin'),
            ('Milk', 'Milk'),
            ('Molluscs', 'Molluscs'),
            ('Mustard', 'Mustard'),
            ('Nuts', 'Nuts'),
            ('Peanuts', 'Peanuts'),
            ('Sesame', 'Sesame seeds'),
            ('Soya', 'Soya'),
            ('Sulphites', 'Sulphur dioxide and sulphites'),
            ]

        class Allergen(models.Model):
            name = models.CharField(max_length=50, choices=ALLERGEN_CHOICES)

        class Meta:
            ordering = ['name']

        def __str__(self):
            return self.name

        class MenuItem(models.Model):

            """
            Stores information about a menu item.
            """

            category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
            name = models.CharField(max_length=200)
            description = models.TextField()
            allergen = models.ManyToManyField(Allergen, blank=True)

            def __str__(self):
            return self.name

To fix this I removed the choices=ALLERGEN_CHOICES which instantly removed the duplicate allergens appearing

#### Tasting Menu ordering by alphabet rather than individual order
After adding in a tasting menu after researching other Michelin restaurants and seeing this as a common feature, I realised that the tasting menu was ordering by alphabetical order as it was with the A La Carte - whicih wasn't matching the tasting menu order. To fix this I added in a custom ordering field, specifically for the tasting menu but not the A La Carte.

Code before change: 

        class MenuItem(models.Model):

         """
        Stores information about a menu item.
        """

            category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
            name = models.CharField(max_length=200)
            description = models.TextField()
            allergen = models.ManyToManyField(Allergen, blank=True)

            class Meta:
                ordering = ['category', 'name']


Code after change:
            class MenuItem(models.Model):

         """
            Stores information about a menu item.
         """

                category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
                name = models.CharField(max_length=200)
                description = models.TextField()
                allergen = models.ManyToManyField(Allergen, blank=True)
                tasting_order = models.PositiveIntegerField(
                    null=True,
                    blank=True,
                    help_text="Order for tasting menu (1 = first course)"
                )

                class Meta:
                    ordering = ['category', 'name']

I also updated the view to ensure that this was reflected on the website: 

Code before change: 

            def menu(request):
                menu_items = {
                    'entrees': MenuItem.objects.filter(category='Entree'),
                    'mains': MenuItem.objects.filter(category='Main'),
                    'side': MenuItem.objects.filter(category='Side'),
                    'desserts': MenuItem.objects.filter(category='Dessert'),
                    'tasting': MenuItem.objects.filter(category='Tasting'),
                }
                return render(
                    request, 'menu/menu.html', 
                    {'menu_items': menu_items})

Code after change:

            def menu(request):
                menu_items = {
                    'entrees': MenuItem.objects.filter(category='Entree'),
                    'mains': MenuItem.objects.filter(category='Main'),
                    'side': MenuItem.objects.filter(category='Side'),
                    'desserts': MenuItem.objects.filter(category='Dessert'),
                    'tasting': MenuItem.objects.filter(category='Tasting').order_by('tasting_order'),
                }
                return render(
                    request, 'menu/menu.html', 
                    {'menu_items': menu_items})


            def tasting_menu(request): 
                items = MenuItem.objects.filter(category='Tasting').order_by('tasting_order')
                return render(request, 'menu/tasting_menu.html', {'items': items})

            def a_la_carte_menu(request): 
                items = MenuItem.objects.exclude(category='Tasting').order_by('category', 'name')
                return render(request, 'menu/a_la_carte.html', {'items': items})

And finally I also updated the admin to make it easier for staff and administrative members to update the individual order of the tasting menu without impacting the A La Carte:

Code before the change:

            @admin.register(MenuItem)
                class MenuItemAdmin(admin.ModelAdmin):
                    list_display = ('name', 'category')  
                    list_filter = ('category',)  
                    search_fields = ('name', 'description')  
                    filter_horizontal = ('allergen',)  

Code after the change:

            @admin.register(MenuItem)
                class MenuItemAdmin(admin.ModelAdmin):
                    list_display = ('name', 'category', 'tasting_order')
                    list_editable = ('tasting_order',)
                    list_filter = ('category',)
                    ordering = ('category', 'tasting_order', 'name')


### Reservation
#### Reservation time showing as midnight on all bookings
Whilst tweaking the administrative panel for reservations, I noticed that for some reason all of my bookings were coming up as midnight, though the date was correct. To fix this I 
updated the reservation model, and split the time and the date so that this would show up correctly.

#### Reservation date could change to past date
I noticed that whilst customers couldn't immediately book a date in the past, this didn't stop the booker or the administrator being able to go in and change the booking seperately to the past. To combat this, I added an additional layer of validation at the model level which disabled customers from changing the date to the past. To do this I added the following code to the reservation model to ensure the data is sent cleanly:

            def clean(self):
            """Prevent saving or editing reservations in the past."""
            super().clean()

            if self.reservation_date and self.time_slot:
                try:
                    reservation_time = datetime.strptime(self.time_slot, "%H:%M").time()
                    reservation_datetime = datetime.combine(self.reservation_date, reservation_time)
                    reservation_datetime = timezone.make_aware(
                        reservation_datetime,
                        timezone.get_current_timezone()
                    )

                    if reservation_datetime < timezone.now():
                        raise ValidationError("Reservations cannot be set in the past.")
                except ValueError:
                    raise ValidationError("Invalid time format for reservation.")

            def save(self, *args, **kwargs):
                """Ensure validation always runs when saving the model."""
                self.full_clean()
                super().save(*args, **kwargs)

And added the following code to the modal on the current reservations page:

                min="{{ today }}"

## Developmental Bugs - Unsolved
### Issue with CSS hiding tooltip on Reservation form 

# Testing
## HTML Validation
Using Nu HTML checker, I checked the validity of my HTML by direct input due to the project being deployed through Heroku. This returned with zero errors or warnings

![HTML Validation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/html-validation.png)

## CSS Validation
I used the W3C CSS validator to check the validity of my CSS throughout the project. This returned with zero errors or warnings.

![CSS Validation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/css-validation.png)

## Accessibility Testing

## Lighthouse Testing

## JShint Validation
I used JShint to validate the JS that I wrote for the project. Initially I ran into 46 warnings about the use of const and the undefined variable of Bootstrap, however to stop this from showing up I added the following at the top of my code:

            /* jshint esversion: 6 */
            /* global bootstrap */

Upon adding this all of the warnings went away and the mention of Bootstrap as an unused variable also disappeared. 

JShint Validation for edit_reservation.js
![JShint Validation for edit_reservation.js](https://github.com/foster95/kytchentable/blob/main/static/images/readme/jshint-validation-edit-reservation.png)

JShint Validation for make_reservation.js
![JShint Validation for make_reservation.js](https://github.com/foster95/kytchentable/blob/main/static/images/readme/jshint-validation-make-reservation.png)

## PEP8 Validation
## Device Testing
## Automated Testing
## Manual Testing


# Tools & Technologies Used
* Balsamiq for wireframes
* Mermaid for ERD's
* Canva & Photoshop for favicon, logo and watermark creation
* Gemini AI as a prompt to create content for menus
* Google Fonts for web fonts
* Favicon for favicon
* Coolors for colour palette generation
* Our Own Thing's Font Pairing website for typography
* Mermaid to create an ERD for Kytchen Table
* GitHub
* GitHub Issues
* GitHub Projects Kanban Board
* VSCode
* Chat GPT for debugging assistance 
