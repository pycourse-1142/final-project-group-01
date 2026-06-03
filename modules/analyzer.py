# =========================
# analyzer.py
# =========================

# 負責分析資料


def analyze_county_cases(df):

    # 計算每個縣市案件數
    result = (
        df.groupby("county_name")
        .size()
        .reset_index(name="case_count")
        .sort_values(
            by="case_count",
            ascending=False
        )
        .head(10)  
    )

    return result


def analyze_transgress_type(df):

    # 計算案件數
    result = (
        df.groupby("transgress_type")
        .size()
        .reset_index(name="case_count")
        .sort_values(
            by="case_count",
            ascending=False
        )
    )

    return result


def analyze_avg_penalty_by_type(df):

    penalty_df = df[df["penalty_money"] > 0]

    # 計算各違規類型平均裁罰金額
    result = (
        penalty_df.groupby("transgress_type")["penalty_money"]
        .mean()
        .reset_index(name="avg_penalty")
        .sort_values(
            by="avg_penalty",
            ascending=False
        )
    )

    return result


def analyze_improve_status(df):

    # 分析改善狀態分布
    result = (
        df.groupby("is_improve")
        .size()
        .reset_index(name="case_count")
        .sort_values(
            by="case_count",
            ascending=False
        )
    )

    return result