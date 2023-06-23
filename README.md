# **PC HAVEN**

## **Overview**

PC HAVEN is a B2C e-commerce site that sells Computer components. The site allows both registered and guest users to add Products to cart and checkout. Users of the site can search for products via search bar, filter Products or browse through all products available.

There are features available to Registered users including a personal Profile, Wishlist, the ability to review their Order history, add Product reviews and like Blog posts. The site also allows the user to subscribe to the PC HAVEN Newsletter and there is a Contact Us page in place if user needs to Contact the site owner to report issues.

Developed by Sean Finn.

![Techsini Screenshot](/docs/readme_screenshots/pchaven.webp)

[PC HAVEN - Live Webpage](https://pc-haven.herokuapp.com/) (Right-click to open in a new tab)

## **Project Goals**

This is my fifth portfolio project for [Code Institute](https://codeinstitute.net/) and my goal with this project is to display the skills I have learned throughout the course. I decided to build a Computer components e-commerce site as building PCs is something I am interested in.

## **Contents**

1. [Overview](#overview)
1. [Project Goals](#project-goals)
1. [UX](#ux)
   - [The Strategy Plane](#the-strategy-plane)
     - [The Ideal User](#the-ideal-user)
     - [Site Goals](#site-goals)
   - [Agile Planning](#agile-planning)
     - [Epics](#epics)
     - [User Stories](#user-stories)
   - [The Skeleton Plane](#the-skeleton-plane)
     - [Wireframes](#wireframes)
     - [Database Schema](#database-schema)
     - [Security](#security)
   - [The Scope Plane](#the-scope-plane)
   - [The Structure Plane](#the-structure-plane)
     - [Features](#features)
     - [Future Features](#future-features)
   - [The Surface Plane](#the-surface-plane)
     - [Design](#future-features)
       - [Colour Scheme](#colour-scheme)
       - [Typography](#typography)
       - [Imagery](#Imagery)
1. [Technologies Used](#technologies-used)
   - [Languages Used](#languages-used)
   - [Frameworks and Tools Used](#frameworks-and-tools-used)
   - [Libraries Used](#libraries-used)
1. [Testing](#testing)
1. [Deployment](#deployment)
1. [Credits](#credits)
1. [Acknowledgements](#acknowledgements)

## **UX**

## **The Strategy Plane**

PC HAVEN is intended to be a one stop shop for users looking to purchase Computer components. It is a business to consumer e-commerce site supplying various Computer components. All users will be able to browse/sort Products, add to cart and checkout. Registered users will be able to add Products to their Wishlist, view their Order history and update/save their delivery information for quicker checkouts. Registered users will also be able to review Products and like/comment on Blog posts.

Staff will be able to add/edit/delete Products and add/edit/delete Blog Posts without entering admin. Any user reviews can be edited/deleted by Staff if required. When dealing with Products Staff will be able to make a Product a featured Product to be displayed on Homepage or put a Product on sale.

The graphical elements and overall design of the site provide the user with an enjoyable experience with an aesthetically pleasing display.

### **The Ideal User**

- Someone looking to purchase Computer components
- Someone who would like to review/rate Products
- Someone who would like to create a wishlist of Products
- Someone who would like to view a tech Blog

### **Site Goals**

- To provide users with a place to purchase Computer components
- To provide users with the ability to review/rate products
- To provide users with the ability to create their own Profile and add Products to a Wishlist
- To provide users with the ability to view Blog posts related to tech

[Back to top &uarr;](#contents)

## **Agile Planning**

This project was developed using agile methodologies by delivering small features across the duration of the project. All User Stories were assigned to Epics, prioritized under the labels, Must Have, Should Have and Could Have. They were assigned story points according to complexity. Fibonacci sequence is employed for the Story points. "Must Have" stories were completed first, "Should Have's" and then finally "Could Have's".

It was done this way to ensure that all core requirements were completed first to give the project a complete feel. In some scenarios, certain "Should Have's" were implemented before schedule due to the nature of the implementation i.e. some Product related "Should Have's" were done during Product development with some "Must Have's" - Error templates developed later on. The rest were applied based on capacity and timing.

The Kanban board was created using Github projects and can be located [here](https://github.com/users/seanf316/projects/8) and can be viewed to see more information on the project cards. All stories have a full set of acceptance criteria to define the functionality that marks that story as complete.

![Project Kanban](docs/readme_screenshots/project.webp)

### **Epics**

18 Epics (milestones) were created which were then further developed into 45 User Stories. The details on each epic, along with the user stories linked to each one can be found in the project kanban board linked above. 2 Epics "Blog" & "Documentation" were missed when adding Epics at the start of the Project and were added at the time of implementation.

#### **EPIC: Initial Django Setup [#1](https://github.com/seanf316/PC-Haven/issues/2)**

`As a Developer, I can setup Django and start project, so that I can develop the site`

The Initial Django Setup epic was required to setup the project and confirm libraries, frameworks etc were installed correctly. Only then could further development progress.

#### **EPIC: AWS Setup [#2](https://github.com/seanf316/PC-Haven/issues/3)**

`As a Developer, I can setup AWS, so that I can store my static and media files for the site.`

AWS was setup to store all static and media files, this was done early in project development to help with early deployment.

#### **EPIC: Heroku Deployment [#3](https://github.com/seanf316/PC-Haven/issues/4)**

`As a Developer, I can deploy my site with Heroku, so that user's can view and interact with the site`

The Heroku Deployment epic was completed early on as we were advised during the course material that early deployment is critical to avoid any issues down the line with the production app. Heroku app was created and config vars were updated, app was linked to my projects Github repo for automatic deployments.

#### **EPIC: Base Html/Homepage [#4](https://github.com/seanf316/PC-Haven/issues/5)**

`As a Developer, I can design a nice aesthetically pleasing Homepage, so that the user has an enjoyable experience when entering the site`

The Base Html/Homepage epic was used to link various User Stories based around the design and responsiveness of the site. The Base template was created first so I could extend within further templates and then the homepage(index.html) was built using bootstrap and styled.

#### **EPIC: Setup AllAuth [#5](https://github.com/seanf316/PC-Haven/issues/6)**

`As a Developer, I can install AllAuth, so that it handles all the sites Authentication including Sign Up/Login/Logout/Email Verification and Password Reset`

AllAuth was installed to manage all of the sites authentication. Various User Stories were assigned to this Epic.

#### **EPIC: Products Setup (CRUD) [#6](https://github.com/seanf316/PC-Haven/issues/7)**

`As a Developer, I can setup Products to be displayed to the User, so that they can browse Products they may want to purchase`

The Products Setup Epic was used to link various User Stories based around the design and implementation of all the Product functionality.

#### **EPIC: Purchasing/Checkout [#7](https://github.com/seanf316/PC-Haven/issues/8)**

`As a Developer, I can create the Checkout functionality, so that customers can purchase Products on the site`

The Purchasing/Checkout was used to link various User Stories based around the design and implementation of all the Checkout functionality.

#### **EPIC: Stripe Setup [#8](https://github.com/seanf316/PC-Haven/issues/9)**

`As a Developer, I can setup Stripe, so that customers can successfully pay for their chosen Products`

The Stripe Epic covered any of the Stripe related User Stories. Stripe was installed to allow users to pay for their chosen Products.

#### **EPIC: User Profile (CRUD) [#9](https://github.com/seanf316/PC-Haven/issues/10)**

`As a Developer, I can add a Profile page for the user, so that they can store information about themselves i.e. Name, Shipping/Billing Address etc`

The User Profile epic is for all User Stories related to the setup of the profile, the CRUD functionality and templates design.

#### **EPIC: User Wishlist [#10](https://github.com/seanf316/PC-Haven/issues/11)**

`As a Developer, I can provide the User with a Wishlist function/page, so that they can add products to a Wishlist for future purchases`

The Wishlist epic was used to link any User Stories related to the setup of the Wishlist functionality and design.

#### **EPIC: Setup Email [#11](https://github.com/seanf316/PC-Haven/issues/12)**

`As a Developer, I can setup email functionality on the site, so that customers can receive emails containing such information like verification emails/password reset/order info etc`

The Setup Email epic was used to link any User Stories for the implementation of email functionality for the site. This was progressed early on in the development to be ready for early deployment.

#### **EPIC: Review Products (CRUD) [#12](https://github.com/seanf316/PC-Haven/issues/13)**

`As a Developer, I can add a Review option on the site Products, so that the user can provide their feedback on Products`

The Review Products epic is for all User Stories related to the Review Product functionality. Any templates created or styled were linked also.

#### **EPIC: Web Marketing [#13](https://github.com/seanf316/PC-Haven/issues/14)**

`As a Developer, I can create a Facebook page and Newsletter for the site, so that customers can follow the site via their Facebook account or subscribe to our sites Newsletter to keep up to date with new sales or products that may be launching`

The Web Marketing epic is for all User Stories related to Web Marketing like the setup of Newsletter and site Facebook page.

#### **EPIC: SEO [#14](https://github.com/seanf316/PC-Haven/issues/15)**

`As a Developer, I can research Google to find a list of short and long tail keyword, so that they can be applied to the sites code for SEO consideration`

The SEO epic is for all User Stories related to the site SEO implementation.

#### **EPIC: Contact Us [#15](https://github.com/seanf316/PC-Haven/issues/16)**

`As a Developer, I can provide functionality for users to Contact the site admin directly, so that they can provide feedback on the site or get in touch if they experience issues on the site`

The Contact Us epic is for all User Stories related to the Contact functionality. Any templates created or styled were linked also.

#### **EPIC: Status Error Templates [#16](https://github.com/seanf316/PC-Haven/issues/17)**

`As a Developer, I can create Status Error templates, so that I can secure my views and advise User when there is an issue`

The Status Error Templates epic is for all User Stories related to providing status error feedback to the User like 403, 404 and 500 status errors. Any templates created or styled were linked also.

#### **EPIC: Blog [#17](https://github.com/seanf316/PC-Haven/issues/52)**

`As a Developer, I can create functionality to add Blog Posts to the site, so that customers visiting the site can view posts related to the site and may spend more time on the site.`

The Blog epic is for all User Stories related to the Blog functionality. Any templates created or styled were linked also.

#### **EPIC: Documentation [#18](https://github.com/seanf316/PC-Haven/issues/63)**

`As a Developer, I can create documentation, so that fellow developers can understand what the site is and how it was built`

This epic is for all document related stories and tasks that are needed to document the software development lifecycle of the application. It aims to deliver quality documentation, explaining all stages of development and necessary information on running, deploying and using the application.

[Back to top &uarr;](#contents)

### **User Stories**

The following user stories (by epic) were completed throughout development.

#### **EPIC: Initial Django Setup [#1](https://github.com/seanf316/PC-Haven/issues/2)**

- As a Developer I can set up Django and install the supporting libraries predicted to be needed so that I am ready to start development [#19](https://github.com/seanf316/PC-Haven/issues/18)
- As a Developer I need to create the env.py and add to .gitignore so that I can securely deploy the site without exposing developer keys/information [#20](https://github.com/seanf316/PC-Haven/issues/19)

#### **EPIC: AWS Setup [#2](https://github.com/seanf316/PC-Haven/issues/3)**

- As a Developer I can setup the AWS Groups/Policies and Users so that so that the hosted static and media files are available to site when deployed. [#21](https://github.com/seanf316/PC-Haven/issues/20)

#### **EPIC: Heroku Deployment [#3](https://github.com/seanf316/PC-Haven/issues/4)**

- As a Developer I can deploy site to Heroku early so that I can confirm everything works before development of the site and to enable continuous testing within the production environment [#22](https://github.com/seanf316/PC-Haven/issues/21)

#### **EPIC: Base Html/Homepage [#4](https://github.com/seanf316/PC-Haven/issues/5)**

- As a Developer I can build a base template so that it can be extended to any templates that may require it [#23](https://github.com/seanf316/PC-Haven/issues/22)
- As a Developer I can design an aesthetically pleasing Homepage so that users have a positive experience when visiting the site [#24](https://github.com/seanf316/PC-Haven/issues/23)
- As a Developer I can implement message toasts so that the user/customer is alerted when they carry out and action or encounter and error. [#45](https://github.com/seanf316/PC-Haven/issues/45)

#### **EPIC: Setup AllAuth [#5](https://github.com/seanf316/PC-Haven/issues/6)**

- As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users [#25](https://github.com/seanf316/PC-Haven/issues/24)

#### **EPIC: Products Setup (CRUD) [#6](https://github.com/seanf316/PC-Haven/issues/7)**

- As a Developer I can create functional code to apply Products to my site so that the customer has Products to purchase [#27](https://github.com/seanf316/PC-Haven/issues/26)
- As a User I would like the ability to search for a product so that to see if the site sells it [#28](https://github.com/seanf316/PC-Haven/issues/27)
- As a User I would like to view a page containing the search results from my Product search so that so that I can find my prefered Product or see similar Products [#29](https://github.com/seanf316/PC-Haven/issues/28)
- As a User I would like a page that displays All Products the site offers so that I can browse and find products that I may want to purchase [#30](https://github.com/seanf316/PC-Haven/issues/29)
- As a User I would like the ability to sort products so that I can identity the best priced/rated Products the site offers [#31](https://github.com/seanf316/PC-Haven/issues/30)
- As a Developer I can allow the functionality to edit Products by staff members so that they can reduce/increase prices, change product descriptions/images etc [#32](https://github.com/seanf316/PC-Haven/issues/31)
- As a Developer I can add functionality for staff members to delete Products so that if they do not sell or there is problems with the Product it can be removed from the storefront [#33](https://github.com/seanf316/PC-Haven/issues/32)
- As a User I would like to view the details of any Product so that I can see if the Product has the required specifications that I need/want [#34](https://github.com/seanf316/PC-Haven/issues/33)

#### **EPIC: Purchasing/Checkout [#7](https://github.com/seanf316/PC-Haven/issues/8)**

- As a Customer I would like to add items that to a cart so that I can view all items and purchase or remove items at will. [#35](https://github.com/seanf316/PC-Haven/issues/34)
- As a Customer I would like to view all items in my cart so that I can manage the items I want to buy. [#36](https://github.com/seanf316/PC-Haven/issues/36)
- As a Developer I can add in functionality to advise customer of free delivery at a certain threshold so that customer is aware of delivery costs and can add more items if price is suitable. [#37](https://github.com/seanf316/PC-Haven/issues/37)
- As a Customer I would like to adjust/remove the amount of a certain item so that I can manage my items for purchase. [#38](https://github.com/seanf316/PC-Haven/issues/38)
- As a Customer I would like to receive a confirmation of my order so that I know the purchase has went through and I can see what I ordered [#39](https://github.com/seanf316/PC-Haven/issues/39)
- As a Developer I can add the code to update the stock levels when a purchase has occurred so that shop owner can manage the stock levels and order where required [#40](https://github.com/seanf316/PC-Haven/issues/40)
- As a Customer, I would like to save my billing/shipping information, so that I don't need to enter these details on every purchase [#41](https://github.com/seanf316/PC-Haven/issues/41)
- As a Developer I can create a checkout page so that the customer can enter their billing/shipping/payment information to complete purchase. [#42](https://github.com/seanf316/PC-Haven/issues/42)
- As a Customer I would like the ability to edit the quantity of an item in my cart so that I can update the amount I want to buy of a specific item [#43](https://github.com/seanf316/PC-Haven/issues/43)
- As a Customer I would like to remove an item from my cart so that if i decide its not what I want i can easily remove that item and continue purchase with the rest of my cart items [#44](https://github.com/seanf316/PC-Haven/issues/44)

#### **EPIC: Stripe Setup [#8](https://github.com/seanf316/PC-Haven/issues/9)**

- As a Developer I can implement Stripe so that it can manage payments for the site products at checkout [#46](https://github.com/seanf316/PC-Haven/issues/46)

#### **EPIC: User Profile (CRUD) [#9](https://github.com/seanf316/PC-Haven/issues/10)**

- As a customer I would like the ability to create my own Profile page so that I can save my shipping address for future purchases and track my orders [#47](https://github.com/seanf316/PC-Haven/issues/47)
- As a Developer I can implement functionality to allow a customer to save information to a personal Profile so that they can save information i.e. shipping address/orders for future review [#48](https://github.com/seanf316/PC-Haven/issues/48)

#### **EPIC: User Wishlist [#10](https://github.com/seanf316/PC-Haven/issues/11)**

- As a Customer I would like the ability to add products to a Wishlist so that I can keep a list of my products to purchase in the future [#49](https://github.com/seanf316/PC-Haven/issues/49)

#### **EPIC: Setup Email [#11](https://github.com/seanf316/PC-Haven/issues/12)**

- As a Developer I can add functionality to verify email and reset password so that the user has better security over their email being used and can reset password if they forget it [#26](https://github.com/seanf316/PC-Haven/issues/25)

#### **EPIC: Review Products (CRUD) [#12](https://github.com/seanf316/PC-Haven/issues/13)**

- As a Customer I would like to leave a review on a Product so that my fellow shoppers can benefit from my feedback and make informed purchasing decisions. [#50](https://github.com/seanf316/PC-Haven/issues/50)
- As a Developer I can build a page to display the Review form so that customer has the ability to write their review and submit it. [#51](https://github.com/seanf316/PC-Haven/issues/51)

#### **EPIC: Web Marketing [#13](https://github.com/seanf316/PC-Haven/issues/14)**

- As a Developer I can create a Facebook business page for my site so that I can market my website on the social platform [#60](https://github.com/seanf316/PC-Haven/issues/61)
- As a Developer I can implement a newsletter on my site so that customers can subscribe for future updates and deals which should bring them back to the site for future purchases. [#61](https://github.com/seanf316/PC-Haven/issues/62)

#### **EPIC: SEO [#14](https://github.com/seanf316/PC-Haven/issues/15)**

- As a Developer I can add helpful description and keywords so that my site can reach a wider audience [#59](https://github.com/seanf316/PC-Haven/issues/60)

#### **EPIC: Contact Us [#15](https://github.com/seanf316/PC-Haven/issues/16)**

- As a Developer I can add functionality to allow the customer to contact the site owner so that any issue they encounter can be logged and resolved [#57](https://github.com/seanf316/PC-Haven/issues/58)
- As a Developer I can build a Contact template so that customer can submit their issues [#58](https://github.com/seanf316/PC-Haven/issues/59)

#### **EPIC: Status Error Templates [#16](https://github.com/seanf316/PC-Haven/issues/17)**

- As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views [#54](https://github.com/seanf316/PC-Haven/issues/55)
- As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist [#55](https://github.com/seanf316/PC-Haven/issues/56)
- As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs [#56](https://github.com/seanf316/PC-Haven/issues/57)

#### **EPIC: Blog [#17](https://github.com/seanf316/PC-Haven/issues/52)**

- As a Developer I can create the functionality for site admin to add Blog Posts so that customer may spend more time on the site which may lead to more purchases. [#52](https://github.com/seanf316/PC-Haven/issues/53)
- As a Developer I can build some Blog related templates so that the site admin can display blog posts on their site for a good customer experience [#53](https://github.com/seanf316/PC-Haven/issues/54)

#### **EPIC: Documentation [#18](https://github.com/seanf316/PC-Haven/issues/63)**

#### **EPIC: Complete Documentation [#10](https://github.com/seanf316/PC-Haven/issues/10)**

- Create/Write README.md [#62](https://github.com/seanf316/PC-Haven/issues/64)
- Create/Write TESTING.md [#63](https://github.com/seanf316/PC-Haven/issues/65)

[Back to top &uarr;](#contents)

## **The Skeleton Plane**

#### **Wireframes**

This is the prototype of the project that may change during its development. Further styling was applied to Allauth email and password templates but they were not in the original scope of the project.

<details><summary>Desktop</summary>

![Desktop Part 1](/docs/wireframes/desktop/homepage.webp)
![Desktop Part 2](/docs/wireframes/desktop/products.webp)
![Desktop Part 3](/docs/wireframes/desktop/product_detail.webp)
![Desktop Part 4](/docs/wireframes/desktop/cart.webp)
![Desktop Part 5](/docs/wireframes/desktop/checkout.webp)
![Desktop Part 6](/docs/wireframes/desktop/order_complete.webp)
![Desktop Part 7](/docs/wireframes/desktop/blog.webp)
![Desktop Part 8](/docs/wireframes/desktop/blog_post.webp)
![Desktop Part 9](/docs/wireframes/desktop/contact.webp)
![Desktop Part 10](/docs/wireframes/desktop/sign_up.webp)
![Desktop Part 11](/docs/wireframes/desktop/sign_in.webp)
![Desktop Part 12](/docs/wireframes/desktop/sign_out.webp)

</details>

<details><summary>Tablet</summary>

![Tablet Part 1](/docs/wireframes/tablet/tablet1.webp)
![Tablet Part 2](/docs/wireframes/tablet/tablet2.webp)
![Tablet Part 3](/docs/wireframes/tablet/tablet3.webp)
![Tablet Part 4](/docs/wireframes/tablet/tablet4.webp)
![Tablet Part 5](/docs/wireframes/tablet/tablet5.webp)
![Tablet Part 6](/docs/wireframes/tablet/tablet6.webp)

</details>

<details><summary>Mobile</summary>

![Mobile Part 1](/docs/wireframes/mobile/mobile1.webp)
![Mobile Part 2](/docs/wireframes/mobile/mobile2.webp)
![Mobile Part 3](/docs/wireframes/mobile/mobile3.webp)
![Mobile Part 4](/docs/wireframes/mobile/mobile4.webp)
![Mobile Part 5](/docs/wireframes/mobile/mobile5.webp)
![Mobile Part 6](/docs/wireframes/mobile/mobile6.webp)

</details>

#### **Database Schema**

Entity relationship diagram was created using [DBeaver](https://dbeaver.io/) and shows the schemas for each of the models and how they are related.

![DB Diagram](docs/readme_screenshots/pchaven_erd.webp)

#### **Security**

Views were secured where needed using the Django decorator @login_required. Access to the views using the @login_decorator can only be accessed by registered users. This means that if a user tries to access a view that is decorated with @login_required, but they are not currently logged in, they will be redirected to the login page instead.

Environment variables were stored in an env.py for local development for security purposes to ensure no secret keys, API keys, or sensitive information was added to the repository. In production, these variables were added to the Heroku config vars within the project.

[Back to top &uarr;](#contents)

## **The Scope Plane**

- Responsive Design - The site should be fully functional on all devices from 320px up
- Hamburger menu for mobile devices
- Ability to perform CRUD functionality on Products, Profiles, Reviews, Blog Posts and Comments
- Restricted features for registered users such as Product reviewing, adding Products to Wishlist, editing Profile and Commenting/Liking Blog posts.
- Newsletter Subscribing

[Back to top &uarr;](#contents)

## **The Structure Plane**

### **Features**

`As a Developer I can design an aesthetically pleasing Homepage so that users have a positive experience when visiting the site`

**Navbar**

The Navbar contains links for Home, an All Products mega dropdown menu, About Us, Blog and Contact Us. There is also a Search link, My Account link with Account related dropdown and a link to the customer Cart.

The following navigation items are available on all pages:

- Home -> index.html - Visible to all
- All Products (Mega Drop Down):
  - Categories (e.g Cases) -> products.html - Visible to all
  - Sub-Categories (e.g Full Tower) -> products.html - Visible to all
- About Us -> index.html(#about) - Visible to all
- Blog -> blogs.html - Visible to all
- Contact Us -> contact.html - Visible to all
- Search -> base.html(Navbar/Search Input) - Visible to all
- My Account -> (Drop Down)- Visible to all
  - Register -> accounts/signup.html - Visible to logged out users
  - Login -> accounts/login.html - Visible to logged out users
  - My Profile -> profile.html - Visible to logged in users
  - Logout -> logout.html - Visible to logged in users
  - Product Management -> add_product.html - Visible to logged in super users
  - Blog Management -> add_blog.html - Visible to logged in super users
- Cart -> cart.html - Visible to all

The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices. It is easily noticeable, intuitive, and easy to use.

![Navbar Desktop 1](/docs/readme_screenshots/desktop_navbar.webp)
![Navbar Mobile 1](/docs/readme_screenshots/mobile_navbar.webp)

**Footer**

The footer is placed at the bottom of the page. There are 4 sections in the Footer - Products, Information, Follow Us and Subcribe. The Products section contains links to the various Product Categories, the Information section contains links to useful information for customers like the sites Privacy Policy/Terms And Conditions. The Follow Us setcion contains a link to the sites Facebook page. The Facebook link is displayed with the Facebook icon provided by Font Awesome. The Subscribe section contains a link to the sites Newsletter signup. There is also a small portion of text for the Copyright/Disclaimer. A link to the developer's Github repository is provided and displayed using the Font Awesome Github icon. These icons have aria labels added to ensure users with assistive screen reading technology know the purpose of the links. They also open new tabs as they lead users away from the site.

![Footer Desktop](/docs/readme_screenshots/desktop_footer.webp)
![Footer Tablet](/docs/readme_screenshots/tablet_footer.webp)
![Footer Mobile](/docs/readme_screenshots/mobile_footer.webp)

**Homepage**

The Homepage was originally planned to be a single landing page but was expanded throughout development. The Homepage is now a scrollable page containing various sections including About Us, Latest/Featured/On Sale Products and a Newsletter section for the user to view.

**Landing Page**

The Landing page contains a small welcome message/mission statement and a hero image containing various Computer components. A wave background svg image was created with Share Divider app.

![Landing Page](/docs/readme_screenshots/landing.webp)

**About Us**

The About Us section advises the User about the site and provides the overall mission statement.

![About Us](/docs/readme_screenshots/about.webp)

**Products On Sale**

The Products On Sale section provides an asthectically pleasing carousel containing Product cards that consists of all the Products on sale. This will benefit the customer who is looking for the latest deals on the site.

![Products On Sale](/docs/readme_screenshots/sale.webp)

**Featured Products**

The Featured Products section provides an asthectically pleasing carousel containing Product cards that consists of all the Faetured Products from the site stock. This will benefit the customer who is looking for the more cutting edge Products the site offers.

![Featured Products](/docs/readme_screenshots/featured.webp)

**Latest Products**

The Latest Products section provides an asthectically pleasing carousel containing Product cards that consists of all the Latest Products from the site stock. This will benefit the customer who is looking for the latest Products that were added to the sites stock.

![Latest Products](/docs/readme_screenshots/latest.webp)

**Newsletter**

`As a Developer I can implement a newsletter on my site so that customers can subscribe for future updates and deals which should bring them back to the site for future purchases.`

The Newsletter section provides an asthectically pleasing embedded form provided by Mailchimp. This allows the user to subscribe to the sites Newsletter and receive updates/latest offerings for the site. The Newsletter will be expanding upon further in the Web Marketing section.

![Newsletter](/docs/readme_screenshots/newsletter.webp)

**Movie Search**

`As a User I want to have a section where I can search for a Movie so that I can easily find the Movie I want to review`

The Movie Search page has a similar layout to the Home page as it includes the hero image but this time a search input is provided and a search button to execute the users' Movie search. The search feature works in tandem with the TMDB and makes an API based on the query the user enters.

![Search Desktop](/docs/readme_screenshots/desktop_search.webp)

**Movie Search Results**

`As a Developer I can create the Movie Search Results template so that the User has a clear display of the results from their search`

The Search Results page is displayed with the users' Movie search query at the top of the page and for each Movie received in the results of the API call a card is generated containing the Movie backdrop image, the title of the movie, and a "View Movie" button. If a backdrop image is not available for Movies in the results a default image has been provided as backup. I have set the results to display 12 movies per page, this was a design choice to have an even layout across devices. Prev/Next buttons are displayed at the bottom of the page for pagination with the views.

In the occurrence where no results for the query are available a message will be displayed to the user along with a button linking the user back to the Movie Search page.

![Search Results Desktop 1](/docs/readme_screenshots/desktop_searchresults1.webp)
![Search Results Desktop 2](/docs/readme_screenshots/desktop_searchresults2.webp)

**Trending/Top Rated Movies**

`As a Developer I can build a page to display Trending Movies so that the User can see the latest Trending Movies`

`As a Developer I can build a page to display the Top Rated Movies so that the User can easily get access to the Top Rated Movies of all time`

There are two Movie category pages provided for the user - Trending & Top Rated. They were not in the original scope of the project but during development, I decided to implement them as an extra feature for the user. Each page makes a call to the TMDB API and displays the most up-to-date results on the page to the user in the form of Movie posters. Each Movie poster is an anchor that can be clicked and will bring the user to the Movie Details page for that selected Movie. If a poster image is not available for Movies in the results a default image has been provided as a backup. I have set the results to display 18 movies per page, this was a design choice to have an even layout across devices. Prev/Next buttons are displayed at the bottom of the page for pagination with the views.

![Trending Movies Desktop](/docs/readme_screenshots/desktop_trending.webp)
![Top Rated Movies Desktop](/docs/readme_screenshots/desktop_toprated.webp)

**Movie Details**

`As a User I want to view the Movie details from my search so that I can read the synopsis and check reviews`

`As a User I would like the ability to add Movies to a watchlist so that I can have a list of movies that I can refer to when looking for something to watch`

Registered users can access the Movie Details page.

The Movie Details page contains all the details of the Movie selected by the user from the pages mentioned above. A horizontal card layout is used to display the following details from the API - Movie poster/backdrop, title, overview, director, runtime, and release year. A rating is provided too if the Movie has been reviewed, it retrieves all the ratings from all user reviews for this specific movie and shows the average rating. Buttons for Trailer and IMDb are displayed if they are contained in the movie results from the API call. If a trailer does exist users can click the trailer button and a modal will appear containing that movie trailer. If there is an IMDb id provided the button will bring the user to the movies' IMDb page in a new tab.

2 more buttons are displayed to the user "Add to Watchlist +" and "Review". Clicking the "Add to Watchlist +" will add the movie to the user's watchlist which can be viewed on the user's Profile page. Clicking the "Review" button will open the Review form page and allow the user to submit a review which again will be linked back to their Profile page where they can view all reviewed Movies. If a user has added the movie to their watchlist the button will change to "Remove from Watchlist -" and this can be toggled again to remove the Movie from the user's watchlist. User can manage their watchlist from their Profile page. If the movie has been reviewed by the user the "Review" button will now display "Reviewed", users can manage (Edit/Delete) their reviews from the All Reviews page or can manage reviews directly from their Profile page.

![Movie Details](/docs/readme_screenshots/desktop_movie.webp)
![Movie Details Trailer](/docs/readme_screenshots/desktop_movietrailer.webp)

**Reviews**

`As a User I want the ability to review Movies so that I can share my thoughts of the Movie with family and friends`

`As a User I would like the ability to edit my review so that I can fix any spelling or format issues`

`As a User I would like the ability to delete my review so that I can manage my reviews and in the case of accidentally selecting the wrong Movie and reviewing it`

Creating and viewing reviews are features only available to registered users.

When the user clicks the Review button on the Movie Details page they will brought to the Review page that contains the Review form for the user to fill out. The page contains the backdrop image for that movie, the movie title, the reviewer's username, and the form itself. There are 2 inputs on the form "Review (Max 2500 Characters)" and "Rating (1-10)" with 2 buttons "Update" and "Delete". When the form is filled out correctly the user can submit their review, by submitting the review will be added to the user's review list and the review will be rendered on the Reviews page.

The user can manage their review from the Reviews page or on their Profile page. They can edit their review from either location, if the user decides to delete their review a modal will pop up asking for the user to confirm the deletion. Once deleted the Review will be removed from the Profile reviews list and the button on the Movie Details page will be returned to the "Review" state. Each review will also show a "Comment" button on the Review page to allow users to comment on reviews.

![Review 1](/docs/readme_screenshots/desktop_review.webp)
![Review 2](/docs/readme_screenshots/desktop_reviews.webp)
![Review 3](/docs/readme_screenshots/desktop_reviewdelete.webp)

**Comment**

`As a User I would like the ability to comment on Reviews so that I can participate in conversations with fellow reviewer's`

Creating and viewing comments are features only available to registered users.

On the Reviews page, users can comment on any review by clicking the "Comment" button. When the button is clicked users will be brought to the comment page that renders the comment form. The page contains the backdrop image for that movie, the movie title, the reviewer's username, and the form itself. There is 1 input on the comment form "Comment (Max 500 Characters)" and 1 button "Update". When the user has submitted their comment it will be applied to the Review card on the Reviews page. Here the user will see their comment, Edit & Delete icons, the date of the comment, and the commenter's username. The user can edit or delete their comment by clicking either icon.

![Comment 1](/docs/readme_screenshots/desktop_comment.webp)
![Comment 2](/docs/readme_screenshots/desktop_commentreview.webp)

**Profile**

`As a User I would like access to my Profile so that I can upload an image or alter my details where needed`

Profile features are only available to registered users.

When a user signs up to the site a Profile will automatically be created for them. They can access their Profile page from the Profile Navbar link. On the Profile page, the user can add/change information like their username, first name, surname, about, and more. Users can also upload their own Profile image and if they do not want to a default image is provided. Users will also be able to manage their Movie Watchlist and Reviews list.

![Profile 1](/docs/readme_screenshots/desktop_profile.webp)
![Profile 2](/docs/readme_screenshots/desktop_profileedit1.webp)
![Profile 3](/docs/readme_screenshots/desktop_profileedit2.webp)

**Toasts**

Custom toasts were implemented throughout the site. This will provide feedback to the user when they carry out an action on the site. Below are are few toast references:

![Toast 1](/docs/readme_screenshots/desktop_toast.webp)
![Toast 2](/docs/readme_screenshots/desktop_toast1.webp)
![Toast 3](/docs/readme_screenshots/desktop_toast2.webp)
![Toast 4](/docs/readme_screenshots/desktop_toast3.webp)
![Toast 5](/docs/readme_screenshots/desktop_toast4.webp)
![Toast 6](/docs/readme_screenshots/desktop_toast5.webp)
![Toast 7](/docs/readme_screenshots/desktop_toast6.webp)
![Toast 8](/docs/readme_screenshots/desktop_toast7.webp)

**Error Pages**

**404 Page**

`As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist`

A 404 page has been implemented and will display if a user navigates to a broken link.

The 404 page will allow the user to easily navigate back to the main website if they direct to a broken link / missing page, without the need for the browser's back button.

![Error 404](/docs/readme_screenshots/desktop_404.webp)

**403 & 403_csrf Pages**

`As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views`

A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content. Users will be directed to this page if they alter the URLs and attempt to edit, delete, or access pages that are restricted.
A 403_csrf error page has been implemented to provide feedback to the user when there is an issue with csrf verification.

![Error 403](/docs/readme_screenshots/desktop_403.webp)
![Error 403_csrf](/docs/readme_screenshots/desktop_403_csrf.webp)

**500 Page**

`As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs`

A 500 error page has been displayed to alert users when an internal server error occurs. The message relays to users that the problem is on our end, not theirs.

![Error 500](/docs/readme_screenshots/desktop_500.webp)

**Favicon**

A favicon has been added the website to enable users to easily locate the website in the browser when multiple tabs are open.

**Mobile**

`As a User I would like to view the site on my different devices so that I can view the site on the go`

The site was created Mobile first and scaled up to larger devices using Bootstrap and media queries.

![Mobile 1](/docs/readme_screenshots/mobile1.webp)
![Mobile 2](/docs/readme_screenshots/mobile2.webp)
![Mobile 3](/docs/readme_screenshots/mobile3.webp)
![Mobile 4](/docs/readme_screenshots/mobile4.webp)
![Mobile 5](/docs/readme_screenshots/mobile5.webp)
![Mobile 6](/docs/readme_screenshots/mobile6.webp)

[Back to top &uarr;](#contents)

### **Future Features**

**More Movie Categories**

In the future I would like to spend more time working with the TMDB API to add further Movie categories for the user like Upcoming movies, Now Playing, etc

**Movie Details Enhancements**

I would like to enhance the Movie Details information in the future to branch off into a Cast/Crew page that would display all the actors involved in the Movie. Within the Cast information, a user could click on an Actor's image and be shown other movies that they have appeared in.

**Latest Trailers**

A page dedicated to just Trailers for new and upcoming movies that the user can view. The thinking would be that it would update weekly and show the latest trailers at the top of the page.

**Genre Page**

A page where a user would have a dropdown containing all the different Movie genres i.e. Action, Thriller, Comedy, etc
The user would select one and a call would be made to the API to retrieve the latest Movies in the genre chosen.

[Back to top &uarr;](#contents)

## **The Surface Plane**

### **Design**

#### **Colour Scheme**

I opted for a very minimalistic aesthetic and the below 4 colours were chosen. I went for a darker theme with an aqua blue to add some contrast and vibrance to the site. The colours have been implemented across the site and are included in the buttons/links and their hover effects.

![Coolors](/docs/readme_screenshots/coolors.webp)

#### **Typography**

The Poppins font was used throughout the website. This font is from google fonts and was imported into the style sheet.

#### **Imagery**

The hero image was taken from TopPng and was free for personal use. The image used as the Profile background was taken from wallpaperflare.com

[Back to top &uarr;](#contents)

## **Technologies Used**

### **Languages Used**

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### **Frameworks and Tools Used**

1. [Django](https://www.djangoproject.com/)
   - Django was used as the main python framework in the development of this project
1. [Bootstrap](https://blog.getbootstrap.com/)
   - Bootstrap was used for general layout and spacing requirements for the site.
1. [ElephantSQL](https://www.elephantsql.com/)
   - ElephantSQL was used for the Production database.
1. [Cloudinary](https://cloudinary.com/)
   - Cloudinary was used to store all static files and images
1. [TMDB](https://www.themoviedb.org/)
   - TMDB API functionality was used throughout the project.
1. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub is used to store the project's code after being pushed from Git.
1. [Heroku](https://www.heroku.com/)
   - Heroku was used to deploy the app.
1. [Balsamiq](https://balsamiq.com/)
   - Balsamiq was used to produce the sites wireframes
1. [XConvert](https://www.xconvert.com/)
   - XConvert was used to convert images to webp or png where required.
1. [Stackoverflow](https://stackoverflow.com/)
   - Stackoverflow was used on many occasions to figure out some troublesome code.
1. [CI Python Linter](https://pep8ci.herokuapp.com/)
   - I used CI Python Linter for the validation of the site's Python code.
1. [Grammarly](https://www.grammarly.com/)
   - Grammarly was used to check typography.
1. [Quicktime Player](https://support.apple.com/downloads/quicktime)
   - Quicktime Player was used to take recordings of the screen.
1. [ezgif.com](https://ezgif.com/)
   - ezgif.com was used to convert screen recordings to gif.
1. [Xnip](https://www.xnipapp.com/)
   - Xnip was used to capture all the game screenshots.
1. [DBeaver](https://dbeaver.io/)
   - DBeaver was used to generate the Database Schema diagram.

### **Libraries Used**

- asgiref - A standard Python library to allow for asynchronous web apps and servers to communicate with each other.
- cloudinary - A Python package allowing integration between the application and Cloudinary.
- coverage - is a third-party package that helps developers measure code coverage in their Python codebase.
- dj-database-url - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
- dj3-cloudinary-storage - A Django package that facilitates integration with Cloudinary storage.
- Django - A python package for the Django framework.
- django-active-link - A Django package used to highlight an active link in the site navigation bars.
- django-allauth - An integrated set of Django applications addressing user authentication, registration and account management.
- django-ckeditor - is a third-party package that provides a rich text editor widget for Django web applications.
- django-crispy-forms - A Django package that provides tags and filters to control the rendering behaviour of Django forms.
- django-js-asset - is a third-party package for Django that simplifies the process of including JavaScript assets in Django templates.
- django-richtextfield - is a third-party package for Django that provides a model field for rich text editing.
- gunicorn - A Python WSGI HTTP Server for UNIX.
- oauthlib - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
- psycopg2 - A PostgreSQL database adapter for Python.
- PyJWT - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
- python3-openid - A set of Python packages to support use of the OpenID decentralized identity system.
- pytz - A Python package for world timezone definitions, modern and historical.
- requests-oauthlib - A Python package for OAuthlib authentication support for Requests.
- sqlparse - A non-validating SQL parser for Python.

[Back to top &uarr;](#contents)

## **Testing**

I have included details of testing both during development and post-development in a separate document called [TESTING.md](TESTING.md)

[Back to top &uarr;](#contents)

## **Deployment**

### **GitHub**

This project was developed by forking a specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.

1. Click Use this template
2. Name the repository
3. Launch using the Gitpod web extension
4. Pin project in Gitpod workspaces

### **Version Control**

For version control the following steps were made:

For version control the following steps were made:

1. Changes made to files in Gitpod
2. Files made ready for commit with command - git add "filename", or git add . to add all files
3. For the commits the following command was run along with commit description - git commit -m "This is my commit etc"
4. To move the changes to Github the following command was run - git push
5. Alternatively files can be made ready for commit using the Source Control staging area in Gitpod
6. Files were staged and a message describing the commit was made before committing and pushing it to GitHub

### **Clone Repo**

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:

1. Navigating to https://github.com/seanf316/P4-Cinema-Go
2. Clicking on the arrow on the green code button at the top of the list of files
3. Select Local then HTTPS copy the URL it provides to the clipboard
4. Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
5. Type 'git clone' and paste the HTTPS link you copied from GitHub
6. Press enter and git will clone the repository to your local machine

### **Forking the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the repository [P4-Cinema-Go](https://github.com/seanf316/P4-Cinema-Go)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### **Final Deployment with Heroku**

The below steps were followed to deploy this project to Heroku:

1. Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars, enter the below:
   - SECRET_KEY: (Enter your secret key)
   - DATABASE_URL: (Enter the database URL from ElephantSQL)
   - CLOUNDINARY_URL: (Enter Cloudinary API URL)
   - PORT: 8000
   - API_KEY: (An API key will need to be retrieved from the [TMDB](https://www.themoviedb.org/))
4. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
   Once GitHub is chosen, find your repository and connect it to Heroku.
5. Scroll down to Manual Deploy, make sure the "main" branch is selected, and click "Deploy Branch".
6. The deployed app can be found [here](https://cinema-go-p4.herokuapp.com/).

[Back to top &uarr;](#contents)

## **Credits**

1. [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
   - This repository was created using the template provided by Code Institute. Also, without the knowledge gained through the coursework, I would not be able to create this site so thank you Code Institute.
1. [Django Documentation](https://docs.djangoproject.com/en/4.0/)
   - Thanks to the Django docs which were also used as a step-by-step while going through the project to ensure everything was set up correctly.
1. [Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/faq.html)
   - Thanks to the Alluath documentation which was referenced during development.
1. [Daisy McGirr - Gamer Reviews](https://github.com/Daisy-McG/Gamer-Reviews)
   - The above was created in a study group for students with CI, I have used the Debug method in my project.
1. [Corey Schafer](https://www.youtube.com/watch?v=FdVuKt_iuSI)
   - Corey Schafer for the tutorial to get automatic profile creation and updating working as intended for my project.
1. [Stackoverflow](https://stackoverflow.com/)
   - I found myself on Stackoverflow so many times researching issues. This a fantastic place to learn and troubleshoot code.
1. [Slack](https://slack.com/intl/en-ie/)
   - The slack community is great and I reached out to fellow students who had already completed their P4 for their advice and got some nice tips and feedback. I attending some webinars by CI staff which I found very beneficial.
1. [Youtube](https://www.youtube.com/)
   - Various videos were watched for further learning and Django project ideas. Some playlists I have reviewed are [Django Project: Movie App](https://www.youtube.com/watch?v=tm9Yps3IkmQ&list=PLBQzvdjNG8c-g_mVYUNiVDwwO5YgcbNwT), [Django IMDB clone](https://www.youtube.com/watch?v=FawGmAas4h0&list=PL9tgJISrBWc6ktmvTSLGrn055XzVb0OwZ&index=1)
1. Matt Boden, Gareth McGirr & Fernanda Brito
   - I reviewed the above Project 4 repos for inspiration on README layouts and testing.

## **Acknowledgements**

- To my amazing wife Denise who has supported me every day and kept me motivated. P4 has been by far the most time-consuming to date, Denise consistently encouraged me to work on the project while keeping our 6-year-old son entertained. I couldn't do this without her.
- My son Alex for always making me laugh and never getting mad when Dad had to study.
- To my family and friends who tested the site and provided information on bugs/errors and general feedback
- To my mentor Daisy Mc Girr, Daisy always goes above and beyond. Even outside of project planning she is great for advice and is a great help to the Slack community too.

[Back to top &uarr;](#contents)
