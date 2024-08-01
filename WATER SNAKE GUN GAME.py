import random
import pandas as pd
comp=random.randint(0,2)
user=int(input("Enter 0 for snake, 1 for water and 2 for gun"))
def checking(comp,user):
    if (comp==user):
        return 0
    if (comp==0 and user ==1):
        return -1
    if (comp==1 and user==2):
        return -1
    if (comp==2 and user==2):
        return -1
    return 1
score=checking(comp,user)
print("You:",user)
print("Computer:",comp)
if (score==0):
    print("Draw!")
elif (score==-1):
    print("loss!")
else:
    print("Won!")
    
