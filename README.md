#  Smartphone-Based Recognition of Human Activities and Postural Transitions Data Set

	Dataset : https://archive.ics.uci.edu/ml/datasets/Smartphone-Based+Recognition+of+Human+Activities+and+Postural+Transitions
	
	Operating system used : Ubuntu 18.04.3 LTS

## scriptToConvertDatasetInCsv.py :

	This python script converts the original dataset into a much easier to use .csv file.
	The file will be generated in the project directory "outputScripts"

## scriptToCreateActivityJsonRepresentation.py : 

	This script python converts a line from the csv file (one line corresponds to a participant's activity) into a json format. This json will allow to test the Rest API, it will be sent to the API to make a prediction.
	The file will be generated in the project directory "outputScripts"

## outputScripts : 

	This folder contains the output of the 2 python scripts

## ESILV_PythonProject_Classification_Smartphone-Based_Recognition_Human_Activities.ipynb :

	This file contains data analysis, it will also allow to serialise the best model found in .joblib format

## HumanActivitiesRecognition.joblib : 

	The serialised model

## apirest : 

	The Rest Django API which allows you to make predictions on data
	
	The folder contains 2 example scripts : 
	
		* curl_predict_example.sh
		* curl_predict_example2.sh

    To test the API : 

		1. Go into the django directory (apirest/apirestFolder)
		2. Start the server with the command : python3 manage.py runserver
		3. Start the example script : curl_predict_example.sh / curl_predict_example2.sh
		
	It is also possible to send a json directly from the API url http://127.0.0.1:8000/api/predict/
	
	Json can be generated with the script "scriptToCreateActivityJsonRepresentation", the var activityDataLine allows you to choose the line of the csv that you want to convert to json.
	The prediction from the Rest API can then be checked using the csv file.
	
