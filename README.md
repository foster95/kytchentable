# Kytchen Table

The project was developed using Django, Bootstrap, PostgreSQL, Allauth authentication, and Agile methodology. It is inspired by modern farm-to-table Michelin-style restaurants.

![Kytchen Table Mock Ups](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-mocks.png)

To see the full deployed project please click [here](https://kytchen-table-56648feabc6b.herokuapp.com/)

*Kytchen Table: Come Home to the Table*

Welcome to Kytchen Table, your newest farm to table restaurant, serving food from the heart, and sourced and supported by local farmers and suppliers and run by Head Chef Kyran Becker. Kytchen Table's website is designed with users at its heart, allowing them to see the menu with ease, as well as signing up to the restaurant to allow them to make and amend bookings and join their mailing list to receive up to date information about the restaurants seasonal menu changes. The website also has backend functionality, allowing Super Admins to add, modify and make changes to menu options on the live site, as well as control and amend bookings. 

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
    * [Testing Overview](#testing-overview)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [Accessibility Testing](#accessibility-testing)
    * [Lighthouse Testing](#lighthouse-testing)
    * [JShint Validation](#jshint-validation)
    * [PEP8 Validation](#pep8-validation)
    * [Device Testing](#device-testing)
    * [Browser Testing](#browser-testing)
    * [Automated Testing](#automated-testing)
    * [Manual Testing](#manual-testing)
    * [Testing Against User Stories](#testing-against-user-stories)
    * [Overall Testing Conclusion](#overall-testing-conclusion)
8. [Deployment](#deployment)
9. [Forking and Cloning](#forking-and-cloning)
10. [Tools & Technologies Used](#tools--technologies-used)
11. [Credits and Acknowledgements](#credits-and-acknowledgements)
12. [A Final Note from the Developer](#a-final-note-from-the-developer)

# UX
## Five Planes of UX Design
To build out Kytchen Table, I used the theory of the 5 planes of UX, going through them one by one to help flesh out the project needs and requirements. The theory of the 5 planes of UX design is the following: Strategy, Scope, Structure, Skeleton and Surface.

## Strategy
### Purpose
* To provide the restaurant management team with a website that can monitor and manage restaurant reservations and menus
* To provide potential customers with a holistic and intuitive website which allows the user to find out about the website, including the menu available at the time of year, and make a reservation, as well as give them the tools to amend the booking if required.

### Primary User Needs
* Restaurant management need to be able to see an overview of the reservations by day
* Restaurant management need to be able to amend any booking via an admin system in case of last minute bookings/cancellations etc
* Restaurant management need to be able to amend the menu to update every season
* Users need to be able to create their own reservation and modify or cancel the reservation after the fact
* Guests, Users and Management need to be able to see the seasonal menu at the time, including allergens. 

### Business Goals
* To provide a website that provides an upscale, sleek experience, mirroring the experience they will be recieving at the restaurant.
* The website should include a management portal for restaurant managers to be able to add, remove or amend all menus, as well as update allergens. 
* The website management portal should also make life as easy for staff as possible, with an immediate overview as to not just bookings by day but the available tables by day and time slot as well

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
* Management will be able to amend the information seen by the users, including menus and allergens

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
User | Wants to amend reservation | Home -> Login -> User provides login information -> My Reservations -> Amend
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
Kytchen Table is a luxury restaurant, modelled after the typical website of a Michelin starred restaurant, which I looked into prior to beginning the project as a form of research. The website therefore, should mirror this as a luxury, sleek website which is not littered with images, and has a consistent colour palette across the website which is mirrored in the logo design and tied together with a cohesive set of fonts. Additionally I considered using some earthy greens within the palette as that referred back to the harmony the restaurant has with the land, however on development I found the green clashed and looked wrong when paired with the purples so I further revised the palette, closing in on shades of various purple for accents instead of the original planned green. 

### Kytchen Table Colour Palette
#### Original Palette
![Ktychen Table Colour Palette](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-colour-palette.png)

#### Refined Palette upon website build
![Kytchen Table Revised Palette](https://github.com/foster95/kytchentable/blob/main/static/images/readme/revised-colour-palette.png)

### Kytchen Table Logo
![Kytchen Table Wordmark](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-watermark.png)

### Kytchen Table Branded Fonts
To figure out the best font pairings I used the Our Own Thing font pairing website, which allowed me to look through all of the fonts available through Google Fonts and choose. As a result, the following fonts were chosen:

* [Aboreto Regular](https://fonts.google.com/specimen/Aboreto?preview.text=Kytchen%20Table) is used as the primary font for headings and is also the font used for the logo and for the favicon. The font was chosen as it was a readable font whilst still providing a statement that fitted with the sleek, upmarket feel of the website
* [Abyssinica SIL](https://fonts.google.com/specimen/Abyssinica+SIL?preview.text=Kytchen%20Table) is used for all secondary font and body text. I chose this font as I felt it paired nicely, providing a warmth and softness to give the website a bit more of a comforting feel
* [Font Awesome](https://fontawesome.com/) was used for the social media icons used in the footer

# Development using Agile Methodology
## User Stories
Using the Agile Methodology, I first created a series of user stories to help break down the requirements of the website. These user stories were all writen in the following formation: As a *Role* I can *Capability* so that *Receive Benefit*.

* As a Site Admin I can create and amend menu items so that I can add or remove food options as new dishes are created in the restaurant
* As a Site Admin I can create times and days of the week slots the restaurant is open so that I can monitor booking availability throughout the week
* As a Site Admin I can book tables in the booking slots so that I can book tables on behalf of guests
* As a Site Admin I can see all of the bookings currently made so that I can be informed about how many covers are required at the restaurant at any given day and make any changes to bookings if needed
* As a Site Admin I can be blocked from any more bookings that slots available per time slot so that I do not overbook any tables
* As a Site Admin I can delete any account so that I can control access to the user panel
* As a User I can register for an account with Kytchen Table so that I can log into the user portal
* As a User I can delete my account so that I no longer have an account with Kytchen Table
* As a User I can see the availability of tables at any given day and time slot so that I can decide what day and time to book a table
* As a User I can book a table in a slot so that I can reserve my table at the restaurant
* As a User I can amend an upcoming booking so that I can change the details provided to the restaurant
* As a User I can log out of the user portal so that I can know that I am no longer in my account
* As a User I can see a home page which provides an overview of the restaurant so that I can know more about the restaurant
* As a User I can see the contact details of the restaurant so that I know where to go and what number to call
* As a User I can find out about the ethos of the restaurant so that I can decide if it is my sort of place to visit
* As a User I can view the menu so that I can decide what I would like to have
* As a User I can sign up to the restaurants mailing list so that I can receive up to date information about changing menus at the restaurant
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
* As a Site Admin I can delete any account so that I can control who has a registered account
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
* As a User I can delete my account so that *I no longer have an account with Kytchen Table

### Could Have
* As a user I can sign up to the restaurants mailing list so that I can receive up to date information about changing menus at the restaurant
* As a User I can see a 404 error page so that I can know I've gone to the wrong page

### Won't Have
* As a User I can filter the menu by allergen so that I can easily see what items contain food I am allergic to

## GitHub Issues
From the beginning of development, I used GitHub Issues as means to manage and create EPICS with user stories inside them, as well as build out the acceptance criteria for each user story. In the later stages of development, I used GitHub issues to manage and track bugs that had developed throughout the project

### GitHub Issues - Start of Project Prior to Coding
![GitHub Issues - Start of Project Prior to Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghi-start-of-project.png)

### GitHub Issues - End of Project After Coding
![GitHub Issues - End of Project after Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghi-end-of-project.png)


## GitHub Projects
In the later stages of development I used GitHub Projects kanban board as a tracker. EPICS with user stories inside them, were placed in the Todo section and were steadily moved over as they were completed.

### GitHub Projects Board - Start of Project Prior to Coding
![GitHub Projects - Start of Project Prior to Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghp-start-of-project.png)

### GitHub Projects Board - End of Project After  Coding
![GitHub Projects - End of Project after Coding](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ghp-end-of-project.png)

# Database Design
## Data Models
Prior to beginning the actual build of the website, I created an Entity Relationship Diagram to help me visualise the relationships between the different databases that would run through the project. To create this I used Mermaid.

![Kytchen Table ERD](https://github.com/foster95/kytchentable/blob/main/static/images/readme/kytchen-table-erd.png)

# Features
## Header
The header extends the base.html template and follows a minimalistic design that matches the rest of the website. The header has the restaurant name which is a hyperlink to the home page and a simple navigation bar. The navigation bar comes from Bootstrap and therefore is responsive to screen sizes, stretching to a full bar only on desktops and wider. At all other times the navigation bar is accessible via the burger icon.

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

### Rooted in the land: 

        <div class="row align-items-center mb-4">
            <div class="col-12 col-md-6">

### Rhythm of the Season:

        <div class="row align-items-center mb-4 flex-md-row-reverse">
            <div class="col-12 col-md-6">

### Refined, Not Restricted:

        <div class="row align-items-center mb-4">
            <div class="col-12 col-md-6">

## Menu
The Menu app is compromised of two models - one for the menu item itself and one for the allergens in each item. The menu has been split across two different options - an Ala Carte and a Tasting Menu which have been created as categories within the model. Along with this, the admin panel has been coded to ensure that the menu items can be displayed and edited along with their title, description and category filter. The allergies have been set so that the Superadmin can create the menus in the back administrative system and these can then be applied to each individual item. Each item can be edited, removed and deleted by the Superadmin but not by a general user. Equally, allergens can also be added, deleted and amended. 

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
The reservation form can only be accessed by registered users and upon a user clicking on "Make a Reservation" they are redirected to the account sign in page. Upon signing into their account, the full form is then shown. The form is built off one main model which includes time slots for the booking, and requires users to provide a guest name, a guest phone number, a guest email and their reservation details - the date they wish to make the reservation for and the timeslot they wish to book. Registered users are then given the option to complete the optional 'Allergies' section and 'Special Requests' sections. Upon confirming their reservation, the registered user is shown a green alert stating "Your reservation has been submitted successfully!" informing the user that the reservation form has been sent to the website admin. To avoid overbooking, the model also includes a maximum figure so that once 15 tables have been booked in each slot, a registered user cannot book anymore in that slot.

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

If a user wishes to make any amendments to their booking they can either 'Edit Reservation' or 'Delete Reservation', providing the registered user CRUD functionality. Depending on what the user wants to do, this will launch a modal (details of these features can be found below). If any amendments are made to the reservation, all changes also show in the admin panel in real time, and the Superadmin can make changes to the reservation which are reflected in the users reservations details.  

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
If the user wishes to log out of the website, they can click the Sign Out button in the navigation bar. Upon clicking this, they will be taken to a page that will ask the user to reconfirm that they would like to sign out to avoid accidentally signing out of the account without further confirmation. If the user clicks this, they will be taken to a Successful Sign Out page, where the user will be told they have signed out and a green Bootstrap alert will also indicate the user has been logged out. 

# Future Features
While the current version meets the MVP criteria, several features have been identified for future expansion to enhance user experience and increase functionality including functionality on the reservation form to warn and bar users from being able to make a booking when the restaurant is closed. Additionally, the future version of this website would build out the 'My Reservations' page further, turning it into a 'My Account' page where users could provide a profile picture, their birthday, their allergy preferences, and provide reviews. 

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

Before (original code):

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


After (updated with fix):
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

Before (original code):

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

After (updated with fix):

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

Before (original code):

            @admin.register(MenuItem)
                class MenuItemAdmin(admin.ModelAdmin):
                    list_display = ('name', 'category')  
                    list_filter = ('category',)  
                    search_fields = ('name', 'description')  
                    filter_horizontal = ('allergen',)  

After (updated with fix):

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
I noticed that whilst customers couldn't immediately book a date in the past, this didn't stop the booker or the administrator being able to go in and change the booking separately to the past. To combat this, I added an additional layer of validation at the model level which disabled customers from changing the date to the past. To do this I added the following code to the reservation model to ensure the data is sent cleanly:

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
During development I discovered an issue where form validation works correctly — users are prevented from submitting forms with invalid or missing data — however, the HTML validation tooltips (e.g. “Please fill out this field”) do not appear. This behaviour has been confirmed only in Google Chrome. When testing in Mozilla Firefox and Safari, the validation messages appear as expected. From this I have concluded that this issue is browser-specific rather than a fault in the form logic.

To try and resolve this issue I attempted the following options:
* Ensured Django renders the correct HTML5 field type using:

            self.fields['reservation_date'].input_type = 'date'

* Removed any possibility of novalidate being present in the form tag.
* Checked for CSS that may be suppressing native validation UI.
* Confirmed that validation does work — only the tooltip display is affected.

Despite the above, the  validation message still does not appear in Chrome, even though users cannot submit the form and are prompted by a blue highlight bar where they need to fill in information. 

Further investigation through various full-stack development forums and developer discussions indicated that Chrome is known to occasionally hide these HTML validation tooltips, particularly with date fields and Bootstrap-styled forms. This appears to be a widespread, Chrome-specific behaviour, with multiple developers reporting the same issue and no consistently successful workaround.

As this issue did not affect form submission or overall functionality, it was deemed acceptable for MVP scope and documented here for transparency.

# Testing
Multiple testing methods were carried out to ensure the quality, functionality, and responsiveness of the Kytchen Table website. These included automated validation tools, device and browser testing, Lighthouse analysis, accessibility checks, and user-story-based manual testing. All core functionality works as expected, with only minor issues documented in Unsolved Bugs.

Testing was carried out using a mix of automated tools and manual user-story-based methods.

## Testing Overview

Testing Method | Tools Used | Purpose | Result 
--- | --- | --- | ---
HTML Validation | Nu HTML Checker | Check HTML structure | Passed – 0 errors 
CSS Validation | W3C CSS Validator | Validate custom CSS | Passed – 0 errors 
JavaScript Validation | JSHint | Validate ES6 syntax | Passed after config 
Python Validation | CI PEP8 Linter | Check PEP8 compliance | Passed across apps 
Accessibility | WAVE | WCAG & ARIA validation | Minor contrast issue 
Performance | Google Lighthouse | Measure performance & best practices | Good overall 
Browser Testing | Chrome, Safari, Firefox, Edge | Cross-browser consistency | Passed 
Device Testing | iPhone, Android, Tablet, Desktop | Cross-device consistency | Passed
Manual Testing | Developer testing | To test that all website features were working manually | Passed
Device Testing | iOS, Android, Tablets, Laptops | Responsiveness testing | Passed 
User Story Testing | Manual testing table | Verify all features against stories | Good overall 

## HTML Validation
Using Nu HTML checker, I checked the validity of my HTML by direct input due to the project being deployed through Heroku. This returned with zero errors or warnings

![HTML Validation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/html-validation.png)

## CSS Validation
I used the W3C CSS validator to check the validity of my CSS throughout the project. This returned with zero errors or warnings.

![CSS Validation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/css-validation.png)

## Accessibility Testing
To check that the website was considered accessible, I used WAVE's accessibility checker. This checker raised one issue of contrast errors with the text used on top of the hero image not considered contrasting enough. Whilst I considered changing this to make it more contrasting, changing it made the statement much bolder on the page which made it stand out and ruin the overall sleek subtlety of the message on top of the hero image. With that in mind I decided to not change the text colour to improve contrast as I felt that it would have more of a negative impact than a positive impact, and was ultimately minor in terms of the information it provided to a user. WAVE also alerted me that there was a redundant link as I had linked the website title, as well as having a "home" button. Again I decided to leave this as it was, to ensure there was no ambiguity for users when it came to returning to the home page. 

![WAVE Testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/wave-validation.png)

## Lighthouse Testing

Device | Website Section | Lighthouse Result | Notes
--- | --- | --- | ---
Mobile | Home Page | ![Lighthouse Testing Mobile - Home](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-home.png) | Some minor issues with performance and best practise due to the use of Cloudinary in hero image
Mobile | Our Philosophy | ![Lighthouse Testing Mobile - Our Philosophy](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-philosophy.png) | Some minor issues with performance due to the presence of images on the page 
Mobile | Menu | ![Lighthouse Testing Mobile - Menu](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-menu.png) |
Mobile | Dine With Us | ![Lighthouse Testing Mobile - Make Reservation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-make-reservation.png) |
Mobile | My Reservations | ![Lighthouse Testing Mobile - My Reservations](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-my-reservations.png) |
Mobile | Sign In | ![Lighthouse Testing Mobile - Sign In](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-sign-in.png) |
Mobile | Sign Up | ![Lighthouse Testing Mobile - Sign Up](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-sign-up.png) |
Mobile | Sign Out | ![Lighthouse Testing Mobile - Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-sign-out.png) |
Mobile | Successful Sign Out | ![Lighthouse Testing Mobile - Successful Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-mobile-succesful-sign-out.png) |
Desktop | Home Page | ![Lighthouse Testing Desktop - Home](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-home.png) | Some minor issues with performance and best practise due to the use of Cloudinary in hero image
Desktop | Our Philosophy | ![Lighthouse Testing Desktop - Our Philosophy](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-philosophy.png) |
Desktop | Menu | ![Lighthouse Testing Desktop - Menu](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-menu.png) |
Desktop | Dine With Us | ![Lighthouse Testing Desktop - Make Reservation](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-make-reservation.png) |
Desktop | My Reservations | ![Lighthouse Testing Desktop - My Reservations](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-my-reservations.png) |
Desktop | Sign In | ![Lighthouse Testing Desktop - Sign In](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-sign-in.png) |
Desktop | Sign Up | ![Lighthouse Testing Desktop - Sign Up](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-sign-up.png) |
Desktop | Sign Out | ![Lighthouse Testing Desktop - Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-sign-out.png) |
Desktop | Successful Sign Out | ![Lighthouse Testing Desktop - Successful Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/lighthouse-desktop-succesful-sign-out.png) |

## JShint Validation
I used JShint to validate the JS that I wrote for the project. Initially I ran into 46 warnings about the use of const and the undefined variable of Bootstrap, however to stop this from showing up I added the following at the top of my code:

            /* jshint esversion: 6 */
            /* global bootstrap */

Upon adding this all of the warnings went away and the mention of Bootstrap as an unused variable also disappeared. 

### JShint Validation for edit_reservation.js
![JShint Validation for edit_reservation.js](https://github.com/foster95/kytchentable/blob/main/static/images/readme/jshint-validation-edit-reservation.png)

### JShint Validation for make_reservation.js
![JShint Validation for make_reservation.js](https://github.com/foster95/kytchentable/blob/main/static/images/readme/jshint-validation-make-reservation.png)

## PEP8 Validation
App | File | PEP8 Response
--- | --- | ---
Home | admin.py | ![PEP8 - Home - admin.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-home-admin.png)
Home | apps.py | ![PEP8 - Home - apps.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-home-apps.png)
Home | models.py | ![PEP8 - Home - models.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-home-models.png)
Home | urls.py | ![PEP8 - Home - urls.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-home-urls.png)
Home | views.py | ![PEP8 - Home - views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-home-views.png)
Menu | admin.py | ![PEP8 - Menu - admin.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-admin.png)
Menu | apps.py | ![PEP8 - Menu - apps.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-apps.png)
Menu | models.py | ![PEP8 - Menu - models.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-models.png)
Menu | test_views.py | ![PEP8 - Menu - test_views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-test-views.png)
Menu | urls.py | ![PEP8 - Menu - urls.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-urls.png)
Menu | views.py | ![PEP8 - Menu - views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-menu-views.png)
My_Reservations | apps.py | ![PEP8 - My_Reservations - apps.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-my-reservations-apps.png)
My_Reservations | models.py | ![PEP8 - My_Reservations - models.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-my-reservations-models.png)
My_Reservations | test_views.py | ![PEP8 - My_Reservations - test_views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-my-reservations-test-views.png)
My_Reservations | urls.py | ![PEP8 - My_Reservations - urls.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-my-reservations-url.png)
My_Reservations | views.py | ![PEP8 - My_Reservations - views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-my-reservation-views.png)
Philosopy | apps.py | ![PEP8 - Philosophy - apps.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-philosophy-apps.png)
Philosophy | urls.py | ![PEP8 - Philosophy - urls.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-philosophy-url.png)
Philosophy | views.py | ![PEP8 - Philosophy - views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-philosophy-views.png)
Reserve | admin.py | ![PEP8 - Reserve - admin.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-admin.png)
Reserve | apps.py | ![PEP8 - Reserve - apps.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-apps.png)
Reserve | forms.py | ![PEP8 - Reserve - forms.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-forms.png)
Reserve | test_forms.py | ![PEP8 - Reserve - test_forms.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-test-forms.png)
Reserve | test_views.py | ![PEP8 - Reserve - test_views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-test-views.png)
Reserve | urls.py | ![PEP8 - Reserve - urls.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-urls.png)
Reserve | views.py |![PEP8 - Reserve - views.py](https://github.com/foster95/kytchentable/blob/main/static/images/readme/ci-linter-reserve-view.png)

## Device Testing
I used Blisk to conduct device testing across multiple devices

Type of Device | Devices Tested | Page | Screenshot | Notes
--- | --- | --- | --- | --- 
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Home | ![iPhone Home testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-home.png)| No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Our Philosophy | ![iPhone Our Philosphy testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-philosophy.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Menu | ![iPhone Menu testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-menu.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Reserve | ![iPhone Reserve testig](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-reserve.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | My Reservations | ![iPhone My Reservations testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-my-reservations.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Edit Reservation | ![iPhone Edit Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-edit-reservation.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Delete Reservation | ![iPhone Delete Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-delete-reservation.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Sign In | ![iPhone Sign In testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-sign-in.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Sign Up | ![iPhone Sign Up testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-sign-up.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Sign Out | ![iPhone Sign Out testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-sign-out.png) | No issues
iPhone | iPhone 16, iPhone 15 Plus, iPhone 14, iPhone 13 Pro Max, iPhone 8 | Successful Sign Out | ![iPhone Successful Sign Out testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-iphone-succesful-sign-out.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Home | ![Android Home testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-home.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Our Philosophy | ![Android Our Philosophy testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-philosophy.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Menu | ![Android Menu testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-menu.png)| No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Reserve | ![Android Reserve testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-reserve.png)| No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | My Reservations | ![Android My Reservations testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-my-reservations.png)| No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Edit Reservation | ![Android Edit Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-edit-reservation.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Delete Reservation | ![Android Delte Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-delete-reservation.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Sign In | ![Android Sign In testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-sign-in.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Sign Up | ![Android Sign Up testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-sign-up.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Sign Out | ![Android Sign Out testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-sign-out.png) | No issues
Android | Google Pixel 8, Google Pixel 6, Google Pixel 4XL, Galaxy S23 Plus, Galaxy S21 Plus | Successful Sign Out | ![Android Successful Sign Out testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-android-succesful-sign-out.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Home | ![Tablet Home testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-home.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Our Philosophy | ![Tablet Philosophy testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-philosophy.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Menu | ![Tablet Menu testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-menu.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Reserve | ![Tablet Reserve testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-reserve.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | My Reservations | ![Tablet My Reservations testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-my-reservation.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Edit Reservation | ![Tablet Edit Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-edit-reservation.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Delete Reservation | ![Tablet Delete Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-delete-reservation.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Sign In | ![Tablet Sign In testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-sign-in.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Sign Up | ![Tablet Sign Up](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-sign-up.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Sign Out | ![Tablet Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-sign-out.png) | No issues
Tablet | iPad Mini 4, iPad Pro 9, iPad Pro 11 | Successful Sign Out | ![Tablet Successful Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-ipad-succesful-sign-out.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Home | ![Desktop Home testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-home.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Our Philosophy | ![Desktop Our Philosophy testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-philosophy.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Menu | ![Desktop Menu testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-menu.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Reserve | ![Desktop Reserve testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-reserve.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | My Reservations | ![Desktop My Reservations testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-my-reservations.png)| No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Edit Reservation | ![Desktop Edit Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-edit-reservation.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Delete Reservation | ![Desktop Delete Reservation testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-delete-reservation.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Sign In | ![Desktop Sign In testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-sign-in.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Sign Up | ![Desktop Sign Up testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-sign-up.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Sign Out | ![Desktop Sign Out testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-sign-out.png) | No issues
Desktop | Small Laptop, Medium Laptop, MacBook Pro, iMac Retina | Successful Sign Out | ![Desktop Successful Sign Out](https://github.com/foster95/kytchentable/blob/main/static/images/readme/blisk-device-desktop-succesful-sign-out.png) | No issues

## Browser Testing
I used BrowserStack to test the website under various different browser conditions - for some reason I was not able to log in to the user area under any of the browser models, so I was unable to the reservation form and the My Reservations area of the website

Browser | Notes
--- | ---
Edge 142 | No issues
Firefox 144 | No issues
Google 142 | No issues
Opera 122 | No issues
Safari 5.1 | No issues

## Automated Testing
I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

To conduct these tests I used Django's built in unit testing framework. To run these tests I can the python3 manage.py test command into the terminal.

![Django Automated Testing](https://github.com/foster95/kytchentable/blob/main/static/images/readme/automated-testing-result.png)

## Manual Testing
### Base
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Navigation Bar | Navigation bar is responsive | Navigation bar shows responsively as a drop down on mobiles and tablets and as a full navigation bar on desktops | Navigation bar shows responsively as a drop down on mobiles and tablets and a full navigation bar on desktops
Navigation Bar Links | User can use Navigation Bar to navigate around site | User should be able to click through to "Our Philosophy", "Menu", "Dine with Us" (they will be redirected to the login if they are not logged in), "My Reservations" (if logged in) and "Sign In"/"Sign Out". Upon hovering over the link, the text should change in colour. Any active links should be italicised. | User is able to click through to "Our Philosophy", "Menu", "Dine with Us" (they are  redirected to the login if they are not logged in), "My Reservations" (if logged in) and "Sign In"/"Sign Out". Upon hovering over the link, the text changes in colour. Any active links are be italicised. 
Sign in Indicator | Sign in indicator is shown on sign in | Sign in indicator shows only when a registered user logs in. The sign in indicator has the message "You are signed in as (username)". The sign in indicator disappears when the registered user logs out. | Sign in indicator shows only when a registered user logs in. The sign in indicator has the message "You are signed in as (username)". The sign in indicator disappears when the registered user logs out.
Footer | Footer is responsive | Footer is responsive to devices. When viewed with a mobile, the footer stacks on top of each other, with content centred. As the device gets bigger the content stretches out into a row and on a desktop the content sits neatly on one row with even spacing between each column. | Footer is responsive to devices. When viewed with a mobile, the footer stacks on top of each other, with content centred. As the device gets bigger the content stretches out into a row and on a desktop the content sits neatly on one row with even spacing between each column. 
Footer | Social Media Links | Social Media links work and open up to the relevant website in a new tab. | Social Media links work and open up to the relevant website in a new tab. 

### Home
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Homepage loads | User opens Kytchen Table | User opens Kytchen Table and is automatically taken to the main homepage | User opens Kytchen Table and is automatically taken to the main homepage 
Logomark | User clicks on logomark to be taken to homepage | User can click on "Kytchen Table" and site will reload to home page | User can click on "Kytchen Table" and site reloads to home page
Hero Image | Hero image shows | Hero image should show at the top of the page with the words "Welcome to our Table" on top of this. The hero image should be responsive depending on the device used. | The hero image shows at the top of the page with the words "Welcome to our Table" on top of it. The hero image is responsive depending on the device used.
"Reserve a Table" Button | "Reserve a Table" button works | "Reserve a Table" button should take user to the reservation form if they are signed in or redirect them to sign in if they are not currently signed in. The button should change colour and invert when hovered over. | The "Reserve a Table" button takes user to reservation form if they are signed in or redirects them to sign in if they are not currently signed in. The button changes colour and inverts when hovered over. 
Image Gallery Carousel | Image Gallery shows a carousel of images | Image gallery shows carousel of images that automatically start when the page is loaded. When accessing the page as a desktop, arrows should be seen allowing the user to manually click through the photos. The photos can be updated through the Superadmin panel | Image gallery shows carousel of images that automatically starts when the page is loaded. When accessing the page as a desktop, arrows can be seen allowing the user to manually click through the photos. The photos can be updated through the Superadmin panel. 

### Our Philosophy
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Images | Images load | Images load when page loads | Images load when page loads. 
Images | Images are responsive | Images stack responsively depending on which device is used. On mobile devices images stack in a central column. On larger tablets and up images split out into formation sitting neatly with each block of text in alternating pattern to create a visually striking page. | Images stack responsively depending on which device is used. On mobile devices images stack in a central column. On larger tablets and up images split out into formation sitting neatly with each block of text in alternating pattern to create a visually striking page.

### Menu 
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Tasting and Signature Menus | Menu loads on launch | On launching the website both menus load, however the A La Carte menu remains hidden by Bootstrap pills until activated by the user. The user should instantly be able to see the signature tasting menu | On launching the website both menus load, however the A La Carte menu remains hidden by Bootstrap pills until activated by the user. The user can instantly be able to see the signature tasting menu 
Tasting Menu Order | Menu loads in correct order  | The Tasting Menu is ordered individually rather than following the alphabetising of the A La Carte. The order of the menu can be decided by the SuperAdmin and updates. | The Tasting Menu is ordered individually rather than following the alphabetising of the A La Carte. The order of the menu can be decided by the SuperAdmin and on reload updates to follow the order set in the Admin panel
Allergies | Allergies shown | Allergies should be shown underneath the menu item description and should be alphabetised. The allergies for each dish can be updated by the SuperAdmin in the Admin panel. | Allergies are shown underneath the menu item description and are alphabetised. The allergies for each dish can be updated by the SuperAdmin in the Admin panel and show on load. 
Bootstrap Pills | Pills launch content when clicked | User loads A La Carte menu when they click the "A La Carte" pill. User loads the starters of the A La Carte Menu when they click "Starters". User loads the mains of the A La Carte Menu when they click "Mains". User loads the Sides of the A La Carte Menu when they click "Sides". User loads the Desserts of the A La Carte Menu when they click "Desserts" | User loads A La Carte menu when they click the "A La Carte" pill. User loads the starters of the A La Carte Menu when they click "Starters". User loads the mains of the A La Carte Menu when they click "Mains". User loads the Sides of the A La Carte Menu when they click "Sides". User loads the Desserts of the A La Carte Menu when they click "Desserts"
Bootstrap Pills | Pills color inverts when active | The colour of the pill that is active inverts when the pill is active and showing the correct content. When a user hovers over an inactive pill, the colour inverts to show the user where they can click. | The colour of the pill that is active inverts when the pill is active and showing the correct content. When a user hovers over an inactive pill, the colour inverts to show the user where they can click. 

### Dine With Us
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Log in Required | Reservation form requires a user to be signed in to view | A user must be logged in as a registered user in order to see the reservation form. If the user is not logged in, they are redirected to the sign in page | A user must be logged in as a registered user in order to see the reservation form. If the user is not logged in, they are redirected to the sign in page
Reservation form loads | Reservation form loads | Provided a user is logged in they can see the reservation form on load. |  Provided a user is logged in they can see the reservation form on load.
Validation | Form Validation is working | If a user tries to submit a reservation form without providing the following fields: name, email, phone, reservation date, reservation time, guest number, they are immediately prompted to go back and fill the missing fields and the form cannot be submitted. | If a user tries to submit a reservation form without providing the following fields: name, email, phone, reservation date, reservation time, guest number, they are immediately prompted to go back and fill the missing fields and the form cannot be submitted. NOTE - Due to a bug that was unsolved at the time of submission, the expected HTML tooltip is not showing when the information is not provided. The validation works however, as a user cannot submit the form without providing valid information in the fields. 
Validation | Email validation is working | If a user tries to submit a reservation without a @ in the email field, they are prompted to go back and fill in the form | If a user tries to submit a reservation without a @ in the email field, they are prompted to go back and fill in the form. NOTE - Due to a bug that was unsolved at the time of submission, the expected HTML tooltip is not showing when the information is not provided correctly. The validation works however, as a user cannot submit the form without providing valid information in the email field. 
Validation | Phone validation is working | If a user tries to submit a reservation with letters or symbols rather than numbers then they are prompted to go back and fill in the form. | If a user tries to submit a reservation with letters or symbols rather than numbers then they are prompted to go back and fill in the form. NOTE - Due to a bug that was unsolved at the time of submission, the expected HTML tooltip is not showing when the information is not provided correctly. The validation works however, as a user cannot submit the form without providing valid information in the phone field.
Booking for past date | User cannot book a past date | The user is barred from booking a past date and previous dates are disabled for clicking. | The user is barred from booking a past date and previous dates are disabled for clicking. NOTE - There is a discrepency with Safari when accessed via a mobile phone which means that past dates can be clicked on. This appears to be a general issue with Safari on mobile and at the time of submission I was unable to figure a work around for it. However when trying to submit a reservation form through mobile Safari, the user is still unable to submit the form with a past date and a tooltip shows specifically on mobile Safari browsers saying "you cannot choose a past date".
Allergies tickbox | User can provide allergies | Allergies can be checked and unchecked to be provided at the time of form submission. There is no limit as to how many allergies can be added and as this is not a required field, forms can also be submitted without providing any allergies | Allergies can be checked and unchecked to be provided at the time of form submission. There is no limit as to how many allergies can be added and as this is not a required field, forms can also be submitted without providing any allergies
Special request | User can provide Special requests | Special requests can be provided in a text box form at the bottom of the reservation form which allows the user to send a short message to the restaurant ie if a guest is going for a birthday, or if they have an accessibility requirement that needs to be met. The special requests form is an optional form and therefore the form can be submitted wihout providing any special requests. | Special requests can be provided in a text box form at the bottom of the reservation form which allows the user to send a short message to the restaurant ie if a guest is going for a birthday, or if they have an accessibility requirement that needs to be met. The special requests form is an optional form and therefore the form can be submitted wihout providing any special requests. 
Successful Form Submission | Bootstrap Alert | When a form is successfully received, a small Bootstrap alert should show at the top of the scren saying "Your reservation has been submitted successfully!". When the user reloads the alert disappears. | When a form is successfully received, a small Bootstrap alert should show at the top of the scren saying "Your reservation has been submitted successfully!". When the user reloads the alert disappears.
Successful Form Submission | Django Admin panel | When a form is successfully received, it can be seen through the Django Admin panel. The admin panel is ordered by date, with the upcoming reservation at the top of the list. The admin panel shows the following information: user, Guest Name, Guest Email, Guest Phone, Reservation Date, Time Slot, Guest No., Special Requests, Allergies| When a form is successfully received, it can be seen through the Django Admin panel. The admin panel is ordered by date, with the upcoming reservation at the top of the list. The admin panel shows the following information: user, Guest Name, Guest Email, Guest Phone, Reservation Date, Time Slot, Guest No., Special Requests, Allergies

### My Reservations
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Upcoming reservations | Upcoming reservations displayed | Registered users hould see a full list of all their upcoming reservations, ordered by date from closest to furthest away. The user should see the date of the reservation, the timeslot for the reservation and the number of guests for the reservation along with two buttons - "Edit Reservation" and "Delete Reservation" | The user can see a full list of their upcoming reservations, ordered by date from closest to furthest away. The user can see the date of the reservation, the timeslot of the reservation and the number of guests for the reservation as well as two buttons - "Edit Reservation" and "Delete Reservation"
Buttons | Buttons colour change | The colours of the buttons should invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to | The colours of the button invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to
Modal | Edit Reservation modal launches | Upon clicking the "Edit Reservation" button, the modal should launch. The modal should show all of the booking details which the user can then update | Upon clicking the "Edit Reservation" button, the modal launches. The modal shows all of the booking details which can be updated by the user
Modal | Edit Reservation details | Once the reservation modal has launched, the user should be able to update any of the information in the modal and this should reflect on the booking admin page, and on the details on the My Reservation page. The modal should have the same validation as the original booking form, only allowing users to submit updated information if the name, email, phone number, reservation date and time slot are filled in. If any of these are not filled in, the user should be prompted to fill these in before the booking can be updated | Once the reservation modal has launched, the user can update any of the information in the modal and this is reflected on the booking admin page, and the details on the My Reservation page. The modal has the same validation as the original booking form, meaning users can only submit updated information when the name, emial, phone number, reservation date and time slots are filled in. If these fields are not completed, the user is prompted to fill these in before the booking can be updated. NOTE - the HTML tooltip does appear to show in the modal update, even though it does not appear on the original booking form. 
Modal | Delete Reservation modal launches | Upon clicking the "Delete Reservation" button, the user should be asked to confirm a second time that they would like to delete their reservation | Upon clicking the "Delete Reservation" button, the user is asked to confirm a second time that they would like to delete their reservation
Modal | Delete Reservation removes data | Upon being asked for secondary confirmation that the user wishes to delete the booking, the booking should be removed from the users My Reservations page, and the admin panel | Upon being asked for secondary confirmation that the user wishes to delete the booking, the booking is removed from the users My Reservations page and is removed from the admin panel. 

### Sign Up
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Sign Up | AllAuth form | AllAuth form loads, asking user to provide a mandatory username and password and an optional email. If the user tries to submit the form without providing this information, they should be prompted to fill in the required fields | AllAuth form loads, asking the user to provide a mandatory username and password, with an optional email. If the user tries to submit a form without providing the required fields, they are prompted to fill in the required fields
Button | Button colours change | The colours of the buttons should invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to | The colours of the button invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to 
Button | AllAuth form is successful | Upon the user providing all the required information, the user can hit Sign Up and the account is created and the page reloads to the home page |  Upon the user providing all the required information, the user can hit Sign Up and the account is created and the page reloads to the home page
Sign In link | Sign In link redirects | If the user clicks on the hyperlinked "log in here" they should be redirected to the sign in page | If the user clicks on the hyperlinked "log in here" they are redirected to the sign in page. 

### Sign In
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Sign In | AllAuth form | AllAuth form loads, asking user to provide mandatory username and password. If the user tries to log in without providing this information they should be prompted to fill in the required fields | AllAuth form loads, asking user to provide mandatory username and password. If the user tries to log in without providing this information, they are prompted to fill in the required fields.
Button | Button colours change | The colours of the buttons should invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to | The colours of the button invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to 
Sign in successful | User is logged in with correct credentials | Provided the correct credentials are provided, the user shoud be logged in and taken back to the home page. If the login credentials are incorrect, the user should be informed that the information provided is incorrect and should not be logged in.  | Providing the correct credentials are provided, the user is logged in and taken back to the home page. If the login credentials are incorrect, the user is informed that the information provided is incorrect and is not logged in
Sign Up link | Sign Up link redirects | If the user clicks on the hyperlinked "Sign Up here" they should be redirected to the Sign Up page | If the user clicks on the hyperlinked "Sign Up here" they are redirected to the Sign Up page. 

### Sign Out
Test | Action | Expected Result | Actual Result
--- | --- | --- | ---
Button | Button colours change | The colours of the buttons should invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to | The colours of the button invert when the user hovers their mouse over the button, allowing the user to see where they are pointing to 
Button | Sign out button works | Sign out button should successfully sign out the user, redirecting them to the Successful Sign Out page | Sign out button successfully signs out user and redirects them to the Successful Sign Out page
Successful Sign Out | Successful Sign Out page loads | Upon clicking the "Sign Out" button, the user should be taken to a page confirming successful sign out along with a "return home" button and a link to redirect the user back to the sign in page | Upon clicking the "Sign Out" button, the user is taken to a Successful Sign Out page along with a "return home" button and a link to redirect the user back to the sign in page
Sign Back In link | Sign Back in redirects to correct page | The Sign Back in link should redirect back to the login page | The Sign Back In Link redirects back to the login page

## Testing Against User Stories
User Story | Category (MoSCoW) | Met?
--- | --- | --- 
As a Site Admin I can create and amend menu items so that I can add or remove food options as new dishes are created in the restaurant | Must Have | Met
As a Site Admin I can create times and days of the week slots the restaurant is open so that I can monitor booking availability throughout the week | Must Have | Met - But created through model not through admin panel
As a Site Admin I can book tables in the booking slots so that I can book tables on behalf of guests | Must Have | Met
As a Site Admin I can see all of the bookings currently made so that I can be informed about how many covers are required at the restaurant at any given day and make any changes to bookings if needed | Must Have | Met
As a Site Admin I can delete any account so that I can control access to the user panel | Must Have | Met
As a User I can book a table in a slot so that I can reserve my table at the restaurant | Must Have | Met
As a User I can amend an upcoming booking so that I can change the details provided to the restaurant | Must Have | Met
As a User I can log out of the user portal so that I can know that I am no longer in my account | Must Have | Met
As a user I can view the menu so that I can decide what I would like to have | Must Have | Met
As a Site Admin I can be blocked from any more bookings that slots available per time slot so that I do not overbook any tables | Should Have | Met
As a User I can see the availability of tables at any given day and time slot so that I can decide what day and time to book a table | Should Have | Not Met - Future Feature
As a User I can see a home page which provides an overview of the restaurant so that I can know more about the restaurant | Should Have | Met
As a User I can see the contact details of the restaurant so that I know where to go and what number to call | Should Have | Met
As a user I can find out about the ethos of the restaurant so that I can decide if it is my sort of place to visit | Should Have | Met
As a User I can delete my account so that I no longer have an account with Kytchen Table | Should Have | Not Met - Future Feature
As a user I can sign up to the restaurants mailing list so that I can receive up to date information about changing menus at the restaurant | Could Have | Not Met - Future Feature
As a User I can see a 404 error page so that I can know I've gone to the wrong page | Could Have | Not Met - Future Feature
As a User I can filter the menu by allergen so that I can easily see what items contain food I am allergic to | Won't Have | Not Met - Future Feature

### Overall Testing Conclusion

All essential functionalities of the Kytchen Table website work as intended and meet the requirements of the user stories. Testing confirmed:
* Full CRUD functionality works for reservations
* Sign-up, login, and logout processes function correctly
* Responsiveness is maintained across all devices and browsers
* Accessibility standards are mostly met, with only minor colour contrast concerns

Overall testing confirms that the application is stable, user-friendly, fully responsive, and ready for production deployment. Any remaining issues are documented in Unsolved Bugs and planned for future development.

## Deployment
The live deployed application can be found on Heroku

This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

* Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
* Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click Create App.
* From the new app Settings, click Reveal Config Vars, and set your environment variables to match your private env.py file.

Key	| Value
--- | ---
CLOUDINARY_URL | user-inserts-own-cloudinary-url
DATABASE_URL | user-inserts-own-postgres-database-url
DISABLE_COLLECTSTATIC | 1 (this is temporary, and can be removed for the final deployment)
SECRET_KEY | any-random-secret-key

Heroku needs some additional files in order to deploy properly.

            requirements.txt
            Procfile
            
You can install this project's requirements.txt (where applicable) using:

            pip3 install -r requirements.txt

If you have your own packages that have been installed, then the requirements file needs updated using:

            pip3 freeze --local > requirements.txt

The Procfile can be created with the following command:

            echo web: gunicorn app_name.wsgi > Procfile

Replace app_name with the name of your primary Django app name; the folder where settings.py is located

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (recommended):

Select Automatic Deployment from the Heroku app.

Or:

* In the Terminal/CLI, connect to Heroku using this command: heroku login -i
* Set the remote for Heroku: heroku git:remote -a app_name (replace app_name with your app name)
* After performing the standard Git add, commit, and push to GitHub, you can now type:

            git push heroku main

* The project should now be connected and deployed to Heroku
* After deployment, I applied database migrations on Heroku using heroku run python manage.py migrate.

## Forking and Cloning
### Forking
Fork Repository
Follow the below steps to fork the repository:

Go to the GitHub repository
Click on Fork button in upper right hand corner

### Cloning
Follow the below steps to clone the repository:

Go to the GitHub repository
* Locate the Code button above the list of files and click it
* Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
* Open Git Bash
* Change the current working directory to the one where you want the cloned directory
* Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
* Press Enter to create your local clone.

# Tools & Technologies Used
* Balsamiq for wireframes
* Canva & Photoshop for favicon, logo and watermark creation
* Gemini AI as a prompt to create content for menus
* Google Fonts for web fonts
* Favicon for favicon
* Coolors for colour palette generation
* Our Own Thing's Font Pairing website for typography
* Mermaid to create an ERD for Kytchen Table
* Pexels for images that appeared across the website
* GitHub
* GitHub Issues
* GitHub Projects Kanban Board
* VSCode - along with Django
* Chat GPT for debugging assistance 
* CI PEP8 Linter
* JShint
* Heroku
* Google Lighthouse
* WAVE Accessibility Checker
* BrowserStack for browser testing
* Blisk for device testing

# Credits and Acknowledgements
Kytchen Table was heavily inspired by a restaurant I visited for my 30th birthday which is Simon Rogan's Henrock. It was a place that I was instantly inspired by with their ethos of sustainable farming and farm to table cooking which I find fascinating. That said, every menu item that appears on the website was created by me with some assistance from Gemini AI in putting the final menu together. Kyran Becker is a character I created as is the restaurant "Kytchen Table". To my knowledge there is no restaurant currently operating that has this restaurant name or the menu included on the website.

Some code was taken from the Code Institute I Think Therefore I Blog, particularly with the settings app. 

# A Final Note from the Developer
It feels almost silly to say, but as with every Code Institute project, the next one is always a steep learning curve which challenges and forces me to question my ability not just as a coder, but also as a creative. I really struggled when it came to deciding what I actually wanted to do for this final "big dog" full stack project, but the minute I got my inspiration I was off like a greyhound on a track. I found this genuinely puzzling, challenging, perplexing and at times really quite isolating as I tried to figure out how to build the website I wanted to create in what felt like so little time. I am pleased to say that I am truly proud of this final project that I have pulled together, despite all of the challenges along the way. There are still many features I would love to add — including a full user account page, a seasonal opening-hours system, and allergen filtering — but I am proud of how this MVP version reliably meets the core needs of both users and restaurant staff.

I continue to be endlessly appreciative of my mentor Spencer Barribal, who I can only hope and pray that by the time I got my results back from this project will have finally managed to complete on his house and will be off sunning himself on a beach somewhere. His was a voice of reason but also of hilarity, and I so endlessly enjoyed every single one of our calls, even if we did have to remind each other to stay on track!

I will never not be grateful to the love and support of my partner Jon who has taken on so much this year to ensure that I have the space and ability to put the time and effort into coding and to building my projects in a way that I am satisfied with, and I thank my lucky stars every day that a year from now we get to legally share the brain cell for the rest of our lives. I am also grateful to our little furry baby, Deedee, who was always there demanding pets and strokes when I was in a coding black hole. And of course, I could not have done this course at all without the love and support (both emotional and financial) of my parents, who have never known how to say no to me a day in their lives, but who love to remind me that there is a brain under all that fluff!

With just one more project to go in my Code Institute journey, I would like to finally thank Code Institute, for putting together this program which has helped me grasp a new interest in life. 

All trademarked and/or copyrighted content are the property of their respective owners.

Developed by Alice Foster, 2025.
