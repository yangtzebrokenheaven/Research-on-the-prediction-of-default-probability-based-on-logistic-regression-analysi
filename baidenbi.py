import pandas as pd
# 读取Excel文件，并只选取"Amount"和"IsValid"这两列
data = pd.read_excel('C:\\Users\\34844\\Desktop\\附件2.xlsx', usecols=[1, 7, 8])
data.columns = ['Sample', 'Amount', 'IsValid']
# 将数据按照'Sample'列进行分组
grouped = data.groupby('Sample')

# 初始化一个空的字典来存储每个样本的结果
results = {}

# 遍历每一个分组

for name, group in grouped:
    # 在当前分组中，选取发票有效的数据
    valid_data = group[group['IsValid'] == 1]['Amount']

    # 计算有效数据中小于0的数据的数量
    count_negative = (valid_data < 0).sum()

    # 计算有效数据的总数量
    count = len(valid_data)

    # 计算小于0的数据的量占比，并将结果存储到字典中
    results[name] = count_negative / count

results_df = pd.DataFrame(list(results.items()), columns=['Sample', 'Proportion'])

# 将结果写入到新的Excel文件中
results_df.to_excel('results1.xlsx', index=False)















































  