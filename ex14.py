from sys import argv

script, username = argv
prompt = '$ '

print(f"Hi {username}, I'm the {script} script")
print("I'd like to ask you a few question")
print(f"Do you like me {username}")
likes = input(prompt)

print("Where do you live {}?".format(username))
lives = input(prompt)

print("What type of computer do you use")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. You live in {lives}. Not sure where that is. And you have a {computer} computer. Nice""")
