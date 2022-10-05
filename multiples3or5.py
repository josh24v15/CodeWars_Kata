"""Multiples of 3 or 5 Kata

def solution(number):
    if number < 0:
        return 0
    else:
        multiples = []
        i = 1
        j = 1
        total = 0
        while (i * 3) < number:
            multiples.append(i*3)
            i += 1
        while (j * 5) < number:
            if (j * 5) not in multiples:
                multiples.append(j*5)
            j += 1
        for number in multiples:
            total += number
        return total
"""

def solution(number):
    if number < 0:
        return 0
    else:
        multiples = []
        total = 0
        for three in range(3, number, 3):
            multiples.append(three)
        for five in range(5, number, 5):
            if five not in multiples:
                multiples.append(five)
        for number in multiples:
            total += number
        return total

def solution(number):
    if number < 0:
        return 0
    else:
        total = 0
        multiples = [x for x in range(3, number, 3)]
        for five in range(5, number, 5):
            if five not in multiples:
                multiples.append(five)
        for number in multiples:
            total += number
        return total




for three in range(3, 27, 3):
    print(three)


