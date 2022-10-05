def duplicate(sentence):
    sentence = sentence.lower()
    duples = []
    for letter in sentence:
        if sentence.count(letter) > 1 and letter not in duples:
            duples.append(letter)
        else:
            continue
    print(duples)
    new_string = ""
    for letter in sentence:
        if letter in duples:
            new_string += ')'
        else:
            new_string += '('
    print(new_string)
duplicate("abcdefghijklmnopqrstuvwxyzAB")
duplicate("This is a string that I'm typing")
duplicate("din")
duplicate("recede")
duplicate("Success")
duplicate("(( @")