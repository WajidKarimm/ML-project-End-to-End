import os
import sys
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    """
    Save a Python object to a file using dill serialization.
    Automatically creates the directory if it doesn't exist.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:  # FIX: file_path instead of dir_path
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
