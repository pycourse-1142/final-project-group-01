[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/V3HMcGvn)
# 1142_final_project
1142期末分組專題規劃與開發日誌
2026/5/27-6/17(共四周)進行各組自訂專題。組別照舊。
2026/6/24進行各組成果發表

* 參考資料集:
確認下載使用的儘量是原始資料（CSV/JSON/TXT），而不是已經整理好的 Excel
1.	[臺灣政府資料開放平台](https://data.gov.tw/datasets/search)
2.	[環境部空氣品質監測資料](https://airtw.moenv.gov.tw/cht/Query/DataDownload.aspx)
3.	[全民健康保險醫療統計](https://dep.mohw.gov.tw/dos/lp-5103-113.html)


2026/5/27 討論想法，結束時，各組提交一頁專題規劃如下:
##  一、專題規劃 (5/27 提交)
* **專題名稱**：  臺灣環境違規裁罰資料分析：各縣市、違規類型與裁罰金額之比較
* **資料來源**：  政府資料開放平台。https://data.gov.tw/dataset/34101
* **主要問題**：  主要想分析環境違規裁罰資料中，不同縣市與不同違規類型的裁罰情況是否存在明顯差異。透過裁罰案件數、裁罰總金額、平均裁罰金額與繳款／改善狀態等指標，找出環境違規較集中、裁罰金額較高，或後續改善狀況較需要注意的對象。
* **次要問題**：  1. 如何處理裁罰金額為 0 的資料？ 2. 如何處理缺失值很多的欄位？ 3. 如何比較不同污染類型？ 4. 如何分析裁罰處理時間？
* **預期產出圖表**： 圖表一：各縣市裁罰案件數排名圖    圖表二：不同違規類型的案件數分布圖    圖表三：各違規類型平均裁罰金額比較圖    圖表四：繳款狀態或改善狀態分布圖

---

##  二、組員分工紀錄 (佔比 10%)
| 學號 | 姓名 | 主要負責模組 / 任務描述 | 預估貢獻度 (%) |
| :--- | :--- | :--- | :---: |
| **11131614** | **蔡政洋** | **`main.py` (主程式串接與流程控制) & `visualizer.py` (整合繪圖) & `data_loader.py`(資料讀取)   & `cleaner.py` (資料流與清洗)**<br>負責控管整體資料分析 Pipeline 流程，串接資料載入、清洗與核心統計模組。共同參與視覺化模組實作與除錯，管理相對路徑起點，並主導最終期末報告與 README 撰寫。主要把所有架構的程式碼邏輯建立出來。 | **40%** |
| **1111316109** | **黃琬芸** | **`data_loader.py` & `cleaner.py` (資料流與清洗)**<br>負責Debug這兩個.py檔案與實作原始 CSV 資料流載入，編寫自動辨識並切換 UTF-8 與 Big5 編碼的防崩潰機制；處理金額與日期的欄位型態轉換（`pd.to_numeric`, `pd.to_datetime`）並過濾髒數據。 | **30%** |
| **1112316137** | **陳敏綺** | **`analyzer.py` (核心數據統計分析)**<br>負責這區塊的Debug與核心統計邏輯（Logic），運用 Pandas 進行分組（`.groupby`）與聚合計算，包含各縣市案件排序、過濾 0 元資料後的平均裁罰金額計算，以及改善狀態分布統計。 | **30%** |

---

## 三、數據自我測試紀錄 (佔比 25%)
> **重要規範**：請手動修改 `data/` 中的原始檔案，測試程式的「穩健性」。若程式因髒數據直接崩潰（Crash），此項不計分。

| 測試情境 | 模擬動作 (如何「弄壞」數據) | 程式原始反應 | 修正後邏輯與檔案位置 |
| :--- | :--- | :--- | :--- |
| **1. 遭遇環境編碼衝突** | 將原始檔案轉換為台灣政府常見的 `Big5` 編碼儲存。 | `pandas` 直接拋出 `UnicodeDecodeError` 導致程式崩潰。 | **修復於 `modules/data_loader.py`**：<br>使用 `try-except` 機制，首選 UTF-8 讀取，若失敗則自動自動切換為 Big5 編碼，確保 100% 成功加載。 |
| **2. 裁罰金額包含非數字** | 在金額欄位故意填入中文 `「新台幣十萬元」` 或空字串。 | `ValueError` 導致無法計算平均值或清洗中斷。 | **修復於 `modules/cleaner.py`**：<br>使用 `pd.to_numeric(..., errors='coerce')` 將無法解析的非數字強制轉為 `NaN`，並以 `fillna(0)` 填補，確保統計不中斷。 |
| **3. 關鍵欄位名稱對不上** | 模擬平台更新，將 `penalty_money` 欄位改名或錯位。 | 拋出 `KeyError: 'penalty_money'` 異常。 | **修復於 `modules/cleaner.py`**：<br>加入欄位存在性檢查與 `try-except` 機制，並在 `main.py` 加入動態調試指令 `print(df.columns)` 以利人工對齊。 |
| **4. 移動端執行路徑錯亂** | 在不同的資料夾路徑層級（如在 `modules/` 內）嘗試執行程式。 | 拋出 `ModuleNotFoundError` 或 `FileNotFoundError`。 | **修復於 `main.py`**：<br>嚴格禁止使用絕對路徑。統一規範為純粹的**相對路徑**（如 `data/ems_p_46.csv`），並配合 VS Code 終端機工作目錄根目錄規範執行。 |


---

##  四、AI 協作與糾錯紀錄 (佔比 10%)
1.  **關鍵 Prompt**：
    > (請在此處貼上你們最常使用的指令)
    
2.  **AI 代碼失效紀錄與人工修正**：
    * **失效說明**
    * **人工修正方法**

---

## 五、專題執行結果呈現 (佔比 15%)
> 請將產出的 4 張圖表存於 `results/`，並在此處進行分析簡述。

### 1. 📊 [分析 1] 各縣市環境違規裁罰案件數 Top 10 (新北市 (210件) 與 臺北市 (198件) 囊括前兩名，執法量最密集。)
**分析簡述：** <br>
根據 1000 筆有效數據統計，**新北市（210 筆）** 與 **臺北市（198 筆）** 顯著位居全臺環境裁罰案件量的前兩名，兩者合計即佔了總案件數的四成。其次為高雄市（98 筆）與桃園市（91 筆）。這項結果反映出雙北都市化程度極高、人口密度稠密，不論是交通工具排放還是密集的商業活動，皆導致環保稽查與民眾檢舉的頻率遠高於其他縣市。
<div align="center">
  <img width="500" height="500" alt="county_case_top10" src="https://github.com/user-attachments/assets/334a4633-94fa-4943-b506-1aae7469b995" />
</div>
<div align="center">
  <img width="1000" height="600" alt="county_case_top10" src="https://github.com/user-attachments/assets/8a05eb80-0bff-464c-a5c2-d9514b52d695" />
</div>

### 2. 📊 [分析 2] 不同環境違規類型之案件數分布 (移動污染 (577件) 壓倒性最多，佔了超過一半的案件量。) 
**分析簡述：** <br>
違規類型的分組數據呈現極端的兩極化。**「移動污染」以 577 筆案件高居第一名**，佔總體案件的 57.7%，其次為一般廢棄物（115 筆）與事業廢棄物（100 筆）。這說明環保單位日常最主要的業務大宗，其實是針對汽機車排煙、烏賊車等機動車輛的「移動污染源」進行稽查取締。
<div align="center">
  <img width="500" height="500" alt="transgress_type_count" src="https://github.com/user-attachments/assets/e1a313f9-4695-4538-ad68-9751df924d9c" />
</div>
<div align="center">
  <img width="1200" height="600" alt="transgress_type_count" src="https://github.com/user-attachments/assets/6ca13de8-7d7b-47bb-a9ac-2fb52b553542" />
</div>


### 3. 📊 [分析 3] 不同違規類型之平均裁罰金額比較 (土壤及地下水污染 平均高達 57.5 萬元，居所有類型之冠。)
**分析簡述：** <br>
將此圖與圖表二對比，產生了非常有趣的「反差效應」。雖然「土壤及地下水污染」在總案件中僅有 2 筆，但其**平均裁罰金額高達 575,000 元**，高居全類型第一！其次為固定空污（約 33 萬元）與營建工程（約 16 萬元）。相反地，案件數最多的移動污染，平均裁罰金額僅 1,725 元。這強力證實了政府的環保執法策略：**對次數多但危害小的民生違規（移動污染）採取輕罰；對次數極少但會造成永久性土地傷害的重大工業違規（水土污染），則採取毀滅性的重罰手段。**
<div align="center">
  <img width="500" height="500" alt="avg_penalty_by_type" src="https://github.com/user-attachments/assets/47ef30fa-7f57-48ac-9eff-201326f83487" />
</div>
<div align="center">
  <img width="1200" height="600" alt="avg_penalty_by_type" src="https://github.com/user-attachments/assets/dda02b57-82ab-49b5-944a-41f134dd4de3" />
</div>

### 4. 📊 [分析 4] 環境違規案件改善狀態分布
**分析簡述：** <br>
在改善狀態（`is_improve`）的分布中，**「不須改善」佔了壓倒性的 914 筆**。這主要是因為高比例的案件屬於移動污染（汽機車排煙），此類違規通常為當場完成檢驗或單次處罰，不涉及後續限期改善工程。在需要改善的案件中，已有 52 筆「已改善完成」，但仍有 **33 筆處於「待改善」狀態**，這 33 筆將是環保單位後續列管追蹤的重點對象。此外，數據中還抓出 1 筆「未如期改善，另開立裁處書」的頑固個案，展現了程式對異常數據的精準捕捉。
<div align="center">
  <img width="350" height="150" alt="improve_status" src="https://github.com/user-attachments/assets/214ec5ac-f92e-4c12-a3d4-5e68a7bc5ded" />
</div>
      
<div align="center">
  <img width="1200" height="600" alt="improve_status" src="https://github.com/user-attachments/assets/6ed5fe79-02b1-41a0-afcd-2e34ef3cbedb" />
</div>

<img width="350" height="20" alt="image" src="https://github.com/user-attachments/assets/b027cdbf-5a46-471a-a38e-cb3e434a1693" />

---

## 教師評分區 (學生請勿填寫)
* **模組化程式結構 (25%)**： (Parser/Logic/Plotter 拆分情形)
* **Git 使用紀錄 (15%)**： (須滿足至少 10 個具備具體描述的 Commit)
* **成果展示 (10%)**：
* **程式碼理解 Q&A (10%)**： (現場即時修改參數測試)

---
### 注意事項 (必讀)
1.  **路徑規範**：禁止使用 `C:\\Users\\...` 絕對路徑。
2.  **模組契約**：各模組間應透過 `return` 傳遞數據，嚴禁大量使用 Global 變數。
3.  **Git 規範**：禁止一次性 Push 全部代碼，必須有開發過程紀錄。
