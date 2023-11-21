# main_program.py
import os
import sys
import tkinter as tk
from tkinter import Text, BOTH

# 現在のディレクトリをPythonのパスに追加
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from program1 import run_program as run_program1
from program2 import run_program as run_program2

class ProgramFrame(tk.Frame):
    def __init__(self, master=None, program_text=""):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.create_widgets(program_text)

    def create_widgets(self, program_text):
        self.program_text = Text(self)
        self.program_text.insert(tk.END, program_text)
        self.program_text.pack(fill=BOTH, expand=True)

def main():
    root = tk.Tk()
    root.title("異なるファイルからのプログラム呼び出し")

    program1_text = run_program1()
    program2_text = run_program2()

    program_frame1 = ProgramFrame(root, program_text=program1_text)
    program_frame2 = ProgramFrame(root, program_text=program2_text)

    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
