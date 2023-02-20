# FinalCapstone project - HyperionDev bootcamp

## Summary of project

* This capstone project was designed to manage stock-taking in a shoe warehouse. The user is able to perform a series of different actions on data using object oriented programming (OOP) and a series of methods and functions as described in _usage_ section below.

* It is designed and written in Python, using object oriented programming (OOP) It sets up a variable to store a list of shoe objects with the following attributes: country of origin, code/barcode, product name, cost, quantity in stock, value of stock (cost * quantity).

## Installation

* To use this program you need to install Python (the latest version). You will need to use an IDE for Python (e.g. Pycharm) to run the files.

* There are three key files that you need to add to the same folder, as follows:

1. 'T32 - capstone - inventory.py' - this is the bulk of the programme and contains all the functions that are called by the user from the main menu)
      
2. 'shoe_class.py' - this file creates the class 'Shoe' with methods inside the class (get_cost to return the cost of shoes, get_quantity to return the quantity of shoes in stock, and rendering the class as a string). 
      
3. Because the python code reads from a text file you will also need to add the text file 'inventory.txt' to the same folder as this contains data that is required by the programme (as well as being the file that you have the option to change/amend).


* Because of the use of tabulate in the 'view all' selection, you will also need to ensure you have imported the tabulate module (does not come as standard with Python).

* When you run the Python file entitled 'T32 - capstone - inventory.py' this will give you a menu inviting you to input your preferred options, and further options which allow you to perform the actions set out in the _usage_ section. You don't need to do anything with the other two files except save them to the same folder.

## Usage

* The programme opens and reads from a text file that contains atrributes about shoe stock. 

* Menu options for the user are as follows (each option calls a different function detailed below):

1. *Read* - allows you to read data from a file (NB this option must be selected before any of the other functions can be called, and if other options are selected when the list is empty then it will ask the user to read the file first)

2. *Add* - allows you to add new data about a shoe (having done this, I also provided the user with the option of adding the information permanently to the text file)

3. *View all* - allows you to see the information in your shoe inventory - data is returned organised using Python's tabulate module

![Screenshot of tabulate display of data in inventory](https://github.com/RosalindHook/finalCapstone/blob/main/Screenshot%202023-02-20%20at%2023.29.41.png)

4. *Restock* - lets you see and restock the shoes with the lowest quantity and 

5. *Search* - lets you search for information about a shoe by either code or product name, and returns the other attributes


![Screenshot of returned data when searched by product name]()

6. *Value* - allows you to find out the total value for each item

7. *Highest* - lets you see the shoes with the highest quantity and asks you to put these on sale

8. *Quit* - quit this programme

Although the bootcamp tast did not require this, I added features such as enabling editing of the text file in some of these options where it made sense to give the user an option to make permanent changes to the text file (e.g. changing the quantity of stock, reducing the price on items with the highest quantity in stock).

![Screenshot of the 'Highest' option where you are asked to put these shoes on sale]()


## Contibutors

* RosalindHook (project owner)

