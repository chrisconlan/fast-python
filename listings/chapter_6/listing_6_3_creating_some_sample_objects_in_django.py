from bookstore.models import Author, Book

some_author = Author(name='Chris Conlan')
some_author.save()

some_book = Book(
    author=some_author,
    title='Fast Python',
    subtitle='Re-learn the basics'
)
some_book.save()