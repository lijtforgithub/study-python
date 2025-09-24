import pandas as pd
import random
import json
import os

# =================== 配置参数 ===================
excel_file = '/Users/lijingtang/Downloads/实验数据3.xlsx'        # Excel 文件路径
output_dir = '/Users/lijingtang/Downloads/output_json3'          # 输出目录
first_file_size = 50                # 第一个文件抽 50 条
other_file_count = 10               # 后面 10 个文件
other_file_size = 10                # 每个 10 条
total_needed = first_file_size + other_file_count * other_file_size  # 150
seed = 42                           # 可复现的随机种子
# ==============================================

# 设置随机种子（确保结果可复现）
random.seed(seed)

# 创建输出目录
os.makedirs(output_dir, exist_ok=True)

# 读取所有 sheet 并合并
print("正在读取 Excel 文件...")
xl = pd.ExcelFile(excel_file)
df_list = []

for sheet_name in xl.sheet_names:
    df = xl.parse(sheet_name)
    df_list.append(df)

# 合并所有数据
df = pd.concat(df_list, ignore_index=True)
df.dropna(how='all', inplace=True)  # 删除完全空行

data_records = df.to_dict(orient='records')
print(f"共加载 {len(data_records)} 条有效数据。")

# 检查数据是否足够
if len(data_records) < total_needed:
    raise ValueError(f"数据不足 {total_needed} 条，当前仅有 {len(data_records)} 条！")

# 随机打乱数据（不可重复抽取的关键）
random.shuffle(data_records)

# 分配数据
print(f"开始分配 {total_needed} 条不重复数据...")

# 第 1 份：50 条
part1 = data_records[:first_file_size]
with open(os.path.join(output_dir, 'data_1.json'), 'w', encoding='utf-8') as f:
    json.dump(part1, f, ensure_ascii=False, indent=2)
print(f"✅ 已生成 data_1.json (50 条)")

# 第 2 到第 11 份：每份 10 条（共 100 条）
start_idx = first_file_size
for i in range(2, 12):
    end_idx = start_idx + other_file_size
    part = data_records[start_idx:end_idx]
    filename = f'data_{i}.json'
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
        json.dump(part, f, ensure_ascii=False, indent=2)
    print(f"✅ 已生成 {filename} (10 条)")
    start_idx = end_idx

print("\n🎉 所有 11 个 JSON 文件生成完成！")
print(f"📁 输出目录: {os.path.abspath(output_dir)}")
print("💡 所有数据均不重复，且已确保随机性（使用 seed=42）")