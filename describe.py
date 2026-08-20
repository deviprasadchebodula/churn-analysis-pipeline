import pandas as pd


class DESCRIBE:
    def __init__(self):
        pass

    def SUMMARY(self, df):
        numeric_df = df.select_dtypes(include=["number"])
        return numeric_df.describe()


if __name__ == "__main__":
    from data_read import FILE
    from missing_data import MISSING

    df = FILE().READ_DATA("telecom_churn_data.csv")
    df = MISSING().HANDLE_MISSING(df)
    print(DESCRIBE().SUMMARY(df))