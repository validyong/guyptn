import random
x = 5
y = "paka"
s2 = "gai"

a, bb, ccc = 22, "unira", 'ddcong'

print(x)
print(y)
print(s2)


print(a)
print(bb)
print(ccc)


print(type(x))
print(type(y))

# COmmentary comment DUDDDEeeeEEEEEE

a = """
fksd
super unira brothers
???
"""
print(a)


x = memoryview(bytes(5))

# display x:
print(x)

# display the data type of x:
print(type(x))


x = 3
y = 1j
z = x + y
ao = 0j

print(x)
print(y)
print(z)
print(ao)

print(type(x))
print(type(y))
print(type(z))
print(type(ao))


print(random.randrange(114, 514))

x = "Hello World"
print(
    len(x)
)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

i = 0


def tri_recursion(k):
    global i
    print('i: ' + str(i))
    print('k: ' + str(k))
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    print('result: ' + str(result))
    i = i+1
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

print('i: ' + str(i))

"""
x = lambda a: a + 10
print(x(5))
"""


def x(a): return a + 10


def fn(arg): return arg * 555


print(fn(3))


print(x(5))

# This is not converted to a 'def' function by PEP8


def myfunc(n):
    return lambda a: a * n

# ゼノ発作
