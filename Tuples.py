#tuple, we use normal brackets
friends = ("Reagan", "Roy", "Henry")
print(friends)

#accessing a tuple item
print(friends[1])

#changing tuple values
friends = ("Reagan", "Roy", "Henry")
y_friends = list(friends)
y_friends[0] = "Poet Rea"
friends = tuple(y_friends)
print(friends)

#adding tuple items
friends = ("Reagan", "Roy", "Henry")
x_friends = list(friends)
x_friends.append("Ann")
friends = tuple(x_friends)
print(friends)

#removing tuple items
subjects = ("Mathematics", "Chemestry", "Physics")
x_subjects = list(subjects)
x_subjects.remove("Physics")
subjects = tuple(x_subjects)
print(subjects)

#adding a tuple item
beverage = ("Tea", "Coffee", "cocoa")
x_beverage = list(beverage)
x_beverage.append("Nescafe")
beverage = tuple(x_beverage)
print(beverage[2])

