import tkinter as tk
from tkinter import filedialog
class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Text Editor")
        self.text_area = tk.Text(self.master, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        self.create_menu()
    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
def main():
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
if __name__ == "__main__":
    main()
