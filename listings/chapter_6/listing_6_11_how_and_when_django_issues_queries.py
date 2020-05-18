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

###

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