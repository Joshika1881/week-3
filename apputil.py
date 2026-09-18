import seaborn as sns
import seaborn as sns
import pandas as pd

url = (
    "https://github.com/melaniewalsh/Intro-Cultural-Analytics/"
    "raw/master/book/data/bellevue_almshouse_modified.csv"
)

df_bellevue = pd.read_csv(url)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    if n < 2:
        return str(n)

    return to_binary(n // 2) + str(n % 2)


def task_1():
    df = df_bellevue.copy()

    invalid_gender = ~df["gender"].isin(["m", "w"])
    df.loc[invalid_gender, "gender"] = pd.NA

    print("The gender column contains unclear values. "
          "These were treated as missing values.")

    return df.isna().sum().sort_values().index.tolist()


def task_2():
    df = df_bellevue.copy()

    df["year"] = pd.to_datetime(df["date_in"]).dt.year

    return (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )


def task_3():
    df = df_bellevue.copy()

    invalid_gender = ~df["gender"].isin(["m", "w"])
    df.loc[invalid_gender, "gender"] = pd.NA

    print("Unclear gender values were excluded from the averages.")

    return df.groupby("gender")["age"].mean()


def task_4():
    return (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )