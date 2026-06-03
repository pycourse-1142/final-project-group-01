# =========================
# visualizer.py
# =========================

import os
import matplotlib.pyplot as plt

# 解決中文亂碼、負號顯示問題
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]

plt.rcParams["axes.unicode_minus"] = False


# 建立 results 資料夾
def ensure_results_folder():

    os.makedirs(
        "results",
        exist_ok=True
    )


# 圖表 1：各縣市案件數 Top 10
def plot_county_cases(df):

    ensure_results_folder()

    # 設定圖表大小
    plt.figure(figsize=(10, 6))

    # 繪製水平長條圖
    plt.barh(
        df["county_name"],
        df["case_count"]
    )

    plt.xlabel("案件數")
    plt.ylabel("縣市")

    # 設定圖表標題
    plt.title("各縣市環境違規裁罰案件數 Top 10")

    # 讓案件數最多顯示在最上方
    plt.gca().invert_yaxis()

    # 自動調整版面
    plt.tight_layout()

    plt.savefig(
        "results/county_case_top10.png"
    )

    plt.close()


# 圖表 2：違規類型案件數分布
def plot_transgress_type(df):

    ensure_results_folder()

    plt.figure(figsize=(12, 6))

    # 繪製長條圖
    plt.bar(
        df["transgress_type"],
        df["case_count"]
    )

    plt.xlabel("違規類型")
    plt.ylabel("案件數")

    plt.title("不同環境違規類型之案件數分布")

    # 旋轉 x 軸文字避免重疊
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        "results/transgress_type_count.png"
    )

    plt.close()


# 圖表 3：平均裁罰金額比較
def plot_avg_penalty_by_type(df):

    ensure_results_folder()

    plt.figure(figsize=(12, 6))

    # 繪製長條圖
    plt.bar(
        df["transgress_type"],
        df["avg_penalty"]
    )

    plt.xlabel("違規類型")
    plt.ylabel("平均裁罰金額")

    plt.title("不同違規類型之平均裁罰金額比較")

    # 旋轉 x 軸文字
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        "results/avg_penalty_by_type.png"
    )

    plt.close()



# 圖表 4：改善狀態分布
def plot_improve_status(df):

    ensure_results_folder()

    plt.figure(figsize=(8, 5))

    # 繪製長條圖
    plt.bar(
        df["is_improve"],
        df["case_count"]
    )

    plt.xlabel("改善狀態")
    plt.ylabel("案件數")

    plt.title("環境違規案件改善狀態分布")

    # 旋轉文字避免重疊
    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig(
        "results/improve_status.png"
    )

    plt.close()