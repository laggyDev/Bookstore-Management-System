
# Test Cases for Book Management System

This document outlines additional test cases for the Python book management application, focusing on various classes and functionalities.

## Book Class Tests

- **Test Initialization with Different Data Types:** Ensure that the `Book` class correctly handles various data types and formats, particularly for `first_published` and `sales_millions`.
- **Negative Values for Numeric Fields:** Verify handling of negative values for `sales_millions`, `number_of_books`, and `price` to ensure appropriate error handling or validation.

## Bookshelf Class Tests

- **Empty CSV File Load:** Test loading from an empty CSV to ensure no errors occur and the book list remains empty.
- **Invalid CSV Format:** Attempt to load from a CSV with missing columns or incorrect data types to test error handling.
- **Duplicate Book Titles:** Add books with identical titles but differing attributes to test duplicate handling.
- **Shelf Update for Non-existent Book:** Try updating the shelf for a book not in the `Bookshelf` and check error handling.
- **Inventory Summary Accuracy:** Manually add books and test the `inventory_summary` method for accurate calculations.

## Customer Class Tests

- **Search Book by Partial and Full Title:** Ensure searches find both partial and full title matches correctly.
- **Search for Non-existent Book:** Test searching for a nonexistent book title to check the "not found" scenario handling.

## Admin Class Tests

- **Add New Book with Valid and Invalid Data:** Test adding books with various data to validate input handling.
- **Update Shelf with Valid and Invalid Shelf Names:** Test shelf updates with both valid and invalid names to ensure correct handling.
- **Add Admin with Existing Username:** Attempt to add a new admin with a duplicate username to test uniqueness validation.

## General System Tests

- **User Authentication:** Test with both valid and invalid credentials to ensure correct authentication.
- **Role-based Access Control:** Verify that customer and admin roles have appropriate access to functionalities.
- **CSV Save and Load Integrity:** After modifications and saving to CSV, reload to test for data integrity.
- **Input Validation and Error Handling:** Test system responses to invalid inputs across various functions.


