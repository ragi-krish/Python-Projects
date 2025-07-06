import tkinter as tk

def change_color(color):
    window.configure(bg=color)

def reset_color():
    window.configure(bg='SystemButtonFace')  # default background color

# Create the main window
window = tk.Tk()
window.title("Simple Color Changer")
window.geometry("400x300")

# Bottom frame to hold buttons horizontally
button_frame = tk.Frame(window)
button_frame.pack(side="bottom", pady=20)

# Create buttons and add them to the frame
btn_red = tk.Button(button_frame, text="Red", bg="#b82404", activebackground ="red",fg="white", width=8, command=lambda: change_color("#b82404"))
btn_red.pack(side="left", padx=5)

btn_green = tk.Button(button_frame, text="Green", bg="green", fg="white", width=8, command=lambda: change_color("green"))
btn_green.pack(side="left", padx=5)

btn_blue = tk.Button(button_frame, text="Blue", bg="blue", fg="white", width=8, command=lambda: change_color("blue"))
btn_blue.pack(side="left", padx=5)

btn_yellow = tk.Button(button_frame, text="Yellow", bg="yellow", fg="black", width=8, command=lambda: change_color("yellow"))
btn_yellow.pack(side="left", padx=5)

btn_reset = tk.Button(button_frame, text="Reset", width=8, command=reset_color)
btn_reset.pack(side="left", padx=5)

# Run the application
window.mainloop()
