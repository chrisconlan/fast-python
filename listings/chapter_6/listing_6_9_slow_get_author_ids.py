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