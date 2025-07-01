import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df_raw = pd.read_csv(path, skiprows=3, engine='python')

    # Strip any whitespace from columns just in case
    df_raw.columns = df_raw.columns.str.strip()

    # Melt from wide to long format
    df_tidy = df_raw.melt(
        id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
        var_name='Year',
        value_name='GDP per capita'
    )

    # Convert year and values to numeric
    df_tidy["Year"] = pd.to_numeric(df_tidy["Year"], errors="coerce")
    df_tidy["GDP per capita"] = pd.to_numeric(df_tidy["GDP per capita"], errors="coerce")
    df_tidy = df_tidy.dropna(subset=["GDP per capita"])

    # For each country, get row with max Year (latest year)
    latest_df = df_tidy.loc[df_tidy.groupby('Country Name')['Year'].idxmax()]

    return latest_df
