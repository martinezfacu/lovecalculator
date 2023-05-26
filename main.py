print("Welcome to the calculator of love <3")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combi_names = name1 + name2
t = combi_names.count('t')
r = combi_names.count('r')
u = combi_names.count('u')
e = combi_names.count('e')

first_digit = t + r + u + e

l = combi_names.count('l')
o = combi_names.count('o')
v = combi_names.count('v')
e = combi_names.count('e')

second_digit = l + o + v + e

final_digit = str(first_digit) + str(second_digit)

print(final_digit)

if int(final_digit) <= 10 or int(final_digit) >= 90:
    print(f"Your score is {final_digit}, you go together like coke and mentos.")
elif int(final_digit) >= 40 and int(final_digit) <= 50:
    print(f"Your score is {final_digit}, you are alright together.")
else:
    print(f"Your score is {final_digit}.")
