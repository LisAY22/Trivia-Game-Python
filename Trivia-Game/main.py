import tkinter as tk


global question_counter
global questions


def questions_answers(s_line: int):
    with open("Questions_Answers.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()
        return lines[s_line:s_line + 5]         # range: inclusive start index but exclusive end index


def number_questions():
    global questions
    with open("Questions_Answers.txt", "r") as file:
        content = file.read()
        questions = content.count("?")


def initialize_variables_questions_window(window):
    global question_counter                     # We need to declare that we are going to use the global variable
    question_counter = 0
    number_questions()
    questions_window(window)


def change_question_answers(window, question, answers):
    global question_counter
    global questions

    question_counter += 5
    if question_counter != (questions * 5):
        n = 1

        q_a = questions_answers(question_counter)

        # config can change the properties of a widget after it was created
        question.config(text=q_a[0])
        for answer in answers:
            answer.config(text=q_a[n])
            n += 1

        # Call this function again, recursion
        window.after(5000, change_question_answers, window, question, answers)
    else:
        window.destroy()


def main_window():
    # Initialize the main window
    window = tk.Tk()
    window.title("Trivia Game")
    window.config(bg="#5DA399")
    window.geometry("450x250")

    title = tk.Label(window, text="TRIVIA GAME", font=("Helvetica", 20, "bold"), bg="#5DA399")
    title.pack(pady=10)

    username_label = tk.Label(window, text="USERNAME", font=("Helvetica", 18), bg="#5DA399")
    username_label.pack(pady=10)

    username = tk.StringVar()
    username_entry = tk.Entry(window, textvariable=username, font=("Helvetica", 18), justify="center")
    username_entry.pack(pady=10)

    # Pass the window reference to the command
    play_button = tk.Button(window, text="PLAY", font=("Helvetica", 18), bg="#3A1772", fg="white",
                            command=lambda: initialize_variables_questions_window(window))
    play_button.pack(pady=10)

    # Start the event loop
    window.mainloop()


def questions_window(first_window):
    global question_counter
    # Create a new top-level window
    question_window = tk.Toplevel(first_window)
    question_window.title("Questions")
    question_window.config(bg="#5DA399")
    question_window.geometry("650x350")

    q_a = questions_answers(question_counter)

    question = tk.Label(question_window, text=q_a[0], font=("Helvetica", 20, "bold"), bg="#5DA399")
    question.pack(pady=10)

    answers_buttons = []
    for i in range(1, 5):
        answer_button = tk.Button(question_window, text=q_a[i], font=("Helvetica", 18))
        answer_button.pack(pady=10)
        answers_buttons.append(answer_button)

    # The after() method allows you to schedule a function to be executed after a certain amount of time has passed.
    # Syntax: delay in milliseconds, function to be called after the delay, optional arguments to pass to the function.
    question_window.after(5000, change_question_answers, question_window, question, answers_buttons)
    # Close the main window
    first_window.withdraw()


def main():
    main_window()


main()
