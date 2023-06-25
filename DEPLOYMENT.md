# **Deployment**

## **Contents**

- [**Github/Gitpod**](#githubgitpod)
  - [**Create repository**](#create-repository)
  - [**Setting up the Workspace**](#setting-up-the-workspace)
- [**ElephantSQL Database**](#elephantsql-database)
- [**AWS Setup**](#aws-setup)
  - [**S3 Bucket**](#s3-bucket)
  - [**IAM**](#iam)
  - [**Final AWS Setup**](#final-aws-setup)
  - [**Connecting to Django**](#connecting-to-django)
- [**Settings.py Setup**](#settingspy-setup)
- [**Heroku Deployment**](#heroku-deployment)
- [**Version Control**](#version-control)
- [**Clone the Github Repository**](#clone-the-github-repository)
- [**Forking the Github Repository**](#forking-the-github-repository)


Below are the steps I took to deploy the site to Heroku.

### **GitHub/Gitpod**

#### **Create Repository**

This project was developed by forking a specialized [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.

1. Click the template link above
1. Click use this template and create a new respository
1. Name the repository
1. Launch using the Gitpod web extension
1. Pin project in Gitpod workspaces

[Back to top &uarr;](#contents)

#### **Setting up the Workspace**

1. Install Django with version 3.2:
   - `pip install django==3.2`
1. Install gunicorn:
   - `pip install gunicorn`
1. Install supporting libraries:
   - `pip install dj_database_url`
   - `pip install psycopg2-binary`
1. Create requirements.txt:
   - `pip freeze --local > requirements.txt`
1. Create a project in the main directory:
   - `django-admin startproject <PROJECT_NAME>`
1. Create an app within the project:
   - `python manage.py startapp APP_NAME`
1. Add a new app to the list of installed apps in settings.py
1. Make migrations:
   - `python manage.py makemigrations`
1. Migrate changes:
   - `python manage.py migrate`
1. Test server works locally:
   - `python manage.py runserver` (You should see the default Django success page)
1. Create env.py file in main directory to store secure variables

   - Add the following variables to env.py

   ```shell
   os.environ["SECRET_KEY"] = "(whatever you want)"
   os.environ["DEVELOPMENT"] = "(whatever you want)"
   ```

[Back to top &uarr;](#contents)

### **ElephantSQL Database**

This project uses ElephantSQL for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

1. Click Create New Instance to start a new database.
1. Provide a name (this is commonly the name of the project: pc-haven).
1. Select the Tiny Turtle (Free) plan.
1. You can leave the Tags blank.
1. Select the Region and Data Center closest to you.
1. Once created, click on the new database name, where you can view the database URL and Password.
1. Add database url to env.py file in workspace

   ```shell
   os.environ["DATABASE_URL"] = (
   "postgres://yourdatabaseurl"
   )
   ```

[Back to top &uarr;](#contents)

### **AWS Setup**

This project uses [AWS](https://aws.amazon.com) to store media and static files online.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

  ```shell
  [
  	{
  		"AllowedHeaders": [
  			"Authorization"
  		],
  		"AllowedMethods": [
  			"GET"
  		],
  		"AllowedOrigins": [
  			"*"
  		],
  		"ExposeHeaders": []
  	}
  ]
  ```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
- Policy Type: **S3 Bucket Policy**
- Effect: **Allow**
- Principal: `*`
- Actions: **GetObject**
- Amazon Resource Name (ARN): **paste-your-ARN-here**
- Click **Add Statement**
- Click **Generate Policy**
- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

  ```shell
  {
  	"Id": "Policy1234567890",
  	"Version": "2012-10-17",
  	"Statement": [
  		{
  			"Sid": "Stmt1234567890",
  			"Action": [
  				"s3:GetObject"
  			],
  			"Effect": "Allow",
  			"Resource": "arn:aws:s3:::your-bucket-name/*"
  			"Principal": "*",
  		}
  	]
  }
  ```

- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
- Click **Save**.

- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

[Back to top &uarr;](#contents)

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
- Suggested Name: `group-pc-haven` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

  ```shell
  {
  	"Version": "2012-10-17",
  	"Statement": [
  		{
  			"Effect": "Allow",
  			"Action": "s3:*",
  			"Resource": [
  				"arn:aws:s3:::your-bucket-name",
  				"arn:aws:s3:::your-bucket-name/*"
  			]
  		}
  	]
  }
  ```

- Click **Review Policy**.
- Suggested Name: `policy-pc-haven` (policy + the project name)
- Provide a description:
  - "Access to S3 Bucket for pc-haven static files."
- Click **Create Policy**.

- From **User Groups**, click your "group-pc-haven".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-pc-haven") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
  - Suggested Name: `user-pc-haven` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-pc-haven`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
  - **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
  - This contains the user's **Access key ID** and **Secret access key**.
  - `AWS_ACCESS_KEY_ID` = **Access key ID**
  - `AWS_SECRET_ACCESS_KEY` = **Secret access key**

[Back to top &uarr;](#contents)

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

[Back to top &uarr;](#contents)

#### Connecting to Django

- Install required packages to used AWS S3 Bucket in Django:

  - `pip install boto3`
  - `pip install django-storages`

- Add 'storages' to the bottom of the installed apps section of settings.py file:

  ```shell
   INSTALLED_APPS = [
   …,
       'storages'
   …,
  ]
  ```

- Update AWS variables in env.py

  ```shell
  os.environ["AWS_ACCESS_KEY_ID"] = "your_aws_accesskeyid"
  os.environ[
  "AWS_SECRET_ACCESS_KEY"
  ] = "your_aws_secretkey"
  ```

[Back to top &uarr;](#contents)

### **Settings.py Setup**

- At the top of your settings.py add the following:

  ```shell
  import os
  from pathlib import Path
  import dj_database_url

  if os.path.isfile("env.py"):
  import env
  ```

- Add the below for Debug/Secret Key

  ```shell
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = os.environ.get("SECRET_KEY")

  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = "DEVELOPMENT" in os.environ
  ```

- Add a conditional in setting.py DATABASES section by replacing it with the following snippet to link up the Heroku Postgres server when in production and SQLite3 when developing locally

  ```shell
  if "DATABASE_URL" in os.environ:
  	DATABASES = {
  		"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
  	}
  else:
  	DATABASES = {
  		"default": {
  			"ENGINE": "django.db.backends.sqlite3",
  			"NAME": os.path.join(BASE_DIR, "db.sqlite3"),
  		}
  	}
  ```

- Tell Django to where to store media and static files by placing this snippet under the comments indicated below

  ```shell
  # Static files (CSS, JavaScript, Images)
  # https://docs.djangoproject.com/en/3.2/howto/static-files/

  STATIC_URL = "/static/"
  STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

  MEDIA_URL = "/media/"
  MEDIA_ROOT = os.path.join(BASE_DIR, "media")
  ```

- Import setting and static functions into the project urls.py file:

  ```shell
     from django.conf import settings
     from django.conf.urls.static import static
  ```

- Add the following snippet to the end of the urlpatterns list:

  ```shell
     urlpatterns =[
          path('admin/', admin.site.urls),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

- Within TEMPLATES array, add `'DIRS':[TEMPLATES_DIR]` like the below example:

  ```shell
     TEMPLATES = [
         {
             …,
             "DIRS": [
           		os.path.join(BASE_DIR, "templates"),
  			]
             …,

          },
     ]
  ```

- Link S3 Bucket to Django Project by adding the following to the settings.py file

  ```shell
     if "USE_AWS" in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "pc-haven"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # Static and media files
    STATICFILES_STORAGE = "custom_storages.StaticStorage"
    STATICFILES_LOCATION = "static"
    DEFAULT_FILE_STORAGE = "custom_storages.MediaStorage"
    MEDIAFILES_LOCATION = "media"

    # Override static and media URLs in production
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/"
  ```

- Create a file call "Custom_storages.py" in the main directory of the project and add the following code:

  ```python
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
  	location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
  	location = settings.MEDIAFILES_LOCATION
  ```

- Add allowed hosts to settings.py:

- `ALLOWED_HOSTS = ["project_name.herokuapp.com", "localhost", "gitpod_workspace_name(this is a new requirement)"]`

- Create Procfile in main directory and insert the following:

- ` web: gunicorn project_name.wsgi:application`

- Make an initial commit and push the code to the GitHub Repository.
- `git add .`
- `git commit -m "Initial deployment"`
- `git push`

[Back to top &uarr;](#contents)

### **Heroku Deployment**

The below steps were followed to deploy this project to Heroku:

1. Go to [Heroku](https://dashboard.heroku.com/apps) and click "New" to create a new app.
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars, enter the below

    | Key                     | Value                                                                  |
    | ----------------------- | ---------------------------------------------------------------------- |
    | `DATABASE_URL`          | insert your own ElephantSQL database URL here                          |
    | `SECRET_KEY`            | insert your Django secret key                                          |
    | `DISABLE_COLLECTSTATIC` | 1 (_this is temporary and can be removed when static files available_) |
    | `PORT`                  | 8000                                                                   |
    | `AWS_ACCESS_KEY_ID`     | insert your own AWS Access Key ID key here                             |
    | `AWS_SECRET_ACCESS_KEY` | insert your own AWS Secret Access key here                             |
    | `USE_AWS`               | True                                                                   |

4. Leave "Settings" and go to "Deploy". Scroll down and set Deployment Method to GitHub.
   Once GitHub is chosen, find your repository and connect it to Heroku.
5. Scroll down to Manual Deploy, make sure the "main" branch is selected, and click "Deploy Branch".
6. The deployed app can be found [here](https://pc-haven.herokuapp.com/).

[Back to top &uarr;](#contents)

### **Version Control**

For version control the following steps were made:

1. Changes made to files in Gitpod
1. Files made ready for commit with command - git add "filename", or git add . to add all files
1. For the commits the following command was run along with commit description - git commit -m "This is my commit etc"
1. To move the changes to Github the following command was run - git push
1. Alternatively files can be made ready for commit using the Source Control staging area in Gitpod
1. Files were staged and a message describing the commit was made before committing and pushing it to GitHub

[Back to top &uarr;](#contents)

### **Clone the Github Repository**

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally, this can be done by:

1. Navigating to [PC-HAVEN repo](https://github.com/seanf316/PC-Haven)
1. Clicking on the arrow on the green code button at the top of the list of files
1. Select Local then HTTPS copy the URL it provides to the clipboard
1. Navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
1. Type 'git clone' and paste the HTTPS link you copied from GitHub
1. Press enter and git will clone the repository to your local machine

[Back to top &uarr;](#contents)

### **Forking the GitHub Repository**

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the repository [PC-HAVEN repo](https://github.com/seanf316/PC-Haven)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

[Back to top &uarr;](#contents)

[Back to Readme](README.md)
