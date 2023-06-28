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

![Home](/docs/unit_testing/test_home.webp)

#### **Movie**

**Views**

![Movie Views](/docs/unit_testing/test_movie_views.webp)

**Models**

![Movie Models](/docs/unit_testing/test_movie_models.webp)

#### **Profiles**

**Views**

![Profiles Views](/docs/unit_testing/test_profiles_views.webp)

**Models**

![Profiles Models](/docs/unit_testing/test_profiles_models.webp)

**Forms**

![Profiles Forms](/docs/unit_testing/test_profiles_forms.webp)

#### **Review**

**Views**

![Review Views](/docs/unit_testing/test_review_views.webp)

**Models**

![Review Models](/docs/unit_testing/test_review_models.webp)

**Forms**

![Review Forms](/docs/unit_testing/test_review_forms.webp)

[Back to top &uarr;](#contents)

### **Site Coverage Report**

Through my testing, I was able to get a total of 95% coverage across the site. The remaining 5% will be covered through manual testing.

![Coverage 1](/docs/unit_testing/coverage1.webp)
![Coverage 2](/docs/unit_testing/coverage2.webp)
![Coverage 3](/docs/unit_testing/coverage3.webp)

[Back to top &uarr;](#contents)

## **Manual Testing/User Story Testing**

Some features of the site are restricted to registered users such as adding Product reviews, adding Products to wishlist, Commenting/Liking on blog posts, and editing a Profile. There are also features retricted to Staff, the functional tests take this into account.

### **Navbar**

`As a Developer I can build a base template so that it can be extended to any templates that may require it`

**Acceptance Criteria**

- When the template is extended to another template all html code is applied i.e. Navbar/Footer

`As a User I would like the ability to search for a product so that I can see if the site sells it`

**Acceptance Criteria**

- User has access to a Product Search input that will reference the database for the users requested Product

Functional testing was carried out on the Navbar and all links go to their relevant pages as expected. Navbar is fully responsive see Feature images and Mobile gifs in [README.md](README.md)

All users can enter a Search query in the Search input from the Search dropdown.

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
- User can easily identify what the site is about based off the landing page

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

Product reviews is a restricted feature available to registered users only.

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

A custom Order confirmation email has been created and is sent automatically to the Order email address, you can see more in the Feature imgs in [README.md](README.md)

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

I have 2 blogs fully written and styled so I wont be previewing an empty Blog page but this has been tested in the past and passed.

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

A custom Contact messaged received email has been created and is sent automatically to the Contact email address, you can see more in the Feature imgs in [README.md](README.md)

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

The base.js script handles the Back To Top button, this has been added in the base.html so that it can be utilised by all pages. This has been manually tested and works as expected. See below example:

![BTT Gif](/docs/testing_screenshots/btt.gif)

**message.js**

The message.js is handles the site toasts behaviour, it is setup to close after 3 seconds or if the mouse enters the toast it will stay open until the mouse leaves the toast area. A hide on scroll has been added also to also the user to continue viewing the site without having to wait or manually close the toast. This has been manually tested and works as expected. See below example:

![Toast Gif](/docs/testing_screenshots/toast.gif)

**owl.js**

The owl.js handles the styling/behaviour of the Product Carousels on the home page. This has been manually tested and works as expected. See below example:

![Owl Gif](/docs/testing_screenshots/owl.gif)

Any other scripts used for the site where taken from Boutique Ado or handled by plugins/libraries.

[Back to top &uarr;](#contents)

## **Validators**

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined in below:

![PEP8 Results](/docs/validation/pep_results.webp)

[Back to top &uarr;](#contents)

### **JSHint**

[JSHint](https://jshint.com/) was used to validate the Javascript/jQuery code used in the project. Only one undefined variable is showing "Stripe" - this is a part of the Stripe js implementation so I have not changed this.

![JSHint Results](/docs/validation/jshint.jpg)

[Back to top &uarr;](#contents)

### **W3C CSS Validator**

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the site's CSS code.

All css files were validated and any errors were corrected.

![W3C CSS Validator](/docs/validation/css.jpg)

[Back to top &uarr;](#contents)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially, there were some errors due to missing closing tags, elements nested within elements all of these issues were corrected and all pages passed validation. There were some errors that were related to the Summernote widgets and 1 error related to the custom_clearable_file_input.html, see error details below. I have not altered anything for these errors as I cannot access the setup of the Summernote widget and the custom_clearable_file_input.html was taken from the Boutique Ado walkthrough and any erros that could be fixed were fixed.

Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw HTML code into the validator as this will be only the HTML-rendered code.

![W3C Markup Validator](/docs/validation/html.jpg)
![Summernote Errors](/docs/validation/html.jpg)
![Custom Widget Errors](/docs/validation/widget.jpg)

[Back to top &uarr;](#contents)

### **Lighthouse**

<details><summary>Desktop Results</summary>

Home(User not signed in)

![Lighthouse Desktop Score](/docs/validation/lighthouse/nosignin_desktop.webp)

Home(User signed in)

![Lighthouse Desktop Score](/docs/validation/lighthouse/signedin_desktop.webp)

Trending Movies

![Lighthouse Desktop Score](/docs/validation/lighthouse/trending_desktop.webp)

Top Rated Movies

![Lighthouse Desktop Score](/docs/validation/lighthouse/toprated_desktop.webp)

Movie Search

![Lighthouse Desktop Score](/docs/validation/lighthouse/search_desktop.webp)

Movie Search Results

![Lighthouse Desktop Score](/docs/validation/lighthouse/searchresults_desktop.webp)

Movie Details

![Lighthouse Desktop Score](/docs/validation/lighthouse/moviedetails_desktop.webp)

All Reviews

![Lighthouse Desktop Score](/docs/validation/lighthouse/allreviews_desktop.webp)

Review

![Lighthouse Desktop Score](/docs/validation/lighthouse/review_desktop.webp)

Comment

![Lighthouse Desktop Score](/docs/validation/lighthouse/comment_desktop.webp)

Profile

![Lighthouse Desktop Score](/docs/validation/lighthouse/profile_desktop.webp)

Sign Up

![Lighthouse Desktop Score](/docs/validation/lighthouse/signup_desktop.webp)

Login

![Lighthouse Desktop Score](/docs/validation/lighthouse/login_desktop.webp)

Logout

![Lighthouse Desktop Score](/docs/validation/lighthouse/logout_desktop.webp)

</details>

<details><summary>Mobile Results</summary>

Home(User not signed in)

![Lighthouse Mobile Score](/docs/validation/lighthouse/nosignin_mobile.webp)

Home(User signed in)

![Lighthouse Mobile Score](/docs/validation/lighthouse/signedin_mobile.webp)

Trending Movies

![Lighthouse Mobile Score](/docs/validation/lighthouse/trending_mobile.webp)

Top Rated Movies

![Lighthouse Mobile Score](/docs/validation/lighthouse/toprated_mobile.webp)

Movie Search

![Lighthouse Mobile Score](/docs/validation/lighthouse/search_mobile.webp)

Movie Search Results

![Lighthouse Mobile Score](/docs/validation/lighthouse/searchresults_mobile.webp)

Movie Details

![Lighthouse Mobile Score](/docs/validation/lighthouse/moviedetails_mobile.webp)

All Reviews

![Lighthouse Mobile Score](/docs/validation/lighthouse/allreviews_mobile.webp)

Review

![Lighthouse Mobile Score](/docs/validation/lighthouse/review_mobile.webp)

Comment

![Lighthouse Mobile Score](/docs/validation/lighthouse/comment_mobile.webp)

Profile

![Lighthouse Mobile Score](/docs/validation/lighthouse/profile_mobile.webp)

Sign Up

![Lighthouse Mobile Score](/docs/validation/lighthouse/signup_mobile.webp)

Login

![Lighthouse Mobile Score](/docs/validation/lighthouse/login_mobile.webp)

Logout

![Lighthouse Mobile Score](/docs/validation/lighthouse/logout_mobile.webp)

</details>

[Back to top &uarr;](#contents)

### **Lighthouse Errors**

The errors encountered in the various reports are outlined below:

- "Eliminate render-blocking resources" - this was pointing towards bootstrap.min.css throughout, I am unaware of how to fix it at this time
- "Displays images with incorrect aspect ratio", "Properly size images", "Serve images in next-gen formats" - I have tried resizing how the images are displayed but due to the fact they are being retrieved from the API, there is not much I can do here.

I have tested the site on various devices and networks (3g, 4g & WIFI) and the above is not affecting the site, load times are good and no issues/delays reported by test users.

There is one console error due to the embedded Youtube video that cannot be fixed at this time, it refers to "Ensure CORS response header values are valid". The error only occurs when the user clicks play on the video. I have researched this previously and the issue appears to be between Google and Youtube so I am unable to fix this error. Please note this error does not seem to affect the performance of the site.

![Lighthouse Console Error](/docs/validation/lighthouse/trailer_console.webp)

[Back to top &uarr;](#contents)

### **Wave Accessibility Tests**

Every page of the site was passed through the [Wave Evaluation Tool](https://wave.webaim.org/) via the Chrome extension. Only 1 page returned errors which was the Reviews Page. It showed 91 contrast errors due to no fallback contrast being in place if the image does not populate, to resolve I added a background colour to the Review cards and all contrast errors were cleared.

![Wave](/docs/validation/wave.webp)

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

| **Bug**                                                     | **Issue**                                                                                                                                                                                           | **Resolution**                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Current Profile image URL not showing in Edit Profile form  | When a user wants to change their Profile picture the current profile link would not display in the crispy form                                                                                     | Upon researching this issue I found that there was an issue between the Bootstrap version I was running and Crispy Bootstrap 5. To resolve the issue I changed the Crispy Template pack to bootstrap 4 and removed Crispy Bootstrap 5. Users can now view the image URL in the Edit Profile form.                                   |
| Summernote not displaying toolbar items                     | Summernote was installed and settings were applied in settings.py, unfortunately, the buttons were not displaying or working correctly when used with Crispy forms.                                 | After much testing, I changed the editor to Richtextfield editor, and the fields/toolbars are displaying and working as expected.                                                                                                                                                                                                   |
| Richtextfield max length issue                              | Richtextfield was not reading the max length applied in the model field                                                                                                                             | To resolve I added the MaxLength Validator to the model field                                                                                                                                                                                                                                                                       |
| Richtextfield counts the background HTML tags as characters | I noticed while doing negative testing that I had set the max characters of the Review field to 2500 characters but the max I could enter was only 2493 - This was due to the background p tags ( ) | To resolve I raised the max length in the review model field to 2507 characters. Now users can enter 2500 characters although if styling is used this will cause more issues. This is a Richtextfield limitation at this time. Impact on the user would be very rare considering the max length allowed should be more than enough. |
| Search Result cards of different sizes                      | I noticed while building the Search Results page that the cards being displayed were different sizes when API results did not contain a background image.                                           | To resolve I created a fallback background image and scaled it to match the image size received from the TMDB API.                                                                                                                                                                                                                  |
| Heroku builds failing                                       | I was receiving emails from time to time saying the app build failed from Heroku - after researching it seemed to be related to a version of Cloudinary                                             | To resolve this I just manually deployed the app when required.                                                                                                                                                                                                                                                                     |

[Back to top &uarr;](#contents)

## **Unresolved Bugs/Issues**

The console error related to the Youtube embedded video is the main unresolved bug for the site, I have mentioned the error to CI staff on calls and the consensus was it was out of my control and to make sure it was documented in README.md

The other bug that I have encountered is that a User can enter just white spaces in the Richtextfield inputs and submit. This issue only occurs with Richtextfields, I have tried adding clean functions but nothing works. To resolve this issue you could remove all the Richtextfields and Richtext widgets and place a standard Textfield. After speaking with my Mentor and the Users that tested the site the consensus was to keep the editor that they would miss the functionality and that 99.9% of people reviewing a Movie would not enter blank spaces. I have decided to leave the editors in place based on the feedback received.

[Return to README.md](README.md)
