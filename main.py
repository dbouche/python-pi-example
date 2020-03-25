#!/usr/bin/python3
import random

#I would think comments are made using the pound sign
#The following command prints the message
def main(msg):
    print(msg)

main("Hello People")
if (random.randint(1,1001)%2==1):
    print("Odd")
else:
    print("Pair")
