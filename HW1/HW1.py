import os
import pandas as pd
import matplotlib.pyplot as plt

def question_1(file, folder): # Race/ethnicity <=> Parent Level of Education
    # 讀取 CSV 檔案
    df = pd.read_csv(file)   
    # 提取族群、父母最高教育程度
    data = df[["race/ethnicity", "parental level of education"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"族群: {row[0]}\t父母最高教育程度: {row[1]}")

    # 使用 groupby 分組並計算每個分組中 'parental level of education' 列的次數
    grouped_counts = data.groupby(['race/ethnicity', 'parental level of education']).size().unstack(fill_value=0)
    # 繪製堆疊的條形圖
    grouped_counts.plot(kind='bar', stacked=True, figsize=(6, 7))
    # 添加標籤和標題
    plt.title('Whether Race/Ethnicity Affects Parental Level of Education')
    plt.xlabel('Race/Ethnicity', fontsize = 14)
    plt.ylabel('Parental Level of Education', fontsize = 14)
    # 調整圖例字型大小與位置
    plt.legend(fontsize = 10, loc = 'upper left')
    # 將x軸刻度旋轉15度
    plt.xticks(rotation = 15)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question1.png')
    plt.savefig(save_path)

def question_2(file, folder): # Parental level of education <=> Test preparation course
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取父母最高教育程度、是否完成作業
    data = df[["parental level of education", "test preparation course"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"父母最高教育程度: {row[0]}\t是否完成作業: {row[1]}")

    # 使用 groupby 分組並計算每個分組中 'test preparation course' 列的次數
    grouped_counts = data.groupby(['parental level of education', 'test preparation course']).size().unstack(fill_value=0)
    # 只保留 'completed' 和 'none' 的數量
    grouped_counts = grouped_counts[['completed', 'none']]
    # 繪製堆疊的條形圖
    grouped_counts.plot(kind='bar', stacked=True, figsize=(6, 8))
    # 添加標籤和標題
    plt.title('Does Parental Level of Education Affects Whether \nTest Preparation Course is Completed', fontsize = 16)
    plt.xlabel('Parental Level of Education', fontsize = 14)
    plt.ylabel('Test Preparation Course', fontsize = 14)
    # 將x軸標籤旋轉15度
    plt.xticks(rotation=16)
    # 將圖例移至左上角
    plt.legend(loc='upper left', fontsize = 12)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question2.png')
    plt.savefig(save_path)

def question_3(file, folder): # Test preparation course <=> Average score
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目average score做math score、reading score和writing score的總和後取平均
    df["average Score"] = df[["math score", "reading score", "writing score"]].mean(axis=1).fillna(0)
    # 提取是否完成作業、平均成績
    data = df[["test preparation course", "average Score"]]
    # 將資料依照test preparation course中的項目進行分類
    data_completed = df[df["test preparation course"] == "completed"]["average Score"]
    data_none = df[df["test preparation course"] == "none"]["average Score"]
    # 印出資料
    for index, row in data.iterrows():
        print(f"是否完成作業: {row[0]}\t平均成績: {row[1]}")
    
    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    plt.boxplot([data_completed, data_none], labels=["Completed", "None"])
    # 添加標籤和標題
    plt.title('Does Completing Test Preparation Course Affect Average Score', fontsize = 16)
    plt.xlabel('Test Preparation Course', fontsize = 14)
    plt.ylabel('Average Score', fontsize = 14)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question3.png')
    plt.savefig(save_path)

def question_4(file, folder): # Parental level of education <=> Average score
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目average score做math score、reading score和writing score的總和後取平均
    df["average Score"] = df[["math score", "reading score", "writing score"]].mean(axis=1).fillna(0)
    # 提取是否完成作業、平均成績
    data = df[["parental level of education", "average Score"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"是否完成作業: {row[0]}\t平均成績: {row[1]}")

    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    bp = df.boxplot(column='average Score', by='parental level of education', figsize=(8, 6))
    # 添加標籤和標題
    plt.title('Does Parental Level of Education Affect Average Score', fontsize = 16)
    plt.xlabel('Parental Level of Education', fontsize = 14)
    plt.ylabel('Average Score', fontsize = 14)
    # 將x軸標籤旋轉15度
    plt.xticks(rotation=15)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question4.png')
    plt.savefig(save_path)

def question_5(file, folder): # Gender <=> Average score
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目average score做math score、reading score和writing score的總和後取平均
    df["average Score"] = df[["math score", "reading score", "writing score"]].mean(axis=1).fillna(0)
    # 提取是否完成作業、平均成績
    data = df[["gender", "average Score"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"性別: {row[0]}\t平均成績: {row[1]}")
    
    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    data.boxplot(column='average Score', by='gender')
    # 添加標籤和標題
    plt.title('Does Gender Affect Average Score', fontsize = 16)
    plt.xlabel('Gender', fontsize = 14)
    plt.ylabel('Average Score', fontsize = 14)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question5.png')
    plt.savefig(save_path)

def question_6(file, folder): # Writing <=> Reading score
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取寫作成績、閱讀成績
    data = df[["writing score", "reading score"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"寫作成績: {row[0]}\t閱讀成績: {row[1]}")
    
    # 建立散點圖
    plt.figure()
    # 繪製散點圖
    plt.scatter(data["writing score"], data["reading score"])
    # 添加標籤和標題
    plt.title('Relationship Between Writing Score and Reading Score', fontsize = 14)
    plt.xlabel('Writing Score', fontsize = 13)
    plt.ylabel('Reading Score', fontsize = 13)
    # 調整圖片排版
    plt.tight_layout()
    # 儲存圖片
    save_path = os.path.join(folder, 'Question6.png')
    plt.savefig(save_path)

if __name__ == '__main__':

    os.chdir("D:\My 資料夾\學校\大學\通識\學習分析工具實務應用")
    csv_file = '.\exams.csv'

    folder_name = f'Pics of analysis'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name) 
        
    print("族群與父母最高教育程度之關係：")
    question_1(csv_file, folder_name)

    print("父母最高教育程度與是否完成作業之關係：")
    question_2(csv_file, folder_name)

    print("是否完成作業與平均分數之關係")
    question_3(csv_file, folder_name)

    print("父母最高教育程度與平均分數之關係")
    question_4(csv_file, folder_name)

    print("性別與平均分數之關係")
    question_5(csv_file, folder_name)

    print("寫作分數與閱讀分數之關係")
    question_6(csv_file, folder_name)