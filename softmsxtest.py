import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 读取数据
data = pd.read_excel(r'C:\\Users\34844\\Desktop\\3指标 (1).xlsx')

# 假设前三列是特征，第四列是目标变量
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 划分训练集和测试集，80%的数据用于训练，20%的数据用于测试
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建并拟合模型
model = LogisticRegression()
model.fit(X_train, y_train)

# 在测试集上做预测
y_test_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_test_pred)
print(f"Accuracy: {accuracy}")

# 计算混淆矩阵
tn, fp, fn, tp = confusion_matrix(y_test, y_test_pred).ravel()

# 绘制TP、TN、FP、FN
plt.bar(['TP', 'TN', 'FP', 'FN'], [tp, tn, fp, fn])
plt.show()
