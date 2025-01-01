import random
f = open("name.txt", 'r')
name = f.read().replace('\n', '')
print("happy new year " + name + "!")
g = open("greetings.txt", 'r')
greetings = g.read().split('\n')
ind = random.randint(0, len(greetings)-1)
print(greetings[ind])
