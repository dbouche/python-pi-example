#!/usr/bin/python3
import random

#No longer need coments
def main(msg):
    print(msg)

def secondary():
    print("New function")

main("Hello People")
if (random.randint(1,1001)%2==1):
    print("Odd")
else:
    print("Pair")
