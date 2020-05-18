# This is O(log(n)) because title is an indexed field
this_book = Book.objects.get(
    title='Fast Python'
)

# This is O(n) because subtitle is not indexed
also_this_book = Book.objects.get(
    subtitle='Re-learn the basics'
)