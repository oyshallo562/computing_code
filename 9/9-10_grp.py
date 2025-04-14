import tkinter as tk
from tkinter import messagebox

# 한-영 단어 사전
dictionary = {
    "사과": "apple",
    "바나나": "banana",
    "오렌지": "orange",
    "딸기": "strawberry",
    "포도": "grape"
}

# 번역 실행 함수
def translate():
    word = entry.get().strip()
    if word == "":
        result_label.config(text="⚠️ 단어를 입력해주세요!", fg="red")
    elif word in dictionary:
        result_label.config(text=f"✅ {word} → {dictionary[word]}", fg="white")
    else:
        result_label.config(text="❌ 사전에 없는 단어입니다.", fg="yellow")

# 종료 함수
def quit_app():
    if messagebox.askyesno("종료 확인", "정말 종료하시겠습니까?"):
        root.destroy()

# 윈도우 설정
root = tk.Tk()
root.title("한-영 단어 번역기")
root.geometry("800x600")
root.configure(bg="green")

# 폰트 설정
FONT_LARGE = ("Arial", 24, "bold")
FONT_MEDIUM = ("Arial", 16)
FONT_SMALL = ("Arial", 12)

# 타이틀
title = tk.Label(root, text="🍏 한-영 과일 단어 번역기 🍇", font=FONT_LARGE, bg="green", fg="white")
title.pack(pady=40)

# 입력 필드
entry = tk.Entry(root, font=FONT_MEDIUM, width=30, justify="center")
entry.pack(pady=20)

# 번역 결과 표시
result_label = tk.Label(root, text="", font=FONT_LARGE, bg="green")
result_label.pack(pady=30)

# 버튼 프레임
btn_frame = tk.Frame(root, bg="green")
btn_frame.pack(pady=20)

# [번역하기] 버튼
translate_btn = tk.Button(
    btn_frame, text="🔍 번역하기", font=FONT_MEDIUM,
    width=15, bg="white", fg="green", command=translate
)
translate_btn.grid(row=0, column=0, padx=20)

# [종료하기] 버튼
exit_btn = tk.Button(
    btn_frame, text="❌ 종료하기", font=FONT_MEDIUM,
    width=15, bg="white", fg="red", command=quit_app
)
exit_btn.grid(row=0, column=1, padx=20)

# 도움말
help_label = tk.Label(root, text="※ 예: 사과, 바나나, 오렌지, 딸기, 포도", font=FONT_SMALL, bg="green", fg="white")
help_label.pack(pady=10)

# GUI 실행
root.mainloop()
