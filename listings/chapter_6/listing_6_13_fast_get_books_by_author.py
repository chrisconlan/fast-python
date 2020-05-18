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