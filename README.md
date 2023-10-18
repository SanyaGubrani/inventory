# Inventory Management System

**Video Demo: https://youtu.be/L_oNSpYBgQs?si=hJBVhEJN6TjNp-ZN**

## Description

The **Inventory Management System** is my final project for CS50's Introduction to Programming with Python (CS50P).
This project is a command-line interface used for managing a list of items in an inventory.
It allows you to add, remove, update, search, and view items in your inventory.

## Folder Contents

- `project.py`: This is the main Python script file for the Inventory Management System.
- `test_project.py`: This is the Python script file containing tests for the project.
- `requirements.txt`: This file lists the Python libraries used in the project. You could install them using `pip install -r requirements.txt`.
- `.gitignore`: This is a configuration file that specifies what files and directories to ignore when using Git.


## Dependencies
This project requires Python 3 and the following Python library installed:

- tabulate

You can install this library using pip:

```shell
pip install tabulate
```

## Usage

To run the script, use the following command in your terminal:

```shell
$ python project.py
```

To run the tests, use the following command in your terminal:

```shell
$ pytest test_project.py
```

## Features
Here are the features of the Inventory Management System:

1. **Add Item**: Add a new item to the inventory.
1. **Remove Item**: Remove an item from the inventory.
1. **Update Item**: Update the details of an existing item.
1. **Search Item**: Search for an item in the inventory.
1. **View Items**: Display all items in the inventory.
1. **Clear Inventory**: Remove all items from the inventory.
1. **Exit**: Exit the Inventory Management System.


## Data Storage

The data of this system is stored in a file named ‘Inventory.data’.
Each item occupies two lines in this file - the first line is for item name and the second line is for quantity.