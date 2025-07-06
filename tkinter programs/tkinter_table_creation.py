from tkinter import *

# Sample data
lst = [
    (1, 'Raj', 'Mumbai', 19),
    (2, 'Aaryan', 'Pune', 18),
    (3, 'Vaishnavi', 'Mumbai', 20),
    (4, 'Rachna', 'Mumbai', 21),
    (5, 'Shubham', 'Delhi', 21)
]

# Determine number of rows and columns
total_rows = len(lst)
total_columns = len(lst[0])

# Create root window
root = Tk()
root.title("Table")

# Create table using nested loop
for i in range(total_rows):
    for j in range(total_columns):
        label = Label(root, text=lst[i][j], width=20, fg='black', 
                      font=('Arial', 14), bd=1, relief='solid', padx=5, pady=5)
        label.grid(row=i, column=j)

# Run the application
root.mainloop()
