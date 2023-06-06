from google.cloud import storage
from dotenv import load_dotenv
import joblib
from io import BytesIO
import os


def load_model():
    load_dotenv()
    storage_client = storage.Client()
    bucket_name = os.environ.get("BUCKET_NAME")
    model_bucket = os.environ.get("MODEL_BUCKET")

    model_local = 'local_model.pkl'
    bucket = storage_client.get_bucket(bucket_name)
    #select bucket file
    blob = bucket.blob(model_bucket)
    #download blob into an in-memory file object
    model_file = BytesIO()
    blob.download_to_filename(model_local)
    #load into joblib
    model = joblib.load(model_local)
    return model
