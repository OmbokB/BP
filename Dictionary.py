#Dictionaries are used to store data values in key:value pairs
#ordered, changable and does not allow duplicates]

scores = {"Name": "Blaire", "score": 81, "Grade": "A"}
print(scores)

#accessing an item, by having a key value in square brackets
scores = {"Name": "Blaire", "score": 81, "Grade": "A"}
x = scores["Grade"]
print(x)

#change value
scores = {"Name": "Blaire", "score": 81, "Grade": "A"}
scores["score"] = 74
print(scores)

#adding a value pair
scores = {"Name": "Blaire", "score": 81, "Grade": "A"}
scores["Course"] = "Computer Science"
scores["University"] = "Moi"
print(scores)

#removing items
scores.pop("University")
print(scores)

scores.clear()
print(scores)

units = {"COM 120": 89 , "MAT 111": 90}
units.pop("MAT 111")
print(units)
