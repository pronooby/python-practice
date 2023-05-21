import csv

# 새로운 데이터를 작성할 파일명
filename = "data.csv"

# 입력받은 데이터를 리스트에 추가합니다
data = []
while True:
    user = input("유저 이름을 입력하세요 (종료하려면 q를 입력하세요): ")
    if user == "q":
        break
    character = input("캐릭터 이름을 입력하세요: ")
    level = input("레벨을 입력하세요: ")
    data.append([user, character, level])

# 데이터를 파일에 작성합니다
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
