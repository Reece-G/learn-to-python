#define function count: counts number of X (user defined by variable search) in a string
def count(word, search):
    count = 0
    for letter in word:
        if letter == search:
            count = count + 1
    return(count)

#asks for input and desired search and runs the count function printing the output.
word = input('Enter a word: ')
search = input('What are you searching for? ')
output = count(word, search)
print(output)
