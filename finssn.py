# CHECK ROUTINES FOR FINNISH SOCIAL SECURITY NUMBER

#LIBRARIES AND MODULES
import datetime

#FUNCTIONS

from datetime import date
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
        date : date of birth
    """
    birthday = '1.1.1900'

    # Extract date of birth from ssNumber string
    dd = ssNumber[0:2]
    mm = ssNumber[2:4]
    yy = ssNumber[4:6]

    # Call function centuryCode() to determine birth century
    century = str(centuryCode(ssNumber))[:2]
    
    birthday = dd + '.' + mm + '.' + century + yy

    # Convert to date

    # birthday = date(int(birthday[6:]), int(birthday[3:5], int(birthday[0:2])))
    # birthday = date......
    # TODO: Add datetime library and convert to datetime

    return birthday

def gender(ssNumber):
    """Determines the gender assigned at birth to person from finnish social security number

    Args:
        ssNumber (String): finnish social security number

    Returns:
        String : gender assigned at birth
    """
    gender = ''
    endCredential = int(ssNumber[7:10])
    remainderSsn = endCredential%2

    if remainderSsn == 0:
        gender = 'Nainen'
    else:
        gender = 'Mies'
    
    return gender


def testssss(self, arg):
    pass

if __name__ == "__main__":
    ssNumber = '123456-789I'
    print('syntymävuosisata:',centuryCode(ssNumber))
    print('Syntymäpäivä:', dateOfBirth(ssNumber))
    print('Sukupuoli:', gender(ssNumber))
