# CHECK ROUTINES FOR FINNISH SOCIAL SECURITY NUMBER

#LIBRARIES AND MODULES
import datetime

#FUNCTIONS

from datetime import date
from mmap import mmap
from re import A


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
    dd = int(ssNumber[0:2])
    mm = int(ssNumber[2:4])
    yy = int(ssNumber[4:6])

    # Call function centuryCode() to determine birth century
    century = centuryCode(ssNumber)
    yyyy = century + yy
    
    # birthday = dd + '.' + mm + '.' + century + yy

    # Convert to date

    birthday = datetime.datetime(yyyy, mm, dd)

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


def testSsn(ssNumber):
    # Tarkistettava numero
    checkNumberStr = ssNumber[0:6] + ssNumber[7:10]
    checkNumberInt = int(checkNumberStr)

    # 
    jakoJaanos = checkNumberInt%31

    sanak = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F',
        16 : 'H',
        17 : 'J',
        18 : 'K',
        19 : 'L',
        20 : 'M',
        21 : 'N',
        22 : 'P',
        23 : 'R',
        24 : 'S',
        25 : 'T',
        26 : 'U',
        27 : 'V',
        28 : 'w',
        29 : 'X',
        30 : 'Y',
    }

    if sanak[jakoJaanos] == ssNumber[10:11]:
        return 'Henkilötunnus on validi'
    else:
        return 'Henkilötunnus ei ole validi'

def age(ssNumber):
    """Calculate age of person from finnish social security number

    Args:
        ssNumber (str): finnish social security number

    Returns:
        int : age of person
    """
    currentTime = datetime.date.today()
    birthday = dateOfBirth(ssNumber)

    age = currentTime - birthday

    return age

if __name__ == "__main__":
    ssNumber = '270392-229Y'
    # print('syntymävuosisata:',centuryCode(ssNumber))
    # print('Syntymäpäivä:', dateOfBirth(ssNumber))
    # print('Sukupuoli:', gender(ssNumber))
    print('Testi ', testSsn(ssNumber))
    print('Syntymäpäivä:', str(dateOfBirth(ssNumber))[:10])
    print('Age:', age(ssNumber))