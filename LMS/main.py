# System Requirements

# We will focus on the following set of requirements while designing the Library Management System:
# 1. Any library member should be able to search books by their title, author, subject category as well by the publication date.
# 2. Each book will have a unique identification number and other details including a rack number which will help to locate the book.
# 3. There could be more than one copy of a book, and library members should be able to check-out and reserve any copy. We will call each copy of a book, a book item.
# 4. The system should be able to retrieve information like who took a particular book or what are the books checked-out by a specific library member.
# 5. There should be a maximum limit on how many books a member can check-out.
# 6. The system should be able to collect fines for books returned after the due date.
# 7. Members should be able to reserve books that are not currently available.
# 8. The system should be able to send notifications whenever the reserved books become
# available, as well as when the book is not returned within the due date.
# 9. The system will be able to read barcodes from books and members’ library cards.

from abc import ABC, abstractmethod
from datetime import date, timedelta

class BookFormat:
    HARDCOVER = "HARDCOVER"
    PAPERBOOK = "PAPERBOOK"

class BookStatus:
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    LOANED = "LOANED"
    LOST = "LOST"

class ReservationStatus:
    WAITING = "WAITING"
    PENDING = "PENDING"
    CANCELED = "CANCELED"
    NONE = None

class AccountStatus:
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"

class Constant:
    MAX_NUMBER_OF_DAYS = 7 
    MAX_BOOK_ISSUED_TO_A_USER = 5

class Address:
    def __init__(self, streetAddress : str, city : str, pincode : str, state : str):
        self.streetAddress = streetAddress
        self.city = city
        self.pincode = pincode
        self.state = state
        
class Person:
    def __init__(self, name: str, address : Address, email : str, phoneNo : str):
        self.name = name 
        self.address = address
        self.phoneNo = phoneNo
        self.email = email

class Account(ABC):
    def __init__(self, id : str, status : AccountStatus, password : str, person : Person):
        self.id = id
        self.password = password
        self.status = status
        self.person = person

    def resetPassword(self):
        pass 

class Librarian(Account):
    def addBookItem(self, bookItem):
        pass 
    def deleteMember(self, member):
        pass
    def unblockMember(self, member):
        pass

    def resetPassword(self, newPassoword : str):
        self.password = newPassoword
        show_info(f"Password for account {self.id} has been reset.")

class Member(Account):
    def __init__(self, id: str, password: str, status: AccountStatus, person: Person, date_of_membership: date):
        super().__init__(id, password, status, person)
        self.date_of_membership = date_of_membership
        self.total_books_checked_out = 0

    def checkout_book_item(self, book_item):
        if self.total_books_checked_out >= Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            show_error("The user has already checked out the maximum number of books.")
            return False
        if book_item.checkout(self.id):
            self.total_books_checked_out += 1
            return True
        return False

    def return_book_item(self, book_item):
        if book_item.return_book():
            self.total_books_checked_out -= 1

    def get_total_checked_out_books(self):
        pass

    def reserve_book_item(self, book_item):
        pass

    def return_book_item(self, book_item):
        pass

    def renew_book_item(self, book_item):
        pass

class BookReservation:
    def __init__(self, creation_date: date, status: ReservationStatus, book_item_barcode: str, member_id: str):
        self.creation_date = creation_date
        self.status = status
        self.book_item_barcode = book_item_barcode
        self.member_id = member_id

    @staticmethod
    def fetch_reservation_details(barcode: str):
        pass

class BookLending:
    def __init__(self, creation_date: date, due_date: date, return_date: date, book_item_barcode: str, member_id: str):
        self.creation_date = creation_date
        self.due_date = due_date
        self.return_date = return_date
        self.book_item_barcode = book_item_barcode
        self.member_id = member_id

    @staticmethod
    def lend_book(barcode: str, member_id: str):
        pass

    @staticmethod
    def fetch_lending_details(barcode: str):
        pass

class Fine:
    @staticmethod
    def collect_fine(member_id: str, days: int):
        pass

class Book(ABC):
    def __init__(self, ISBN: str, title: str, subject: str, publisher: str, language: str, number_of_pages: int, authors: List[str]):
        self.ISBN = ISBN
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.language = language
        self.number_of_pages = number_of_pages
        self.authors = authors

class BookItem(Book):
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pages, authors, barcode, is_reference_only, price, format, status, date_of_purchase, publication_date, placed_at):
        super().__init__(ISBN, title, subject, publisher, language, number_of_pages, authors)
        self.barcode = barcode
        self.is_reference_only = is_reference_only
        self.borrowed = None  # Initially, the book is not borrowed
        self.due_date = None
        self.price = price
        self.format = format
        self.status = status
        self.date_of_purchase = date_of_purchase
        self.publication_date = publication_date
        self.placed_at = placed_at

    def checkout(self, member_id):
        if self.is_reference_only:
            show_error("This book is Reference only and can't be issued.")
            return False
        if self.status == BookStatus.LOANED:
            show_error("This book is already loaned.")
            return False
        self.status = BookStatus.LOANED
        self.borrowed = date.today()
        self.due_date = date.today() + timedelta(days=Constant.MAX_NUMBER_OF_DAYS)
        show_info(f"Book {self.title} checked out to member {member_id}. Due date is {self.due_date}.")
        return True

    def return_book(self):
        self.status = BookStatus.AVAILABLE
        self.borrowed = None
        self.due_date = None
        show_info(f"Book {self.title} returned.")

class Rack:
    def __init__(self, number: int, location_identifier: str):
        self.number = number
        self.location_identifier = location_identifier

class Search(ABC):
    @abstractmethod
    def search_by_title(self, title: str):
        pass

    @abstractmethod
    def search_by_author(self, author: str):
        pass

    @abstractmethod
    def search_by_pub_date(self, publish_date: date):
        pass

class Catalog(Search):
    def __init__(self):
        self.book_titles: Dict[str, List[Book]] = {}
        self.book_authors: Dict[str, List[Book]] = {}
        self.book_subjects: Dict[str, List[Book]] = {}
        self.book_publication_dates: Dict[str, List[Book]] = {}

    def add_book(self, book):
        if book.title in self.books_by_title:
            self.books_by_title[book.title].append(book)
        else:
            self.books_by_title[book.title] = [book]
        show_info(f"Book {book.title} added to the catalog.")

    def search_by_title(self, query: str):
        return self.books_by_title.get(query, [])

    def search_by_author(self, query: str):
        pass

def show_error(message):
    print(f"Error: {message}")

def show_info(message):
    print(f"Info: {message}")

# Setup
catalog = Catalog()
book1 = BookItem("123-456", "Python Programming", "Programming", "Publisher A", "English", 500, ["Author A"], "001", False, 20.00, BookFormat.PAPERBACK, BookStatus.AVAILABLE, date.today(), date(2020, 5, 20), None)
catalog.add_book(book1)

# Search and checkout
books = catalog.search_by_title("Python Programming")
if books:
    member = Member("001", "password123", AccountStatus.ACTIVE, Person("John Doe", Address("123 Main St", "City", "State", "12345", "Country"), "john.doe@example.com", "123-456-7890"), date.today())
    member.checkout_book_item(books[0])
    # Assume return after some days
    member.return_book_item(books[0])









