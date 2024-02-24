# Bookstore Management System

This bookstore management system is a Python-based application that allows users to manage a collection of books. With features like adding, searching, and updating book information, it is suitable for small libraries or personal collections.

original input data source: https://www.kaggle.com/code/drahulsingh/best-selling-books-notebook/input

## 1. Features

- Load books from a CSV file
- Search for books by title
- Add new books to the inventory
- Update the shelf location of books
- Admin and customer role management
- Inventory summary with total book count and price per shelf

## 2. Getting Started

Follow these instructions to get your Book Management System up and running.

## 3. Prerequisites

You need to have Python 3.x installed on your system to run this application. Python can be downloaded from the [official website](https://www.python.org/downloads/).

You need to have pandas 1.2.4 installed on your system to run this application. pandas can be installed from https://pandas.pydata.org/

### 3.1 Verify Current Interpreter

First, ensure you know which Python interpreter you're using when the error occurs. In IDEs like PyCharm, VSCode, or Jupyter notebooks, the interpreter or kernel can usually be selected or changed from the interface. **Check the interpreter path to confirm whether it points to the expected environment where pandas is installed.**

### 3.2 Ensure Pandas is Installed in the Active Environment(you can skip this once you are sure of the above step)

For standard environments (venv/virtualenv):
Activate the environment and use pip to install pandas:

    source /path/to/env/bin/activate  # On Windows, use `\path\to\env\Scripts\activate`
    pip install pandas
    
For Anaconda environments:
Activate the conda environment and use conda to install pandas:

    conda activate myenv
    conda install pandas


## 4. Simple Execution

download both file:

**Ensure to save both files under the same folder**

    best-selling-books.csv
    main.py
    
### 4.1 Run the application and you will be prompted to enter the username and password

For test authentications, each username and password are as follows

### admin username and password:
    admin1
    adminpass

### customer username and password:
    cust1
    custpass

### Once you log in as **admin** you are prompted you select the following options:
    1. Add Admin
    2. Search Book
    3. Add Book
    4. Change Book Shelf
    5. Show Inventory Summary
    6. Log Off
    
### Once you log in as **customer** you are prompted you select the following options:
    1. Search Book
    2. Log Off

