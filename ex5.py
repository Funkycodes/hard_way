#format strings: strings that have variables in them
# f"srandom string {variable}"  - f tells python that it should format the following string

name = 'Habib'
age = 18 # not a lie
height = 71 # inches
weight = 90
eyes = 'Black'
teeth = 'Yellow'
hair = 'raven'

print(f"Let's talk about {name}")
print(f"He is {height} inches tall")
print(f"He is {weight} lbs heavy")
print(f"Actually that's not too heavy")
print(f"He's got {hair} hair and {eyes} eyes")
print(f"His teeth are usually {teeth} depending on the coffee")

total = age + height + weight
print(f"If I add my height, my age and my weight I get {total}")