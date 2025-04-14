import random
import tkinter as tk
from tkinter import messagebox

def recommend_lunch():
    lunch_options = ["김밥", "라면", "비빔밥", "떡볶이", "피자", "햄버거"]
    recommendation = random.choice(lunch_options)
    # 메시지 박스로 추천 결과 표시
    messagebox.showinfo("점심 추천", f"추천 점심 메뉴: {recommendation}")

# GUI 창 생성
window = tk.Tk()
window.title("점심 메뉴 추천기")
window.geometry("300x150")

# 안내 라벨 추가
label = tk.Label(window, text="버튼을 눌러 점심 메뉴를 추천받으세요!", font=("맑은 고딕", 12))
label.pack(pady=20)

# 추천 버튼 추가
button = tk.Button(window, text="메뉴 추천받기", command=recommend_lunch, font=("맑은 고딕", 10))
button.pack(pady=10)

# 창 실행
window.mainloop()