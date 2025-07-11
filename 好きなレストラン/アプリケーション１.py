import csv
import os

# ==== 保存先 ====
folder = '好きなレストラン'
log_path = os.path.join(folder, 'restaurant_log.csv')
summary_path = os.path.join(folder, 'restaurant_summary.csv')

# ==== 票を加算する関数 ====
def add_vote(restaurant_name):
    data = {}
    if os.path.exists(summary_path):
        with open(summary_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data[row['レストラン']] = int(row['票数'])
    data[restaurant_name] = data.get(restaurant_name, 0) + 1
    with open(summary_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['レストラン', '票数'])
        for name, count in data.items():
            writer.writerow([name, count])

# ==== ログ保存関数 ====
def log_vote(name, restaurant):
    os.makedirs(folder, exist_ok=True)
    write_header = not os.path.exists(log_path)
    with open(log_path, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(['名前', 'レストラン'])
        writer.writerow([name, restaurant])

# ==== スタート ====
print("こんにちは！おすすめレストラン投票アプリです🍽")
name = input("まず、お名前を教えてください：").strip()

# ==== 過去のおすすめ一覧を取得 ====
unique_restaurants = []
if os.path.exists(log_path):
    with open(log_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        seen = set()
        for row in reader:
            r = row['レストラン']
            if r not in seen:
                seen.add(r)
                unique_restaurants.append(r)

liked = False  # Yes が出たかどうか

# ==== おすすめの提示 ====
for rec in unique_restaurants:
    while True:
        print(f"\n{name}さん、私のオススメのレストランは「{rec}」です。")
        answer = input("このレストランは好きですか？ [Yes/No]：").strip().lower()

        if answer in ['yes', 'y']:
            add_vote(rec)
            log_vote(name, rec)
            print("✅ 投票を記録しました！ありがとうございます！")
            liked = True
            break
        elif answer in ['no', 'n']:
            print("😌 そっか、じゃあ他のレストランも見てみましょ！")
            break
        else:
            print("⚠️ Yes か No（または Y/N）で答えてください")

    if liked:
        break  # Yesが出たらすぐ質問終了

# ==== すべてNoだった場合だけ、好きなレストランを聞く ====
if not liked:
    fav = input(f"\n{name}さんの好きなレストランをぜひ教えてください！：").strip()
    add_vote(fav)
    log_vote(name, fav)
    print(f"✅ 「{fav}」に投票しました！教えてくれてありがとう✨")
else:
    print(f"\n{name}さん、また投票しに来てね！😊")


# ==== 最後に現在の集計結果を表示 ====
if os.path.exists(summary_path):
    print("\n📊 現在の人気レストラン投票状況：")
    with open(summary_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['レストラン']
            count = row['票数']
            print(f"{name}: {count}票")
