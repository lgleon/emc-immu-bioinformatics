[![Build Status](https://travis-ci.com/lgleon/emc-immu-bioinformatics.svg?branch=master)](https://travis-ci.com/lgleon/emc-immu-bioinformatics)


<h3 align="center">
EMC Bioinformatic Immunology Lab
</h3>

<h3 align="center">
<img src="lab/static/lab/Picture1Log.png" width=420 alt="Immu Bioinformatics Logo">
</h3>

<div align="center">

[EMC Bioinformatic Immunology Lab](https://github.com/lgleon/emc-immu-bioinformatics) This repository contains the code for the online Web site for Bioinformtic group in the EMC-Immunology department. It is primarily built using Python (back-end) and the 
Django framework and uses sql3 for the database. It also uses the Bootstrap framework on the front-end.
That application was built for fourth Milestone Project at Code Institute.
The live project can be viewed [here](https://##################.herokuapp.com/).

</div>


## Contents Table

1. [**UX**](#ux)
    - [**User stories**](#your-experience-as-user)
    - [**Design Ideas**](#design-ideas)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)
    - [**Challenges**](#learning-challenges)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Media**](#media)
    - [**Acknowledgements and Inspiration**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)


## UX
 
This application is built with a mobile first, responsive design in mind.

### User stories

- As a new user, I should:
    - see a homepage with a cover image with a some lines about our Lab.
    - see a main navigation with links to the different sections in out lab; work, team, contact.
    - see a signup tap to register as user or log in.

- As a register user who wishes to collaborate with us or ask for a bioinformatic analysis (authentication is required for this part), I should:
    - see a form allowing me to register as a client:
        - Using the user name, frecquently a student, register a Supervisor (PI) as client.
        - specified a Department in case is not Immunology
        - Add a project with some specifications
    - see a submit button to send the form
    - got a sucessfully submited messague with user and supervisor names
    - see a log out tab

- As a user who is resgister/accepted as client (authentication is required for this part), I should see a link to "Request analysis" where I can see a form:
    - All fields are required to have an idea reagarding the type of analysis to perform and the study and project realted with.
    - see a submit button to send the form
    - got a sucessfully submited messague with job id and priority status that they will pay for

- As a user who is part of our bioinformatic team (authentication is required for this part), I should:
    - see a form to update the status of the job I am working in
    - got a sucessfully update messague with job name 
    - see a log out tab

- A a user who just request a bioinformatic analysis I should:
    - check the cart and see the job name and the priority status of the job submited 
        - change the priority status if I made a mistake previously
        - click the button to go to checkout, then:
            - see a form for payment
            - make payment
    - see a log out tab

### Design ideas

The design of this website is completely original and base in the personal need when the head of my department, Immunology, requested me to have a record of the projects I am collaborating and the analysis I am doing for each project, also keep a track of the PIs which are requesting an analysis and if I have extrenal (outside our department) collaborations.
 
 ### Wireframes

There are no computer, mobile or any digital wireframes or mockups. 
There is a paper wireframe, picture included in the folder (readme_info/)




## Features
 
### Existing Features

- The **User Registration and User Login** features are taking care by Django framework. 

- The feature for **Analysis request** will be available for users who are logged in and are accepted as clients is accessed by the 'request an analysis' tab in the navbar right-hand corner. This will take the user to a full page form that will allow them to submit detailed information about a new job or analysis.

- The feature for **Client** will be available for users who are logged in and can apply to register as clients using his supervisor name is accessed by 'clients' tab in the navbar right-hand corner. This will take the user to a half page form that will allow them to submit detailed information about the department, project and supervisor of the project.

- The feature for **JobStatus update** will be available for users who are logged in as Team members of the Lab and have Staff priviles is accessed by 'Job sttus' tab in the navbar right-hand corner. This will take the user to a half page form that will allow them to fillup a short form to keep a record of the analysis that they are working on and submit that info to the DB.

- The feature for **Contact** will be available for all users is accessed by the 'contact' tab in the navbar right-hand corner. This will take the user to a short form that they can use if they have any question or they want to ask anything regarding an specific analysis.

### Features Left to implement

- A job status for clients, where they can check the job status update using the job id that they got when they submit the analysis.  



### Challenges

- Learning how to work with Dajngo Framework was a great learning experience. It was chalelnging to learn to with with separate app for the different parts of the website. Also how to trust in Django features for user authentication.

- Wairing the forms, models and htlms in each app and then to the project using the URLconfig.

- Integrate the old static html that I previously created for my Lab to the new backend functionality.




## Technologies Used

Languages, frameworks, libraries, and any other tools used to construct this project. 


- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - **HTML5** HyperText Markup Language.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - **CSS3** Cascading Style Sheets.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - **Javasript** is a high-level, interpreted programming language.
- [PyCharm](https://www.jetbrains.com/pycharm/)
    - **PyCharm** Is the IDE used to develop the website.
- [GitHub](https://github.com/)
    - **Github** is used: 
    1. As a remote backup of code used in the project.
    2. As a remote server for another user to see the code used in the project.
    3. For users to view the deployed version of the website. The deployed version can be viewed [here!](https://lgleon.github.io/DidacCookBook/).
- [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap** is used to create easier & cleaner responsiveness in addition with helping maintain padding and margins.
    - It's also used to include modal features to the website to give it a professional look.
- [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- [Materialize](https://materializecss.com/)
    - **Materialize** to provide the front-end grid framework and support responsive behaviour.
- [Python](https://www.python.org/)
    - **Python** as the server-side programming language to provide back-end logic and serve dynamic web pages to the browser.
- [Django](https://www.djangoproject.com/)
    - **Django** as the back-end framework to simplify configuration of the application and routing, to render HTML templates, work with client requests  and to assist with user session management.
- [Stripe](https://dashboard.stripe.com/register)
    - **Stripe** 
- [Travis](https://travis-ci.org/)
    - **Travis Continuous Integration**, connects to my GitHub account and run test I pushed to gitHub giving me pass/fail results.
- [Heroku](https://www.heroku.com/) 
    - **Heroku**, Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.



## Testing

- the project was continually tested using Travis, checking everytime that it did pass the build test   

- The project was build using Google Chrome and then later tested in other browsers; FireFox and Safary

- This project was tested for responsiveness using the Chrome Developer Tools.



## Deployment

The project was built using [PyCharm](https://www.jetbrains.com/pycharm/), through a built-in function called 'Git', I could commit
the project & push it up to [GitHub](https://github.com/).

- To view the deployed version of [EMC Bioinformatic Immunology Lab ](https://lgleon.github.io/emc-immu-bioinformatics/) I needed to take the following steps:
    - Log in to [GitHub](https://github.com/).
    - Select **lgleon/emc-immu-bioinformatics** from the list of repositories.
    - Select **Settings** from the navbar near the top of the page.
    
- To add this repository to your local workspace:
    - Click on the [EMC Bioinformatic Immunology Lab repository on GitHub!](https://lgleon.github.io/emc-immu-bioinformatics/) link.
    - Select the green button on the right-hand side named **Clone or download** and copy the clone URL.
    - Go into your local workspace and open up a new terminal (git bash).
    - You will need to be inside of the directory that you want to add the cloning to.
    - Type `git clone ` and paste the URL you copied from GitHub and press enter. It should look like this: 
```console
git clone https://github.com/*username*/*repository*
```
The process of cloning will now be completed. For further information on cloning,
visit [How to clone from GitHub](https://help.github.com/en/articles/cloning-a-repository).

This project was then deployed to Heroku to host the live application, following the steps below:

1. Log in to [Heroku](https://www.************************heroku.com/) and create a new app called 'didaccookbook'
2. Log in to Heroku in the CLI
3. Add the remote Heroku repo
4. Create the requirements.txt file by running `pip3 freeze --local > requirements.txt` in the CLI
5. Create a Procfile by running `echo web: python run.py > Procfile` in the CLI
6. Start a web process on Heroku by running `heroku ps:scale web=1` in the CLI
7. Set environment variables in Heroku for IP, PORT and MONGO_URI
8. Restart all dynos on Heroku

The live project can be viewed [here](https://********************************8.herokuapp.com/).

## Databse schema:



## Credits

### Content
- All Content has been thought of and written by the Developer
- The content of the project is original from our Lab and collaborations

### Media
- The images for the home page and proeject are originals generated during the analysis of those data in the projects


## Acknowledgements and Inspiration

- I got Inspiration for this project looking into other bioinformatics websites

[HammerLab](http://www.hammerlab.org/) 
[CBCC](https://ccbc.erasmusmc.nl/)
[TUDelft](https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/intelligent-systems/pattern-recognition-bioinformatics/the-delft-bioinformatics-lab/) 



A huge thank you to:

- Spencer Barriball (Super_Spence_mentor) - For discussing ideas, providing help wherever needed also coaching and "dont give up you are doing great" moments.

- Luis Rodil and David van Zessen for share ideas, show me where to look and their patience.


## Disclaimer

All content on the website, including images, are used for educational purposes only.
