## PicturePerfect



## Description

The **Picfolio-API** is the backbone of an application for an image sharing app.



## Development set up


-   Check that python 3.7.x or above is installed:

    ```
    python --version
    >> Python 3.x.x
    ```

-   Set up the virtual environment and the postgresql database:

    ```
    Follow the guide in this (documentation)[https://docs.google.com/document/d/1G0UQUusBdoAvydu7w_EaaXjvOLC3UidFN3z7dddCG3o/edit?usp=sharing]
    ```


-  Database
    * Swith to postgres account (in terminal)
        ```
        psql
        
        if it fails then use this:
        
        sudo su - postgres
        ```
    * Run PostgreSQL command line client.
 \
    * Create a database instance.
        ```
        CREATE DATABASE pictureperfect;

        ```  


- Clone the pictureperfect repo and cd into it
    ```
    git clone https://github.com/EKibet/PicturePerfect
    ```
- Create  virtual environment
    ```
    virtualenv venv

    ```
- Turn off a virtual environment  
    ```
    exit
    ```

- Spawn a shell in a virtual environment
    ```
    source venv/bin/activate
    ```
- Install dependencies
    ```
   pip install -r requirements 
    ```
- Create Application environment variables and save them in .env file 
    ```
    DJANGO_READ_DOT_ENV_FILE=True
    DJANGO_DEBUG=True
    DATABASE_URL='postgresql://localhost/pictureperfect?user=<yourusername>&password=<yourpassword>'
    SECRET_KEY='super_secret'
    ```

- Add the variables in the .env file to path
    ```
    source .env
    ```
- Running migrations

    - Initial migration commands
        ```
        make migrations
        
        make migrate
        ```



- Run application.
    ```
    make serve
    ```



### Merge Request Process

-   A contributor shall identify a task to be done from the board. 
-   If there is a bug , feature or chore that has not been included among the tasks, the contributor can add it only after consulting the Scrum Master and the task being accepted.
-   The Contributor shall then create a branch off the `development` branch where they are expected to undertake the task they have chosen.
-   After undertaking the task, a fully detailed pull request shall be submitted to the owners of this repository for review.
-   If there any changes requested ,it is expected that these changes shall be effected and the pull request resubmitted for review.Once all the changes are accepted, the pull request shall be closed and the changes merged into `development` by the owners of this repository.
-   There should be only one commit per Merge Request, to achieve this use `git commit --amend`  


### Code Quality Conventions

Please refer to the best practices outlined in BestPractices.md



## Built with
- Python version  3
- Django (DRF)
- Postgres
- Swagger
 ```


