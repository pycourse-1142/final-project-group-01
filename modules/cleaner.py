# =========================
# cleaner.py
# =========================

import pandas as pd

# 負責清理資料


def clean_data(df):

    df = df.copy()

    # 裁罰金額處理
    df["penalty_money"] = (
        df["penalty_money"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    # 將字串轉成數值格式
    df["penalty_money"] = pd.to_numeric(
        df["penalty_money"],
        errors="coerce"
    )


    # 違規日期
    df["transgress_date"] = pd.to_datetime(
        df["transgress_date"],
        errors="coerce"
    )

    # 裁罰日期
    df["penalty_date"] = pd.to_datetime(
        df["penalty_date"],
        errors="coerce"
    )

    # 計算處理天數
    df["process_days"] = (
        df["penalty_date"] - df["transgress_date"]
    ).dt.days

    df.loc[df["process_days"] < 0, "process_days"] = None

    # 缺失值處理
    df["is_improve"] = df["is_improve"].fillna("未知")

    df = df.dropna(
        subset=[
            "county_name",
            "transgress_type",
            "penalty_money"
        ]
    )

    return df