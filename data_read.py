import pandas as pd


class FILE:
    def __init__(self):
        pass

    def READ_DATA(self, file_name):
        df = pd.read_csv(file_name)
        print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns")
        return df


if __name__ == "__main__":
    obj = FILE()
    obj.READ_DATA("/Users/deviprasadchebodula/Downloads/telecom_churn_data.csv")