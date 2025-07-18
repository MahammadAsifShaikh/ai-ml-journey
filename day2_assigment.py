# Convert this list into a dict with square values
# assignment 1
nums = [1, 2, 3, 4]
square_dict = {num:num**2 for num in nums}
print("square_dict >>>",square_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16}


# Count the number of times each word appears
# assignment 1
words = ["ml", "ai", "ml", "data", "ai"]
occurrences = {}
for item in words:
    occurrences[item] = occurrences.get(item, 0) + 1
print("occurrences>>>>>",occurrences)
# Output: {'ml': 2, 'ai': 2, 'data': 1}

# Create a dict for a student: name, age, skills (list)
# Print each key and value nicely
# assignment 3
# Create the student dictionary
student = {
    "name": "Alice Smith",
    "age": 20,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Print each key and value nicely
print("Student Details:")
for key, value in student.items():
    print(f"{key.replace('_', ' ').title()}: {value}")