import os
import tkinter as tk
from tkinter import filedialog

phraze = "[SPOTIFY-DOWNLOADER.COM] "
print(len(phraze))
num_of_files = 0


def update_num_entry(event):
    num_entry.delete(0, tk.END)
    num_entry.insert(tk.END, len(txt_entry.get()))


def shorten_filenames():
    global num_of_files
    folder_path = filedialog.askdirectory()  # Open dialog to select folder
    # get number from text field
    num_str = str(txt_entry.get())
    n = len(num_str)
    # n = int(num_entry.get())  # Get number from entry field
    for filename in os.listdir(folder_path):
        if len(filename) > n:
            new_filename = filename[n:]  # Remove first n symbols
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_filename),
            )
            num_of_files += 1

    tk.messagebox.showinfo(title="Done", message=f"{num_of_files} files renamed.")


# Create GUI window
window = tk.Tk()
window.title("Shorten Filenames")
window.geometry("600x400")

# Add UI elements
folder_button = tk.Button(window, text="Select Folder", command=shorten_filenames)
folder_button.pack(pady=10)

num_label = tk.Label(window, text="Text at the beginning to remove:")
num_label.pack()

txt_entry = tk.Entry(window, width=200)
txt_entry.insert(0, phraze)
txt_entry.pack(padx=10, pady=5, expand=tk.NO)
txt_entry.bind(
    "<KeyRelease>", update_num_entry
)  # Bind KeyRelease event to update_num_entry function


num_label2 = tk.Label(window, text="Number of symbols to remove:")
num_label2.pack()

num_entry = tk.Entry(window)
num_entry.insert(tk.END, len(txt_entry.get()))
num_entry.pack(pady=5)

# Start GUI
window.mainloop()
