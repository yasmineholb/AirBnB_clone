# AirBnB_clone
**Command interpreter to manage the AirBnB objects**
****
## About this project
The AirBnB_clone is the first step towards building our first full web application.\
This web application is composed by:
  -  A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
  -  A website (the front-end) that shows the final product to everybody: static and dynamic
  -  A database or files that store data (data = objects).
  -  An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).\
In this project, we will manipulate 2 types of storage: file and database.\
In this repository, we will focus only on the **command interpreter** and **file storage**.

## About the command interpreter (the console)
 -  Command line interpreter that manipulates data and manages serialization and deserialization of objects.

## How it works
**The console:**
 - Displays the prompt (default prompt: "(cmd)", our prompt: "(hbnb)") and waits for user input.
 - Reads the entered command and the argument.
 - Looks for the function of the command. For example: entering the command "all", makes the console looks for "do_all(self, arg)" function.
 - Executes the function.
 - If the typed command (the function) doesn't exist, the console prints an Error message.
 - Quits when the user enters "quit" or "EOF" or presses Ctrl+d.

## The flow of Serialization-Deserialization
````
**<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE (file.json) -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>**
````
## Files repartition
**AirBnB_clone**
 - ├── console.py
 - ├── file.json (stores a JSON string representation of objects)
 - ├── AUTHORS
 - ├── README.md
 - ├── tests/ (unittests)
 - └── models
     - ├── __ init__.py
     - ├── base_model.py
     - ├── user.py
     - ├── state.py
     - ├── place.py
     - ├── city.py
     - ├── amenity.py
     - ├── review.py
     - └── engine
         - ├── __ init__.py
         - └── file_storage.py

## Files description

 - **console.py** -> the entry point of the command interpreter.
 - **models/__init__.py** -> creates a unique FileStorage instance and reloads the objects.
 - **base_model.py** -> contains the class BaseModel that defines all common attributes and methods for all other classes.
 - **user.py** -> one of the classes that inherits from BaseModel.
 - **models/engine/file_storage.py** -> contains the class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances.

## Console functions description
  - **do_create** -> creates a new instance of the entered class, saves the instance to the JSON file and prints its id.
  - **do_show** -> prints the string representation of an instance based on the class name and id.
  - **do_destroy** -> deletes an instance based on the class name and id, and saves the change into the JSON file.
  - **do_all** -> prints all string representation of all instances based or not on the class name.
  - **do_update** -> Updates an instance based on the class name and id by adding or updating attribute and saves the change into the JSON file.
  - **emptyline** -> it does nothing when an empty line is entered.
  - **postloop** -> prints a newline.
  - **do_quit** -> quit command to exit the console.
  - **do_EOF** -> EOF command to exit the console.

## USAGE
You can run this program on your local machine by following these steps:
> **Step 1:** Clone our repository using this command, (you need to have git and python3 installed on your machine first)
````
git clone https://github.com/yasmineholb/AirBnB_clone.git
````
> **Step 2:** Change directory to AirBnB_clone:
````
cd AirBnB_clone
````
> **Step 3:** Execute the console in this way:
````
./console.py
````
> **Step 4:** enter your command (In this example, our command is "help")
````
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
````
**Exiting the program**
When you want to exit the program, you can use one of the following methods:
> **1: Enter "quit" or "EOF"**
````
(hbnb) quit
````
> **2: Press on Ctrl d**
****
## Example of Usage
````
(hbnb) create BaseModel
0caf3180-e6b8-4e2d-aead-b955ea5fa10b
(hbnb) create User
c541aee4-03da-49fd-8fb9-278dbd79f69b
(hbnb) create Place
93af02d8-f99a-469d-b7e5-b0e0502ecfca
(hbnb) all
["[BaseModel] (0caf3180-e6b8-4e2d-aead-b955ea5fa10b) {'id': '0caf3180-e6b8-4e2d-aead-b955ea5fa10b', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 11, 828591), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 11, 828608)}", "[User] (c541aee4-03da-49fd-8fb9-278dbd79f69b) {'id': 'c541aee4-03da-49fd-8fb9-278dbd79f69b', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998198), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998220)}", "[Place] (93af02d8-f99a-469d-b7e5-b0e0502ecfca) {'id': '93af02d8-f99a-469d-b7e5-b0e0502ecfca', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634386), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634408)}"]
(hbnb) all BaseModel
["[BaseModel] (0caf3180-e6b8-4e2d-aead-b955ea5fa10b) {'id': '0caf3180-e6b8-4e2d-aead-b955ea5fa10b', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 11, 828591), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 11, 828608)}"]
(hbnb) 
(hbnb) 
(hbnb) show User c541aee4-03da-49fd-8fb9-278dbd79f69b
[User] (c541aee4-03da-49fd-8fb9-278dbd79f69b) {'id': 'c541aee4-03da-49fd-8fb9-278dbd79f69b', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998198), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998220)}
(hbnb) update User c541aee4-03da-49fd-8fb9-278dbd79f69b id "85"
(hbnb) show User c541aee4-03da-49fd-8fb9-278dbd79f69b
[User] (85) {'id': '85', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998198), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998220)}
(hbnb) update User c541aee4-03da-49fd-8fb9-278dbd79f69b team "Yasmine and Mariem"
(hbnb) show User c541aee4-03da-49fd-8fb9-278dbd79f69b
[User] (85) {'id': '85', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998198), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 18, 998220), 'team': 'Yasmine and Mariem'}
(hbnb) destroy User c541aee4-03da-49fd-8fb9-278dbd79f69b
(hbnb) destroy BaseModel 0caf3180-e6b8-4e2d-aead-b955ea5fa10b
(hbnb) all
["[Place] (93af02d8-f99a-469d-b7e5-b0e0502ecfca) {'id': '93af02d8-f99a-469d-b7e5-b0e0502ecfca', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634386), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634408)}"]
(hbnb) all BaseModel
[]
(hbnb) all User
[]
(hbnb) all Place
["[Place] (93af02d8-f99a-469d-b7e5-b0e0502ecfca) {'id': '93af02d8-f99a-469d-b7e5-b0e0502ecfca', 'created_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634386), 'updated_at': datetime.datetime(2020, 2, 17, 12, 42, 38, 634408)}"]
(hbnb) quit

````
****
## Bugs
No Known Bugs.
## AUTHOR
Yasmine Hamdi : [LinkedIn/Yasmine] | [GitHub/Yasmine] | [Twitter/Yasmine]\
Mariem Matri : [LinkedIn/Mariem] | [GitHub/Mariem] | [Twitter/Mariem]

[LinkedIn/Mariem]: <https://www.linkedin.com/in/mariem-matri-249620178>
[GitHub/Mariem]: <https://github.com/MatriMariem>
[Twitter/Mariem]: <https://twitter.com/MatriMariem>
[LinkedIn/Yasmine]: <https://www.linkedin.com/in/yasmine-h-a6588614b/>
[GitHub/Yasmine]: <https://github.com/yasmineholb>
[Twitter/Yasmine]: <https://twitter.com/yasmine_C10>
