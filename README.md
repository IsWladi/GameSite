# GameSite

Welcome to GameSite, a video game store where you can find games from different categories. We are proud to present our project to you.

## Disclaimer

This project is being developed as part of an academic evaluation for Duoc UC. Any use of this project for academic evaluations without our consent is not authorized.

## Repository

This repository is used to track our work during the bimester.

### Course

- PROGRAMACION WEB_002A

### Team Members

- DANIEL B.
- WLADIMIR U.

## Get Access to Our API

1. Create an account on our web application.
2. Click on 'get API key'.
3. Copy the token.
4. Access with Postman.
5. Take this image as a reference:

### In headers; key: Authorization, value: token pasteYourTokenHere

![image](https://user-images.githubusercontent.com/83993271/235538273-ae43ebae-893f-49bd-8f4f-2448c6ac49c2.png)


## Roles

| Role | Description |
|------|-------------|
| Anonymous | Only has access to view the content of the page. |
| User | Can create an account, log in, purchase games, and view their purchase history. |
| Supervisor | Access to a customized admin panel (with restrictions regarding the superuser panel). |
| Admin | Django superuser, access to everything except buying actions. |

## How to use each role

- **Anonymous:** As an anonymous user, you can browse the website and view game catalogs without creating an account or logging in.
- **User:** To use the user role, you need to create an account and log in. Once logged in, you can purchase games and view your purchase history.
- **Supervisor:** To use the supervisor role, an admin (superuser) must create a user and assign them the role that has the description `have access to the custom admin panel`.
- **Admin:** To use the admin role, you need to have Django superuser privileges. As an admin, you have access to everything except buying actions.

**Note:** All types of users can log in through the website's login page, but only the admin can log in through `http://127.0.0.1:8000/admin/`.

## Getting Started

To get started with this project, you'll need to have a local development environment set up.

### Prerequisites

- Python 3.11.3(recommended)

### Installation in local machine with oracle 21c xe

1. Create a database with the user "USR_GAMESITE" and password "duoc123456".
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Run `python manage.py migrate` to apply database migrations.
5. Create a superuser by running `python manage.py createsuperuser`.
6. Run the Django development server by running `python manage.py runserver`.
7. Open your web browser and navigate to `http://localhost:8000`.

### Using Docker

0. You must have Docker and docker compose
1. docker compose build
2. docker compose up
3. execute Django commands(without stop the containers):
    * docker compose exec web python manage.py migrate
    * docker compose exec web python manage.py createsuperuser

**Note:** Table insertions are done automatically when performing database migrations.

## License

This project is licensed under the MIT License.
