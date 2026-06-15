import tkinter as tk

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
        self.root.configure(bg="#1e1e2e") 

        self.current_question_idx = 0
        self.score = 0

        
        self.progress_label = tk.Label(root, text="", font=("Arial", 11), bg="#1e1e2e", fg="#a6adc8")
        self.progress_label.pack(pady=10)

        self.question_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"), bg="#1e1e2e", fg="#cdd6f4",
            wraplength=480, justify="center"
        )
        self.question_label.pack(pady=20, padx=20)

        self.choices_frame = tk.Frame(root, bg="#1e1e2e")
        self.choices_frame.pack(pady=10)

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

        self.next_button = tk.Button(
            root, text="Next Question ➡️", font=("Arial", 11, "bold"),
            bg="#89b4fa", fg="#11111b", activebackground="#b4befe",
            bd=0, padx=20, pady=8, cursor="hand2", command=self.load_question
        )

        self.load_question()

    def load_question(self):
        self.next_button.pack_forget()

        if self.current_question_idx < len(quiz_data):
            for btn in self.choice_buttons:
                btn.config(bg="#313244", fg="#cdd6f4", state="normal")

            q_dict = quiz_data[self.current_question_idx]
            
            self.progress_label.config(text=f"Question {self.current_question_idx + 1} of {len(quiz_data)}")
            self.question_label.config(text=q_dict["question"])

            for i, choice in enumerate(q_dict["choices"]):
                self.choice_buttons[i].config(text=choice)
        else:
            self.show_final_score()

    def check_answer(self, selected_idx):
        for btn in self.choice_buttons:
            btn.config(state="disabled")

        current_q = quiz_data[self.current_question_idx]
        selected_answer = self.choice_buttons[selected_idx].cget("text")
        correct_answer = current_q["answer"]

        if selected_answer == correct_answer:
            self.choice_buttons[selected_idx].config(bg="#a6e3a1", fg="#11111b") # Turn green
            self.score += 1
        else:
            self.choice_buttons[selected_idx].config(bg="#f38ba8", fg="#11111b") # Turn selected red
            for btn in self.choice_buttons:
                if btn.cget("text") == correct_answer:
                    btn.config(bg="#a6e3a1", fg="#11111b")

        self.current_question_idx += 1
        
        self.next_button.pack(pady=20)

    def show_final_score(self):
        self.progress_label.pack_forget()
        self.choices_frame.pack_forget()
        self.next_button.pack_forget()

        percentage = (self.score / len(quiz_data)) * 100

        end_title = "🎉 Quiz Completed! 🎉" if percentage >= 75 else "👍 Nice Attempt!"
        score_report = f"Your Score: {self.score} / {len(quiz_data)}\nPercentage: {percentage:.1f}%"

        self.question_label.config(text=f"{end_title}\n\n{score_report}", font=("Arial", 16, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()