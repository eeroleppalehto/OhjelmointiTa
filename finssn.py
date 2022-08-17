# CHECK ROUTINES FOR FINNISH SOCIAL SECURITY NUMBER

#LIBRARIES AND MODULES

#FUNCTIONS

def centuryCode(ssNumber):
    """Extracts the century of birth from
    finnish social security number

    Args:
        ssNumber (string): a social security number

    Returns:
        int: century 1800, 1900 or 2000
    """
    

    cCode = ssnumber[6]
    codeDict = {'+' : 1800, '-':1900, 'A' : 2000}
    century = codeDict[cCode]

    return century

if __name__ == "__main__":
    ssnumber = '123456-789I'
    print('syntymävuosisata:',centuryCode(ssnumber))
