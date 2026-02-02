import sys
input = sys.stdin.readline

# input
words = []
for _ in range(3):
    word = input().strip()
    words.append(word)

# Algorithm - Implementation
order = 0
for idx, word in enumerate(words):
    if word.isnumeric():
        order = idx

answer = int(words[order]) + (3-order)
if answer%3==0 and answer%5==0:
    print("FizzBuzz")
elif answer%3==0 and answer%5!=0:
    print("Fizz")
elif answer%3!=0 and answer%5==0:
    print("Buzz")
else:
    print(answer)