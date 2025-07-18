# List - ordered, mutable, allows duplicates
fruits = ["apple", "banana", "mango"]

print(fruits[1])  # Output: banana
fruits.append("grapes")  # Add
fruits.remove("banana") 

for fruit in fruits:
    print("Fruit :",fruit)
    
# Tuple - ordered, immutable, allows duplicates
point = (3, 4)

x, y = point  # tuple unpacking
print("X:", x, "Y:", y)

# Set - unordered, unique items
languages = {"Python", "Java", "C++", "Python"}  # "Python" appears once

languages.add("Go")
print(languages)

# Dict - key-value pairs, fast lookup
profile = {
    "name": "Asif",
    "age": 25,
    "skills": ["Python", "Git"]
}

print(profile["skills"])
profile["city"] = "Mumbai"
print("profile >>>",profile)


# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print("squares list comprehension >>>>",squares)

# Dict comprehension
squared_dict = {x: x**2 for x in range(5)}
print("squares dict comprehension >>>>",squared_dict)

# Set comprehension
even_set = {x for x in range(10) if x % 2 == 0}
print("even set comprehension >>>>",even_set)


# real time use case in ML/AI 
# Suppose you got a list of model accuracies
accuracies = [0.83, 0.91, 0.88, 0.76]

# Get only those > 0.85
high_scores = [acc for acc in accuracies if acc > 0.85]
print("High scores:", high_scores)