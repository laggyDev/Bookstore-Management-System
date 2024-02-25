
# Bookstore Management System

The Bookstore Management System is a versatile Python-based application designed to help users efficiently manage a collection of books. Ideal for small libraries or personal collections, it incorporates a range of functionalities such as book addition, search, and shelf location updates, alongside role-based access for admins and customers.

**Original Input Data Source:** [Kaggle Notebook - Best Selling Books](https://www.kaggle.com/code/drahulsingh/best-selling-books-notebook/input)
**Video Presentation & Documents:** https://drive.google.com/drive/folders/1M9GRTupvYxAnrQ6GpXubpwe2o7w-9il9?usp=sharing

## Features Overview

- **Load Books:** Import book details from a CSV file into the system.
- **Book Search:** Find books within the inventory by title.
- **Inventory Management:** Add new books to the system and update existing book information.
- **Shelf Management:** Adjust the shelf locations of books as needed.
- **Role-Based Access:** Separate access controls for admin and customer roles.
- **Inventory Summary:** Generate summaries of book counts and total prices, organized by shelf.

## Getting Started

To set up the Book Management System on your machine, follow the steps outlined below.

## Prerequisites

Ensure Python 3.x and pandas 1.5.3 are installed on your system:

- **Python 3.x:** Download from the [official Python website](https://www.python.org/downloads/).
- **Pandas 1.5.3:** Install via pip (`pip install pandas`) or conda for Anaconda environments (`conda install pandas`). Visit [pandas' official site](https://pandas.pydata.org/) for more details.

### Setting Up Your Environment

#### Verify Python Interpreter

- **Check Interpreter Path:** In your IDE (e.g., PyCharm, VSCode), confirm the interpreter path points to the environment where pandas is installed.

#### Install Pandas

- **Standard Python Environment:**
  ```bash
  source /path/to/env/bin/activate  # Use \path\to\env\Scripts\activate on Windows
  pip install pandas
  ```

- **Anaconda Environment:**
  ```bash
  conda activate myenv
  conda install pandas
  ```

## Running the Application

Ensure you have downloaded and saved both `best-selling-books.csv` and `main.py` in the same directory.

### Initial Setup

- **Start the Application:** Run `main.py` in your terminal, IDEs, or command prompt. You will be prompted to log in using a username and password.

### Authentication Details

- **Admin Access:**
  - Username: `admin1`
  - Password: `adminpass`

- **Customer Access:**
  - Username: `cust1`
  - Password: `custpass`

## User Options

### Admin Options

Once logged in as an **admin**, you will have the following options:
1. Add Admin
2. Search Book
3. Add Book
4. Change Book Shelf
5. Show Inventory Summary
6. Log Off

### Customer Options

As a **customer**, you can:
1. Search Book
2. Log Off

Follow the on-screen prompts to navigate through the application.
