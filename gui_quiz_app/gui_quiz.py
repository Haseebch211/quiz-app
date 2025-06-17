import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for themed widgets
import json

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x500") # Increased window size for better layout
        self.root.resizable(False, False) # Make window non-resizable

        # Configure styles for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('clam') # Using 'clam' theme for a modern look

        self.style.configure("TLabel", font=("Arial", 14), wraplength=500)
        self.style.configure("TRadiobutton", font=("Arial", 12), padding=5)
        self.style.configure("TButton", font=("Arial", 12, "bold"), padding=8)

        self.load_questions()
        self.current_question = 0
        self.score = 0
        self.user_answer = tk.StringVar()

        self.create_widgets()
        self.display_question()

    def load_questions(self):
        try:
            with open("questions.json", "r") as f:
                self.questions = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Error", "questions.json not found. Please create the file.")
            self.questions = [] # Initialize as empty list if file not found
            self.root.destroy() # Close the app if questions can't be loaded

    def create_widgets(self):
        # Main frame to hold all content, centered
        main_frame = ttk.Frame(self.root, padding="20 20 20 20")
        main_frame.pack(expand=True, fill="both")

        # Question Label
        self.question_label = ttk.Label(main_frame, text="", anchor="center")
        self.question_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew") # Use sticky="ew" to expand horizontally

        # Options Frame to group radio buttons
        options_frame = ttk.Frame(main_frame)
        options_frame.grid(row=1, column=0, columnspan=2, padx=50, pady=10, sticky="w")

        self.options = []
        for i in range(4):
            btn = ttk.Radiobutton(options_frame, text="", variable=self.user_answer, value="")
            btn.pack(anchor="w", pady=5) # pack within the options_frame
            self.options.append(btn)

        # Submit Button
        self.submit_btn = ttk.Button(main_frame, text="Submit", command=self.submit_answer)
        self.submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

        # Configure column weights so elements expand with the window
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

    def display_question(self):
        if not self.questions:
            return

        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        self.user_answer.set(None) # Clear previous selection

        for i, option in enumerate(question_data["options"]):
            self.options[i].config(text=option, value=option)

    def submit_answer(self):
        selected = self.user_answer.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option")
            return

        correct = self.questions[self.current_question]["answer"]
        if selected == correct:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Result", f"Your score: {self.score}/{len(self.questions)}")
        self.root.destroy() # Close the application after showing results

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()