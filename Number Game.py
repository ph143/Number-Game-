import time
import random
n=random.randint(1,100)
g=int(input("Guess the number between 1 to 100"))
while g!=n:
    if g>n:
            print("Shorter Number pls")
    elif g<n:
            print("Greater Number pls")        
    g=int(input(""))
   
if g==n:
            print("You're Correct")

            

   
