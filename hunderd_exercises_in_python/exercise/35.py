'''

Question: Create a function that takes any string as input and 
returns the number of words for that string.



'''
s = input()
def len_of_words(s):
    s = s.split(' ')
    print(len(s))

len_of_words(s)