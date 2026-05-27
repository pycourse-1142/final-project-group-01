import os
import matplotlib.pyplot as plt

#  這個檔案負責視覺化資料，包含各種圖表繪製函數。

def ensure_results_folder():
    os.makedirs("results", exist_ok=True)


def plot_county_cases(df):
    ensure_results_folder()

    plt.figure(figsize=(10, 6))
    plt.barh(df["county_name"], df["case_count"])
    plt.xlabel("案件數")
    plt.ylabel("縣市")
    plt.title("各縣市環境違規裁罰案件數 Top 10")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("results/county_case_top10.png")
    plt.close()


def plot_transgress_type(df):
    ensure_results_folder()

    plt.figure(figsize=(10, 6))
    plt.bar(df["transgress_type"], df["case_count"])
    plt.xlabel("違規類型")
    plt.ylabel("案件數")
    plt.title("不同環境違規類型之案件數分布")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("results/transgress_type_count.png")
    plt.close()


def plot_avg_penalty_by_type(df):
    ensure_results_folder()

    plt.figure(figsize=(10, 6))
    plt.bar(df["transgress_type"], df["avg_penalty"])
    plt.xlabel("違規類型")
    plt.ylabel("平均裁罰金額")
    plt.title("不同違規類型之平均裁罰金額比較")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("results/avg_penalty_by_type.png")
    plt.close()


def plot_improve_status(df):
    ensure_results_folder()

    plt.figure(figsize=(8, 5))
    plt.bar(df["is_improve"], df["case_count"])
    plt.xlabel("改善狀態")
    plt.ylabel("案件數")
    plt.title("環境違規案件改善狀態分布")
    plt.tight_layout()
    plt.savefig("results/improve_status.png")
    plt.close()