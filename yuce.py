import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
import matplotlib.pyplot as plt

# 读取训练数据
train_data = pd.read_excel(r'C:\\Users\34844\\Desktop\\3指标 (1).xlsx')

# 假设前三列是特征，第四列是目标变量
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

# 创建并拟合模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 读取新数据
new_data = pd.read_excel('C:\\Users\\34844\\Desktop\\第二问期望，标准差，占比.xlsx', )

# 假设前三列是特征
X_new = new_data.iloc[:, :]

# 在新数据上预测违约概率
new_pred = model.predict_proba(X_new)

# 将预测的概率矩阵写入新的Excel文件
pd.DataFrame(new_pred).to_excel('predicted_probabilities.xlsx', index=False)

# 计算训练集的预测值
y_train_pred = model.predict(X_train)

# 计算准确率和对数损失
accuracy = accuracy_score(y_train, y_train_pred)
loss = log_loss(y_train, y_train_pred)

# 打印准确率和对数损失
print(f'Training Accuracy: {accuracy}')
print(f'Training Log Loss: {loss}')

# 绘制准确率和对数损失
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(['Accuracy'], [accuracy])
plt.ylim([0, 1])
plt.subplot(1, 2, 2)
plt.bar(['Log Loss'], [loss])
plt.show()
