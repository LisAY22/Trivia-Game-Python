# Libraries
import tkinter as tk


def main():
    # Initialize the main window
    main_window = tk.Tk()

    main_window.title("Trivia Game")
    main_window.config(bg="#5DA399")
    main_window.geometry("450x250")

    title = tk.Label(main_window, text="TRIVIA GAME", font=("Helvetica", 20, "bold"), bg="#5DA399")
    # Add label to the window, geometry manager: pack
    title.pack(pady=10)
    username_label = tk.Label(main_window, text="USERNAME", font=("Helvetica", 18), bg="#5DA399")
    username_label.pack(pady=10)
    username = tk.StringVar()
    username_entry = tk.Entry(main_window, textvariable=username, font=("Helvetica", 18), justify="center")
    username_entry.pack(pady=10)
    play_button = tk.Button(main_window, text="PLAY", font=("Helvetica", 18), bg="#3A1772", fg="white")
    play_button.pack(pady=10)

    # Start the event loop
    main_window.mainloop()


main()
