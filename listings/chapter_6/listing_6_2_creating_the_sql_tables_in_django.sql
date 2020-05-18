CREATE TABLE "bookstore_author" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "name" varchar(254) NOT NULL UNIQUE
); args=None

CREATE TABLE "bookstore_book" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "title" varchar(254) NOT NULL, 
    "subtitle" varchar(254) NOT NULL, 
    "author_id" integer NOT NULL REFERENCES 
    "bookstore_author" ("id") DEFERRABLE INITIALLY DEFERRED
); args=None

CREATE INDEX "bookstore_book_title_40d52b28" ON 
    "bookstore_book" ("title"); args=()
    
CREATE INDEX "bookstore_book_author_id_c8c6315b" ON 
    "bookstore_book" ("author_id"); args=()