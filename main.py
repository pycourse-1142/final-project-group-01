# =========================
# main.py
# =========================

from data_loader import load_data
from cleaner import clean_data
from analyzer import (
    analyze_county_cases,
    analyze_transgress_type,
    analyze_avg_penalty_by_type,
    analyze_improve_status,
)
from visualizer import (
    plot_county_cases,
    plot_transgress_type,
    plot_avg_penalty_by_type,
    plot_improve_status,
)


def main():
    # 讀取資料
    file_path = "ems_p_46.csv"
    df = load_data(file_path)

    print("原始資料筆數：", len(df))

    # 清理資料
    df = clean_data(df)

    print("清理後資料筆數：", len(df))

    # =========================
    # 分析 1：各縣市案件數
    # =========================
    county_cases = analyze_county_cases(df)

    print("\n各縣市案件數 Top 10")
    print(county_cases)

    plot_county_cases(county_cases)

    # =========================
    # 分析 2：違規類型案件數
    # =========================
    transgress_type = analyze_transgress_type(df)

    print("\n違規類型案件數")
    print(transgress_type)

    plot_transgress_type(transgress_type)

    # =========================
    # 分析 3：平均裁罰金額
    # =========================
    avg_penalty = analyze_avg_penalty_by_type(df)

    print("\n各違規類型平均裁罰金額")
    print(avg_penalty)

    plot_avg_penalty_by_type(avg_penalty)

    # =========================
    # 分析 4：改善狀態
    # =========================
    improve_status = analyze_improve_status(df)

    print("\n改善狀態分布")
    print(improve_status)

    plot_improve_status(improve_status)

    print("\n所有分析完成，圖表已輸出至 results 資料夾")

from modules.data_loader import load_data
from modules.cleaner import clean_data
from modules.analyzer import (
    analyze_county_cases,
    analyze_transgress_type,
    analyze_avg_penalty_by_type,
    analyze_improve_status
)
from modules.visualizer import (
    plot_county_cases,
    plot_transgress_type,
    plot_avg_penalty_by_type,
    plot_improve_status
)

#  這是主程式，用來串接所有功能模組，完成資料分析流程。

def main():
    # 1. 讀取資料
    df = load_data("data/ems_p_46.csv")

    # 2. 清理資料
    cleaned_df = clean_data(df)

    # 3. 分析資料
    county_cases = analyze_county_cases(cleaned_df)
    transgress_type = analyze_transgress_type(cleaned_df)
    avg_penalty = analyze_avg_penalty_by_type(cleaned_df)
    improve_status = analyze_improve_status(cleaned_df)

    # 4. 畫圖並輸出到 results 資料夾
    plot_county_cases(county_cases)
    plot_transgress_type(transgress_type)
    plot_avg_penalty_by_type(avg_penalty)
    plot_improve_status(improve_status)

    print("資料分析完成，圖表已輸出到 results 資料夾。")


if __name__ == "__main__":
    main()