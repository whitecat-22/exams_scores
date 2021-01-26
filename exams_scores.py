import pandas as pd
import matplotlib.pyplot as plt

book = pd.ExcelFile('exams_scores.xlsx')
sheet_name = book.sheet_names
sheet_df = book.parse(sheet_name[0])

i = 0
label = []
x = []
height = []
print("氏名", "国語", "数学", "英語", "理科", "社会", "合計点")
for i, col in sheet_df.iterrows():
    label.append(col[0])
    x = label
    height.append(col[1]+col[2]+col[3]+col[4]+col[5])
    print(i, col[0], col[1], col[2], col[3], col[4], col[5], height[i])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(x, height, label=label, linewidth=1, edgecolor="#000000")
plt.show()
