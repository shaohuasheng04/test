import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件数据
df = pd.read_excel('F1-score.xlsx')

# 提取数据列
methods = df.columns[0:]
data = df.values[:, 0:]

# 绘制折线图
plt.figure(figsize=(10, 6))  # 设置图表大小

for i in range(len(methods)):
    plt.plot(df.index, data[:, i], linestyle='-', label=methods[i], linewidth=2)

plt.xlabel('File index')
plt.ylabel('F1-score')
plt.title('F1-score Comparison')
plt.legend()
plt.grid(True)
plt.savefig("F1-score.png")

# 显示图表
plt.show()