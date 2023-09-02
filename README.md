# PROJECT TITLE: Sala Bianca
## Video Demo:  https://youtu.be/WCea1TtHlbo
## Github Repo: https://github.com/ApostolosVarvatis/SalaBianca
## Description
My Capstone project for CS50W is a responsive webpage for a neighborhood cocktail bar, developed locally in VScode and uploaded online using Git and GitHub.

More thoroughly my web-app tech stack consists of:
- **Django** for the backend.
- **MySQL** as a relational database management system.
- **JavaScript** for interactive behavior.
- **TailwindCSS** and **CSS** for the frontend.
- **Github Actions** and **Selenium** for testing.
- **Docker** for containerization.


## Contents

This Django project contains multiple files and folders:

- The .github\workflows folder contains the GitHub Actions YAML file that runs the Django and Selenium tests on every push.

- The requirements.txt file that lists all the needed libraries to install to successfully run the Django app.

- Inside the sala_bianca folder exists the basic structure of every Django project. In addition to that the Dockerfile and the docker-compose.yml file contain the configuration of running the docker container if needed. Also, a db.sqlite3 database file exists for testing purposes.

- Inside of main there are a number of files and folders. The basic structure of a Django app is also followed here with urls.py containing routes, views.py containing the logic and functionality of the app, tests.py containing both Django tests as well as selenium tests, admin.py which registers the models in the admin panel for easy CRUD operations, and models.py containing all required database models. The templates folder contains all of the HTML files of the website, the static folder stores the styles.css and script.js files as well as another folder called images responsible for storing every image in the app.

- The sala_bianca folder then contains the settings.py file that stores all of the important information about how the site should run.

- And lastly, this README.md file tries to best explain the project.


## How To Run

- Firstly you have to run pip install -r requirements.txt to install all required libraries. 

- Secondly to run the application you can use the testing db.sqlite3 database or you can use a MySQL server. Depending on your choice you have to comment the database you don't want to use and uncomment your preferred one at settings.py. After you have made your database choice you have to run, "python manage.py makemigrations" and then "python manage.py migrate" to configure the database correctly.

- Thirdly, if you want to run the application on debug mode, on settings.py turn debug mode to True. Otherwise, if you want to run with debug set to False to experience the 404 page as well, continue to the next step.

- Lastly, with debug=False run "python3 manage.py runserver --insecure", with debug=True run "python3 manage.py runserver". You can also choose a port by adding a port number after the previous arguments.

- In addition, if you want to run tests you can do that by "python manage.py test". If you want to run Selenium tests you should uncomment the #Selenium tests section on tests.py, uncomment your preferred browser, and install its webdriver.


## Distinctiveness and Complexity

To begin with, I started by documenting and planning my thoughts on how I wanted the site to look and what technologies I wanted to use. I started by designing the look and the feel of the website which came naturally to me. After that, I wanted to fit in as many new frameworks and technologies as I could to further improve my skills while making my site look professional. That did not go as planned. I created a timeline graph to calculate how much each process (Project Preparation, Backend, Frontend, CI/CD, Scalability and Security, Deployment) would take and what tech would each process require me to learn and apply. When I started building, was exactly when reality hit me. Trying to combine frameworks you have little to no experience with can be exceptionally challenging and frustrating, especially when deadlines are following you. Nevertheless, I stuck through the steep learning curve and made things work for the first few technologies. I then realized that using every tool and middleware was not the right move, so I decided to focus on the ones that I wanted to learn the most and would be most useful and beneficial for me in the long run. After this phase, I worked on the site extensively while learning Git, Github Actions, MySQL, Javascript, Tailwind, Advanced CSS, and Docker on the side.

What I am saying is that the distinctiveness and the complexity of this project comes from the following factors:
- The size of the project. Compared to each other project I have ever done in this course or in general, this one took the most time and coding lines to complete.

- The number of frameworks. Learning and at the same time applying a new technology on a project is very demanding, and this project had a lot of new technologies which means a lot of independent learning and real-life application of these. 

- Combining tools together. The hardest part of all was combining all of these newly learned tools to work in harmony with each other, errorlessly.


## Unused feature: API route

When I started the application the idea was that a database would store all of the items of the bar's menu, and then with API calls each item would get loaded onto the page asynchronously, so, I created the item model and the API route. After some thought, I came to the conclusion that all of those calls would slow down the site drastically and would add unnecessary complexity given the amount of menu items per page. So I abandoned that idea and I embedded the items right into the HTML to minimize load times, though I did not delete the item model and the API as it leaves room for scaling the application if needed.
    

All in all, I am very proud of my Capstone project and my determination, despite the deadlines and the learning curves of the tools used.

# THANK YOU CS50W!