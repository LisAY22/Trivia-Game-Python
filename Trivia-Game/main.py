import tkinter as tk


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
                            command=lambda: questions_window(window))
    play_button.pack(pady=10)

    # Start the event loop
    window.mainloop()


def questions_window(first_window):
    # Create a new top-level window
    question_window = tk.Toplevel(first_window)
    question_window.title("Questions")
    question_window.config(bg="#5DA399")
    question_window.geometry("450x350")

    question = tk.Label(question_window, text="Question", font=("Helvetica", 20, "bold"), bg="#5DA399")
    question.pack(pady=10)

    answer1_button = tk.Button(question_window, text="Answer1", font=("Helvetica", 18))
    answer1_button.pack(pady=10)

    answer2_button = tk.Button(question_window, text="Answer2", font=("Helvetica", 18))
    answer2_button.pack(pady=10)

    answer3_button = tk.Button(question_window, text="Answer3", font=("Helvetica", 18))
    answer3_button.pack(pady=10)

    answer4_button = tk.Button(question_window, text="Answer4", font=("Helvetica", 18))
    answer4_button.pack(pady=10)

    # Close the main window
    first_window.withdraw()


def main():
    main_window()


main()
