SELECT 
    "bookstore_book"."id", 
    "bookstore_book"."author_id", 
    "bookstore_book"."title", 
    "bookstore_book"."subtitle" FROM 
    
    "bookstore_book" INNER JOIN "bookstore_author" ON (
        "bookstore_book"."author_id" = 
        "bookstore_author"."id"
    ) WHERE "bookstore_author"."name" = 'Chris Conlan'
        LIMIT 21; 
        
args=('Chris Conlan',)
