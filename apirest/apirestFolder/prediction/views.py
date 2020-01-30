from rest_framework.response import Response
from rest_framework.views import APIView

from .apps import PredictionConfig
import pandas as pd


# Class based view to predict based on IRIS model
class Human_Activity_Model_Predict(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = request.data
        keys = []
        values = []

        for key in data:
            keys.append(key)
            values.append(data[key])

        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_classifier = PredictionConfig.classifier
        y_pred = loaded_classifier.predict(X)
        response_dict = {"Predicted activity": y_pred}

        return Response(response_dict, status=200)
