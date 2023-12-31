# Foodtracks Store Challenge API

This repository contains the implementation of the Foodtracks Store Challenge API, built with Django. The API is designed to manage companies and their branches with different roles, including owner/admin, regional manager, site manager, and employer.

## Getting Started

Follow these steps to set up and run the Foodtracks Store Challenge API on your local machine:

### Prerequisites

- **Git:** [Download and Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

- **Python:** [Download and Install Python](https://www.python.org/downloads/)
- **Virtual Environment (optional but recommended):** [Creating Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- **Docker:** [Download and Install Docker](https://www.docker.com/products/docker-desktop)


### Clone the Repository

```bash
git clone git@github.com:Lih3006/foodtracks-store-challenge.git


cd foodtracks-store-challenge

```
# Set Up Virtual Environment (Optional)

# Copy code
````bash
# Create a virtual environment
python -m venv venv

# Set Up Virtual Environment (Optional)

# On Windows
source venv/scripts/activate

# On macOS/Linux
source venv/bin/activate
````

# Install Dependencies

````bash
# Copy code

pip install -r requirements.txt
````
# Run Migrations


```bash

# Copy code

python manage.py makemigrations

python manage.py migrate


````
# Start the Development Server


````bash
# Copy code

TEST=TEST ./manage.py runserver 

````



# Run with Docker Compose
To run the project using Docker, make sure Docker is installed. Then, execute the following commands:


Copy the .env.example file and rename it with .env and inside it enter your credentials for accessing postgresql

````bash
# Copy code

docker compose up 
````

# API Documentation

Swagger Documentation: http://localhost:8000/api/docs/swagger-ui/


# Testing
No automated tests have been implemented yet. 

# Roles and Responsibilities

## Owner/Admin:

- Can create a company.
- Can create multiple branches under the company.
- Can edit branch data.
- Can delete branches.

## Regional Manager:

- Can be created only if there is at least one branch linked.
- Can edit branch data.
- Cannot create or delete branches.

## Site Manager:

- Can be created with only one branch linked.
- Can edit branch data.
- Cannot create or delete branches.

## Employer:

- Has access only to view company and branch data.