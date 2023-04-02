# Harmonize - Django REST Framework API

# Overview

This repository serves as Harmonize App Backend REST API. The purpose is to provide data to be used in Front-End design with [React. js](https://reactjs.org/). For the main projects documentation refer to [Harmonize](https://github.com/JureSeselj/harmonize-drf-api) project.
The API endpoint can be found [here]()

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories - UX

The back-end section of the project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content.

## Database

The following models were created to represent the database model structure of the application:
<img src="documentation/readme/harmonize-database-diagram.png">

#### User Model

- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field
- ForeignKey relation with the Follower model owner and followed fields
- ForeignKey relation with the Post model owner field
- ForeignKey relation with the Comment model owner field
- ForeignKey relation with the Like model owner field

#### Profile Model

- The Profile model contains the following fields: owner, name, description, created_on, updated_on and image
- One-to-one relation between the owner field and the User model id field

#### Post Model

- The Post model contains the following fields: owner, created_on, updated_on, title, description, category and image
- ForeignKey relation with the Comment model post field
- ForeignKey relation with the Like model post field

#### Follower Model

- The Follower model contains the following fields: owner, followed and created_on
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the followed field and the User model post field

#### Comment Model

- The Comment model contains the following fields: owner, post, created_on, updated_on and content
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the User model post field

#### Like Model

- The Like model contains the following fields: owner, post and created_on
- ForeignKey relation between to the User model id field
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the Post model post field

[Back to Top](#table-of-contents)

## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Gitpod)](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site
- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing
- [Cloudinary](https://cloudinary.com/) to store static files
- [Coverage](https://coverage.readthedocs.io/en/6.4.4/) used to produce automated testing report
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) was used as a ElephantSQL database adapter for Python
- [Heroku](https://heroku.com) was used to deploy the project into live environment
- [ElephantSQL](https://www.elephantsql.com/) – deployed project on Heroku uses a ElephantSQL database

## Validation

### PEP8 Validation

All code was formatted using [autopep8](https://pypi.org/project/autopep8/).
Additionally, manual validation was done with [PEP8 online](http://pep8online.com).

The only code which was left with long-line prompts is `settings.py` for code functionality.

<img src="documentation/testing/pep8-validation.png">

## Testing

The following tests were carried out on the app:
1. Manual testing of user stories
2. Automated testing

### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected

In addition, posts, comments, likes and following can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

- USER
<details><summary>Create user</summary>
    <img src="">
    </details>
    <details><summary>Change user permissions</summary>
    <img src="">
    </details>
    
- PROFILE
- POST
- COMMENT
- LIKE
- FOLLOWER

### Automated testing

## Credits

[Back to Top](#table-of-contents)

---

**<div align='center'>Copyright @ Jure Seselj 2023</div>**
<div align='center'>
    <a href="https://www.linkedin.com/in/jure-seselj-062654192/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>
</div>