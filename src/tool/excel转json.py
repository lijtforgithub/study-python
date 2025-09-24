import pandas as pd

# 读取 Excel 文件（支持 .xlsx 和 .xls）
file_path = '/Users/lijingtang/Downloads/联邦学习/单节点苏州.xlsx'  # 替换为你的文件路径
sheet_name = 'Sheet1'         # 替换为工作表名称，或使用索引如 0
output_json = '/Users/lijingtang/Downloads/联邦学习/output_json_9019.json'         # 替换为工作表名称，或使用索引如 0

# 读取 Excel 到 DataFrame
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 转换为 JSON
json_result = df.to_json(orient='records', force_ascii=False, indent=2)

# 打印或保存到文件
print(json_result)

# 保存到文件
with open(output_json, 'w', encoding='utf-8') as f:
    f.write(json_result)