

import matplotlib.pyplot as plt 
import numpy as np 

# 다항식
fp1 = np.polyfit(df['계'], df['소계'], 1)
f1 = np.poly1d(fp1)
print(f1)

# 잔차 계산
df['잔차'] = np.abs(df['소계'] - f1(df['계']))
plt.figure(figsize=(14,12))
plt.scatter(df['계'], df['소계'], c=df['잔차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

# 그래프에 텍스트 출력하기
for n in range(25) : 
    # 각 점들의 좌표 우측 
    plt.text(df['계'][n] * 1.02, 
             df['소계'][n] * 1, 
             df.index[n], 
             fontsize=12)

             