# FinalCapstone project - HyperionDev bootcamp

## Summary of project

* This capstone project was designed to manage stock-taking in a shoe warehouse. The user is able to perform a series of different actions on data using object oriented programming (OOP) and a series of methods and functions as described in _usage_ section below.

* It is designed and written in Python, using object oriented programming (OOP) and creates the class 'Shoe' with methods inside the class (get_cost to return the cost of shoes and get_quantity to return the quantity of the shoes). It sets up a variable to store a list of shoe objects with the following attributes: country of origin, code/barcode, product name, cost, quantity in stock, value of stock (cost * quantity).

## Installation

* To use this program you need to install Python (the latest version). You will need to an IDE for Python (e.g. Pycharm), open the file entitled 'T32 - capstone - inventory.py' and run it. Because the python code reads from a text file you will also need to add the text file 'inventory.txt' to the same folder.

* When you run the Python file this will give you a menu inviting you to input your preferred options, and further options which allow you to perform the actions set out in the _usage_ section.

## Usage

* The programme opens and reads from a text file that contains atrributes about shoe stock. 

* Menu options for the user are as follows (each option calls a different function detailed below):

*Read* - allows you to read data from a file (NB this option must be selected before any of the other functions can be called, and if other options are selected when the list is empty then it will ask the user to read the file first)
*Add* - allows you to add new data about a shoe (having done this, I also provided the user with the option of adding the information permanently to the text file)
*View all* - allows you to see the information in your shoe inventory - data is returned organised using Python's tabulate module
*Restock* - lets you see and restock the shoes with the lowest quantity and 
*Search* - lets you search for information about a shoe by either code or product name, and returns the other attributes
*Value* - allows you to find out the total value for each item
*Highest* - lets you see the shoes with the highest quantity and asks you to put these on sale
*Quit* - quit this programme

Although the bootcamp tast did not require this, I added features such as enabling editing of the text file in some of these options (e.g. add / 
It also enables editing of the text file (e.g. changing the quantity of stock, reducing the price on items with the highest quantity in stock).

To follow -screenshots


## Contibutors

* RosalindHook (project owner)

