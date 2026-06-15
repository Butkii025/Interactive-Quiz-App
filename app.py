import tkinter as tk

# 1. Define the Quiz Questions Dataset
# A list of dictionaries containing the question, choices, and correct answer string.
quiz_data = [
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "choices": ["Brackets", "Indentation", "Parentheses", "Quotation marks"],
        "answer": "Indentation"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "choices": [".pt", ".pyt", ".py", ".pyw"],
        "answer": ".py"
    },
    {
        "question": "Which built-in function can tell us the number of items in a list?",
        "choices": ["count()", "size()", "length()", "len()"],
        "answer": "len()"
    },
    {
        "question": "What is the output of print(2 ** 3) in Python?",
        "choices": ["6", "8", "9", "5"],
        "answer": "8"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Core Quiz")
        self.root.geometry("550x450")
        self.root.configure(bg="#1e1e2e") # Elegant dark theme

        # Track current state tracking variables
        self.current_question_idx = 0
        self.score = 0

        # --- UI Components Layout Setup ---
        
        # Progress Tracking Display
        self.progress_label = tk.Label(root, text="", font=("Arial", 11), bg="#1e1e2e", fg="#a6adc8")
        self.progress_label.pack(pady=10)

        # Question Display Box
        self.question_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#cdd6f4",
            wraplength=480, justify="center"
        )
        self.question_label.pack(pady=20, padx=20)

        # Container Frame for choice buttons
        self.choices_frame = tk.Frame(root, bg="#1e1e2e")
        self.choices_frame.pack(pady=10)

        # Create 4 placeholder choice buttons
        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.choices_frame, text="", font=("Arial", 11), width=35, 
                bg="#313244", fg="#cdd6f4", activebackground="#45475a", activeforeground="#cdd6f4",
                bd=0, pady=10, cursor="hand2",
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.grid(row=i, column=0, pady=8)
            self.choice_buttons.append(btn)

        # Next Button (initially hidden or disabled until user picks an option)
        self.next_button = tk.Button(
            root, text="Next Question ➡️", font=("Arial", 11, "bold"),
            bg="#89b4fa", fg="#11111b", activebackground="#b4befe",
            bd=0, padx=20, pady=8, cursor="hand2", command=self.load_question
        )
        # We don't pack it immediately; it shows up after an answer is submitted.

        # Load the very first question configuration details
        self.load_question()

    def load_question(self):
        # Hide the next button until they choose another answer
        self.next_button.pack_forget()

        if self.current_question_idx < len(quiz_data):
            # Reset button colors and enable them again
            for btn in self.choice_buttons:
                btn.config(bg="#313244", fg="#cdd6f4", state="normal")

            # Fetch data block
            q_dict = quiz_data[self.current_question_idx]
            
            # Update labels text
            self.progress_label.config(text=f"Question {self.current_question_idx + 1} of {len(quiz_data)}")
            self.question_label.config(text=q_dict["question"])

            # Map choice array values to button components
            for i, choice in enumerate(q_dict["choices"]):
                self.choice_buttons[i].config(text=choice)
        else:
            self.show_final_score()

    def check_answer(self, selected_idx):
        # Lock buttons immediately so user can't click multiple options
        for btn in self.choice_buttons:
            btn.config(state="disabled")

        current_q = quiz_data[self.current_question_idx]
        selected_answer = self.choice_buttons[selected_idx].cget("text")
        correct_answer = current_q["answer"]

        # Evaluation checks logic
        if selected_answer == correct_answer:
            self.choice_buttons[selected_idx].config(bg="#a6e3a1", fg="#11111b") # Turn green
            self.score += 1
        else:
            self.choice_buttons[selected_idx].config(bg="#f38ba8", fg="#11111b") # Turn selected red
            # Highlight the actual correct answer in green so the user learns
            for btn in self.choice_buttons:
                if btn.cget("text") == correct_answer:
                    btn.config(bg="#a6e3a1", fg="#11111b")

        # Advance our global state index counter
        self.current_question_idx += 1
        
        # Show the next question confirmation action button
        self.next_button.pack(pady=20)

    def show_final_score(self):
        # Clear away widgets inside our main containers
        self.progress_label.pack_forget()
        self.choices_frame.pack_forget()
        self.next_button.pack_forget()

        # Calculate percentage rating performance
        percentage = (self.score / len(quiz_data)) * 100

        # Create final score banner display strings
        end_title = "🎉 Quiz Completed! 🎉" if percentage >= 75 else "👍 Nice Attempt!"
        score_report = f"Your Score: {self.score} / {len(quiz_data)}\nPercentage: {percentage:.1f}%"

        self.question_label.config(text=f"{end_title}\n\n{score_report}", font=("Arial", 16, "bold"))

# --- Driver Script Execution Engine ---
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()