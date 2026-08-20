import matplotlib.pyplot as plt


class CHART_DATA:
    def __init__(self):
        pass

    def PLOT(self, keys, values, column_name):
        plt.figure()
        plt.bar(keys, values)
        plt.title(f"Frequency of {column_name}")
        plt.savefig(f"freq_{column_name}.jpg")
        plt.show()

    def HISTOGRAM(self, df, column):
        plt.figure()
        df[column].plot(kind="hist", bins=20)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.savefig(f"hist_{column}.jpg")
        plt.show()


if __name__ == "__main__":
    from data_read import FILE
    from missing_data import MISSING
    from tables_data import TABLE_DATA

    df = FILE().READ_DATA("telecom_churn_data.csv")
    df = MISSING().HANDLE_MISSING(df)
    keys, values = TABLE_DATA().FREQUENCY(df, "gender")

    obj = CHART_DATA()
    obj.PLOT(keys, values, "gender")
    obj.HISTOGRAM(df, "age")