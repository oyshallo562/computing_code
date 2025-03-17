import tkinter as tk

window = tk.Tk()
window.title("test")
window.geometry("500x500+500+150")
window.resizable(True,True)

label=tk.Label(window,text="이것은텍스트다.",width=10,height=5)
label.pack()

button=tk.Button(window,text="이것은버튼이다.",padx=30,pady=15,fg="white",bg="black")
button.pack()

entry=tk.Entry(window,)
entry.pack()

window.mainloop()