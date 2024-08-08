class Book:
  def __init__(self, isbn, title, author):
    self.__isbn = isbn  # Private attribute for ISBN
    self.title = title
    self.author = author
    self._available = True  # Protected attribute for availability (use property)

  @property
  def available(self):
    return self._available

  def get_isbn(self):
    return self.__isbn

  def display_info(self):
    print(f"ISBN: {self.get_isbn()}")
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    #print(f"Available: {self.available}")

  def check_out(self):
    if self.available:
      self._available = False
      print(f"Book '{self.title}' is checked out successfully!")
    else:
      print(f"Sorry, book '{self.title}' is not available.")

  def check_in(self):
    if not self.available:
      self._available = True
      print(f"Book '{self.title}'has been returned successfully!")
    else:
      print(f"Book '{self.title}' is already available.")    

class Member:
  def __init__(self, member_id, name):
    self.__member_id = member_id  # Private attribute for member ID
    self.name = name
    self._books_borrowed = []  # list to store borrowed books

  def get_member_id(self):
    return self.__member_id

  def borrow_book(self, book):
    if book in self._books_borrowed:
      print(f"You have already borrowed '{book.title}'.")
    elif book.available:
      #book.lowercase()
      book.check_out()
      self._books_borrowed.append(book)
      print(f"{book.title} borrowed by {self.name}.")
    else:
      print(f"Sorry, book '{book.title}' is not available.")

  def return_book(self, book):
    if book in self._books_borrowed:
      book.check_in()
      self._books_borrowed.remove(book)
      print(f"{book.title} returned by {self.name}.")
    else:
      print(f"You haven't borrowed '{book.title}'.")

  def display_borrowed_books(self):
    if not self._books_borrowed:
      print(f"{self.name} has no borrowed books.")
    else:
      print(f"\nBorrowed books by {self.name}:")
      for book in self._books_borrowed:
        book.display_info()
        print("-" * 10)

class Library:
    """
    This class represents the library itself and manages the collection of books and members.

    Attributes:
        name (String): The name of the library.
        books (list): A list of Book objects representing the library's book collection.
        members (list): A list of Member objects representing the library's registered members.
    """

    def __init__(self, name):
        """
        Initializes a Library object with the provided name.

        Args:
            name (String): The name of the library.
        """
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        """
        Adds a new Book object to the library's collection.

        Args:
            book (Book): The Book object to be added to the library.
        """
        self.books.append(book)
        print(f"Book '{book.title}' has been added to library.")

    def add_member(self, member):
        """
        Adds a new Member object to the library's registered members list.

        Args:
            member (Member): The Member object to be registered in the library.
        """
        self.members.append(member)
        print(f"Member '{member.name}' has been registered successfully.")

    def display_available_books(self):
        """
        Prints information about all available books (books with availability set to True) in the library.
        """
        print("\nAvailable Books:")
        for book in self.books:
            if book.available:
                book.display_info()
                print("-" * 20)

    def check_out_book(self, book_title, member_name):
        """
        Attempts to check out a book by a member based on title and member name.

        Args:
            book_title (String): The title of the book to borrow.
            member_name (String): The name of the member borrowing the book.
        """
        book = None
        member = None

        # Search for the book by title in the library's book collection
        for b in self.books:
            if b.title == book_title:
                book = b
                break

        # Search for the member by name in the library's member list
        for m in self.members:
            if m.name == member_name:
                member = m
                break

        if book and member:
            member.borrow_book(book)  # Call borrow_book method of the Member object
        else:
            if not book:
                print(f"Book '{book_title}' not found in the library.")
            if not member:
                print(f"Member '{member_name}' not found in the library.")

    def return_book(self, book_title, member_name):
        """
        Attempts to return a book based on title and member name.

        Args:
            book_title (String): The title of the book to return.
            member_name (String): The name of the member returning the book.
        """
        book = None
        member = None

        # Search for the book by title in the library's book collection
        for b in self.books:
            if b.title == book_title:
                book = b
                break

        # Search for the member by name in the library's member list
        for m in self.members:
            if m.name == member_name:
                member = m
                break

        if book and member:
            member.return_book(book)  # Call return_book method of the Member object
        else:
            if not book:
                print(f"Book '{book_title}' not found.")
            if not member:
                print(f"Member '{member_name}' not found.")


class LibraryManager:
    """
    This class implements the Singleton pattern to ensure only one instance of the library manager exists.
    It provides a method to get the instance of the Library class.
    """

    _instance = None

    @classmethod
    def get_instance(cls):
        """
        Returns the existing instance of LibraryManager or creates a new one if it doesn't exist.
        """
        if cls._instance is None:
            cls._instance = LibraryManager()
        return cls._instance

    def run(self):
        """
        Simulates a user interface for interacting with the library management system.
        Provides a menu-driven interface for adding books, displaying books, registering members,
        borrowing/returning books, and displaying borrowed books.
        """
        library_name = ("Welcome to the Library! ")
        library = Library(library_name)

        while True:
            print("""
            Library Management System
            1. Add a new book
            2. Display all books
            3. Register a new member
            4. Borrow a book
            5. Return a book
            6. Display a member's borrowed books
            7. Exit
            """)

            choice = int(input("Select an option: "))

            if choice == 1:
                isbn = input("Enter ISBN: ")
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(isbn, title, author)
                library.add_book(book)

            elif choice == 2:
                library.display_available_books()

            elif choice == 3:
                member_id = int(input("Enter member ID: "))
                name = input("Enter member name: ")
                member = Member(member_id, name)
                library.add_member(member)

            elif choice == 4:
                book_title = input("Enter book title to borrow: ")
                member_name = input("Enter member name: ")
                library.check_out_book(book_title, member_name)

            elif choice == 5:
                book_title = input("Enter book title to return: ")
                member_name = input("Enter member name: ")
                library.return_book(book_title, member_name)

            elif choice == 6:
                member_name = input("Enter member name: ")
                for member in library.members:
                    if member.name == member_name:
                        member.display_borrowed_books()
                        break

            elif choice == 7:
                print("Thank you for visiting the library")
                break

            else:
                print("Please check your input.")

if __name__ == "__main__":
    library_manager = LibraryManager.get_instance()
    library_manager.run()

