import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class EditReservationPage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.frame = ttk.Frame(parent)
        self.reservation_id = None
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.frame, text="Edit Reservation", font=('Times New Roman', 18, 'bold'))
        title_label.pack(pady=20)
        
        # Form
        form_frame = ttk.Frame(self.frame)
        form_frame.pack(pady=20, padx=50, fill='x')
        
        # Input fields
        fields = [
            ("Passenger Name:", "name"),
            ("Flight Number:", "flight_number"),
            ("Departure:", "departure"),
            ("Destination:", "destination"),
            ("Date (YYYY-MM-DD):", "date"),
            ("Seat Number:", "seat_number")
        ]
        
        self.entries = {}
        
        for i, (label_text, field_name) in enumerate(fields):
            ttk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky='w', pady=5)
            entry = ttk.Entry(form_frame, width=30)
            entry.grid(row=i, column=1, pady=5, padx=(10, 0))
            self.entries[field_name] = entry
        
        # Buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=30)
        
        update_btn = ttk.Button(button_frame, text="Update Reservation", command=self.update_reservation)
        update_btn.pack(side='left', padx=10)
        
        cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.go_back)
        cancel_btn.pack(side='left', padx=10)
    
    def populate_form(self, reservation_data):
        self.reservation_id = reservation_data[0]
        
        # Fill form with existing data
        field_names = ['name', 'flight_number', 'departure', 'destination', 'date', 'seat_number']
        for i, field_name in enumerate(field_names):
            self.entries[field_name].delete(0, tk.END)
            self.entries[field_name].insert(0, reservation_data[i + 1])
    
    def update_reservation(self):
        # Validate inputs
        data = {}
        for field_name, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror("Error", f"Please fill in {field_name}")
                return
            data[field_name] = value
        
        # Validate Destination (must be alphabetic characters and spaces)
        if not data['destination'].replace(' ', '').isalpha():
             messagebox.showerror("Error", "Destination must contain only letters and spaces.")
             return
        # Validate Seat Number (must be digits/numeric)
        if not data['seat_number'].isdigit():
            messagebox.showerror("Error", "Seat Number must be a number.")
            return
        # Validate Departure (must be alphabetic characters and spaces)
        if not data['departure'].replace(' ', '').isalpha():
             messagebox.showerror("Error", "Departure must contain only letters and spaces.")
             return
        # Validate Flight Number (must be digits/numeric)
        if not data['flight_number'].isdigit():
            messagebox.showerror("Error", "Flight Number must be a number.")
            return
        # Validate Passenger Name (must be alphabetic characters and spaces)
        if not data['name'].replace(' ', '').isalpha(): # Allows spaces within the name
             messagebox.showerror("Error", "Passenger Name must contain only letters and spaces.")
             return
        # Validate date format
        try:
            # Validate Date format (YYYY-MM-DD)
            user_date = datetime.strptime(data['date'], '%Y-%m-%d')

            # Check if Date is in the future (or today)
            today = datetime.now().date()
            if user_date.date() < today:
                messagebox.showerror("Error", "Date must be today or in the future.")
                return 

        except ValueError:
            messagebox.showerror("Error", "Date must be in YYYY-MM-DD format")
            return
     
        # Update in database
        try:
            self.app.db.update_reservation(
                self.reservation_id, data['name'], data['flight_number'],
                data['departure'], data['destination'], data['date'], data['seat_number']
            )
            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.go_back()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update reservation: {str(e)}")
    
    def go_back(self):
        self.app.show_page('reservations')
    
    def show(self, **kwargs):
        if 'reservation_data' in kwargs:
            self.populate_form(kwargs['reservation_data'])
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        self.frame.pack_forget()