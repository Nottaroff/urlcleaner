"""
URL Cleaner - A simple application to clean and format URLs.

Author: Nottaroff
"""

import tkinter as tk
from urllib.parse import urlparse

def extract_domain():
    urls = url_entry.get("1.0", tk.END).strip().split("\n")
    
    results = []
    for url in urls:
        url = url.strip()
        if not url:
            continue

        # Add default scheme if not present
        if not urlparse(url).scheme:
            url = "http://" + url

        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        scheme = parsed_url.scheme

        if http_var.get() == 0 and www_var.get() == 0:
            # No checkboxes selected
            if domain.startswith("www."):
                domain = domain[4:] 
            domain = domain.split(':')[0]  

            # Reconstruct domain 
            domain_parts = domain.split('.')
            if len(domain_parts) > 2:
                domain = '.'.join(domain_parts[-2:])  
            result = domain
        else:
            # Adjust based on checkbox
            if http_var.get() == 1 and www_var.get() == 1:
                if not domain.startswith("www."):
                    domain = "www." + domain
                result = f"{scheme}://{domain}"
            elif http_var.get() == 1:
                result = f"{scheme}://{domain}"
            elif www_var.get() == 1:
                if not domain.startswith("www."):
                    domain = "www." + domain
                result = domain
            else:
                # Default option
                if domain.startswith("www."):
                    domain = domain[4:]  
                result = domain

        results.append(result)

    result_text.config(state=tk.NORMAL)  
    result_text.delete(1.0, tk.END)      
    result_text.insert(tk.END, "\n".join(results))  
    result_text.config(state=tk.DISABLED)  

def clear_entry():
    url_entry.delete(1.0, tk.END)
    result_text.config(state=tk.NORMAL)  
    result_text.delete(1.0, tk.END)      
    result_text.config(state=tk.DISABLED) 

def copy_to_clipboard():
    result_text.config(state=tk.NORMAL)  
    text_to_copy = result_text.get("1.0", tk.END).strip()
    app.clipboard_clear()  
    app.clipboard_append(text_to_copy)  
    result_text.config(state=tk.DISABLED) 

# Interface
app = tk.Tk()
http_var = tk.IntVar()
www_var = tk.IntVar()

app.title("URL Cleaner")

# Size
app.geometry("900x400")

# Background
app.configure(bg='#1f1f1f')  

# Functions
tk.Label(app, text="Enter the URLs:", bg='#1f1f1f', fg='#DADADA').grid(row=0, column=0, padx=10, pady=10, sticky="w")
url_entry = tk.Text(app, height=7, width=80, wrap=tk.WORD, bg='#FFFFFF', fg='#000000', insertbackground='black') 
url_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Checkbuttons
tk.Label(app, text="Options:", bg='#1f1f1f', fg='#DADADA').grid(row=1, column=0, padx=10, pady=10, sticky="w")

http_check = tk.Checkbutton(app, text="http(s)://", variable=http_var, bg='#1f1f1f', fg='#DADADA', selectcolor='#333333', highlightthickness=0)
http_check.grid(row=1, column=1, padx=10, pady=10, sticky="w")

www_check = tk.Checkbutton(app, text="www.", variable=www_var, bg='#1f1f1f', fg='#DADADA', selectcolor='#333333', highlightthickness=0)
www_check.grid(row=1, column=2, padx=10, pady=10, sticky="w")

# Action buttons 
extract_button = tk.Button(app, text="Extract", command=extract_domain, width=15, bg='#4CAF50', fg='#FFFFFF', relief='raised')
extract_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

clear_button = tk.Button(app, text="Clear", command=clear_entry, width=15, bg='#2196F3', fg='#FFFFFF', relief='raised')
clear_button.grid(row=2, column=0, padx=10, pady=10)

copy_button = tk.Button(app, text="Copy", command=copy_to_clipboard, width=15, bg='#9C27B0', fg='#FFFFFF', relief='raised')
copy_button.grid(row=2, column=2, padx=10, pady=10)

# Result 
tk.Label(app, text="Result:", bg='#1f1f1f', fg='#DADADA').grid(row=3, column=0, padx=10, pady=10, sticky="w")
result_text = tk.Text(app, height=7, width=80, wrap=tk.WORD, borderwidth=1, relief="solid", bg='#FFFFFF', fg='#000000')
result_text.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
result_text.config(state=tk.DISABLED)  

# Resizing
app.grid_columnconfigure(0, weight=0)  
app.grid_columnconfigure(1, weight=1)  
app.grid_columnconfigure(2, weight=0)  
app.grid_rowconfigure(2, weight=1) 

# Mainloop
app.mainloop()

