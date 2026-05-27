# =========================
# visualizer.py
# =========================

import os
import matplotlib.pyplot as plt

# 解決 matplotlib 中文亂碼問題
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]

# 解決負號顯示問題
plt.rcParams["axes.unicode_minus"] = False

def ensure_results_folder():

    os.makedirs(
        "results",
        exist_ok=True
    )


# =========================
# 圖表 1：各縣市案件數 Top 10
# =========================
def plot_county_cases(df):

    # 確保輸出資料夾存在
    ensure_results_folder()

    # 設定圖表大小
    plt.figure(figsize=(10, 6))

    # 繪製
    plt.barh(
        df["county_name"],
        df["case_count"]
    )

    plt.xlabel("案件數")
    plt.ylabel("縣市")

    plt.title("各縣市環境違規裁罰案件數 Top 10")
    plt.gca().invert_yaxis()
    plt.tight_layout()

    # 儲存圖片
    plt.savefig(
        "results/county_case_top10.png"
    )

    # 關閉圖表
    plt.close()


# =========================
# 圖表 2：違規類型案件數分布
# =========================
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

    # 旋轉文字避免重疊
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        "results/transgress_type_count.png"
    )

    plt.close()


# =========================
# 圖表 3：平均裁罰金額比較
# =========================
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

    # 旋轉文字
    plt.xticks(rotation=45, ha="right")

    plt.tight_layout()

    plt.savefig(
        "results/avg_penalty_by_type.png"
    )

    plt.close()


# =========================
# 圖表 4：改善狀態分布
# =========================
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

    # 旋轉文字
    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig(
        "results/improve_status.png"
    )

    plt.close()