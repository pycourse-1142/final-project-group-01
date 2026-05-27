# =========================
# cleaner.py
# =========================

import pandas as pd

# 清理資料

def clean_data(df):
    df = df.copy()

    # 裁罰金額處理
    # 金額欄位
    df["penalty_money"] = (
        df["penalty_money"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df["penalty_money"] = pd.to_numeric(
        df["penalty_money"],
        errors="coerce"
    )

    # 日期格式處理
    df["transgress_date"] = pd.to_datetime(
        df["transgress_date"],
        errors="coerce"
    )

    # 將裁罰日期轉成 datetime
    df["penalty_date"] = pd.to_datetime(
        df["penalty_date"],
        errors="coerce"
    )

    # 計算處理天數
    df["process_days"] = (
        df["penalty_date"] - df["transgress_date"]
    ).dt.days

    # 如果出現負數，則改成空值
    df.loc[df["process_days"] < 0, "process_days"] = None

    # 缺失值處理
    df["is_improve"] = df["is_improve"].fillna("未知")

    # 移除重要欄位缺失的資料
    df = df.dropna(
        subset=[
            "county_name",
            "transgress_type",
            "penalty_money"
        ]
    )

    return df