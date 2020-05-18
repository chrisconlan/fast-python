def add_two(x: float, y: float) -> float:
    """
    O(1) because is performs one addition
    """
    return x + y

def add_a_few(x: float, y: float, z: float) -> float:
    """
    O(1) because is performs 2 additions
    """
    return x + y + z

def loop_through_it(n: int) -> int:
    """
    O(n) because it performs n additions
    """
    value = 0
    for i in range(n):
        value += i
    return value

def loop_through_it_squarely(n: int) -> int:
    """
    O(n^2) because it performs 2*n^2 additions
    """
    value = 0
    for i in range(n):
        for j in range(n):
            value += i + j
    return value

def loop_through_it_twice(n: int) -> int:
    """
    O(n) because it performs 2*n additions and n 
    multiplications
    """
    value = 0
    for i in range(n):
        value += i
    for i in range(n):
        value += 2 * i
    return value