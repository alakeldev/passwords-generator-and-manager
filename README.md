<h1 align="center">🔐Passwords Generator & Manager🔐</h1>
“Passwords Generator and Manager” starts with an application that helps you generate strong and secure passwords for your online accounts. With the password generator application, you can create unique passwords that are difficult to guess or hack. This application also leads you to a password manager application (Section) that helps you manage your passwords by storing them securely in an encrypted file. You can easily access your passwords whenever you need them, without having to remember them all.<br></br>

![PWD-image](assets/readme-images/pwd.jpg)

The Passwords Generator and Manager application is live and deployed on Heroku cloud platform. Please click [HERE](https://password-generator-and-manager-a88bcb86c5e0.herokuapp.com/) to check it out.

## Table of Contents
- [Table of Contents](#table-of-contents)
- [UX](#ux)
  - [App Purpose:](#app-purpose)
  - [App Goal:](#app-goal)
  - [Audience:](#audience)
  - [Communication:](#communication)
  - [Current User Goals:](#current-user-goals)
  - [New User Goals:](#new-user-goals)
  - [Future Goals:](#future-goals)
- [Logic](#logic)
  - [Diagrams-App:](#diagrams-app)
- [Design](#design)
  - [Colour:](#colour)
  - [Existing Features:](#existing-features)
    - [Landing Page + Passwords Generator App Start:](#landing-page--passwords-generator-app-start)
    - [Get Full-Name + Welcome Message:](#get-full-name--welcome-message)
    - [Passwords Generator Run Full-Path:](#passwords-generator-run-full-path)
    - [Passwords Generator Run "Exit" Path:](#passwords-generator-run-exit-path)
    - [Passwords Manager App Start + Welcome Message:](#passwords-manager-app-start--welcome-message)
    - [Passwords Manager App - "Save" Path:](#passwords-manager-app---save-path)
    - [Passwords Manager App - "View" Path:](#passwords-manager-app---view-path)
    - [Passwords Manager App - "Exit" =\> Ask: Delete The Previous Saved Data:](#passwords-manager-app---exit--ask-delete-the-previous-saved-data)
    - [Passwords Manager App - "Exit" =\> No Ask: No Previous Saved Data:](#passwords-manager-app---exit--no-ask-no-previous-saved-data)
    - [Passwords Generator + Manager Apps =\> "Exit" Paths:](#passwords-generator--manager-apps--exit-paths)
  - [Hidden(Background) Features](#hiddenbackground-features)
  - [Future Features](#future-features)

## UX

### App Purpose:
It is an application that helps you generate strong and secure passwords for your online accounts. With this application, you can create unique passwords that are difficult to guess or hack. The application also leads you to a password manager application that allows you to store your passwords securely in an encrypted file. You can easily access your passwords whenever you need them, without having to remember them all. This application is designed to make your online life easier and more secure.

### App Goal: 
- Generate strong and unique passwords that are difficult to guess or hack.
- Store your passwords & its username securely in an encrypted file, so you don’t have to remember them all.

### Audience:
Everyone who wants unique passwords that are difficult to guess or hack for their accounts and also who have multiple online accounts and have trouble remembering all their passwords and want to store them in secure place.

### Communication:
The App expresses its intent through the print statements generated, prompting the user to walk through the options available & make their selections. Various statements also print in a variety of colour to help break up the monotony of the white text, making it easier to read.

### Current User Goals:
- Generate strong and unique passwords for their online accounts.
- Store their passwords and usernames securely in an encrypted file.
- Easily to back to their saved passwords whenever they need them.

### New User Goals:
- Generate fast small passwords that are easy to remember but still secure.
- Share their passwords and usernames with trusted family members or friends.

### Future Goals:
The most of these features are in the version of "Norton" Passwords Generator and Manager:
- Provide a password strength meter that shows the strength of each password generated.
- Provide a feature that allows users to import and export their passwords to other applications.
- Biometric authentication technologies such as facial recognition or fingerprint scanning.
- Encrypt the data with public key and decrypt these data with different privet key (asymmetric encryption).
- Remove the file of my-passwords.txt file and save the user passwords in encrypted version direct only.
- Make the encrypt and decrypt through APIs.

## Logic

### [Diagrams-App](https://app.diagrams.net/):
This flowchart was created to visualise the logical flow and various paths possible.                          
You can view the Application diagram-flowchart and see each path in detail by clicking [HERE](https://alakeldev.github.io/pp3-diagram/).<br></br>
![App-Diagram](assets/readme-images/pp3-diagram.png)

## Design

### Colour:
The Python “Termcolor” module was utilized to add color to the project. The colors green, yellow, and red were employed to represent different paths and results. Green was utilized for Apps titles, welcome , bye messages, and normal and important results such as the new generator password. Red was utilized for errors and non-normal messages. Yellow was utilized to indicate unique questions or guide.

### Existing Features:
#### Landing Page + Passwords Generator App Start:
![Landing Page and Passwords Generator start](assets/readme-images/loading-app.png)

#### Get Full-Name + Welcome Message:
![Welcome Message](assets/readme-images/welcome-msg-app.png)

#### Passwords Generator Run Full-Path:
![Passwords Generator Normal Path](assets/readme-images/pwd-generator-app.png)

#### Passwords Generator Run "Exit" Path:
![Passwords Generator Exit Path](assets/readme-images/pwd-generator-app-exit.png)

#### Passwords Manager App Start + Welcome Message:
![Passwords Manager start + Msg](assets/readme-images/pwd-manager-start.png)

#### Passwords Manager App - "Save" Path:
![Passwords Manager - Save Path](assets/readme-images/pwd-manager-save-path.png)

#### Passwords Manager App - "View" Path:
![Passwords Manager - View Path](assets/readme-images/pwd-manager-view-path.png)

#### Passwords Manager App - "Exit" => Ask: Delete The Previous Saved Data:
![Passwords Manager - Exit & Delete](assets/readme-images/pwd-manager-exit-delete-saved-data-path.png)

#### Passwords Manager App - "Exit" => No Ask: No Previous Saved Data:
![Passwords Manager - Exit](assets/readme-images/pwd-manager-exit-no-saved-data.png)

#### Passwords Generator + Manager Apps => "Exit" Paths:
![Passwords Generator and Manager Apps 'Exit'](assets/readme-images/exit-all-path.png)

### Hidden(Background) Features


### Future Features
- Create an account for each user that shows only their passwords and requires a master password and username to access.
- Remove and Edits a specific saved username or password inside the file without effect any other saved data.
- Password expiration reminders, two-factor authentication.
- Create simple beatiful GUI for application.

