import tkinter as tk
from tkinter import messagebox
import os

base_dir = "/home/lasha/lessons.linux/lesson3/"

topics = {
    "Linux ადმინისტრირება N3. ფაილური სისტემები. Linux-ის კატალოგების სტრუქტურა": [
        ("Linux-ის ძირითადი დირექტორიების სტრუქტურა", "examen"),
        ("ჟურნალირება ლინუქსში", "ჟურნალირება"),
        ("backup", "backup"),
        ("snapshot", "snapshot"),
        ("indexing", "indexing"),
        ("Defragmentation", "Defragmentation"),
        ("drive fooling", "drive.fooling"),
        ("Filesystem Striping", "filesystem.striping"),
        ("swap", "swap")
    ],
    "ლინუქსი 2": [("ლაშა", "tema2_1.txt"), ("2", "tema2_2.txt"), ("3", "tema2_3.txt"), ("4", "tema2_4.txt"), ("5", "tema2_5.txt")],
    "თემა 3": [("ლაშა", "tema3_1.txt"), ("2", "tema3_2.txt"), ("3", "tema3_3.txt"), ("4", "tema3_4.txt"), ("5", "tema3_5.txt")],
}

def open_file(filepath, text_widget):
    full_path = os.path.join(base_dir, filepath)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", content)
    else:
        messagebox.showerror("შეცდომა", f"ფაილი ვერ მოიძებნა:\n{full_path}")

def open_topic_window(topic_name, items):
    topic_win = tk.Toplevel(root)
    topic_win.title(topic_name)
    topic_win.geometry("1000x700")
    topic_win.configure(bg="#2e2e2e")

    left_panel = tk.Frame(topic_win, bg="#2e2e2e", width=300)
    left_panel.pack(side="left", fill="y")

    right_panel = tk.Frame(topic_win, bg="#2f2f2f")
    right_panel.pack(side="right", expand=True, fill="both")

    text_area = tk.Text(right_panel, wrap="word", bg="#333333", fg="white", font=("Arial", 12))
    text_area.pack(expand=True, fill="both", padx=10, pady=10)

    for label, path in items:
        btn = tk.Button(left_panel, text=label, font=("Arial", 12), bg="white", fg="black",
                        relief="flat", height=2, width=25,
                        command=lambda p=path: open_file(p, text_area),
                        activebackground="#007bff", activeforeground="white",
                        wraplength=200, justify="center")
        btn.pack(pady=5, padx=10, fill="x")

root = tk.Tk()
root.title("ლინუქსის გაკვეთილები")
root.geometry("700x500")
root.configure(bg="#2e2e2e")

title = tk.Label(root, text="თემების მენიუ", font=("Arial", 16, "bold"), bg="#2e2e2e", fg="white")
title.pack(pady=20)

# ერთნაირი ღილაკები
for topic, items in topics.items():
    btn = tk.Button(root, text=topic, font=("Arial", 12), bg="white", fg="black",
                    relief="flat", height=3, width=40,
                    command=lambda t=topic, i=items: open_topic_window(t, i),
                    activebackground="#007bff", activeforeground="white",
                    wraplength=300, justify="center")
    btn.pack(pady=10)

root.mainloop()

