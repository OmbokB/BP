#set
#Items in a set are unordered
#we use curly brackets
months = {"January", "February", "March", "April"}
print(months)

#accessing an item
months = {"January","February", "March", "April"}
for x in months:
    print(x)
print("March" in months)

#adding and removing item from a set
course_code = {"COM", "MAT", "COM 121"}
course_code.add("MAT 111")
print(course_code)
course_code.remove("COM")
print(course_code)

