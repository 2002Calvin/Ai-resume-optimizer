import tkinter as tk
from tkinter import scrolledtext, messagebox
from optimizer import optimize_resume
import os


API_KEY = os.environ.get('API_KEY')  #here the teacher mr Nguh will have to put his own api key since i cannot share mine

def run_optimizer():
    resume = input_text.get("1.0", tk.END).strip()
    if not resume:
        messagebox.showwarning("Input Missing", "Please paste your resume.")
        return
    try:
        result = optimize_resume(resume, API_KEY)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
window = tk.Tk()
window.title("AI Resume Optimizer")
window.geometry("900x600")

tk.Label(window, text="Paste your resume below:", font=("Arial", 12)).pack()
input_text = scrolledtext.ScrolledText(window, height=10, wrap=tk.WORD)
input_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

tk.Button(window, text="Optimize Resume", command=run_optimizer, bg="blue", fg="white").pack(pady=10)

tk.Label(window, text="Optimized Resume:", font=("Arial", 12)).pack()
output_text = scrolledtext.ScrolledText(window, height=10, wrap=tk.WORD)
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

window.mainloop()
