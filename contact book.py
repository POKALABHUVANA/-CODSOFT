import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = {}

def clear_entries():
    for e in entries.values():
        e.delete(0, tk.END)
        
def add_contact():
    name , phone = entries["Name"].get().strip(), entries["Phone"].get().strip()
    if not name or not phone:
       messagebox.showwarning("Error","Name & Phone required!")
       return
    contacts[name] = {f:entries[f].get().strip() for f in fields if f != "Name"}
    messagebox.showinfo("Saved",f"contact '{name}' added!")
    clear_entries(); view_contacts()
    
def view_contacts():
    listbox.delete(0, tk.END)
    for n, d in contacts.items():
        listbox.insert(tk.END, f"{n} - {d['Phone']}")
        
def search_contact():
    q = simpledialog.askstring("Search", "Enter Name/Phone:")
    if not q: return
    listbox.delete(0,tk.END)
    for n, d in contacts.items():
        if q.lower() in n.lower() or q == d['phone']:
            listbox.insert(tk.END, f"{n} - {d['Phone']} | {d['Email']} | {d['Address']}")
            return
    messagebox.showinfo("Not Found", "No match found!")
    
def update_contact():
    n = simpledialog.askstring("Update", "Enter Name:")
    if n not in contacts: 
       messagebox.showerror("Error","Not found!")
       return 
    for f in fields[1:]:
        val = simpledialog.askstring(f, f"{f} ({contacts[n][f]}):") or contacts[n][f]
        contacts[n][f] = val
    messagebox.showinfo("Updated", f"{n} updated!"); view_contacts()
    
def delete_contact():
    n = simplwdialog.askstring("Delete", "Enter Name:")
    if n in contacts and messagebox.askynesno("confirm", f"Delete {n}?"):
        del contacts[n]; view_contacts(); messagebox.showinfo("deleted", f"{n} removed!")
        
#GUI
root = tk.Tk(); root.title("Contact Book");root.geometry("500x380")
fields = ["Name", "Phone", "Email", "Address"]
entries = {}

#Input fields
for i,f in enumerate(fields):
    tk.Label(root, text=f + ":").grid(row=i, column=0,sticky="w", padx=10, pady=3)
    e=tk.Entry(root, width=40); e.grid(row=i,column=1, pady=3)
    entries[f] = e
    
#Buttons
    btns = [("Add", add_contact,"lightgreen"),("View", view_contacts,"lightblue"),
            ("Search", search_contact,"Khaki"),("Update", update_contact,"orange"),
            ("Delete", delete_contact,"red"),("Exit", root.quit,"grey")]
for i,(t, cmd , c) in enumerate(btns):
    tk.Button(root, text=t, command=cmd, width=15, bg=c).grid(row=4+i//2, column=i%2, pady=5)
    
#Listbox
listbox = tk.Listbox(root, width=70, height=8)
listbox.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
