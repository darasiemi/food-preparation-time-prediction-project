from sklearn.model_selection import train_test_split

def split_data(df):
    X = df.drop(["delivery_time", "food_preparation_time" ], axis=1)
    y = df["food_preparation_time"]
    X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, stratify=y_full_train, test_size=0.25, random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test