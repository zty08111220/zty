import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取CSV文件 这个得根据实际情况变更
#！！！
data = pd.read_csv('E:/Git/zty/tenth_week/coffee.csv')

#coffee.csv的纵轴的含义
"""
Shop – ID number of shop
Chain - Thanks a Latte = 1	Deja Brew = 2
Sales - Weekly Sales in 1,000, so 5 = $5,000 in sales
Costs - Weekly Costs in 1,000, so 5 = $5,000 in sales
Employees – number of employees in shop
Distrival – how far in miles to the nearest rival coffeeshop
DistWLL – how far in miles to the nearest Whole Latte Love coffeeshop
YearOp – Year opened
BusTime - Busiest time of day, using 24 hour clock
Happy – Do patrons look happy? 1=not at all 7=very much
Clean – Is the shop clean? 1=not at all 7=very much
SocMedia – Is the shop active on social media? 1=not at all 7=very much
TradMedia - Is the shop active on traditional media? 1=not at all 7=very much
DrinkPcnt - % sales which are drinks
Recommendations – Has it got recommendations online? 1=not at all 7=very much
Sqft - Square footage of shop
Environ – How environmentally friendly is the store? 1=not at all 7=very much
Salechange - % increase or decrease in sales last 12 months compared to prior 12 months
"""

#预处理
# 处理缺失值
# 对于Sales列，使用均值填充缺失值：
data['Sales'].fillna(data['Sales'].mean(), inplace=True)

# 处理异常值
# 对于Sales列，删除小于0的异常值：
data = data[data['Sales'] >= 100]

# 特征缩放
# 特征之间的数值范围差异较大，可以使用特征缩放方法，如标准化或归一化
# 对于'Sqft'列，使用标准化进行特征缩放：
data['Sqft'] = (data['Sqft'] - data['Sqft'].mean()) / data['Sqft'].std()

#可视化
#clean和对应sales均值的组成的柱状图
clean_sales_mean = data.groupby('Clean')['Sales'].mean()

#设置图表大小
plt.figure(figsize=(8, 6))

#绘制柱状图
sns.barplot(x='Clean', y='Sales', data=data, ci=None)

#显示均值
for i, (clean, sales_mean) in enumerate(clean_sales_mean.items()):
    plt.text(i, sales_mean, f'{sales_mean:.2f}', ha='center', va='bottom')

#添加标题和轴标签
plt.title('Sales by Clean')
plt.xlabel('Clean')
plt.ylabel('Average Sales')

#显示图表
plt.show()
