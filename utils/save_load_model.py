import pickle

def save_model(pipeline, file_path):
    with open(file_path, "wb") as f:
        pickle.dump(pipeline, f)


def load_model(file_path):
    with open(file_path, "rb") as f:
        pipeline = pickle.load(f)
    
    return pipeline

