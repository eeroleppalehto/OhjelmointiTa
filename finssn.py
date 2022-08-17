# CHECK ROUTINES FOR FINNISH SOCIAL SECURITY NUMBER

#LIBRARIES AND MODULES

#FUNCTIONS

from mmap import mmap


def centuryCode(ssNumber):
    """Extracts the century of birth from
    finnish social security number

    Args:
        ssNumber (string): a social security number

    Returns:
        int: century 1800, 1900 or 2000
    """
    

    cCode = ssNumber[6]
    codeDict = {'+' : 1800, '-':1900, 'A' : 2000}
    century = codeDict[cCode]

    return century

def dateOfBirth(ssNumber):
    """Extracts date of birth from finnish social security number

    Args:
        ssNumber (String): finnish social security number

    Returns:
        String : date of birth
    """
    birthday = '1.1.1900'

    dd = ssNumber[0:2]
    mm = ssNumber[2:4]
    yy = ssNumber[4:6]
    century = str(centuryCode(ssNumber))[:2]
    
    birthday = dd + '.' + mm + '.' + century + yy

    return birthday


if __name__ == "__main__":
    ssNumber = '123456-789I'
    print('syntymävuosisata:',centuryCode(ssNumber))
    print('Syntymäpäivä:', dateOfBirth(ssNumber))
