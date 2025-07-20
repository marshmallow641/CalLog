import datetime as dt    # Used for timestamping the notes.
import tkinter as tk     # Used for creating the GUI.
from tkinter import ttk  # Used for creating the frame inside of tk's window as well as the components in the frame.

import pyperclip as clip # Used for copying the note to the clipboard.

# Defines the window, title and behavior for the 1st row and column.
root = tk.Tk()
root.title("Call Log Creator")
root.rowconfigure(0, weight=1)     # The 1st column should expand with the window.
root.columnconfigure(0, weight=1)  # The 1st row should expand with the window.

# Defines the frame that goes inside of the window and gives it simmilar behavior to the window (above).
frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)  # Gives padding to all sides of the frame (North, South, East, and West).
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Function for timestamping the note
def timestamp():
    date = dt.datetime.now()
    hour = date.hour

    # If the hour is at noon or later, subtract 12 to disaplay the time in 12-hour format, and add the string to the end of the date_entry tkinter component.
    if int(hour) > 11:
        date_entry.insert(tk.END,f"{date.month}/{date.day}/{date.year} {date.hour - 12}:{date.minute}:{date.second} p.m.")

    # Add the date and time (in 12-hour format) to the end of the date_entry tkinter component.
    else:
        date_entry.insert(tk.END, f"{date.month}/{date.day}/{date.year} {date.hour}:{date.minute}:{date.second} a.m.")

# Take the text from the tkinter components, put it in a formatted string, then copy text to clipboard and remove the text from the components.
def add_to_list():
    phone   = phone_entry.get()
    caller  = caller_entry.get()
    date    = date_entry.get()
    company = company_text.get()
    issue   = issue_text.get("1.0", tk.END)
    reason  = reason_text.get("1.0", tk.END)
    actions = actions_text.get("1.0", tk.END)

    text = ""

    text_length = 0

    if phone and caller and not company:
        text = f"{caller} ({phone}) called {reason}\n\nIssue(s): {issue}\nActions Taken: {actions}"
        txt_list.insert(tk.END, text)
        txt_list.insert(tk.END, f"--------------------------------------------------------------------------------")

        clip.copy(text)

    elif phone and caller and company:
        text = f"{caller} ({phone}), from {company}, called {reason}\nIssue(s): {issue}\n\nActions Taken: {actions}"
        txt_list.insert(tk.END, text)
        txt_list.insert(tk.END, f"--------------------------------------------------------------------------------")

        clip.copy(text)

    else:
        raise Exception("Enter values for phone number, caller, and company (optional)")


    # Delete text from tkinter components
    phone_entry.delete(0, tk.END)
    caller_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    company_text.delete(0, tk.END)
    issue_text.delete("1.0", tk.END)
    reason_text.delete("1.0", tk.END)
    actions_text.delete("1.0", tk.END)

# Label and component definition for phone number.
phone_label = ttk.Label(frame, text="Phone Number (XXX-XXX-XXXX) ").grid(row=0, column=0, padx=5, pady=5)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5, columnspan=2)

# Label and component definition for caller.
caller_label = ttk.Label(frame, text="Name of Caller ").grid(row=1, column=0, padx=5, pady=5)
caller_entry = ttk.Entry(frame)
caller_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5, columnspan=2)

# Label and component definition for timestamp as well as a button for generating the timestamp.
date_label = ttk.Label(frame, text="Date and Time ").grid(row=2, column=0, padx=5, pady=5)
date_entry = ttk.Entry(frame)
date_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5, columnspan=2)
gen_date = ttk.Button(frame, text="Get Current Date and Time ", command=timestamp)
gen_date.grid(row=2, column=3, padx=5, pady=5)

# Label and component definition for company (with scrollbars).
company_label = ttk.Label(frame, text="Company ").grid(row=3, column=0, padx=5, pady=5)
company_text = ttk.Entry(frame)
company_text.grid(row=3, column=1, sticky="ew", padx=5, pady=5, columnspan=2)
scroll = tk.Scrollbar(frame, command=company_text.xview)
company_text['xscrollcommand'] = scroll.set

# Label and component definition for caller's issue (with scrollbars).
issue_label = ttk.Label(frame, text="Issue ").grid(row=4, column=0, padx=5, pady=5)
issue_text = tk.Text(frame, height=3, width=10)
issue_text.grid(row=4, column=1, sticky="ew", padx=5, pady=5, columnspan=3)
scroll3 = tk.Scrollbar(frame, command=issue_text.yview)
scroll4 = tk.Scrollbar(frame, command=issue_text.xview)
issue_text['yscrollcommand'] = scroll3.set
issue_text['xscrollcommand'] = scroll4.set

# Label and component definition for the reason (with scrollbars).
reason_label = ttk.Label(frame, text="Reason for Call ").grid(row=5, column=0, padx=5, pady=5) # Should be Text object, with horizontal and vertical scrollbars
reason_text = tk.Text(frame, height=3, width=10)
scrolla = tk.Scrollbar(frame, command=reason_text.yview)
scrollb = tk.Scrollbar(frame, command=reason_text.xview)
reason_text['yscrollcommand'] = scrolla.set
reason_text['xscrollcommand'] = scrollb.set
reason_text.grid(row=5, column=1, sticky="ew", padx=5, pady=5, columnspan=3)

# Label and component definition for actions taken (with scrollbars).
actions_label = ttk.Label(frame, text="Actions Taken ").grid(row=6, column=0, padx=5, pady=5) # Should be Text object, with horizontal and vertical scrollbars
actions_text = tk.Text(frame, height=3, width=10)
actions_text.grid(row=6, column=1, sticky="ew", padx=5, pady=5, columnspan=3)
scrollc = tk.Scrollbar(frame, command=actions_text.yview)
scrolld = tk.Scrollbar(frame, command=actions_text.xview)
actions_text['yscrollcommand'] = scrollc.set
actions_text['xscrollcommand'] = scrolld.set

# Button to copy text to clipboard as well as clear the tkinter text components.
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=add_to_list).grid(row=7, column=2, padx=5, pady=5)

# Label and component definition for previous notes generated.
txt_list = tk.Text(frame, height=8, width=10)
txt_list.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
scrolle = tk.Scrollbar(frame, command=actions_text.yview)
scrollf = tk.Scrollbar(frame, command=actions_text.xview)
txt_list['yscrollcommand'] = scrolle.set
txt_list['xscrollcommand'] = scrollf.set



if __name__ == '__main__':
    root.mainloop()
