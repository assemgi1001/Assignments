print("Let's play a game Smart Cookie")
def question_1():
    answer = input("How much is 3+2? ")
    answer = int(answer)
    if answer == 5:
        print("Correct")
    else:
     answer = 0
     while answer != 5:
      c = input("Try again! How much is 3+2? ")
      c = int(c)
g = input("Part 1. Are you ready (Y/N)? ")
if g == "Y":
    print("Let's get started")
    question_1()
else:
    print("Good bye!")






