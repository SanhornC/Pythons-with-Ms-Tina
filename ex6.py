types_of_people = 10
x = f"There are {types_of_people} types of people."
# there are 10 types of people
# f"" is similar to str.format
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print x and y
print(x)
print(y)

# print the following sentences (formated)
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
# w + e means you add two strings together
