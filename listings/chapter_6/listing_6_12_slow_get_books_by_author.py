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