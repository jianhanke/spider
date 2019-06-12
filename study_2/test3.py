import random
word=["Dolphin","Angel","computer","hacker","information","program"]
same=word
for i in range(0,6):
	show = random.choice(same)
	print(show)
	same.remove(show)
