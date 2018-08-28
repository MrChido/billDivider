import math

def splitCheck(total,partySize):
    if partySize <=1:
        raise ValueError("Not enough people. Go grab that hobo you saw down the street a moment ago.")
    cpp= math.ceil(total / partySize)
    return cpp

try:
    totalDue= float(input("What did the end amount come to? "))
    crewSize= float(input("how many people attended? "))
    amountDue = splitCheck(totalDue,crewSize)
except ValueError as err:
    print("Incorrect value, please try again.")
    print("({})".format(err))
else:
    print("The cost per person is:$", amountDue)