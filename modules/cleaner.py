import pandas as pd

#  這個檔案負責清理資料，包含轉換資料格式、處理缺失值等。

def clean_data(df):
    df = df.copy()

    # 將裁罰金額轉成數值
    df["penalty_money"] = pd.to_numeric(df["penalty_money"], errors="coerce")

    # 將日期轉成 datetime 格式
    df["transgress_date"] = pd.to_datetime(df["transgress_date"], errors="coerce")
    df["penalty_date"] = pd.to_datetime(df["penalty_date"], errors="coerce")

    # 計算從違規到裁罰經過幾天
    df["process_days"] = (df["penalty_date"] - df["transgress_date"]).dt.days

    # 移除主要欄位缺失的資料
    df = df.dropna(subset=["county_name", "transgress_type", "penalty_money"])

    return df