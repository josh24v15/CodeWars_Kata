def order(sentence):
    new_sentence = sentence.split()
    ordered_string = ""
    for i in range(len(new_sentence) + 1):
        for item in new_sentence:
            if str(i) in item:
                ordered_string += item + " "       
        else:
            continue
    print(ordered_string)
    print(len(new_sentence))
    print(new_sentence)
    ordered_string



    return ordered_string.strip()

print(order("Th3is i2s a4 se1ntence."))
