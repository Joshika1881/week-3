import pandas as pd
import seaborn as sns

url = (
    "https://github.com/melaniewalsh/Intro-Cultural-Analytics/"
    "raw/master/book/data/bellevue_almshouse_modified.csv"
)

df_bellevue = pd.read_csv(url)


def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(n):
    """Return the binary representation of n as a string using recursion."""
    if n < 2:
        return str(n)

    return to_binary(n // 2) + str(n % 2)


def task_1():
    """Return columns sorted from least to most missing values."""
    df = df_bellevue.copy()

    # Treat unclear gender values as missing before counting missing data.
    invalid_gender = ~df["gender"].isin(["m", "w"])
    df.loc[invalid_gender, "gender"] = pd.NA

    print(
        "The gender column contains unclear values. "
        "These were treated as missing values."
    )

    return df.isna().sum().sort_values().index.tolist()


def task_2():
    """Return total admissions for each year as a DataFrame."""
    df = df_bellevue.copy()

    df["year"] = pd.to_datetime(df["date_in"]).dt.year

    return (
        df.groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )


def task_3():
    """Return the average age for each valid gender as a Pandas Series."""
    df = df_bellevue.copy()

    # Exclude unclear gender values from the average age calculation.
    invalid_gender = ~df["gender"].isin(["m", "w"])
    df.loc[invalid_gender, "gender"] = pd.NA

    print("Unclear gender values were excluded from the averages.")

    return df.groupby("gender")["age"].mean()


def task_4():
    """Return the five most common professions from most to least common."""
    return (
        df_bellevue["profession"]
        .value_counts()
        .head(5)
        .index
        .tolist()
    )