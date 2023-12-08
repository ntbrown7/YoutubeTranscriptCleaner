import tkinter as tk
from tkinter import filedialog, messagebox

def remove_timestamps_and_newlines(text):
    lines = text.split('\n')
    cleaned_lines = [line for line in lines if not any(char.isdigit() for char in line)]
    return ' '.join(cleaned_lines)

def upload_file():
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    with open(file_path, 'r') as file:
        content = file.read()

    cleaned_content = remove_timestamps_and_newlines(content)

    save_path = filedialog.asksaveasfilename(title="Save the cleaned text", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not save_path:
        return

    with open(save_path, 'w') as file:
        file.write(cleaned_content)

    messagebox.showinfo("Success", "File processed and saved successfully!")

app = tk.Tk()
app.title("Text Cleaner")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Upload a text file to remove timestamps and newlines:")
label.pack(pady=10)

upload_btn = tk.Button(frame, text="Upload File", command=upload_file)
upload_btn.pack(pady=10)

app.mainloop()
