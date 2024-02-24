import pandas as pd
from datetime import datetime

# Define classes
class Book:
    def __init__(self, title, authors, original_language, first_published, sales_millions, genre, shelves, number_of_books, price):
        self.title = title
        self.authors = authors
        self.original_language = original_language
        self.first_published = first_published
        self.sales_millions = sales_millions
        self.genre = genre
        self.shelves = shelves
        self.number_of_books = number_of_books
        self.price = price

    def __repr__(self):
        return (f"Title: '{self.title}'\n"
                f"Authors: {self.authors}\n"
                f"Original Language: {self.original_language}\n"
                f"First Published: {self.first_published}\n"
                f"Sales (millions): {self.sales_millions}\n"
                f"Genre: {self.genre}\n"
                f"Shelves: {self.shelves}\n"
                f"Number of Books: {self.number_of_books}\n"
                f"Price: {self.price}")

class Bookshelf:
    def __init__(self):
        self.books = []

    def load_from_csv(self, file_name):
        df = pd.read_csv(file_name)
        for _, row in df.iterrows():
            self.books.append(Book(row['Book'],
                                   row['Author(s)'],
                                   row['Original language'],
                                   row['First published'],
                                   row['Approximate sales in millions'],
                                   row['Genre'],
                                   row['Shelves'],
                                   row['Number of Books'],
                                   row['Price']))

    def find_book(self, title_fragment):
        found_books = []
        lower_title_fragment = title_fragment.lower()
        for book in self.books:
            if lower_title_fragment in book.title.lower():
                found_books.append(book)
        
        return found_books

    def list_books(self):
        for book in self.books:
            print(book)

    def update_shelf(self, title, new_shelf):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.shelves = new_shelf
                print(f"'{book.title}' has been moved to shelf {new_shelf}.")
                return True
        print("Book not found.")
        return False
    
    def inventory_summary(self):
        shelf_inventory = {}
        for book in self.books:
            # Check if the shelf exists in the dictionary
            if book.shelves not in shelf_inventory:
                shelf_inventory[book.shelves] = {'titles': [], 'total_price': 0, 'count': 0}
            # Append the book title to the shelf's list
            shelf_inventory[book.shelves]['titles'].append(book.title)
            # Update the total price for the shelf by multiplying the book's price by its number of copies
            shelf_inventory[book.shelves]['total_price'] += book.price * book.number_of_books
            # Increment the count of books on the shelf
            shelf_inventory[book.shelves]['count'] += book.number_of_books  # Adjusted to add the number of books, not just 1

        # Print the summary for each shelf
        for shelf, info in shelf_inventory.items():
            print("\n------------------------------------------------------------")
            print(f"Shelf {shelf} summary:")
            print(f"Number of titles: {len(info['titles'])}")
            print(f"Total number of books: {info['count']}")
            print(f"Total price of books: ${info['total_price']:.2f}")
            print("Book titles:")
            for title in info['titles']:
                print(f" - {title}")
            print("------------------------------------------------------------")

    def save_to_csv(self, file_name):
        import pandas as pd
        data = []
        for book in self.books:
            data.append({
                'Book': book.title,
                'Author(s)': book.authors,
                'Original language': book.original_language,
                'First published': book.first_published,
                'Approximate sales in millions': book.sales_millions,
                'Genre': book.genre,
                'Shelves': book.shelves,
                'Number of Books': book.number_of_books,
                'Price': book.price
            })
        df = pd.DataFrame(data)
        df.to_csv(file_name, index=False)
        print("Bookshelf saved to CSV.")

class User:
    def __init__(self, username):
        self.username = username

class Customer(User):
    def search_book(self, bookshelf):
        title_fragment = input("Enter the title of the book you're searching for: ")
        found_books = bookshelf.find_book(title_fragment) # Assuming this returns a list
        
        if found_books:  # Check if the list is not empty
            print("\nFound book(s):")
            for book in found_books:
                print(book)
                print("\n")
            print(f"Total books found: {len(found_books)}") # Print the count of found books
        else:
            print("No books found matching your query.")

class Admin(Customer):
    def add_admin(self, username, password):
        if username in users:
            print("Username already exists.")
            return
        users[username] = {'password': password, 'role': 'Admin'}
        print(f"Admin account created for {username}.")
        
    def update_book_shelf(self, bookshelf):
        title = input("Enter the title of the book to update its shelf: ")
        new_shelf = input("Enter the new shelf: ")
        if bookshelf.update_shelf(title, new_shelf):
            print(f"Successfully updated the shelf of '{title}'.")
        else:
            print(f"Failed to update the shelf. The book '{title}' may not exist.")

    def add_book(self, bookshelf):
        current_year = datetime.now().year
        title = input("Enter the title of the book: ")
        authors = input("Enter the authors of the book: ")
        original_language = input("Enter the original language of the book: ")
        
        # Using a while loop to keep prompting for input until it's valid
        while True:
            try:
                first_published = int(input("Enter the year the book was first published: "))
                if 0 <= first_published <= current_year:
                    break  # The year is valid
                else:
                    print("The year must be a positive number and less than or equal to the current year.")
            except ValueError:
                print("Invalid input for the year. Please enter a valid integer.")
       
        while True:
            try:
                sales_millions = float(input("Enter the approximate sales in millions: "))
                if sales_millions >=0 :
                    break  # Break the loop if the input is valid
                else:
                    print("The sales data must be positive")
            except ValueError:
                print("Invalid input for sales. Please enter a valid number.")
        
        genre = input("Enter the genre of the book: ")
        shelves = input("Enter the shelf for the book: ")
        
        while True:
            try:
                number_of_books = int(input("Enter the number of copies: "))
                if number_of_books >= 0:
                    break  # Break the loop if the input is valid
                else:
                    print("The number of books must be positive")
            except ValueError:
                print("Invalid input for the number of copies. Please enter a valid integer.")
        
        while True:
            try:
                price = float(input("Enter the price of the book: "))
                if price >= 0:
                    break  # Break the loop if the input is valid
                else:
                    print("The price of book must be positive")
            except ValueError:
                print("Invalid input for the price. Please enter a valid number.")
        
        new_book = Book(title, authors, original_language, first_published, sales_millions, genre, shelves, number_of_books, price)
        bookshelf.books.append(new_book)
        print(f"\nBook '{title}' has been added to the bookshelf.\n")

users = {
    'admin1': {'password': 'adminpass', 'role': 'Admin'},
    'cust1': {'password': 'custpass', 'role': 'Customer'},
}

def authenticate():
    while True:  # Loop indefinitely until successful authentication
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the username exists
        if username not in users:
            print("The username does not exist. Please try again.")
        else:
            # Username exists, now check password
            if password == users[username]['password']:
                role = users[username]['role']
                print(f"Welcome {username}! You are logged in as a {role}.")
                if role == 'Admin':
                    return Admin(username)
                else:
                    return Customer(username)
            else:
                # Password is incorrect
                print("The password is incorrect. Please try again.")

def main():
    while True:  # Loop to keep the application running
        user = authenticate()  # Authenticate a user
        if not user:  # If authentication fails or returns None, break the loop
            print("Authentication failed. Exiting the application.")
            break

        bookshelf = Bookshelf()
        # Load data from CSV
        bookshelf.load_from_csv('best-selling-books.csv')

        while True:  # Inner loop for user operations
            if isinstance(user, Admin):
                print("\n1. Add Admin\n2. Search Book\n3. Add Book\n4. Change Book Shelf\n5. Show Inventory Summary\n6. Log Off")
                choice = input("Select an option: ")
                if choice == '1':
                    new_admin_username = input("Enter new admin username: ")
                    new_admin_password = input("Enter new admin password: ")
                    user.add_admin(new_admin_username, new_admin_password)
                elif choice == '2':
                    user.search_book(bookshelf)
                elif choice == '3':
                    user.add_book(bookshelf)
                    bookshelf.save_to_csv('best-selling-books.csv')
                elif choice == '4':
                    user.update_book_shelf(bookshelf)
                    bookshelf.save_to_csv('best-selling-books.csv')
                elif choice == '5':
                    bookshelf.inventory_summary()
                elif choice == '6':
                    print("Logging off. You may log in with another account.")
                    break  # Break to log off and possibly re-login
                else:
                    print(f"{choice} is Invalid Option!! Please enter the valid option")
            elif isinstance(user, Customer):
                print("\n1. Search Book\n2. Log Off")
                choice = input("Select an option: ")
                if choice == '1':
                    user.search_book(bookshelf)
                elif choice == '2':
                    print("Logging off. You may log in with another account.")
                    break  # Break to log off and possibly re-login
            else:
                print("Invalid role. Exiting...")
                break  # In case of invalid user role
        
        # Ask if the user wants to exit the application or log in again
        exit_choice = input("Do you want to exit the application? \n (Type 'yes' to exit or press any other key to return to the login): ")
        if exit_choice.lower() == 'yes':
            print("Exiting the application. Goodbye!")
            break  # Assuming this is within a loop, it will exit the application
        else:
            print("Returning back to the login...")


if __name__ == "__main__":
    main()

