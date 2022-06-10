import random

n = 0
while n < 11:
    a = random.randint(1,9)
    b = random.randint(1,9)
    guess = int(input("Question:" + str(a)+"x"+ str(b)+"="))
    answer = a*b
    n +=1
    if guess == answer:
        print("Right!")
    else:
        print("Wrong, the answer is ",answer)
