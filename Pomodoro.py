import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import threading

class Pomodoro:
    def __init__(self, root):
        self.root = root
        self.is_running = False

    def work_break(self, timer):
        #common block to display minutes and seconds on GUI
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        if timer > 0:
            self.root.after(1000, self.work_break, timer - 1) #Schedule next update
        else:
            # Once work is done play a sound and switch for a break
            playsound("sound.ogg")
            messagebox.showinfo("Good Job", "Take A Break!")
            self.start_break_timer()

    def start_break_timer(self):
        break_timer = 5 * 60 #Set break time (5 minutes)
        self.work_break(break_timer)

    def work(self):
       if not self.is_running:
        self.is_running = True
        timer = 25 * 60 #Work time (25 minutes)
        self.work_break(timer)

    def main(self):

        # GUI window configuration
        self.root.geometry("450x455")
        self.root.resizable(False,False)
        self.root.title("Pomodoro Timer")

        # label
        self.min = tk.StringVar(self.root)
        self.min.set("25")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root, textvariable=self.min, font= ("Arial", 22, "bold"), bg="black", fg='white')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root, textvariable=self.sec, font=("arial", 22, "bold"), bg="black", fg='white')
        self.sec_label.pack()

        # create three buttons with countdown functions command
        btn_work = tk.Button(self.root, text="Start", bd=5, command=self.work, bg="lightyellow", font=("arial", 15, "bold")).place(x=240, y=380)

        self.root.mainloop()

if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()