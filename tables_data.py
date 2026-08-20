import pandas as pd


class TABLE_DATA:
    def __init__(self):
        pass

    def FREQUENCY(self, df, column):
        keys = df[column].value_counts().keys()
        values = df[column].value_counts().values
        return (keys, values)


if __name__ == "__main__":
    from data_read import FILE
    from missing_data import MISSING

    df = FILE().READ_DATA("telecom_churn_data.csv")
    df = MISSING().HANDLE_MISSING(df)
    keys, values = TABLE_DATA().FREQUENCY(df, "gender")
    print(keys, values)