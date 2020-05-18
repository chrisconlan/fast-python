

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


class A(object):
    def __init__(self, value: int):
        self.value = value

    def __add__(self, another_value: int):
        accum = 0
        for _ in range(self.value):
            accum += 1
        for _ in range(another_value):
            accum += 1
        return A(accum)

a = A(3)
print((a+4).value)
# Returns 7

a = A(8)
a += 9
print(a.value)
# Returns 17


x = list()
for i in range(5):
    x += [i]
print(x)
# Returns [0, 1, 2, 3, 4]

x = list()
for i in range(5):
    x.append(i)
print(x)
# Returns [0, 1, 2, 3, 4]

