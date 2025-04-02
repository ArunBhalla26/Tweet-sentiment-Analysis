# Project Setup

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (preferably 3.x)
- `pip` (Python package manager)

If you don’t have Python installed, download and install it from the official website: [Python Downloads](https://www.python.org/downloads/)

## Step 1: Set Execution Policy (Windows Users Only)

Before starting, you need to set the execution policy to allow PowerShell scripts to run.

1. Open PowerShell or VsCode Terminal.
2. Run the following command to bypass the execution policy:

```powershell / Terminal
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```

## Step 2: Install Virtualenv

Next, install the virtualenv package using pip to create isolated Python environments for the project.

Open a terminal or command prompt.

Run the following command to install virtualenv:

```Terminal
pip install virtualenv
```

## Step 3: Create a Virtual Environment

Now, create a virtual environment where your project dependencies will be installed.

Navigate to your project directory where you want to create the virtual environment.

Run the following command to create a virtual environment:

```Terminal
virtualenv env
```

## Step 4: Activate the Virtual Environment

To activate the virtual environment, run the following command:

```Terminal
.\env\Scripts\activate
```

## Step 5: Install Project Dependencies

Make sure all the necessary project dependencies are listed in the package.txt file. To install them, run:

```Terminal
pip install -r package.txt
```

## Step 6: Apply Database Migrations

To set up your database schema, run the following Django management commands:

Generate migration files for any changes in your models:

```Terminal
python ./manage.py makemigrations
```

Apply the migrations to the database:

```Terminal
python ./manage.py migrate
```

## Step7: Start the Development Server

Now that your environment is set up, you can start the Django development server with the following command:

```Terminal
python ./manage.py runserver
```
