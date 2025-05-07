import json
import tkinter as tk

class ConfigGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Configuration")
        self.master.configure(bg="#2b2b2b")
        self.center_window(300, 400)
        self.create_widgets()
        self.load_config()

    def center_window(self, width, height):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.master.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Configuration", font=("Helvetica", 16), fg="white", bg="#2b2b2b")
        title_label.pack(pady=10)

        tk.Label(self.master, text="Description:", font=("Helvetica", 12), fg="white", bg="#2b2b2b").pack(pady=5)
        self.desc_entry = tk.Entry(self.master, font=("Helvetica", 12), bg="#3a3a3a", fg="white", insertbackground="white", width=30)
        self.desc_entry.pack(pady=5)

        tk.Label(self.master, text="Title:", font=("Helvetica", 12), fg="white", bg="#2b2b2b").pack(pady=5)
        self.title_entry = tk.Entry(self.master, font=("Helvetica", 12), bg="#3a3a3a", fg="white", insertbackground="white", width=30)
        self.title_entry.pack(pady=5)

        save_button = tk.Button(self.master, text="Save", font=("Helvetica", 12), fg="white", bg="#444444", command=self.save_config)
        save_button.pack(pady=10)

        example_text = """
Example Description:
"Express yourself on the battlefield."

Example Title:
"Victory! Spray"
"""
        example_label = tk.Label(self.master, text=example_text, font=("Helvetica", 10), fg="lightgrey", bg="#2b2b2b", justify="left")
        example_label.pack(side="bottom", anchor="w", padx=10, pady=10)

    def load_config(self):
        try:
            with open("Config.json", "r", encoding="utf-8") as config_file:
                config = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            config = {}

        description = config.get("description", "Express yourself on the battlefield.")
        title = config.get("title", "Victory! Spray")

        self.desc_entry.insert(0, description)
        self.title_entry.insert(0, title)

    def save_config(self):
        config = {
            "description": self.desc_entry.get(),
            "title": self.title_entry.get()
        }

        with open("Config.json", "w", encoding="utf-8") as config_file:
            json.dump(config, config_file, indent=4)

def main():
    root = tk.Tk()
    app = ConfigGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
