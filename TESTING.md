# **Cinema | Go Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself and also by my peers.

## **Contents**

1. [Testing Overview](#testing-overview)
1. [Automated Testing](#automated-testing)
   - [Unit Testing](#unit-testing)
   - [Site Coverage Report](#site-coverage-report)
1. [Manual Testing/User Story Testing](#manual-testinguser-story-testing)
   - [Navbar](#navbar)
   - [Homepage](#homepage)
   - [Footer](#footer)
   - [Products](#products)
   - [Cart](#cart)
   - [Checkout](#checkout)
   - [Order Complete](#order-complete)
   - [Profile](#profile)
   - [Blog/Blog Posts](#blogblog-posts)
   - [Contact Us](#contact-us)
   - [Authentication](#authentication)
1. [Javascript Testing](#javascript-testing)
1. [Validators](#validators)
   - [CI Python Linter](#ci-python-linter)
   - [JSHint](#jshint)
   - [W3C CSS Validator](#w3c-css-validator)
   - [W3C Markup Validator](#w3c-markup-validator)
   - [Lighthouse](#lighthouse)
   - [Lighthouse Errors](#lighthouse-errors)
   - [Wave Accessibility Tests](#wave-accessibility-tests)
1. [Responsiveness](#responsiveness)
1. [Bugs & Fixes](#bugs--fixes)
1. [Unresolved Bugs/Issues](#unresolved-bugsissues)

## **Automated Testing**

### **Unit Testing**

Unit tests were created to test the functionality of the apps. These can be found in the tests.py files in the respective apps.

#### **Home**

![Home](/docs/unitests/home.jpg)

#### **Blog**

![Blog](/docs/unitests/blog.jpg)

#### **Cart**

![Cart](/docs/unitests/cart.jpg)

#### **Checkout**

![Checkout](/docs/unitests/checkout.jpg)

#### **Contact**

![Contact](/docs/unitests/contact.jpg)

#### **Products**

![Products](/docs/unitests/products.jpg)

#### **Profiles**

![Contact](/docs/unitests/profiles.jpg)

#### **Reviews**

![Contact](/docs/unitests/reviews.jpg)

[Back to top &uarr;](#contents)

### **Site Coverage Report**

Through my testing, I was able to get a total of 91% coverage across the site. The remaining 9% should be covered through the manual testing below.

![Coverage](/docs/unitests/coverage.jpg)

[Back to top &uarr;](#contents)

## **Manual Testing/User Story Testing**

Some features of the site are restricted to registered users such as adding Product reviews, adding Products to a wishlist, Commenting/Liking blog posts, and editing a Profile. There are also features restricted to Staff, the functional tests take this into account.

### **Navbar**

`As a Developer I can build a base template so that it can be extended to any templates that may require it`

**Acceptance Criteria**

- When the template is extended to another template all HTML code is applied i.e. Navbar/Footer

`As a User I would like the ability to search for a product so that I can see if the site sells it`

**Acceptance Criteria**

- User has access to a Product Search input that will reference the database for the users requested Product

Functional testing was carried out on the Navbar and all links go to their relevant pages as expected. Navbar is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

All users can enter a search query in the Search input from the Search dropdown.

**User Not Registered**

![Navbar 1](/docs/testing_screenshots/navbar_loggedout.jpg)

**User Registered**

![Navbar 2](/docs/testing_screenshots/navbar_loggedin.jpg)

**User Registered and Staff**

![Navbar 3](/docs/testing_screenshots/navbar_staff.jpg)

**All Users**

![Search Dropdown](/docs/testing_screenshots/search.jpg)
![Search Query](/docs/testing_screenshots/search1.jpg)
![Search Results](/docs/testing_screenshots/search2.jpg)

![All Products Dropdown](/docs/testing_screenshots/allproducts.jpg)
![Category Select](/docs/testing_screenshots/category.jpg)
![Category Results](/docs/testing_screenshots/category_results.jpg)

[Back to top &uarr;](#contents)

### **Homepage**

`As a Developer I can design an aesthetically pleasing Homepage so that users have a positive experience when visiting the site`

**Acceptance Criteria**

- Homepage is created and is responsive on all devices
- Users can easily identify what the site is about based on the landing page

Functional testing was carried out on the Homepage, this included all links/buttons on the Homepage. The Homepage is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

The landing page contains text Welcoming the user and providing information about the site, the About Us section on Homepage expands on this - see Feature images and Mobile gifs in [README.md](README.md).

![Landing Page Text](/docs/testing_screenshots/landing.jpg)

**All Users**

![Homepage](/docs/testing_screenshots/homepage.jpg)
![Homepage](/docs/testing_screenshots/homepage.gif)

[Back to top &uarr;](#contents)

#### **Newsletter**

`As a Developer I can implement a newsletter on my site so that customers can subscribe for future updates and deals which should bring them back to the site for future purchases.`

**Acceptance Criteria**

- User can subscribe to the site Newsletter

![Newsletter1](/docs/testing_screenshots/newsletter2.jpg)
![Newsletter1](/docs/testing_screenshots/newsletter.jpg)
![Newsletter2](/docs/testing_screenshots/newsletter1.jpg)

[Back to top &uarr;](#contents)

### **Footer**

`As a Developer I can build a base template so that it can be extended to any templates that may require it`

**Acceptance Criteria**

- When the template is extended to another template all html code is applied i.e. Navbar/Footer

Functional testing was carried out on the Footer and all links are working as expected. Links not relative to the site open in a separate tab. The Footer is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

![Footer](/docs/testing_screenshots/footer.jpg)
![Footer Gif](/docs/testing_screenshots/footer.gif)

[Back to top &uarr;](#contents)

### **Products**

#### **Products Page**

`As a User I would like a page that displays All Products the site offers so that I can browse and find products that I may want to purchase`

**Acceptance Criteria**

- User can access a Products Page that displays all products the site has for sale

`As a User I would like the ability to sort products so that I can identity the best priced Products the site offers`

**Acceptance Criteria**

- User can sort Products by Price

Functional testing was carried out on the All Products page, the All Products page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

**User Not Registered**

![Products Page1](/docs/testing_screenshots/products.jpg)
![Products Gif1](/docs/testing_screenshots/products.gif)
![Products Cart Add](/docs/testing_screenshots/products_cart.gif)

**User Registered**

![Products Page2](/docs/testing_screenshots/products1.jpg)
![Products Gif2](/docs/testing_screenshots/products1.gif)

**User Registered and Staff**

![Products Page3](/docs/testing_screenshots/products2.jpg)
![Products Gif3](/docs/testing_screenshots/products2.gif)

[Back to top &uarr;](#contents)

#### **Products Detail Page**

Functional testing was carried out on the Products Detail page, the Products Detail page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

**User Not Registered**

![Products Detail Page1](/docs/testing_screenshots/prod_details1.jpg)
![Products Detail Gif1](/docs/testing_screenshots/prod_details1.gif)
![Products Detail Gif2](/docs/testing_screenshots/prod_details2.gif)

**User Registered**

![Products Detail Page2](/docs/testing_screenshots/prod_details2.jpg)
![Products Detail Gif3](/docs/testing_screenshots/prod_details3.gif)

**User Registered and Staff**

![Products Detail Page3](/docs/testing_screenshots/prod_details3.jpg)
![Products Detail Gif4](/docs/testing_screenshots/prod_details4.gif)

[Back to top &uarr;](#contents)

#### **Products Reviews**

Product reviews are a restricted feature available to registered users only.

`As a Customer I would like to leave a review on a Product so that my fellow shoppers can benefit from my feedback and make informed purchasing decisions.`

**Acceptance Criteria**

- Customer can write a review for a Product

`As a Developer I can build a page to display the Review form so that customer has the ability to write their review and submit it.`

**Acceptance Criteria**

- Customer clicks Add Review button and Add Review page is displayed.

**User Registered**

![Add Product Review](/docs/testing_screenshots/add_review.jpg)
![Add Product Gif](/docs/testing_screenshots/add_review.gif)

![Edit Product Review](/docs/testing_screenshots/edit_review.jpg)
![Edit Product Gif](/docs/testing_screenshots/edit_review.gif)

[Back to top &uarr;](#contents)

#### **Product Management**

Product Management features are restricted to staff(super_users) only. This includes the Adding/Editing/Deleting of Products.

**User Registered and Staff**

`As a Developer I can create functional code to apply Products to my site so that the customer has Products to purchase`

**Acceptance Criteria**

- Customer clicks Add Review button and Add Review page is displayed.

![Add Product](/docs/testing_screenshots/add_product.jpg)
![Add Product Gif](/docs/testing_screenshots/add_product.gif)

`As a Developer I can allow the functionality to edit Products by staff members so that they can reduce/increase prices, change product descriptions/images etc`

**Acceptance Criteria**

- Staff members can Edit Products

`As a Developer I can add functionality for staff members to delete Products so that if they do not sell or there is problems with the Product it can be removed from the storefront`

**Acceptance Criteria**

- Staff members have the ability to Delete Products

![Edit Product](/docs/testing_screenshots/edit_product.jpg)
![Edit Product Gif](/docs/testing_screenshots/edit_product.gif)
![Delete Product Gif](/docs/testing_screenshots/delete_product.gif)

[Back to top &uarr;](#contents)

### **Cart**

Functional testing was carried out on the Cart page, the Cart page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

`As a Customer I would like to add items that to a cart so that I can view all items and purchase or remove items at will.`

**Acceptance Criteria**

- Customer both Guest/Registered can add items from the Products page to the cart.

`As a Customer I would like to view all items in my cart so that I can manage the items I want to buy.`

**Acceptance Criteria**

- Customer can click on the Cart icon in nav and view items in the cart.

`As a Customer I would like the ability to edit the quantity of an item in my cart so that I can update the amount I want to buy of a specific item`

**Acceptance Criteria**

- Customer can update the quantity of an item in their cart

`As a Customer I would like to remove an item from my cart so that if i decide its not what I want i can easily remove that item and continue purchase with the rest of my cart items`

**Acceptance Criteria**

- Customer can delete and item from their cart

**All Users**

![Cart](/docs/testing_screenshots/cart.jpg)
![Cart Gif1](/docs/testing_screenshots/cart.gif)
![Cart Gif2](/docs/testing_screenshots/cart1.gif)
![Cart Gif3](/docs/testing_screenshots/cart2.gif)

[Back to top &uarr;](#contents)

### **Checkout**

Functional testing was carried out on the Checkout page, the Checkout page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

`As a Developer I can create a checkout page so that the customer can enter their billing/shipping/payment information to complete purchase.`

**Acceptance Criteria**

- User clicks checkout in cart view and checkout page is displayed

`As a Customer, I would like to save my billing/shipping information, so that I don't need to enter these details on every purchase`

**Acceptance Criteria**

- Customer can save their billing/shipping information on purchase

**User Not Registered**

![Checkout 1](/docs/testing_screenshots/checkout1.jpg)
![Checkout Gif 1](/docs/testing_screenshots/checkout1.gif)
![Checkout Gif 2](/docs/testing_screenshots/checkout2.gif)

**User Registered**

![Checkout 2](/docs/testing_screenshots/checkout2.jpg)
![Checkout Gif 3](/docs/testing_screenshots/checkout3.gif)

[Back to top &uarr;](#contents)

### **Order Complete**

Functional testing was carried out on the Order Complete page, the Order Complete page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

A custom order confirmation email has been created and is sent automatically to the Order email address, you can see more in the Feature images in [README.md](README.md)

`As a Customer I would like to receive a confirmation of my order so that I know the purchase has went through and I can see what I ordered`

**Acceptance Criteria**

- When customer completes their purchase they will receive a confirmation email of their order.

**All Users**

![Order Complete](/docs/testing_screenshots/order_complete.jpg)
![Order Complete Gif 1](/docs/testing_screenshots/order_complete.gif)
![Order Complete Gif 2](/docs/testing_screenshots/order_complete1.gif)

[Back to top &uarr;](#contents)

### **Profile**

`As a customer I would like the ability to create my own Profile page so that I can save my shipping address for future purchases and track my orders`

**Acceptance Criteria**

- When customer registers on site they will have access to their own Profile page where they can add/edit/delete their information

`As a Developer I can implement functionality to allow a customer to save information to a personal Profile so that they can save information i.e. shipping address/orders for future review`

**Acceptance Criteria**

- Customer can click Profile link and be brought to a page containing their information

**User Registered**

![Profile](/docs/testing_screenshots/profile.jpg)
![Profile Gif 1](/docs/testing_screenshots/profile.gif)
![Profile Gif 2](/docs/testing_screenshots/profile1.gif)
![Profile Gif 3](/docs/testing_screenshots/profile2.gif)

[Back to top &uarr;](#contents)

### **Blog/Blog Posts**

Functional testing was carried out on the Blog/Blog Post page, the pages are fully responsive see Feature images and Mobile gifs in [README.md](README.md)

I have 2 blogs fully written and styled so I won't be previewing an empty Blog page but this has been tested in the past and passed.

`As a Developer I can create the functionality for site admin to add Blog Posts so that customer may spend more time on the site which may lead to more purchases.`

**Acceptance Criteria**

- Site admin can add Blog Posts

`As a Developer I can build some Blog related templates so that the site admin can display blog posts on their site for a good customer experience`

**Acceptance Criteria**

- When customer clicks Blog link site Blog Posts are displayed

**Unregistered Users**

![Blog](/docs/testing_screenshots/blog.jpg)
![Blog Gif](/docs/testing_screenshots/blog.gif)
![Blog Post](/docs/testing_screenshots/blogpost.jpg)
![Blog Post Gif](/docs/testing_screenshots/blogpost.gif)

**Registered Users**

![Blog Post 1](/docs/testing_screenshots/blogpost1.jpg)
![Blog Post Gif 1](/docs/testing_screenshots/blogpost1.gif)

**Staff(super_users)**

![Blog 1](/docs/testing_screenshots/blog1.jpg)
![Blog Gif 1](/docs/testing_screenshots/blog1.gif)
![Add Blog](/docs/testing_screenshots/add_blog.jpg)
![Add Blog Gif](/docs/testing_screenshots/addblog.gif)
![Edit Blog](/docs/testing_screenshots/edit_blog.jpg)
![Edit Blog Gif](/docs/testing_screenshots/editblog.gif)

[Back to top &uarr;](#contents)

### **Contact Us**

Functional testing was carried out on the Contact Us page, the Contact Us page is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

A custom Contact message received email has been created and is sent automatically to the Contact email address, you can see more in the Feature images in [README.md](README.md)

`As a Developer I can add functionality to allow the customer to contact the site owner so that any issue they encounter can be logged and resolved`

**Acceptance Criteria**

- Customer can click contact link and submit a contact form

`As a Developer I can build a Contact template so that customer can submit their issues`

**Acceptance Criteria**

- Customer clicks Contact link and a Contact Us Form is displayed

**All Users**

![Contact](/docs/testing_screenshots/contact.jpg)
![Contact Gif](/docs/testing_screenshots/contact.gif)

[Back to top &uarr;](#contents)

### **Authentication**

`As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users`

**Acceptance Criteria**

- Users are able to Sign Up
- Registered Users are able to Login/Logout

`As a Developer I can add functionality to verify email and reset password so that the user has better security over their email being used and can reset password if they forget it`

**Acceptance Criteria**

- Users receive emails from the site email address for emails like Verification, Password Reset

Allauth is used to manage the authentication of the site, Users can Sign up, Login and Logout. Email verification and Password rest functionality were also added.

The Sign Up page can be accessed via the link in Navbar in the My Account dropdown or the Sign Up link on the Login page. All links have been tested and work as expected.

The Sign Up page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Sign Up](/docs/testing_screenshots/signup.jpg)
![Sign Up Gif](/docs/testing_screenshots/signup.gif)

The Login page can be accessed via the link in the Navbar in the My Account dropdown, the link has been tested and works as expected.

The Login page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Login](/docs/testing_screenshots/login.jpg)
![Confirm Gif](/docs/testing_screenshots/confirm.gif)
![Forgot Password](/docs/testing_screenshots/forgot.gif)
![Change Password](/docs/testing_screenshots/change.gif)

The Logout page can be accessed via the link in the Navbar, the link has been tested and works as expected.

For Logout the User can click the "Sign Out" button on the Logout page, they will then be redirected to the Homepage for unregistered Users.

The Logout page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Logout](/docs/testing_screenshots/logout.jpg)
![Logout Gif](/docs/testing_screenshots/logout.gif)

[Back to top &uarr;](#contents)

### **Javascript/jQuery Testing**

**base.js**

The base.js script handles the Back To Top button, this has been added in the base.html so that it can be utilized by all pages. This has been manually tested and works as expected. See the below example:

![BTT Gif](/docs/testing_screenshots/btt.gif)

**message.js**

The message.js handles the site toasts behavior, it is set up to close after 3 seconds or if the mouse enters the toast it will stay open until the mouse leaves the toast area. A hide-on scroll function has been added also so the user can continue viewing the site without having to wait or manually close the toast. This has been manually tested and works as expected. See the below example:

![Toast Gif](/docs/testing_screenshots/toast.gif)

**owl.js**

The owl.js handles the styling/behavior of the Product Carousels on the home page. This has been manually tested and works as expected. See the below example:

![Owl Gif](/docs/testing_screenshots/owl.gif)

Any other scripts used for the site were taken from Boutique Ado or handled by plugins/libraries.

[Back to top &uarr;](#contents)

## **Validators**

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined below:

![PEP8 Results](/docs/validation/linter.jpg)

[Back to top &uarr;](#contents)

### **JSHint**

[JSHint](https://jshint.com/) was used to validate the Javascript/jQuery code used in the project. Only one undefined variable is showing "Stripe" - this is a part of the Stripe js implementation so I have not changed this.

![JSHint Results](/docs/validation/jshint.jpg)

[Back to top &uarr;](#contents)

### **W3C CSS Validator**

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the site's CSS code.

All CSS files were validated and any errors were corrected.

![W3C CSS Validator](/docs/validation/css.jpg)

[Back to top &uarr;](#contents)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially, there were some errors due to missing closing tags, and elements nested within elements all of these issues were corrected and all pages passed validation. Some errors were related to the Summernote widgets and 1 error was related to the custom_clearable_file_input.html, see error details below. I have not altered anything for these errors as I cannot access the setup of the Summernote widget and the custom_clearable_file_input.html was taken from the Boutique Ado walkthrough and any errors that could be fixed were fixed.

Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw HTML code into the validator as this will be only the HTML-rendered code.

![W3C Markup Validator](/docs/validation/html.jpg)
![Summernote Errors](/docs/validation/html.jpg)
![Custom Widget Errors](/docs/validation/widget.jpg)

[Back to top &uarr;](#contents)

### **Lighthouse**

<details><summary>Desktop Results</summary>

Homepage

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-homepage.jpg)

Products Page

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-allproducts.jpg)

Products Detail Page

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-product-detail.jpg)

Add Product

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-addproduct.jpg)

Edit Product

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-editproduct.jpg)

Add Review

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-addreview.jpg)

Edit Review

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-editreview.jpg)

Cart

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-cart.jpg)

Checkout

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-checkout.jpg)

Order

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-order.jpg)

Blog

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-blog.jpg)

Blog Post

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-blog-post.jpg)

Add Blog

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-addblog.jpg)

Edit Blog Post

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-editblog.jpg)

Add Comment

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-addcomment.jpg)

Edit Comment

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-editcomment.jpg)

Profile

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-profile.jpg)

Sign Up

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-signup.jpg)

Login

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-login.jpg)

Logout

![Lighthouse Desktop Score](/docs/validation/lighthouse/desktop-logout.jpg)

</details>

<details><summary>Mobile Results</summary>

Homepage

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-homepage.jpg)

Products Page

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-allproducts.jpg)

Products Detail Page

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-product-detail.jpg)

Add Product

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-addproduct.jpg)

Edit Product

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-editproduct.jpg)

Add Review

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-addreview.jpg)

Edit Review

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-editreview.jpg)

Cart

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-cart.jpg)

Checkout

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-checkout.jpg)

Order

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-order.jpg)

Blog

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-blog.jpg)

Blog Post

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-blog-post.jpg)

Add Blog

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-addblog.jpg)

Edit Blog Post

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-editblog.jpg)

Add Comment

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-addcomment.jpg)

Edit Comment

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-editcomment.jpg)

Profile

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-profile.jpg)

Sign Up

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-signup.jpg)

Login

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-login.jpg)

Logout

![Lighthouse Mobile Score](/docs/validation/lighthouse/mobile-logout.jpg)

</details>

[Back to top &uarr;](#contents)

### **Lighthouse Errors**

The errors encountered in the various reports are outlined below:

- "Eliminate render-blocking resources" - this was pointing towards bootstrap.min.css throughout, I am unaware of how to fix it at this time

I tried to get Accessibility to 100% on all pages, in some places this could not be acheived due to the use of Summernote. The error related is pictured below.

![Summernote Error](/docs/validation/lighthouse/summernote-error.jpg)

I have tested the site on various devices and networks (3g, 4g & WIFI) and the above is not affecting the site, load times are good and no issues/delays reported by test users.

There was also one error related to the Stripe payment element, see below.

![Stripe Error](/docs/validation/lighthouse/stripe-error.jpg)

Any page/path disallowed in the robots.txt had its SEO score suffer with the robots.txt being specified as a cause.

[Back to top &uarr;](#contents)

### **Wave Accessibility Tests**

Every page of the site was passed through the [Wave Evaluation Tool](https://wave.webaim.org/) via the Chrome extension. All errors that did show were resolved.

![Wave](/docs/validation/wave.jpg)

[Back to top &uarr;](#contents)

## **Responsiveness**

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards. The site was tested on multiple browsers and devices as outlined below.

| **Browser Tested** | **Actual Result** | **Pass/Fail** |
| ------------------ | ----------------- | ------------- |
| Chrome             | As Expected       | Pass          |
| Firefox            | As Expected       | Pass          |
| Edge               | As Expected       | Pass          |
| Mac OS Safari      | As Expected       | Pass          |

| **Device Tested**    | **Actual Result** | **Pass/Fail** |
| -------------------- | ----------------- | ------------- |
| Mac Air M2           | As Expected       | Pass          |
| HP Elite Laptop      | As Expected       | Pass          |
| HP 23 Monitor        | As Expected       | Pass          |
| Samsung Note 10+     | As Expected       | Pass          |
| Samsung Note 20      | As Expected       | Pass          |
| Samsung S21+         | As Expected       | Pass          |
| Samsung Tab S7+      | As Expected       | Pass          |
| iPhone 13 Pro Max    | As Expected       | Pass          |
| iPhone 11            | As Expected       | Pass          |
| iPad Pro 12 inch     | As Expected       | Pass          |
| One Plus 8T          | As Expected       | Pass          |
| Xiaomi Redmi Note 11 | As Expected       | Pass          |

[Back to top &uarr;](#contents)

## **Bugs & Fixes**

| **Bug**                                                        | **Issue**                                                                                                                                                                                                                                                         | **Resolution**                                                                                                                                                                                                                                        |
| -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I found that lighthouse was showing a fault with my robots.txt | The issue was that it was being read as an HTML file, not a text file.                                                                                                                                                                                            | Upon researching this issue I found a tutorial that advised me to move the Robots.txt file into my main templates directory and add a URL in the main Urls.py to point to it and set the file as plain text.                                          |
| Profile shipping details not updating on Save                  | I noticed that when I testing the update form for my profile that when you change the username and try to update the address details afterward this would not update as the username had been changed and any address details were tied to the previous username | To resolve this I just removed the username field from displaying to the user, by doing this the user won't run into issues updated their Profile address details                                                                                      |
| Add to Wishlist too many redirects                             | I noticed while testing my Add to Wishlist view that when I clicked the heart icon while logged out I would be redirected to sign-in due to the login required decorator. After signing in I would receive a too many redirections error                          | To resolve this I removed the login required decorator and updated the code instead to alert the user that they are required to be logged in to add to the wishlist, this works now as intended.                                                          |
| Add like on Blog too many redirects                            | I noticed while testing Liking a Blog post that when I clicked the thumbs-up icon while logged out I would be redirected to sign-in due to the login required decorator. After signing in I would receive a too many redirections error                           | To resolve this I removed the login required decorator and updated the code instead to alert the user that they are required to be logged in to like a Blog post, this works now as intended.                                                         |

[Back to top &uarr;](#contents)

## **Unresolved Bugs/Issues**

| **Bug**                                              | **Issue**                                                                                                                                                                           |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blank spaces - Error 500 on form Checkout submission | I noticed while doing some negative testing that when you use white space on some of they fields required for the Stripe intent when submitting payment the error 500 would appear. |


I discussed this issue with my mentor and advised that the same issue occurs with the Boutique Ado project walkthrough so I would log it as a bug but the likly hood of a user entering blank information on a payment checkout would be virtually 0.

[Return to README.md](README.md)
