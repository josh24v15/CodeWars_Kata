def generate_hashtag(s):
    if s is "":
        return False
    s.lower()
    s.split(" ")
    result = "#"
    for word in s:
        word.capitalize()
        if word is not " ":
            result += word
    if result is not "" and len(result) <= 140:
        return result
    else:
        return False



generate_hashtag('Codewars Is Nice')
test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')

