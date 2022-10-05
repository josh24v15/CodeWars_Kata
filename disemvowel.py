def disemvowel(string_):
    string_= string_.replace('a', '')
    string_= string_.replace('e', '')
    string_= string_.replace('i', '')
    string_= string_.replace('o', '')
    string_= string_.replace('u', '')

    #above needs to be repeated for capitals.
    return string_


replaced = disemvowel("This is a test String")
print(replaced)