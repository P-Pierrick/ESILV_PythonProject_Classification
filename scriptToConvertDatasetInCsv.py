def getActivityName(activity):
    returnValue = "ERROR"

    if activity == 1:
        returnValue = "WALKING"
    elif activity == 2:
        returnValue = "WALKING_UPSTAIRS"
    elif activity == 3:
        returnValue = "WALKING_DOWNSTAIRS"
    elif activity == 4:
        returnValue = "SITTING"
    elif activity == 5:
        returnValue = "STANDING"
    elif activity == 6:
        returnValue = "LAYING"
    elif activity == 7:
        returnValue = "STAND_TO_SIT"
    elif activity == 8:
        returnValue = "SIT_TO_STAND"
    elif activity == 9:
        returnValue = "SIT_TO_LIE"
    elif activity == 10:
        returnValue = "LIE_TO_SIT"
    elif activity == 11:
        returnValue = "STAND_TO_LIE"
    elif activity == 12:
        returnValue = "LIE_TO_STAND"

    return returnValue


pathDatasetDirectory = "HAPT Data Set"
pathFeaturesFile = pathDatasetDirectory + "/features.txt"

index = 0

while index < 2:

    if index == 0:
        pathDatasetFile = pathDatasetDirectory + "/Train/X_train.txt"
        pathNewCsv = "ouputScripts/train.csv"

        pathSubjectID = pathDatasetDirectory + "/Train/subject_id_train.txt"
        pathActivityFile = pathDatasetDirectory + "/Train/y_train.txt"

    elif index == 1:
        pathDatasetFile = pathDatasetDirectory + "/Test/X_test.txt"
        pathNewCsv = "ouputScripts/test.csv"

        pathSubjectID = pathDatasetDirectory + "/Test/subject_id_test.txt"
        pathActivityFile = pathDatasetDirectory + "/Test/y_test.txt"

    # first get all lines from file
    with open(pathSubjectID, 'r') as f:
        linesSubjectID = f.readlines()

    # first get all lines from file
    with open(pathActivityFile, 'r') as f:
        linesActivities = f.readlines()

    # first get all lines from file
    with open(pathFeaturesFile, 'r') as f:
        linesFeatures = f.readlines()

    featuresLineToWrite = ""

    for line in linesFeatures:
        lineWithoutSpace = line.strip()
        featuresLineToWrite = featuresLineToWrite + "\"" + lineWithoutSpace.rstrip('\n') + "\"" + ','

    featuresLineToWrite = featuresLineToWrite + "\"subject\",\"Activity\""

    with open(pathDatasetFile, 'r') as istr:
        with open(pathNewCsv, 'w') as ostr:

            index2 = 0

            print(featuresLineToWrite, file=ostr)

            for line in istr:
                activityNumber = linesActivities[index2].rstrip('\n')
                activityName = getActivityName(int(activityNumber))

                subjectNumber = linesSubjectID[index2].rstrip('\n')
                line = line.rstrip('\n') + ",\"" + str(subjectNumber) + "\"" + ",\"" + activityName + "\""
                index2 = index2 + 1
                print(line, file=ostr)

    # first get all lines from file
    with open(pathNewCsv, 'r') as f:
        lines = f.readlines()

    # remove spaces
    lines = [line.replace(' ', ',') for line in lines]

    # finally, write lines in the file
    with open(pathNewCsv, 'w') as f:
        f.writelines(lines)

    index = index + 1
