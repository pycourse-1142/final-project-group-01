# =========================
# data_loader.py
# =========================

import pandas as pd

# 讀取資料


def load_data(file_path):

    # 使用 UTF-8 編碼讀取
    try:

        df = pd.read_csv(
            file_path,
            encoding="utf-8"
        )

    # 若 UTF-8 失敗，則改用 Big5 編碼
    except:

        df = pd.read_csv(
            file_path,
            encoding="big5"
        )

    return df