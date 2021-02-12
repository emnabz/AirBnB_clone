# AirBnB_clone - The console

## Description of the project


The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of the project is to deploy on your server a simple copy of the AirBnB website. A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

## Installation

   * Clone this repository: https://github.com/emnabz/AirBnB_clone.git
   * Access AirBnb directory: cd AirBnB_clone
   * Run hbnb(interactively): ./console and enter command
   * Run hbnb(non-interactively): echo "<command>" |  ./console.py

It covers the following fields:

   * A website (call front-end) that shows the final product to everybody
   * An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
   * A database or files that store data (data = objects)
   * A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

## Description of the command interpreter:
 
how to start it:

The command interpreter starts when running ./console.py.
It can work both in interactive and non interactive mode (see examples).
The following commands have been implemented:

* EOF - exits console
* quit - exits console
* overwrites default emptyline method and does nothing
* create - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
* destroy - Deletes an instance based on the class name and id (save the change into the JSON file).
* show - Prints the string representation of an instance based on the class name and id.
* all - Prints all string representation of all instances based or not on the class name.
* update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3).
