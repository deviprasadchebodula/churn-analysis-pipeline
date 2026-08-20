import pandas as pd


class CORRELATION:
    def __init__(self):
        pass

    def MATRIX(self, df):
        numeric_df = df.select_dtypes(include=["number"])
        return numeric_df.corr()


if __name__ == "__main__":
    from data_read import FILE
    from missing_data import MISSING

    df = FILE().READ_DATA("telecom_churn_data.csv")
    df = MISSING().HANDLE_MISSING(df)
    corr = CORRELATION().MATRIX(df)
    print(corr["churn"].sort_values(ascending=False))