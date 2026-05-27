#  這個檔案負責分析資料，包含各種統計和分析函數。

def analyze_county_cases(df):
    result = (
        df.groupby("county_name")
        .size()
        .reset_index(name="case_count")
        .sort_values("case_count", ascending=False)
        .head(10)
    )
    return result


def analyze_transgress_type(df):
    result = (
        df.groupby("transgress_type")
        .size()
        .reset_index(name="case_count")
        .sort_values("case_count", ascending=False)
    )
    return result


def analyze_avg_penalty_by_type(df):
    # 只分析裁罰金額大於 0 的案件，避免 0 元案件影響平均值
    penalty_df = df[df["penalty_money"] > 0]

    result = (
        penalty_df.groupby("transgress_type")["penalty_money"]
        .mean()
        .reset_index(name="avg_penalty")
        .sort_values("avg_penalty", ascending=False)
    )
    return result


def analyze_improve_status(df):
    result = (
        df.groupby("is_improve")
        .size()
        .reset_index(name="case_count")
        .sort_values("case_count", ascending=False)
    )
    return result