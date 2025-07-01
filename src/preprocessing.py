import pandas as pd

def has_female_borrower(df: pd.DataFrame) -> pd.DataFrame:
    df["borrower_genders"] = df["borrower_genders"].fillna("")
    df["has_female"] = df["borrower_genders"].apply(lambda x: int("female" in x.split(",")))
    return df

def drop_col(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drop multiple columns from the DataFrame if they exist.
    """
    cols_to_drop = ['id', 'activity', 'use', 'country_code', 'country', 'region', 'currency',
                    'posted_time', 'disbursed_time', 'funded_time', 'tags', 'date',
                    'Indicator Name', 'Indicator Code', 'Country Code', 'Year', 'partner_id']
    
    # Keep only the columns that are present in df
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    
    return df.drop(columns=existing_cols)

def classify_economy(gdp: pd.DataFrame) -> pd.DataFrame:
    """
    Classify countries into income groups based on GDP per capita.
    """
    def label_income(gdp_value):
        if pd.isna(gdp_value):
            return 'Unknown'
        elif gdp_value <= 1135:
            return 'Low'
        elif gdp_value <= 4465:
            return 'Lower-middle'
        elif gdp_value <= 13845:
            return 'Upper-middle'
        else:
            return 'High'

    gdp['Income Group'] = gdp['GDP per capita'].apply(label_income)
    return gdp
