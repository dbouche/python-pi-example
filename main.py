#!/usr/bin/python3
import random

def main(msg):
    print(msg)

main("Hello People")
if (random.randint(1,1001)%2==1):
    print("Odd")
else:
    print("Pair")
