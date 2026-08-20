import pandas as pd


class MISSING:
    def __init__(self):
        pass

    def CHECK_MISSING(self, df):
        return df.isnull().sum()

    def HANDLE_MISSING(self, df):
        missing_counts = self.CHECK_MISSING(df)
        print("Missing values per column:")
        print(missing_counts[missing_counts > 0])

        clean_df = df.copy()
        for col in clean_df.columns:
            if clean_df[col].isnull().sum() == 0:
                continue
            if pd.api.types.is_numeric_dtype(clean_df[col]):
                clean_df[col] = clean_df[col].fillna(clean_df[col].median())
            else:
                clean_df[col] = clean_df[col].fillna("Unknown")

        print("Missing values filled.")
        return clean_df


if __name__ == "__main__":
    from data_read import FILE
    df = FILE().READ_DATA("telecom_churn_data.csv")
    clean_df = MISSING().HANDLE_MISSING(df)