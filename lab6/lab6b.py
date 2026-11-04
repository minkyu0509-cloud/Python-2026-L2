import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 

df = pd.read_csv('scores.csv')

plt.figure(figsize=(12,6))
plt.scatter(df['student_id'], df['math'], label= 'Math' , color='red', alpha= 0.7)
plt.scatter(df['student_id'], df['python'],label= 'Python' , color='blue', alpha= 0.7)
plt.scatter(df['student_id'], df['database'],label= 'Database' , color='green', alpha= 0.7)
plt.title('biểu đồ phân tán điểm số của sinh viên')
plt.xlabel('Student ID')
plt.ylabel('Scores')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('scattered.png')
plt.close()

fig, axes = plt.subplots(1,3, figsize=(15,5))
axes[0].hist(df['math'].dropna(),bins=10, color='red', edgecolor='black')
axes[0].set_title('Math Scores Distribution')
axes[1].hist(df['python'].dropna(),bins=10, color='blue', edgecolor='black')
axes[1].set_title('Python Scores Distribution')
axes[2].hist(df['database'].dropna(),bins=10, color='green', edgecolor='black')
axes[2].set_title('Database Scores Distribution')
plt.tight_layout()
plt.savefig('histo.png')
plt.close()

plt.figure(figsize=(8,5))
df[['math', 'python', 'database']].boxplot()
plt.title('Boxplot of Scores')
plt.ylabel('Scores')
plt.savefig('box.png')
plt.close()

print('The plots have been saved as "scattered.png", "histo.png", and "box.png".')
plt.show()

