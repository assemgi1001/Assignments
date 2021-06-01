# using def we created a function which name is make_a_sandwich
# functions prevents the code bloat(duplicate code)
def make_a_sandwich():
    jelly = input("What flavor of the jelly do you prefer? ")
    butter = input("What kind of butter do you prefer? ")
    print("Thanks for order. It will be ready in 10 minutes")
    print('Toasting two slices of bread...')
    print("Spreading on the toast the " + butter)
    print("Onto the other slice of bread we are spreading " + butter)
    print("Press to slices of bread together")
    print("Finished! There is your " + butter + " and " + jelly + " sandwich!")
# we can reuse this function any time we need it
print("Welcome to our Best_Sandwiches_SanDiego")
another = "Y"
while another == "Y":
    make_a_sandwich()
    another = input("How about another (Y/N)? ")
# we can give a parameter to our function. In this code we do not have any parameter
# stack is where all variables are stored
# stack frame is where all variables within the function are stored.
# Jelly/Butter our local variables which are stored in the stack frame
