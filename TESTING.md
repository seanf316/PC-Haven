# **Cinema | Go Testing**

## **Testing Overview**

A wide range of testing was carried out during development by myself and also by my peers.

## **Contents**

1. [Testing Overview](#testing-overview)
2. [Automated Testing](#automated-testing)
   - [Unit Testing](#unit-testing)
   - [Site Coverage Report](#site-coverage-report)
3. [Manual Testing](#manual-testing)
   - [User Story Testing](#user-story-testing)
   - [Negative Testing](#negative-testing)
   - [Javascript Testing](#javascript-testing)
4. [Validators](#validators)
   - [CI Python Linter](#ci-python-linter)
   - [JSHint](#jshint)
   - [W3C CSS Validator](#w3c-css-validator)
   - [W3C Markup Validator](#w3c-markup-validator)
   - [Lighthouse](#lighthouse)
   - [Lighthouse Errors](#lighthouse-errors)
   - [Wave Accessibility Tests](#wave-accessibility-tests)
5. [Responsiveness](#responsiveness)
6. [Bugs & Fixes](#bugs--fixes)
7. [Unresolved Bugs/Issues](#unresolved-bugsissues)

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

#### **Newsletter**

`As a Developer I can implement a newsletter on my site so that customers can subscribe for future updates and deals which should bring them back to the site for future purchases.`

**Acceptance Criteria**

- User can subscribe to the site Newsletter

![Newsletter1](/docs/testing_screenshots/newsletter2.jpg)
![Newsletter1](/docs/testing_screenshots/newsletter.jpg)
![Newsletter2](/docs/testing_screenshots/newsletter1.jpg)

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





































#### **Authentication**

`As a User I want to Sign Up/Login and Logout so that I can see what features are available to registered users like reviewing/commenting`

**Acceptance Criteria**

- Users are able to Sign Up
- Registered Users are able to Login/Logout

`As a Developer I can add functionality to verify email and reset password so that the user has better security over their email being used and can reset password if they forget it`

**Acceptance Criteria**

- Users are able verify their email when signing up
- Registered Users are able to reset password if they forgot it

Allauth is used to manage the authentication of the site, Users can Sign up, Login and Logout. Email verification and Password rest functionality were also added.

The Sign Up page can be accessed via the link in Navbar, the Sign Up link on the Login page, or lastly via the Sign Up button on the Homepage for unregistered Users. All links have been tested and work as expected.

For Sign Up the user will fill out the required fields on the Sign Up form page and once valid they click the "Sign Up" button. They will be redirected to the Verify Email Address page where the User will be advised that an email is sent to them. Once the User receives the email they can click the confirmation link. This will bring the User to the Confirm E-mail Address page on the site, the User will click the "Confirm" button and be redirected to the Login page.

The Sign Up page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Sign Up](/docs/testing_screenshots/signup.webp)
![Email Verify](/docs/testing_screenshots/emailverify.webp)
![Email](/docs/testing_screenshots/email.webp)
![Confirm Email](/docs/testing_screenshots/confirmemail.webp)
![Sign Up Testing](/docs/testing_screenshots/signuptest.webp)

The Login page can be accessed via the link in the Navbar, the link has been tested and works as expected.

For Login, the User will enter either their Username or Email Address and their password in the required fields, once the fields are valid they can click the "Login" button to gain access to site features restricted to registered Users. If User has forgotten their password they can click the "Forgot Password" button. They will then be redirected to the Password Reset page where they will need to enter the email address they registered with before clicking the "Reset My Password" button. They will now be redirected to the Password Reset email sent page where a message will display advising an email has been sent to the User. When the email is received the User can click on the link to reset the password which will then direct them to the Change Password page on the site. Once the User enters a new password in the fields required they will be redirected to the Change Password confirmed page, here they will be able to click the "Home" button to be redirected to the site Homepage for unregistered Users. They can proceed to log in again with new details.

The Login page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Login](/docs/testing_screenshots/loginpage.webp)
![Password Reset](/docs/testing_screenshots/passwordreset.webp)
![Password Email Sent](/docs/testing_screenshots/passwordemailsent.webp)
![Password Email](/docs/testing_screenshots/passwordemail.webp)
![Change Password](/docs/testing_screenshots/changepassword.webp)
![Password Change Confirmed](/docs/testing_screenshots/passwordconfirmed.webp)
![Login Test](/docs/testing_screenshots/logintest.webp)

The Logout page can be accessed via the link in the Navbar, the link has been tested and works as expected.

For Logout the User can click the "Sign Out" button on the Logout page, they will then be redirected to the Homepage for unregistered Users.

The Logout page is fully responsive see Feature images and Mobile screenshots in [README.md](README.md)

![Logout](/docs/testing_screenshots/logout.webp)
![Logout Test](/docs/testing_screenshots/logouttest.webp)

[Back to top &uarr;](#contents)

#### **Error Pages**

`As a Developer I can implement a 403 error page to redirect unauthorised users so that I can secure my views`

**Acceptance Criteria**

- 403 page created and Error message explained to User

A custom 403 error page & 403_csrf error page were created to handle 403 status errors. Pages were tested by changing URLs to access other Users' information and delete their Profiles, 403 status page displayed as expected. I also removed the csrf token from a form to test the 403_csrf page and 403_csrf status page displayed as expected.

`As a Developer I can implement a 404 error page so that I can alert users when they have accessed a page that doesn't exist`

**Acceptance Criteria**

- 404 page created and Error message explained to User

A custom 404 error page was created to handle 404 status errors. To test I tried to access a page that does not exist, and this worked, 404 status page displayed as expected.

`As a Developer I can implement a 500 error page so that I can alert users when an internal server error occurs`

**Acceptance Criteria**

- 500 page created and Error message explained to User

A custom 500 error page was created to handle 500 status errors. To test I would repeatedly and quickly hit the delete icon for a comment by doing this too fast and not allowing the time for the comment to be deleted the error 500 page was rendered.

All error pages are fully responsive, I do not have any current screenshots of the errors on Mobile/Tablet but you can view the Desktop screenshots in the Features section of the [README.md](README.md)

[Back to top &uarr;](#contents)

### **Negative Testing**

Negative testing was done on the Edit/Delete functionality for Reviews, Comments & Profile. Sign Up username field min length was tested also.

![Testing 7](/docs/testing/test7.webp)

[Back to top &uarr;](#contents)

### **Javascript Testing**

**base.html Javascript**

The JS script in the base.html handles the alert messages for the site. There is a timeout of 2 seconds set for the alert messages to close. This has been manually tested and works as expected. See below example:

![Alert Gif](/docs/gifs/alert.gif)

**Review.js**

The review.js is setup with a mouse leave event on the review cards, when user has moved the mouse outside the review card the text will smoothly scroll back to the top. There is a timeout of 3 seconds applied for this to happen. This has been manually tested and works as expected. See below example:

![Review Gif](/docs/gifs/review.gif)

**Modal.js**

The modal.js was taken from Bootstrap but has been altered slightly to to remove the iframe scource for the trailer once the modal is hidden as well as managing the closing/hiding of the modal. This was done to avoid the trailer continuing to play in the background once modal was closed. This has been manually tested and works as expected. See below example, please note I could not show the sound playing in the gif but you will be able to see the sound icon in the tab:

![Trailer Gif](/docs/gifs/trailer.gif)

[Back to top &uarr;](#contents)

## **Validators**

### **CI Python Linter**

The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code used throughout the project. The results are outlined in below:

![PEP8 Results](/docs/validation/pep_results.webp)

[Back to top &uarr;](#contents)

### **JSHint**

[JSHint](https://jshint.com/) was used to validate the Javascript code used in the project. Only one undefined variable is showing "bootstrap" - this was taken from the walkthrough and altered to fix a console error. No other issues to report.

![JSHint Results](/docs/validation/jshint.webp)

[Back to top &uarr;](#contents)

### **W3C CSS Validator**

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the site's CSS code.

![W3C CSS Validator](/docs/validation/css_results.webp)

[Back to top &uarr;](#contents)

### **W3C Markup Validator**

All pages were run through the [W3C Markup Validator](https://validator.w3.org/nu/). Initially, there were some errors due to missing closing tags, image height values, and Richtextfield inputs. All of these issues were corrected and all pages passed validation.

Due to the Django templating language code used in the HTML files, these could not be copied and pasted into the validator and due to the secured views, pages with login required or a secured view cannot be validated by direct URI. To test the validation on the files, open the page to validate, right click and view page source. Paste the raw HTML code into the validator as this will be only the HTML-rendered code.

![W3C Markup Validator](/docs/validation/html_check.webp)

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
