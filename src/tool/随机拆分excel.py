import pandas as pd
import numpy as np

# 章节一：准备环境与导入必要的库
np.random.seed(42)  # 设置随机种子，保证结果可重复

# 章节二：读取Excel中第3行到第454行的数据（对应pandas索引2到453）
file_path = '/Users/lijingtang/Downloads/实验数据.xlsx'  # 替换为你的实际文件路径
sheet_name = 0  # 可以指定sheet名称或索引

# 读取Excel数据
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 提取第3行到第454行（pandas索引从0开始，所以是2到453）
data = df.iloc[2:454].reset_index(drop=True)
print(f"读取了 {len(data)} 行数据")

# 章节三：随机打乱并分割数据
shuffled_data = data.sample(frac=1).reset_index(drop=True)  # 打乱顺序
split_data = np.array_split(shuffled_data, 3)  # 分成三份

# 保存到新的Excel文件，每个部分在一个Sheet中
output_file = '/Users/lijingtang/Downloads/拆分后的实验数据.xlsx'
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    for i, subset in enumerate(split_data):
        sheet_name = f'Part_{i+1}'
        sorted_subset = subset.sort_values(by=subset.columns[0], ascending=True).reset_index(drop=True)
        sorted_subset.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"数据已成功随机分成三份，并保存到 '{output_file}' 的三个Sheet中。")