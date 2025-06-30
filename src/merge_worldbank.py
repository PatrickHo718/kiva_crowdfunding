import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load the World Bank data from a CSV file.
    
    Args:
        path (str): The file path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    """
    df_raw = pd.read_csv(path, skiprows=3)

    # reshape from wide to long format
    df_cleaned = df_raw.melt(
        id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
        var_name='Year',
        value_name='Poverty Rate'
    )

    # Convert year and values to numeric
    df_tidy["Year"] = pd.to_numeric(df_tidy["Year"], errors="coerce")
    df_tidy["Poverty Rate"] = pd.to_numeric(df_tidy["Poverty Rate"], errors="coerce")

    # Filter indicator and drop missing
    df_tidy = df_tidy[df_tidy["Indicator Code"] == "SI.POV.NAHC"]
    df_tidy = df_tidy.dropna(subset=["Poverty Rate"])

    # Keep only recent years
    df_tidy = df_tidy[df_tidy["Year"] >= 2010]
    return df_cleaned