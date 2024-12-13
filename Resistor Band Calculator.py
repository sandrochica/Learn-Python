import tkinter as tk
from tkinter import messagebox
import random

# Resistor color code data
COLOR_CODES = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3,
    "Yellow": 4, "Green": 5, "Blue": 6, "Violet": 7, "Gray": 8, "White": 9
}
MULTIPLIERS = {
    "Black": 1, "Brown": 10, "Red": 100, "Orange": 1_000,
    "Yellow": 10_000, "Green": 100_000, "Blue": 1_000_000,
    "Violet": 10_000_000, "Gray": 100_000_000, "White": 1_000_000_000
}
TOLERANCES = {
    "Gold": 5, "Silver": 10
}

# Variable to keep track of score
score = 0

# Function to simulate a real-life rectangular resistor with wires on both sides
def draw_resistor_with_wires(canvas, x, y, band_colors):
    body_width = 300
    body_height = 60
    wire_length = 40

    # Draw the left and right wires
    canvas.create_line(x - wire_length, y + body_height // 2, x, y + body_height // 2, fill="black", width=3)
    canvas.create_line(x + body_width, y + body_height // 2, x + body_width + wire_length, y + body_height // 2, fill="black", width=3)

    # Draw resistor body
    canvas.create_rectangle(x, y, x + body_width, y + body_height, fill="#D3D3D3", outline="black", width=3)

    # Draw color bands
    band_width = body_width // 6
    for i, color in enumerate(band_colors):
        band_x = x + (i * band_width)
        canvas.create_rectangle(band_x, y, band_x + band_width, y + body_height, fill=color, outline="black")

# Function to create dropdown menus with color options
def create_color_dropdown(frame, label_text, color_dict, row, column):
    tk.Label(frame, text=label_text, font=("Courier", 12), bg="#F4E1A1").grid(row=row, column=column, padx=10, pady=5)
    color_var = tk.StringVar()
    color_var.set("Select")
    color_menu = tk.OptionMenu(frame, color_var, *color_dict.keys())
    color_menu.config(font=("Courier", 12), width=12, bg="#D3D3D3")
    color_menu.grid(row=row, column=column + 1, padx=10, pady=5)
    return color_var
# Function to show practice mode
def show_practice_mode():
    global score
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Practice Mode: Guess the Resistor Value", font=("Courier", 20, "bold"), pady=10, bg="#F4E1A1").grid(row=0, column=0, columnspan=2)

    instructions = (
        "Instructions:\n"
        "1. Look at the resistor image below and observe the color bands.\n"
        "2. Fill in the blanks for the 1st significant digit, 2nd significant digit, multiplier, and tolerance.\n"
        "3. Click 'Check Answer' to validate your input.\n"
        "4. The resistor value is calculated as:\n"
        "   (1st Significant Digit + 2nd Significant Digit) x Multiplier\n"
        "   ± Tolerance\n"
    )
    tk.Label(root, text=instructions, justify="left", wraplength=400, font=("Courier", 12), bg="#F4E1A1").grid(row=1, column=0, columnspan=2, pady=10)

    band1_color = random.choice(list(COLOR_CODES.keys()))
    band2_color = random.choice(list(COLOR_CODES.keys()))
    multiplier_color = random.choice(list(MULTIPLIERS.keys()))
    tolerance_color = random.choice(list(TOLERANCES.keys()))

    significant_digits = COLOR_CODES[band1_color] * 10 + COLOR_CODES[band2_color]
    multiplier = MULTIPLIERS[multiplier_color]
    tolerance = TOLERANCES[tolerance_color]
    correct_value = significant_digits * multiplier

    canvas = tk.Canvas(root, width=400, height=200, bg="#F4E1A1")
    canvas.grid(row=2, column=0, columnspan=2, pady=20)
    draw_resistor_with_wires(canvas, 50, 50, [band1_color, band2_color, multiplier_color, tolerance_color])

    band1_var = create_color_dropdown(root, "1st Significant Digit:", COLOR_CODES, 4, 0)
    band2_var = create_color_dropdown(root, "2nd Significant Digit:", COLOR_CODES, 5, 0)
    multiplier_var = create_color_dropdown(root, "Multiplier:", MULTIPLIERS, 6, 0)
    tolerance_var = create_color_dropdown(root, "Tolerance (%):", TOLERANCES, 7, 0)

    def check_answer():
        global score
        try:
            user_value = (COLOR_CODES[band1_var.get()] * 10 + COLOR_CODES[band2_var.get()]) * MULTIPLIERS[multiplier_var.get()]
            if user_value == correct_value and tolerance_var.get() == tolerance_color:
                score += 1
                messagebox.showinfo("Result", f"Correct! Score: {score}")
            else:
                messagebox.showerror("Result", f"Incorrect! Correct: {correct_value} ± {tolerance_color}%")
        except KeyError:
            messagebox.showerror("Error", "Please select all fields.")

    tk.Button(root, text="Check Answer", command=check_answer, font=("Courier", 14), width=20, bg="#FF7043", fg="white").grid(row=8, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Back to Main Menu", command=main_menu, font=("Courier", 14), width=20, bg="#FFEB3B", fg="black").grid(row=9, column=0, columnspan=2, pady=10)

# Main menu function
def main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg="#F4E1A1")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="CIRCUIT DECODE", font=("Courier", 28, "bold"), bg="#F4E1A1").grid(row=0, column=0, pady=20)
    tk.Button(frame, text="Practice Mode", command=show_practice_mode, font=("Courier", 14), bg="#FF7043", fg="white").grid(row=1, column=0, pady=10)

# Initialize main window
root = tk.Tk()
root.title("Resistor Color Code")
root.geometry("600x400")
root.configure(bg="#F4E1A1")

main_menu()
root.mainloop()
