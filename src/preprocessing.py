import pandas as pd

def clean_borrower_genders(df: pd.DataFrame) -> pd.DataFrame:

    df["borrower_genders"] = df["borrower_genders"].fillna("")
    df["borrower_list"] = df["borrower_genders"].apply(lambda x: x.split(",") if x else [])
    df["borrower_count"] = df["borrower_list"].apply(len)

    df["num_female"] = df["borrower_list"].apply(lambda lst: sum(1 for g in lst if g == "F"))
    df["gender_ratio"] = df["num_female"] / df["borrower_count"].replace(0, 1)

    return df
