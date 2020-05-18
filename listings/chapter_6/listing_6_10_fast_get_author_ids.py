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