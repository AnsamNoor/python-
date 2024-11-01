#** What is 7 to the power of 4?**

import math

print(math.pow(7, 4))
# ---------------------------------
#** What is the main difference between a tuple and a list? **

# Tuple is immutable
# ---------------------------------
#** Split this string:**

s = "Hi there Sam!"
news = s.split()
print(news)
# ----------------------------------
#** Use .format() to print the following string: **

planet = "Earth"
diameter = 12742
text = 'The diameter of {0} is {1}  kilometers.'.format(planet, diameter);
print(text)
# --------------------------------------
#* Given this nested list, use indexing to grab the word "hello" **

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])
# --------------------------------------
#** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
for i in d.values():

    for j in i[3].values():

        for z in j[3].values():
            print(z[3])
# --------------------------------------
#** Create a function that grabs the email website domain from a string in the form: **

import tldextract

url = "ansam@gmail.com"

extracted = tldextract.extract(url)
main_domain = f"{extracted.domain}.{extracted.suffix}"

print(main_domain)  # Output: example.com
# -------------------------------------
#** Create a basic function that returns True if the word 'dog' is contained in the input string

text = 'Is there a dog here?'

newtext = text.split()
print(newtext)
for i in newtext:
    if i == 'dog':
        print('yes')
# -------------------------------------
#** Create a function that counts the number of times the word "dog" occurs in a string.

strg = 'This dog runs faster than the other dog dude!'
newstrg = strg.split();
print(newstrg.count('dog'))
# -------------------------------------
#** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.
# For example:**

seq = ['soup', 'dog', 'salad', 'cat', 'great']

newseq = filter(lambda i: i[0] == 's', seq)

# Print the filtered result
for word in newseq:
    print(word)
# -------------------------------------
"""You are driving a little too fast, and a police officer stops you.
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
If your speed is 60 or less, the result is "No Ticket".
If speed is between 61 and 80 inclusive, the result is "Small Ticket".
If speed is 81 or more, the result is "Big Ticket".
Unless it is your birthday
(encoded as a boolean value in the parameters of the function) -- on your
birthday, your speed can be 5 higher in all cases. """



def check_speed(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return print("No Ticket")
    elif 61 <= speed <= 80:
        return print("Small Ticket")
    else:
        return print("Big Ticket")

