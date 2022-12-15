
<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/zuri-training/TeamSparrowpp-qr_gen/">
    <img src="https://github.com/zuri-training/TeamSparrowpp-qr_gen/blob/main/static/images/image1.png" alt="Logo"> <!--width="300" height="250"-->
  </a>

<h3 align="center">QR Create</h3>
  <p align="center"><h3>
    </h3>
    <br />
    <h2><a href="https://github.com/zuri-training/TeamSparrowpp-qr_gen/README.md"><strong>Explore the docs »</strong></a></h2>
    <br />
    <a href="">View Demo</a>
    ·
    <a href="#issues">Report Bug</a>
    ·
    <a href="#issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">What are we building?</a>
      <ul>
        <li><a href="#project-documentation">Project Documentation</a></li>
        <li><a href="#project-design-sketch">Project Design Sketch</a></li>  
        <li><a href="#tools-used">Tools Used</a></li>
        <li><a href="#database-schema">Database Schema</a></li>
        <li><a href="#mood-boards">Mood boards</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## `About The Project:`
A platform that allows users generate QR code that specifically does something when scanned.

<!-- Project Documentation -->
We have attached the necessary links for better understanding of our project.

#### `Project Documentation:`
> <a href="https://docs.google.com/document/d/1IO4Uo2x3AgA8C7coABzJxRnoXM5g0VSoyFFFnuNm-Ds/edit?usp=sharing">TeamSparrowpp QR_Generator Docs</a>

<!-- Project Design Sketch -->
#### `Project Design Sketch:`
> <a href="https://www.figma.com/file/YQt9Ek5Ag6pA1MSUNYC8bB/Untitled?node-id=298%3A763">TeamSparrowpp QR_Generator Design Sketch</a>

<!--Project Database Schema-->
#### `Database Schema:`
[Database schema](https://github.com/zuri-training/TeamSparrowpp-qr_gen/blob/main/static/images/Schema.jpg)

#### `Mood boards:`
[Mood boards](https://www.figma.com/file/69WTNnIDkrtL4IIRkP3ZSv/Mood-Board-(Copy)?node-id=0%3A1&t=cU62ZfenT7jozyy2-1)

<!-- Github Project Organization -->
#### `Github Project Organization:`
> <a href="https://github.com/orgs/zuri-training/projects/543">TeamSparrowpp Github Projects</a>


## __Project Status__: _in progress_
<br><br>

## `Tools Used`
  - __Design__ <br/>
  ![figma-#F24E1E](https://user-images.githubusercontent.com/72948572/183909728-8197f9c8-8b97-4015-8e0b-f8e605b19309.svg)
  
  - __Frontend__ <br/>
![html5-#E34F26](https://user-images.githubusercontent.com/72948572/183910382-06b2d259-2f17-4c4f-afb0-0ed20cddd85c.svg) ![css3-#1572B6](https://user-images.githubusercontent.com/72948572/183910424-215b3da2-9067-44ba-a16a-91eefc3d90fc.svg) ![javascript-#323330](https://user-images.githubusercontent.com/72948572/183910461-4e24a5f5-7ad9-48a0-a7b0-94bcba32a94b.svg)

  - __Backend__ <br/>
  ![python-3670A0](https://user-images.githubusercontent.com/72948572/183910681-b6193dcd-8242-4a5e-af78-d79f99fc40b6.svg) ![django-#092E20](https://user-images.githubusercontent.com/72948572/183910701-cdc634b5-9524-4158-8063-045000741e42.svg)

  - __Database__ <br/>
    SQLite3
  
  - __Version Tracking__ <br/>
  ![github-#121011](https://user-images.githubusercontent.com/72948572/183911700-45ab5ec7-8f95-41ce-8d0e-616ddca2827f.svg)
  <br><br>

## `Features`
  `Create Account` Users are able to sign up on *`QR Create`* with their email, username,  and password. 
  
  `Login` Fetches users sign up details from our database, compares the login details and allows authenticated users gain full access to `QR Create's` Services.
  
  `Documentation` All Users have full access to view and interact with the documentation.

  `Generate QR Codes` Authenticated users can Generate Qr for Different use case, Email, Text, etc.
  
  `Download QR Codes` Authenticated users Can download a generated Qr code into their Local Device as PDF, PNG, JPEG, JPG or Even SVG

  `Save QR codes` Authenticated users Can save a Generated QR code to view Later

  `Share` Authenticated users can share Generated QR codes to Twitter, Facebook or Even as an Email.

  `Responsive` Allow user save data and come back to it..

  <br><br>

  ## `How To Use Locally:`
<br>


## `Requirements`
* An IDE
* Git & GitHub 
* A compatible browser
* Python 3.8+
  <br><br>


##  `Setup and Installation`  
  __In your IDE run the following commands in the terminal to setup__
- Install  environment in the root directory `qrcode_gen_project`

    ``` ruby
    pip install virtualenv
    ```
- Create the virtual environment in the same root directory

  - FOR WINDOWS USERS

    ``` ruby
    virtualenv <environment_name>
    ``` 
    - Activate virtual environment

      ``` ruby
      <environment_name>\scripts\activate
      ``` 

  - FOR LINUX USERS

    ``` ruby
    python3 -m virtualenv <environment_name>
    ``` 
    - Activate virtual environment

      ``` ruby
      source/<environment_name>/bin/activate
      ```
  <br>

- Change directory

  ``` ruby
  cd qr_gen_team60/qr_gen_project/
  ```
<br>


- Install all packages/ Dependencies used
    ``` ruby
    pip install -r requirements.txt
    ```
- Run Migrations for the Apps

    ``` ruby
    python manage.py makemigrations accounts
    ``` 

  
    ``` ruby
    python manage.py makemigrations qr_generator
    ```


    ``` ruby
    python manage.py migrate accounts
    ```

    ``` ruby
    python manage.py migrate qr_generator
    ``` 

  ``` ruby
    python manage.py migrate
    ```

- Run Server

    ``` ruby
    python manage.py runserver
    ```

  <br><br>
## `How to Contribute `
- __Fork the project repository__<br/>
In the project repository on github click the fork button in the upper right corner

- __Clone the forked repository to your local machine__

    ```ruby
    git clone https://github.com/zuri-training/TeamSparrowpp-qr_gen.git
    ```
- __Navigate to the local directory and open in your IDE/ Text Editor__

- __In the IDE terminal set upstream branch__

    ```ruby
    git remote add upstream https://github.com/zuri-training/TeamSparrowpp-qr_gen.git
    ```
- __Pull upstream__

    ```ruby
    git pull upstream production
    ```
    
- __Create a new branch to make your changes__

    ```ruby
    git checkout -b <your_branch_name>
    ```
    
- __Stage the file__
After making edits, type the below command in your terminal

    ```ruby
    git add <changed_files>
    ```
    
- __Commit changes__

    ```ruby
    git commit -m "your_message"
    ```
- __Push your local changes__

    ```ruby
    git push origin <your_branch_name>
    ```

- __Create a pull request__

- __Wait till a QR planet admin accepts and merges your pull request__

  <br><br>

## `Contributors`


<div align="center">
    <h1> What are You Waiting For?? Try out QRCreate Today!!!</h1>
</div>

![QR Create](https://github.com/zuri-training/TeamSparrowpp-qr_gen/blob/main/static/images/qr-code.gif)



