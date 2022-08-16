import random
from urllib import response

response=input("enter y to roll again or n to exit ")

while response=="y":
    no=random.randint(1,6)
    print(no)