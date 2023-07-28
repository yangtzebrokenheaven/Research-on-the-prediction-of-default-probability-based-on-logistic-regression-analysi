import pandas as pd
# 读取 Excel 文件
data = pd.read_excel(r'C:\\Users\\34844\\Desktop\\附件2.xlsx',sheet_name=1)
# 确保只考虑有效发票
data = data[data['发票是否有效'] == 1]
# 将日期列转换为 datetime 类型，并提取出年份和月份
data['发票日期'] = pd.to_datetime(data['发票日期'])
data['年份'] = data['发票日期'].dt.year
data['月份'] = data['发票日期'].dt.month
# 计算半年标识
data['半年'] = 'H1'
data.loc[data['月份'] > 6, '半年'] = 'H2'
# 计算每个样本每半年的有效发票金额
data['年份半年'] = data['年份'].astype(str) + data['半年']
grouped = data.groupby(['样本代号', '年份半年'])['发票金额'].sum()
# 转换为宽表格格式
results = grouped.unstack()
# 保存到新的 Excel 文件
results.to_excel('results.xlsx')
