print("Let's play a game Smart Cookie")
g = input("Part 1. Are you ready (Y/N)? ")
if g == "Y":
    print("Let's get started")
else:
    print("Good bye!")
answer = 0
while answer != 5:
 c = input("How much is 3+2? ")
 answer = int(c)
 if answer == 5:
    print("Correct")
    answer = 0
    while answer != 7:
            c = input("How much is 4+3? ")
            answer = int(c)
            if answer == 7:
                print("Correct")
                answer = 0
                while answer != 9:
                    c = input("How much is 6+3? ")
                    answer = int(c)
                    if answer == 9:
                      print("Correct! Let's move to Part2")
                      answer = 0
                      while answer != 9:
                          c = input("Enter the correct answer: 2+3+4 ")
                          answer = int(c)
                          if answer == 9:
                              print("Correct")
                              answer = 0
                              while answer != 10:
                                  c = input("Enter the correct answer: 1+5+4 ")
                                  answer = int(c)
                                  if answer == 10:
                                      print("Correct")
                                      print("you win!")
                                      break

g

