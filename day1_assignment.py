# assignement 1
def get_profile():
    return {
        "name": "Asif Shaikh",
        "age": 25,
        "skills": ["Python", "Git", "AI/ML"]
    }
profile = get_profile()
print("Hi, I'm", profile["name"])
print("Skills:", ", ".join(profile["skills"]))

# assignment 2
# ask for user input
name = input("What is your name? ")
goal = input("What is your AI/ML goal? ")

print(f"Hi {name}! Let's achieve your goal: {goal}")