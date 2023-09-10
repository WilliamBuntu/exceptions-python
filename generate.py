import random, statistics

number = random.randint(1, 10)
choice = random.choice(['a', 'b', 'c'])
mean = statistics.mean([100, 67, 75])
mode = statistics.mode ([100, 67, 75])
median = statistics.median([100, 67, 75])
cards = ['jack', 'queen', 'spades', '5']
random.shuffle(cards)

for card in cards :
    print(card)

print(number)
print(choice)
print(mean, mode , median)


