import tkinter as tk


global question_counter
global questions
global username
global answers
global score
global root


answers = []


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


def final_answer(answer_text, question_window, question, answers_buttons):
    global answers
    answers.append(answer_text)
    change_question_answers(question_window, question, answers_buttons)


def final_score():
    global questions
    global answers
    global score
    score = 0
    answer_number = 0
    with open("CorrectAnswers.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()
    for line in lines:
        if line.strip() == answers[answer_number].strip():
            score += 1
        answer_number += 1


def close_window():
    root.destroy()


def main_window():
    global username
    global root
    # Initialize the main root
    root = tk.Tk()
    root.title("Trivia Game")
    root.config(bg="#5DA399")
    root.geometry("450x250")

    title = tk.Label(root, text="TRIVIA GAME", font=("Helvetica", 20, "bold"), bg="#5DA399")
    title.pack(pady=10)

    username_label = tk.Label(root, text="USERNAME", font=("Helvetica", 18), bg="#5DA399")
    username_label.pack(pady=10)

    username = tk.StringVar()
    username_entry = tk.Entry(root, textvariable=username, font=("Helvetica", 18), justify="center")
    username_entry.pack(pady=10)

    # Pass the root reference to the command
    play_button = tk.Button(root, text="PLAY", font=("Helvetica", 18), bg="#3A1772", fg="white",
                            command=lambda: initialize_variables_questions_window(root))
    play_button.pack(pady=10)

    # Bind the close window event to the close_window function
    root.protocol("WM_DELETE_WINDOW", close_window)

    # Start the event loop
    root.mainloop()


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
        # lambda is a key word in Python that creates an anonym function, these functions are used once.
        # The command parameter in a button is specifically designed to trigger a function when the button is clicked.
        answer_button = tk.Button(question_window, text=q_a[i], font=("Helvetica", 18), command=lambda fa=q_a[i]:
                                  final_answer(fa, question_window, question, answers_buttons))
        answer_button.pack(pady=10)
        answers_buttons.append(answer_button)

    question_window.protocol("WM_DELETE_WINDOW", close_window)

    # Close the main window
    first_window.withdraw()


def change_question_answers(window, question, p_answers):
    global question_counter
    global questions

    question_counter += 5
    if question_counter != (questions * 5):
        n = 1

        q_a = questions_answers(question_counter)

        # config can change the properties of a widget after it was created
        question.config(text=q_a[0])
        for answer in p_answers:
            answer.config(text=q_a[n], command=lambda fa=q_a[n]: final_answer(fa, window, question, p_answers))
            n += 1
    else:
        results_window(window)
        window.withdraw()


def results_window(window):
    global username
    global score
    result_window = tk.Toplevel(window)
    result_window.title("Results")
    result_window.config(bg="#5DA399")
    result_window.geometry("300x200")

    if username.get().strip() == "":
        username.set("UNKNOWN PLAYER")

    final_score()

    title_result = tk.Label(result_window, text="RESULT", font=("Helvetica", 20, "bold"), bg="#5DA399")
    title_result.pack(pady=10)
    username_label = tk.Label(result_window, text=username.get(), font=("Helvetica", 20, "bold"), bg="#5DA399")
    username_label.pack(pady=10)
    score = tk.Label(result_window, text=str(score), font=("Helvetica", 20, "bold"), bg="#3A1772", width=10, fg="white")
    score.pack(pady=10)

    result_window.protocol("WM_DELETE_WINDOW", close_window)

    window.withdraw()


def main():
    main_window()


main()
