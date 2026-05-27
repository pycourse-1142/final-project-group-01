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