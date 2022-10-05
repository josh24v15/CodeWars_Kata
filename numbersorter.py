numbers = 42145
numbers = str(42145)
numberList = map(int, numbers)
numberList = list(numberList)
print(numberList)
numberList.sort()
numberList.reverse()

strings = [str(integer) for integer in numberList]
print(strings)
a_string = "".join(strings)
an_integer = int(a_string)
print(an_integer)

