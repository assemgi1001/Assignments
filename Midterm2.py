print("Let's play a game Smart Cookie")
def Game_over():
    print("Game Over!")
def Question(question, response, message):
    answer = input(question)
    answer = int(answer)
    if answer == response:
        print("Correct")
        print(message)
        return answer
    else:
        #answer = 0
        #while answer != response:
        return Question("Try again! " + question, response, message)

# def question_3():
#     answer = input("How much is 5+5? ")
#     answer = int(answer)
#     if answer == 10:
#         print("Correct")
#         print("You are a Smart Cookie!")
#         Game_over()
#     else:
#      answer = 0
#      while answer != 10:
#        c = input("Try again! How much is 5+5? ")
#        c = int(c)
#        if answer == 10:
#           print("Now is correct!")
#           print("You are a Smart Cookie!")
#           Game_over()
# def question_2():
#     answer = input("How much is 4+3? ")
#     answer = int(answer)
#     if answer == 7:
#         print("Correct")
#         question_3()
#     else:
#      answer = 0
#      while answer != 7:
#       c = input("Try again! How much is 4+3? ")
#       c = int(c)
#       if answer == 7:
#           print("Now is correct!")
#           question_3()
# def question_1():
#     answer = input("How much is 3+2? ")
#     answer = int(answer)
#     if answer == 5:
#         print("Correct")
#         question_2()
#     else:
#      answer = 0
#      while answer != 5:
#       c = input("Try again! How much is 3+2? ")
#       c = int(c)
#       if c == 5:
#           print("Now is correct!")
#          question_2()
g = input("Part 1. Are you ready (Y/N)? ")
if g == "Y":
    print("Let's get started")
    Countofquestions = 0
    if Question("How much is 3+2?", 5, "Now is correct!"):
        Countofquestions += 1
    if Question("How much is 4+3?", 7, "Now is corr(ect!"):
        Countofquestions += 1
    Question("How much is 5+5?", 10, "Correct!")
    Question("How much is 1-1?", 0, "Correct!")
    If Countofquestions > 3:
        print("You are smart cookie!")
    Game_over()
else:
    print("Good bye!")






