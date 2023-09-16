import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result.set(f"{num1} + {num2} = {num1 + num2}")
        elif operator == "-":
            result.set(f"{num1} - {num2} = {num1 - num2}")
        elif operator == "*":
            result.set(f"{num1} × {num2} = {num1 * num2}")
        elif operator == "/":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(f"{num1} ÷ {num2} = {num1 / num2}")
    except ValueError:
        result.set("Invalid Input")

def switch_to_main_menu(frame_to_show):
    frame_to_show.pack()
    calculator_frame.pack_forget()
    entry_num1.delete(0, tk.END)  # Clear the input fields
    entry_num2.delete(0, tk.END)
    result.set("")  # Clear the result label

def open_calculator(operator):
    main_menu_frame.pack_forget()
    calculator_frame.pack()
    operator_var.set(operator)

def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("400x200")

    fullscreen_var = tk.BooleanVar(value=fullscreen)
    tk.Checkbutton(settings_window, text="Fullscreen", variable=fullscreen_var, command=toggle_fullscreen).pack(pady=10)

    tk.Button(settings_window, text="Close", command=settings_window.destroy).pack(pady=10)

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    window.attributes("-fullscreen", fullscreen)
    set_background_color()

def exit_app():
    window.quit()

def set_background_color():
    if fullscreen:
        window.configure(bg="#001F3F")  # Darker blue background
    else:
        window.configure(bg="#001F3F")  # Darker blue background
        main_menu_frame.configure(bg="#001F3F")  # Darker blue background
        calculator_frame.configure(bg="#001F3F")  # Darker blue background

def start_application():
    global window, entry_num1, entry_num2, result, operator_var, calculator_frame, main_menu_frame, fullscreen
    fullscreen = False
    window = tk.Tk()
    window.title("Modern Calculator")
    window.geometry("800x600")

    main_menu_frame = tk.Frame(window, bg="#001F3F")  # Darker blue background
    calculator_frame = tk.Frame(window, bg="#001F3F")  # Darker blue background

    style = ttk.Style()
    style.configure("Blue.TButton", foreground="#004CA5", background="#001F3F", font=("Nunito Bold", 16), relief="flat")
    
    buttons = [
        ("Addition (+)", "+"), ("Subtraction (-)", "-"),
        ("Multiplication (×)", "*"), ("Division (÷)", "/")
    ]

    for text, op in buttons:
        button = ttk.Button(main_menu_frame, text=text, command=lambda op=op: open_calculator(op), style="Blue.TButton")
        button.pack(pady=20, padx=40, fill=tk.BOTH, ipadx=20, ipady=10)

    ttk.Button(main_menu_frame, text="Settings", command=open_settings, style="Blue.TButton").pack(pady=20, padx=40, fill=tk.BOTH)
    ttk.Button(main_menu_frame, text="Exit", command=exit_app, style="Blue.TButton").pack(pady=20, padx=40, fill=tk.BOTH)

    entry_num1 = tk.Entry(calculator_frame, font=("Nunito Bold", 16))
    entry_num2 = tk.Entry(calculator_frame, font=("Nunito Bold", 16))

    ttk.Button(calculator_frame, text="Calculate", command=calculate, style="Blue.TButton").pack(pady=20, padx=40, fill=tk.BOTH)
    result = tk.StringVar()
    tk.Label(calculator_frame, textvariable=result, bg="#001F3F", fg="#004CA5", font=("Nunito Bold", 20)).pack(pady=20, padx=40, fill=tk.BOTH)
    ttk.Button(calculator_frame, text="Back to Main Menu", command=lambda: switch_to_main_menu(main_menu_frame), style="Blue.TButton").pack(pady=20, padx=40, fill=tk.BOTH)

    operator_var = tk.StringVar(calculator_frame)
    operator_var.set("+")

    entry_num1.pack(pady=10, padx=40, fill=tk.BOTH)
    entry_num2.pack(pady=10, padx=40, fill=tk.BOTH)

    switch_to_main_menu(main_menu_frame)
    set_background_color()

    window.mainloop()

if __name__ == "__main__":
    start_application()