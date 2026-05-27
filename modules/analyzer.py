# =========================
# analyzer.py
# =========================


def analyze_county_cases(df):

    # 依照縣市分組
    # 計算每個縣市案件數
    result = (
        df.groupby("county_name")
        .size()
        .reset_index(name="case_count")
        .sort_values(
            by="case_count",
            ascending=False
        )
        .head(10)  # 只取前 10 名
    )

    return result


def analyze_transgress_type(df):

    # 依照違規類型分組
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

    # 排除 0 元案件
    # 避免影響平均值
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