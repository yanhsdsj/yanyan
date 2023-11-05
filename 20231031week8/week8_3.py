#seaborn

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 构造数据集
data = {"total_bill": [16.99, 10.34, 21.01, 23.68, 24.59],
        "tip": [1.01, 1.66, 3.50, 3.31, 3.61],
        "sex": ["Female", "Male", "Male", "Male", "Female"],
        "smoker": ["No", "No", "No", "No", "No"],
        "day": ["Sun", "Rain", "Cloudy", "Sun", "Sun"],
        "time": ["Dinner", "Dinner", "Dinner", "Dinner", "Dinner"],
        "size": [2, 3, 3, 2, 4]}

# 转换为 DataFrame 格式
tips = pd.DataFrame(data)
fig, axs = plt.subplots(1,3, figsize = (12, 4))
# 保存为 CSV 文件
tips.to_csv("tips.csv", index=False)
# x = np.random.normal(size=100)
# y = np.random.normal(size=100)
#设置二十个分组
#kde=True绘制出数据分布曲线
sns.scatterplot(data = tips, x = "total_bill", y = "tip", ax = axs[0])   #   散点图
# plt.show()
sns.lineplot(data = tips, x = "total_bill", y = "tip", ax = axs[1])                 #   折线图
# plt.show()
sns.barplot(data = tips, x = "day", y = "total_bill", ax = axs[2])      #   条形图


axs[0].set_title("scatterplot")
axs[0].set_title("lineplot")
axs[0].set_title("barplot")

plt.tight_layout()      #   调整子图间距

plt.show()

# 可以用plt的plt.subplots功能来把图片打印在一张里
