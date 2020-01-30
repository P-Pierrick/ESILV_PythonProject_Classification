from django.apps import AppConfig
from joblib import load
import os

class PredictionConfig(AppConfig):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #CLASSIFIER_FOLDER = Path("classifier")
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'prediction/classifier/')
    #CLASSIFIER_FILE = CLASSIFIER_FOLDER / "HumanActivitiesRecognition.joblib"
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "HumanActivitiesRecognition.joblib")
    classifier = load(CLASSIFIER_FILE)
