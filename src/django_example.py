"""
Sample code for the Django section. This code is not meant 
to be run independently of a Django project, and is just 
for expositional purposes.
"""


# Setting up some models
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=254, unique=True)


class Book(models.Model):
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=254, db_index=True)
    subtitle = models.CharField(max_length=254)


# Executes the following sql
"""
CREATE TABLE "bookstore_author" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(254) NOT NULL UNIQUE); args=None

CREATE TABLE "bookstore_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(254) NOT NULL, "subtitle" varchar(254) NOT NULL, "author_id" integer NOT NULL REFERENCES "bookstore_author" ("id") DEFERRABLE INITIALLY DEFERRED); args=None

CREATE INDEX "bookstore_book_title_40d52b28" ON "bookstore_book" ("title"); args=()
CREATE INDEX "bookstore_book_author_id_c8c6315b" ON "bookstore_book" ("author_id"); args=()

"""



# Creating some objects
some_author = Author(name='Chris Conlan')
some_author.save()

some_book = Book(
    author=some_author,
    title='Fast Python',
    subtitle='Re-learn the basics'
)
some_book.save()


# Querying the objects
my_books = Book.objects.filter(author__name='Chris Conlan')

for book in my_books:
    print(f'{book.title} by {book.author.name}')



# Authors by name
author_names = [
    'Chris Conlan',
    'William Shakespeare',
    'Edgar Allen Poe',
    ...
]


def slow_get_author_ids(names: List[str]) -> List[int]:
    """
    Given a list of author names, return a list of their 
    database ids (primary key values). This is O(n) because 
    it performs n SQL queries
    """
    author_ids = list()
    for name in names:
        # This results in a single query
        author = Author.objects.get(name=name)
        author_ids.append(author.id)
    return author_ids


def fast_get_author_ids(names: List[str]) -> List[int]:
    """
    Given a list of author names, return a list of their 
    database ids (primary key values). This is O(1) because 
    it performs 1 SQL query
    """
    author_ids = Author.objects\
        .filter(name__in=names)\
        .values_list('id', flat=True)
    return list(author_ids)



# 1 SELECT query on the book table
some_book = Book.objects.get(title='Fast Python')

# No queries
print(some_book.title)

# No queries
print(some_book.author_id)

# 1 SELECT query on the author table
print(some_book.author.id)

# No queries, because author is now cached
print(some_book.author.name)


# 1 JOIN query on books and authors
another_book = Book.objects\
    .filter(title='Faster Python')\
    .select_related('author')\
    .get()

# No queries for any of these
print(another_book.title)
print(another_book.author_id)
print(another_book.author.id)
print(another_book.author.name)

def slow_get_books_by_author() -> Dict[str, List[Book]]:
    """
    Organize all books in the database into a dictionary 
    where the books are stored in a list identified by their
    author's name. This requires n+1 queries for n rows
    in the books table.
    """
    # This queries just the books table
    books = Book.objects.all()
    books_by_author = dict()
    for book in books:
        # This results in a query on the author table
        name = book.author.name
        if not name in books_by_author:
            books_by_author[name] = list()
        books_by_author[name].append(book)
    return books_by_author

def fast_get_books_by_author() -> Dict[str, List[Book]]:
    """
    Organize all books in the database into a dictionary 
    where the books are stored in a list identified by their
    author's name. This requires 1 JOIN query for n rows
    in the books table.
    """
    # This queries books and authors tables simultaneously
    books = Book.objects.all().select_related('author')
    books_by_author = dict()
    for book in books:
        # This does not require a query
        name = book.author.name
        if not name in books_by_author:
            books_by_author[name] = list()
        books_by_author[name].append(book)
    return books_by_author

