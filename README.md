0x00. AirBnB clone - The console
0;276;0c
Project Description:
The project involves creating an AirBnB clone, a web application for property
rentals. In its initial phase, a command interpreter is being developed to
manage AirBnB objects, allowing users to create, retrieve, modify, and delete
objects related to the AirBnB platform.

Command Interpreter Description:
The command interpreter is a text-based interface that interacts with and
manages AirBnB objects. It supports creating, retrieving, updating, and deleting
objects, as well as performing operations on them. Additionally, it can operate
in both interactive and non-interactive modes.

How to Start It:
To initiate the command interpreter, open a terminal and navigate to its
directory. Execute the program using a command like ./console.py.

How to Use It:
When running in interactive mode, users can interactively enter commands to
perform actions such as creating users, retrieving objects, updating attributes,
and more.

In non-interactive mode, users can supply commands via pipes or input
redirection, allowing for automation and scripting. For example:

$ echo "create User" | ./console.py

Examples:
Interactive Mode:
Creating a new user: (hbnb) create User
Retrieving details of a specific place: (hbnb) show Place 789
Counting the number of cities: (hbnb) count City
Updating a user's phone number: (hbnb) update User 456 phone "555-1234"
Deleting a reservation: (hbnb) destroy Reservation 987

Non-Interactive Mode:
$ echo "create User" | ./console.py
