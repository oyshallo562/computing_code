import random
import tkinter as tk
from tkinter import ttk
import time

class TypingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("타자 게임")
        self.geometry("500x600")
        self.configure(bg="#f0f0f0")

        # 단어 리스트 (로마자 표기로 변경)
        self.easy_words = ["사과", "바나나", "오렌지", "포도", "딸기", "복숭아", "배", "수박", "귤", "체리"]
        self.medium_words = ["애플망고", "파인애플", "블루베리", "망고스틴", "키위", "자두", "석류", "복분자", "라임", "구아바"]
        self.hard_words = ["파파야", "두리안", "용과", "산딸기", "천혜향", "자몽", "레몬", "살구", "무화과", "아보카도"]

        # 게임 변수
        self.words = []
        self.current_word = ""
        self.chances = 3
        self.score = 0
        self.start_time = 0
        self.max_time = 10  # 최대 시간 (점수 계산 기준)
        self.timer_id = None
        self.game_active = False

        # GUI 구성
        self.create_widgets()

    def create_widgets(self):
        # 난이도 선택 프레임
        self.difficulty_frame = tk.Frame(self, bg="#f0f0f0")
        self.difficulty_frame.pack(pady=10)

        tk.Label(self.difficulty_frame, text="난이도 선택:", font=("맑은 고딕", 12), bg="#f0f0f0").pack(side=tk.LEFT)
        self.difficulty_var = tk.StringVar(value="medium")
        tk.Radiobutton(self.difficulty_frame, text="쉬움", value="easy", variable=self.difficulty_var, font=("맑은 고딕", 10), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.difficulty_frame, text="보통", value="medium", variable=self.difficulty_var, font=("맑은 고딕", 10), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(self.difficulty_frame, text="어려움", value="hard", variable=self.difficulty_var, font=("맑은 고딕", 10), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)

        # 점수와 기회 라벨
        self.score_label = tk.Label(self, text=f"점수: {self.score}", font=("맑은 고딕", 12), bg="#f0f0f0")
        self.score_label.pack(pady=5)

        self.chances_label = tk.Label(self, text=f"남은 기회: {self.chances}", font=("맑은 고딕", 12), bg="#f0f0f0")
        self.chances_label.pack(pady=5)

        # 타이머 라벨
        self.timer_label = tk.Label(self, text="남은 시간: 10.0초", font=("맑은 고딕", 12), bg="#f0f0f0")
        self.timer_label.pack(pady=5)

        # 단어 표시 라벨
        self.word_label = tk.Label(self, text="게임 시작 버튼을 눌러주세요!", font=("맑은 고딕", 16, "bold"), bg="#f0f0f0")
        self.word_label.pack(pady=20)

        # 결과 라벨
        self.result_label = tk.Label(self, text="", font=("맑은 고딕", 12), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        # 입력창
        self.input_entry = tk.Entry(self, font=("맑은 고딕", 12), width=20)
        self.input_entry.pack(pady=10)
        self.input_entry.bind("<Return>", self.check_input)

        # 입력 히스토리 리스트박스
        self.history_label = tk.Label(self, text="입력 히스토리", font=("맑은 고딕", 12), bg="#f0f0f0")
        self.history_label.pack(pady=5)
        self.history_listbox = tk.Listbox(self, font=("맑은 고딕", 10), height=5, width=40)
        self.history_listbox.pack(pady=5)

        # 게임 시작 버튼
        self.start_button = tk.Button(self, text="게임 시작", command=self.start_game, font=("맑은 고딕", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=20)

    def set_difficulty(self):
        # 난이도에 따라 단어 리스트 설정
        difficulty = self.difficulty_var.get()
        if difficulty == "easy":
            self.words = self.easy_words
        elif difficulty == "medium":
            self.words = self.medium_words
        elif difficulty == "hard":
            self.words = self.hard_words

    def start_game(self):
        # 초기화
        self.score = 0
        self.chances = 3
        self.score_label.config(text=f"점수: {self.score}")
        self.chances_label.config(text=f"남은 기회: {self.chances}")
        self.result_label.config(text="")
        self.history_listbox.delete(0, tk.END)
        self.input_entry.delete(0, tk.END)
        self.input_entry.config(state="disabled")
        self.start_button.config(state="disabled")

        # Frame의 자식 위젯(Radiobutton 등)을 비활성화
        for widget in self.difficulty_frame.winfo_children():
            if isinstance(widget, tk.Radiobutton):  # Radiobutton만 비활성화
                widget.config(state="disabled")

        self.set_difficulty()
        self.game_active = False

        # 카운트다운 시작
        self.countdown(3)

    def countdown(self, count):
        # 3초 카운트다운
        if count > 0:
            self.word_label.config(text=f"게임 시작까지 {count}초")
            self.after(1000, self.countdown, count - 1)
        else:
            self.word_label.config(text="시작!")
            self.game_active = True
            self.new_word()

    def new_word(self):
        # 새로운 단어 선택 및 타이머 시작
        self.current_word = random.choice(self.words)
        self.word_label.config(text=f"단어: {self.current_word}")
        self.input_entry.config(state="normal")
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        # 타이머 업데이트
        if not self.game_active:
            return
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.max_time - elapsed_time)
        self.timer_label.config(text=f"남은 시간: {remaining_time:.1f}초")
        if remaining_time > 0:
            self.timer_id = self.after(100, self.update_timer)
        else:
            # 시간 초과 시 오답 처리
            self.chances -= 1
            self.result_label.config(text="시간 초과!", fg="red")
            self.history_listbox.insert(tk.END, f"단어: {self.current_word} - 시간 초과")
            self.chances_label.config(text=f"남은 기회: {self.chances}")
            self.check_game_over()

    def check_input(self, event=None):
        if not self.game_active:
            return

        # 타이머 중지
        if self.timer_id:
            self.after_cancel(self.timer_id)

        # 사용자 입력 확인
        user_input = self.input_entry.get().strip()
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        # 시간에 따른 점수 계산
        if elapsed_time < self.max_time:
            time_score = int((self.max_time - elapsed_time) * 10)  # 최대 100점
        else:
            time_score = 0

        # 정답/오답 처리
        if user_input == self.current_word:
            self.score += time_score
            self.result_label.config(text=f"정답! (+{time_score}점)", fg="green")
            self.history_listbox.insert(tk.END, f"단어: {self.current_word} - 정답 (+{time_score}점)")
        else:
            self.chances -= 1
            self.result_label.config(text="오답!", fg="red")
            self.history_listbox.insert(tk.END, f"단어: {self.current_word} - 오답")

        # 점수와 기회 업데이트
        self.score_label.config(text=f"점수: {self.score}")
        self.chances_label.config(text=f"남은 기회: {self.chances}")
        self.check_game_over()

    def check_game_over(self):
        if self.chances > 0:
            # 다음 단어로 이동
            self.new_word()
        else:
            # 게임 종료
            self.game_active = False
            self.word_label.config(text=f"게임 종료! 최종 점수: {self.score}")
            self.result_label.config(text="")
            self.timer_label.config(text="남은 시간: 10.0초")
            self.input_entry.config(state="disabled")
            self.start_button.config(text="다시 시작", state="normal")

            # Frame의 자식 위젯(Radiobutton 등)을 활성화
            for widget in self.difficulty_frame.winfo_children():
                if isinstance(widget, tk.Radiobutton):  # Radiobutton만 활성화
                    widget.config(state="normal")

if __name__ == "__main__":
    game = TypingGame()
    game.mainloop()