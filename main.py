import datetime as dt
import tkinter as tk
from tkinter import ttk

import pyperclip as clip

root = tk.Tk()
root.title("Call Log Creator")
root.rowconfigure(0, weight=1)  # The 1st column should expand with the window
root.columnconfigure(0, weight=1)  # The 1st row should expand with the window

frame = ttk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)


def timestamp(event=None):
    date = dt.datetime.now()
    hour = date.hour
    # date_entry = ttk.Entry(frame)

    if int(hour) > 11:
        date_entry.insert(tk.END,f"{date.month}/{date.day}/{date.year} {date.hour - 12}:{date.minute}:{date.second} p.m.")

    else:
        date_entry.insert(tk.END, f"{date.month}/{date.day}/{date.year} {date.hour}:{date.minute}:{date.second} a.m.")


def add_to_list(event=None):
    phone   = phone_entry.get()
    caller  = caller_entry.get()
    date    = date_entry.get()
    company = company_text.get("1.0", tk.END)
    site    = site_text.get("1.0", tk.END)
    reason  = reason_text.get("1.0", tk.END)
    actions = actions_text.get("1.0", tk.END)

    text = ""

    text_length = 0

    if phone and caller and not company:
        text = f"{caller} ({phone}) called {reason}\n\n{actions}\n\nSite(s): {site}"
        txt_list.insert(tk.END, text)
        txt_list.insert(tk.END, f"--------------------------------------------------------------------------------")
        clip.copy(text)

    elif phone and caller and company:
        text = f"{caller} ({phone}), from {company}, called {reason}\n\n{actions}\n\nSite(s): {site}"
        txt_list.insert(tk.END, text)
        txt_list.insert(tk.END, f"--------------------------------------------------------------------------------")
        clip.copy(text)
    else:
        raise Exception("Enter values for phone number, caller, and company (optional)")
        #txt_list.insert(tk.END, f"{caller} ({phone}) called to {reason}\n\n{actions}\n\nSite(s): {site}")

        #txt_list.insert(tk.END, text)


    phone_entry.delete(0, tk.END)
    caller_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    company_text.delete("1.0", tk.END)
    site_text.delete("1.0", tk.END)
    reason_text.delete("1.0", tk.END)
    actions_text.delete("1.0", tk.END)


phone_label = ttk.Label(frame, text="Phone Number (XXX-XXX-XXXX) ").grid(row=0, column=0, padx=5, pady=5)
phone_entry = ttk.Entry(frame)
phone_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
# phone_entry.bind("<Return>", add_to_list)

caller_label = ttk.Label(frame, text="Name of Caller ").grid(row=1, column=0, padx=5, pady=5)
caller_entry = ttk.Entry(frame)
caller_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

date_label = ttk.Label(frame, text="Date and Time ").grid(row=2, column=0, padx=5, pady=5)
date_entry = ttk.Entry(frame)
date_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
gen_date = ttk.Button(frame, text="Get Current Date and Time ", command=timestamp).grid(row=2, column=2, padx=5, pady=5)

company_label = ttk.Label(frame, text="Company ").grid(row=3, column=0, padx=5, pady=5)
company_text = tk.Text(frame, height=2)
company_text.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
scroll1 = tk.Scrollbar(frame, command=company_text.yview)
scroll2 = tk.Scrollbar(frame, command=company_text.xview)
company_text['yscrollcommand'] = scroll1.set
company_text['xscrollcommand'] = scroll2.set

site_label = ttk.Label(frame, text="Site ").grid(row=4, column=0, padx=5, pady=5)
site_text = tk.Text(frame, height=3, width=10)
site_text.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
scroll3 = tk.Scrollbar(frame, command=site_text.yview)
scroll4 = tk.Scrollbar(frame, command=site_text.xview)
site_text['yscrollcommand'] = scroll3.set
site_text['xscrollcommand'] = scroll4.set

reason_label = ttk.Label(frame, text="Reason for Call ").grid(row=5, column=0, padx=5, pady=5) # Should be Text object, with horizontal and vertical scrollbars
reason_text = tk.Text(frame, height=3, width=10)
scrolla = tk.Scrollbar(frame, command=reason_text.yview)
scrollb = tk.Scrollbar(frame, command=reason_text.xview)
reason_text['yscrollcommand'] = scrolla.set
reason_text['xscrollcommand'] = scrollb.set
reason_text.grid(row=5, column=1, sticky="ew", padx=5, pady=5, columnspan=1)

actions_label = ttk.Label(frame, text="Actions Taken ").grid(row=6, column=0, padx=5, pady=5) # Should be Text object, with horizontal and vertical scrollbars
actions_text = tk.Text(frame, height=3, width=10)
actions_text.grid(row=6, column=1, sticky="ew", padx=5, pady=5, columnspan=1)
scrollc = tk.Scrollbar(frame, command=actions_text.yview)
scrolld = tk.Scrollbar(frame, command=actions_text.xview)
actions_text['yscrollcommand'] = scrollc.set
actions_text['xscrollcommand'] = scrolld.set

copy_button = ttk.Button(frame, text="Copy to Clipboard", command=add_to_list).grid(row=7, column=2, padx=5, pady=5)

txt_list = tk.Text(frame, height=8, width=10)
txt_list.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
scrolle = tk.Scrollbar(frame, command=actions_text.yview)
scrollf = tk.Scrollbar(frame, command=actions_text.xview)
txt_list['yscrollcommand'] = scrolle.set
txt_list['xscrollcommand'] = scrollf.set

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root.mainloop()
