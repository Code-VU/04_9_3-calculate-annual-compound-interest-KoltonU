def calculateCompoundInterest():
    compoundinterest()
    print("---")
    compoundinterest()
    print("---")
    compoundinterest()

def compoundinterest():
    client_principal = float(input("Principle (amount): "))
    client_time = float(input("Time:               "))
    client_rate = float(input("Rate:               "))
    total_amount = client_principal * ((1 + (client_rate / 100)) ** client_time)
    compInterest = (total_amount - client_principal)
    print("Compound Interest: "+ str(round(compInterest,2)))




#print("Compound Interest: "+str(intrest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
