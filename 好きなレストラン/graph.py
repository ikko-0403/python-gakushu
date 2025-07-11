import csv
import matplotlib.pyplot as plt
import os

summary_path = '好きなレストラン/restaurant_summary.csv'

# ファイルが存在するか確認
if not os.path.exists(summary_path):
    print("集計ファイルがありません。先に投票をしてから実行してね。")
    exit()

# データ読み込み
restaurants = []
votes = []

with open(summary_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        restaurants.append(row['レストラン'])
        votes.append(int(row['票数']))

# グラフ描画
plt.figure(figsize=(10, 5))
plt.bar(restaurants, votes)
plt.xlabel('レストラン名')
plt.ylabel('票数')
plt.title('🍽 人気レストランランキング')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
