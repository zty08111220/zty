import pandas as pd

# 读取Excel文件
data = pd.read_excel("C:/Users/左庭宇/Desktop/原始数据.xlsx")

# 删除学号字段
data = data.drop("学号", axis=1) 

# 清理数据
data["所在院系"] = data["所在院系"].str.replace("-", "")  # 清理所在院系字段中的"-"

# 清理数据
data["状态"] = data["状态"].str.replace("signin", "")  # 清理状态字段中的"signin"

# 保存清洗后的数据到新的Excel文件
data.to_excel("C:/Users/左庭宇/Desktop/cleaned_data.xlsx", index=False)

