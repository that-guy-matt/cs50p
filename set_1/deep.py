answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
# the requirements did not state that this must be checked as an integer
# and no arithmetic is performed, so it is checking as a string.
if answer .strip() == '42':
    print("Yes")
elif answer.lower().strip() in ["forty-two", "fortytwo", "forty two"]:
    print("Yes")
else:
    print("No")