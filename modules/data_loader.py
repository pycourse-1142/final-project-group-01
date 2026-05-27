import pandas as pd

#  這個檔案負責讀取資料，包含從 CSV 檔案載入資料等功能。

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df