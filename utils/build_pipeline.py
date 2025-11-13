from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction import FeatureHasher
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, OneHotEncoder, StandardScaler


def to_dict_rows(X):
    # X is a DataFrame with the hashed_cols subset
    return X.astype(str).to_dict(orient="records")


def build(categorical_cols, hashed_cols, numeric_cols, model):
    hashed_pipe = Pipeline(
        [
            (
                "to_dict",
                FunctionTransformer(to_dict_rows, feature_names_out="one-to-one"),
            ),
            (
                "hasher",
                FeatureHasher(n_features=2**18, input_type="dict"),
            ),  # adjust n_features as needed
        ]
    )

    cat_pipe = OneHotEncoder(handle_unknown="ignore", sparse_output=True)

    num_pipe = StandardScaler(
        with_mean=False
    )  # keep False because we may end up with sparse matrices

    preproc = ColumnTransformer(
        transformers=[
            ("hash", hashed_pipe, hashed_cols),
            ("cat", cat_pipe, categorical_cols),
            ("num", num_pipe, numeric_cols),
        ],
        remainder="drop",  # or "passthrough" if you want to keep other columns
        sparse_threshold=1.0,  # keep result sparse (good with hashing + OHE)
    )

    # model = LogisticRegression(max_iter=1000)

    pipeline = Pipeline([("preproc", preproc), ("model", model)])

    return pipeline
