# print(1 + 1)
# print("1" + "1")
# age = 23
# print("Jake is " + str(age) + " year old.")
# print("Jake is " + str(23) + " year old.")

# name = "Jack"
# age = "23"
# name_and_age = "My name is {0}. I\'m {1} years old.".format(name, age)
# print(name_and_age)

# name_and_age = "My name is {0}. I\'m {1} years old.".format("Jack", "23")
# print(name_and_age)

# name_and_age = "My name is {}. I\'m {} years old.".format(23, "Jack")
# print(name_and_age)

# week_days = "There are 7 days in a week: {5}, {0}, {3}, {1}, {2}, {4}, {6}."\
#     .format("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
# print(week_days)

# week_days = "There are 7 days in a week: {su}, {mo}, {tu}, {we}, {th}, {fr}, {sa}."\
#     .format(mo = "Monday", tu = "Tuesday", we = "Wednesday", th = "Thursday", fr = "Friday", sa = "Saturday", su ="Sunday")
# print(week_days)

# week_days = "There are 7 days in a week: {su}, {su}, {su}, {su}, {su}, {su}, {su}."\
#     .format(mo = "Monday", tu = "Tuesday", we = "Wednesday", th = "Thursday", fr = "Friday", sa = "Saturday", su ="Sunday")
# print(week_days)

# float_result = 1000 / 7
# print(float_result)
# print("The result of division is {0:1.3f}".format(float_result))
# print('''
# {0:10.2f} {1:10.2f} {2:10.2f}
# {3:10.2f} {4:10.2f} {5:10.2f}
# {6:10.2f} {7:10.2f} {8:10.2f}
# '''.format(1.45778, 345.232352, 34.2344, 1234.23,
#            1.45778, 345.232352, 34.2344, 1234.23,
#            456.43234))

name = "Jack"
age = "23"
name_and_age = "My name is {0}. I\'m {1} years old.".format(name, age)
print(name_and_age)
name_and_age = f"My name is {name}. I\'m {age} years old."
print(name_and_age)

# print("My name is %s. %s %d years old" % (name, "I'm", age)) # not working