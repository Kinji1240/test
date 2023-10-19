import tkinter as tk
import subprocess

def call_analogtime():
    try:
        subprocess.run(["python", "C:\\Users\\204004\\Desktop\\test\\testplay\\analogtime.py"])
    except Exception as e:
        print(f"Error: {e}")

def call_another_script():
    try:
        subprocess.run(["python", "C:\\Users\\204004\\Desktop\\test\\testplay\\time.py"])
    except Exception as e:
        print(f"Error: {e}")

def main():
    root = tk.Tk()
    root.title("Main Program")

    button1 = tk.Button(root, text="Display Analog Time", command=call_analogtime)
    button1.pack(pady=20)

    button2 = tk.Button(root, text="Run Another Script", command=call_another_script)
    button2.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()