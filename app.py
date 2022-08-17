# HENKILÖTIETOJEN KYSELY JA TARKISTUS
# -----------------------------------

# KIRJASTOJEN JA MODULIEN LATAUS

# Module from checking finnish socia security numbers
import finssn # Module for checking

# LUOKKAMÄÄRITYKSET

class Person:
    """Properties of a client and a method
    for cheking the finnish social security number"""
    def __init__(self, firstName, lastName, ssNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.ssNumber = ssNumber
    
# MAIN LOOP
while True:
    stopLoop = ''
    # Ask for user input and store answers to variables
    givenName = input('What is your first name? ')
    surname = input('And what is your surname? ')
    ssn =  input('Lastly, what is your social security number? ')
    stopLoop = input('Do you want to continue, press Q').upper()

    # Create an object from the Person class
    person1 = Person(givenName, surname, ssn)
    century = finssn.centuryCode(person1.ssNumber)

    print('Your first name is', person1.firstName, 'and you have born in the', century)

    if stopLoop =='Q':
        break