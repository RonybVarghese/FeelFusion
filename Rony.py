# import sklearn
# print("hello")

import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen
def submit():

    name=name_var.get()
    password=passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# creating a entry for password
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()



import tkinter as tk
from tkinter import filedialog
def record_voice():
    print("Recording voice...")
def view_emotion():
    print("Viewing emotion...")
def browse_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Audio files", "*.wav *.mp3"), ("all files", "*.*")))
    selected_file_label.config(text=filename)
root = tk.Tk()
root.title("Admin Home")
tk.Label(root, text="Duration").grid(row=0, column=0, padx=10, pady=10)
duration_entry = tk.Entry(root)
duration_entry.grid(row=0, column=1, padx=10, pady=10)

record_button = tk.Button(root, text="RECORD VOICE", command=record_voice)
record_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


tk.Label(root, text="Select a Voice...").grid(row=2, column=0, padx=10, pady=10)
select_button = tk.Button(root, text="Browse", command=browse_files)
select_button.grid(row=2, column=1, padx=10, pady=10)


selected_file_label = tk.Label(root, text="No file selected")
selected_file_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


view_emotion_button = tk.Button(root, text="VIEW EMOTION", command=view_emotion)
view_emotion_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


status_label = tk.Label(root, text="waiting")
status_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

