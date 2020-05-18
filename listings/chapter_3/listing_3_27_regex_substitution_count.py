def re_subn_count(data: str, value: str) -> int:
    """
    Count the number of substitutions that value word 
    perform on data in a regex substitution
    """
    return re.subn(value, '', data)[1]