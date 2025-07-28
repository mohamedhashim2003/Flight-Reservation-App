import tkinter as tk
from tkinter import ttk

class HomePage:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.frame = ttk.Frame(parent)
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = ttk.Label(self.frame, text="Flight Reservation System", font=('Times New Roman', 24, 'bold'))
        title_label.pack(pady=50)
        
        # Buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=30)
        
        book_btn = ttk.Button(button_frame, text="Book Flight", command=self.go_to_booking, width=20)
        book_btn.pack(pady=10)
        
        view_btn = ttk.Button(button_frame, text="View Reservations", command=self.go_to_reservations, width=20)
        view_btn.pack(pady=10)
    
    def go_to_booking(self):
        self.app.show_page('booking')
    
    def go_to_reservations(self):
        self.app.show_page('reservations')
    
    def show(self, **kwargs):
        self.frame.pack(fill='both', expand=True)
    
    def hide(self):
        self.frame.pack_forget()