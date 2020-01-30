input_CsvDataPath = "ouputScripts/test.csv"
output_JsonDataPath = "ouputScripts/jsonActivityDataReprensentation.txt"
activityDataLine = 2595

# Ouvrir le fichier en lecture seule
CsvFile = open(input_CsvDataPath, "r")

# utiliser readlines pour lire toutes les lignes du fichier
# La variable "lignes" est une liste contenant toutes les lignes du fichier
lines = CsvFile.readlines()
# fermez le fichier après avoir lu les lignes
CsvFile.close()

# Ouvrir le fichier en lecture seule
JsonFile = open(output_JsonDataPath, "w")

features = lines[0]
activityDataLine = lines[activityDataLine]

listFeatures = features.split(',')
listDataActivity = activityDataLine.split(',')

del listFeatures[-1]
del listFeatures[-1]

del listDataActivity[-1]
del listDataActivity[-1]

sizeListFeatures = len(listFeatures)
sizeListDataActivity = len(listDataActivity)

if sizeListFeatures == sizeListDataActivity:

    JsonFile.write('{' + '\n')

    index3 = 1

    for index, index2 in zip(listFeatures, listDataActivity):

        if index3 != sizeListFeatures:
            #JsonFile.write('      ' + index + ' : ' + index2 + ',' + '\n')
            JsonFile.write('      \"' + str(index3) + '\" : ' + index2 + ',' + '\n')

        if index3 == sizeListFeatures:
            #JsonFile.write('      ' + index + ' : ' + index2 + '\n')
            JsonFile.write('      \"' + str(index3) + '\" : ' + index2 + '\n')

        index3 += 1

    JsonFile.write('\n' + '}')
else:
    print("Error : the lists do not have the same size ")

# fermez le fichier après avoir lu les lignes
JsonFile.close()
