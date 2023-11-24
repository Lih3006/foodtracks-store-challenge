# Foodtracks Store Challenge API

This repository contains the implementation of the Foodtracks Store Challenge API, built with Django. The API is designed to manage companies and their branches with different roles, including owner/admin, regional manager, site manager, and employer.

## Getting Started

Follow these steps to set up and run the Foodtracks Store Challenge API on your local machine:

### Prerequisites

- **Git:** [Download and Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- **Python:** [Download and Install Python](https://www.python.org/downloads/)
- **Virtual Environment (optional but recommended):** [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

### Clone the Repository

```bash
git clone git@github.com:Lih3006/foodtracks-store-challenge.git


cd foodtracks-store-challenge

```
# Set Up Virtual Environment (Optional)

Copy code
````bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
````

# Install Dependencies

````bash
Copy code

pip install -r requirements.txt
````
# Run Migrations`

```bash

Copy code

python manage.py migrate


````
# Start the Development Server


````bash
Copy code

python manage.py runserver
````


Visit http://127.0.0.1:8000/ in your browser to confirm that the server is running.


# API Documentation

Swagger Documentation: http://127.0.0.1:8000/swagger/


# Testing
No automated tests have been implemented yet. Feel free to contribute by adding test coverage.

# Roles and Responsibilities

## Owner/Admin:

Can create a company.
Can create multiple branches under the company.

## Regional Manager:

Can be created only if there is at least one branch linked.
Can edit company and branch data.

## Site Manager:

Can be created with only one branch linked.
Can edit company and branch data.

## Employer:

Has access only to view company and branch data.
Please note that these roles have specific responsibilities and constraints, as mentioned above.