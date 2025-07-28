import tkinter as tk
from tkinter import ttk, messagebox

class ReservationsPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.frame, text="Flight Reservations", font=('Times New Roman', 18, 'bold'))
        title_label.pack(pady=20)
        
        # Displaying reservations
        self.tree_frame = ttk.Frame(self.frame)
        self.tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tree_frame)
        scrollbar.pack(side='right', fill='y')
        
        # Treeview
        columns = ('ID', 'Name', 'Flight', 'Departure', 'Destination', 'Date', 'Seat')
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
        
        # Configure headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        
        self.tree.pack(fill='both', expand=True)
        scrollbar.config(command=self.tree.yview)
        
        # Buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=20)
        
        refresh_btn = ttk.Button(button_frame, text="Refresh",command=self.load_reservations)
        refresh_btn.pack(side='left', padx=10)
        
        edit_btn = ttk.Button(button_frame, text="Edit Selected",command=self.edit_reservation)
        edit_btn.pack(side='left', padx=10)
        
        delete_btn = ttk.Button(button_frame, text="Delete Selected", command=self.delete_reservation)
        delete_btn.pack(side='left', padx=10)
        
        back_btn = ttk.Button(button_frame, text="Back to Home",command=self.go_back)
        back_btn.pack(side='left', padx=10)
    
    def load_reservations(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Load from database
        reservations = self.app.db.get_all_reservations()
        for reservation in reservations:
            self.tree.insert('', 'end', values=reservation)
    
    def edit_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to edit")
            return
        
        item = self.tree.item(selected[0])
        reservation_data = item['values']
        self.app.show_page('edit', reservation_data=reservation_data)
    
    def delete_reservation(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a reservation to delete")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this reservation?"):
            item = self.tree.item(selected[0])
            reservation_id = item['values'][0]
            
            try:
                self.app.db.delete_reservation(reservation_id)
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                self.load_reservations()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete reservation: {str(e)}")
    
    def go_back(self):
        self.app.show_page('home')
    
    def show(self, **kwargs):
        self.load_reservations()
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        self.frame.pack_forget()