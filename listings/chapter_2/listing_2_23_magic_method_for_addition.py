class A(object):
    def __init__(self, value: int):
        self.value = value

    def __add__(self, another_value: int):
        return A(self.value + another_value)
        
a = A(3)
print((a+4).value)
# Returns 7

a = A(8)
a += 9
print(a.value)
# Returns 17