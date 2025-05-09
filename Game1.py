import random
print ("Welcome Player 456")
print("Enter 0 for rock"
      "enter 1 for paper"
      "enter 2 for scissors")
i= int(input("Enter your choice"))
computer = random.choice([0,1,2])
outcome = [[0,1,-1]
           ,[-1,0,1]
           ,[1,-1,0]]
if(outcome[i][computer] == 0):
    print("A draw")
elif(outcome[i][computer] == 1):
    print("You win")
else:
    print("You lose")