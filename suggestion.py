import pgModule

def suggestion(killId, portion): # TODO: arguments
    # TODO: Finish DatabaseOperations (make use of getAllRowsFromTable method and get connectionArguments)
    # shotted animals info: weight
    DatabaseOperation1 = ...

    kill = [] # TODO:
    portionDict ={
        "Kokonainen": 1,
        "Puolikas": 2,
        "Nejännes": 4
    }

    # Make VIEW in database with groupName, their meat, share multiplier use
    DatabaseOperation2 = ...
    groupsPsyco = [] # TODO:
    
    groups = []
    iD = 0 # TODO: Useless?
    for group in groupsPsyco:
        groups.append(
            {
                "groupID": iD, # TODO: Useless?
                "groupName": group[0],
                "sharedMeat": group[1],
                "shareMultiplier": group[2],
                "expectedValue": 0.0,
                "deltaSquare": 0.0
            }
        )
        iD += 1 # TODO: Useless?

    meatSharedTotal = kill.weight # FIXME: Kill not yet implemented
    multiplierTotal = 0
    for group in groups:
        meatSharedTotal += group["sharedMeat"]
        multiplierTotal += group["shareMultiplier"]
    

    # deltaGroup = []
    deltaSum = 0
    for group in groups:
        # E = TotalMeat * shareMult/TotalMult
        group["expectedValue"] = meatSharedTotal * (group["shareMultiplier"] / multiplierTotal) 
        # Relative Variance = ((E-CurrentMeat)/E)^2
        group["deltaSquare"] = pow((group["expectedValue"] - group["sharedMeat"])/group["expectedValue"], 2) 
        # deltaGroup.append(group["deltaSquare"])
        deltaSum += group["deltaSquare"]

    # TODO: loop according to portions and track data

    resultGroups = []
    i = 0
    while i < portionDict[portion]:
        tempData = suggestionCalc(portion, groupsInfo)
        groups = tempData[0]
        resultGroups.append(tempData[1])
        i += 1

    resultString = ""
    return resultString


def suggestionCalc(portion, groupsInfo): # TODO: arguments

    shareMeatVar = 0
    varianceList = []

    for group in groups:
        shareMeatVar = group["sharedMeat"] + kill.weight # FIXME: Kill not yet implemented

        varianceList.append(
            # SumDelta - ...
            deltaGroupSum - group["deltaSquare"] + pow((shareMeatVar - group["expectedValue"])/group["expectedValue"], 2)
        )
    
    minVariance = min(varianceList)
    indexGroup = 0
    i = 0

    for variance in varianceList:
        if variance == minVariance:
            indexGroup = i
            # break
        i += 1
    
    groups[indexGroup]["sharedMeat"] += kill.weight # FIXME: Kill not yet implemented

    resultList = [
        groups,
        groups[indexGroup]["groupName"] 
    ]
    
    return resultList


# TODO: Make test data and test the algorithm for consistency
# TODO: Button + DialogueWindow to add suggested share to database

if __name__ == "__main__":
    pass