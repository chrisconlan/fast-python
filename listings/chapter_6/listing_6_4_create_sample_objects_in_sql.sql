INSERT INTO "bookstore_author" 
    ("name") VALUES (
        'Chris Conlan'
    ); args=['Chris Conlan']
    
INSERT INTO "bookstore_book" 
    ("author_id", "title", "subtitle") VALUES (
        1, 
        'Fast Python', 
        'Re-learn the basics'
    ); args=[1, 'Fast Python', 'Re-learn the basics']