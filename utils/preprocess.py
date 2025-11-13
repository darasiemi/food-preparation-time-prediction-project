def preprocess(df):

    df = df.drop(["rating"], axis=1)

    categorical_cols =list(df.dtypes[df.dtypes == 'object'].index)

    hashed_cols = ["order_id", "customer_id"]
    numeric_cols = ["cost_of_the_order"]

    return categorical_cols, hashed_cols, numeric_cols
