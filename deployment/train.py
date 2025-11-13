from utils.load_data import load_data
from utils.preprocess import preprocess
from utils.data_split import split_data
from utils.build_pipeline import build
from utils.save_load_model import save_model

from sklearn.ensemble import RandomForestRegressor 



if __name__ == "__main__":
    data_url = "data/food_order.csv"  
    df = load_data(data_url)

    categorical_cols, hashed_cols, numeric_cols = preprocess(df)

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    model = RandomForestRegressor(
    random_state=42,
    max_depth=8,
    min_samples_split=15,
    n_estimators=441,
    n_jobs=-1
    )
    
    best_pipeline = build(categorical_cols, hashed_cols, numeric_cols, model)

    best_pipeline.fit(X_train, y_train)

    file_path = "model/model.pkl"

    save_model(best_pipeline, file_path)

    # best_pipeline.fit(X_train, y_train)
    # y_pred = best_pipeline.predict(X_test)

    # print(y_pred)
    
    # print(hashed_cols)
    # print(numeric_cols)
