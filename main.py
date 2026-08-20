from data_read import FILE
from missing_data import MISSING
from tables_data import TABLE_DATA
from describe import DESCRIBE
from corelation import CORRELATION
from charts import CHART_DATA


file_name = "telecom_churn_data.csv"

# Stage 1: data_read.py
df = FILE().READ_DATA(file_name)

# Stage 2: missing_data.py  (fork point)
df = MISSING().HANDLE_MISSING(df)

# Branch A: tables_data.py -> charts.py (frequency bar chart)
keys, values = TABLE_DATA().FREQUENCY(df, "gender")
CHART_DATA().PLOT(keys, values, "gender")

# Branch B: describe.py -> charts.py (histogram)
print(DESCRIBE().SUMMARY(df))
CHART_DATA().HISTOGRAM(df, "age")

# Branch C: corelation.py
corr = CORRELATION().MATRIX(df)
print(corr["churn"].sort_values(ascending=False))