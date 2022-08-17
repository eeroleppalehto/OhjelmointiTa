# HENKILÖTIETOJEN KYSELY JA TARKISTUS
# -----------------------------------

#KIRJASTOJEN JA MODULIEN LATAUS

#LUOKKAMÄÄRITYKSET

class Person:
    """Properties of a client and a method
    for cheking the finnish social security number"""
    def __init__(self, firstName, lastName, ssNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.ssNumber = ssNumber
    
# MAIN LOOP

#Ask for user input and store answers to variables
givenName = input('What is your first name? ')
surname = input('And what is your surname? ')
ssn =  input('Lastly, what is your social security number? ')

# Create an object from the Person class
person1 = Person(givenName, surname, ssn)

print('Your first name is', person1.firstName)
print('And your last name is', person1.lastName)