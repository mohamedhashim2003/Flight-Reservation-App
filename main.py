import tkinter as tk
from tkinter import ttk
from database import Database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flight Reservation System")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Initialize database
        self.db = Database()
        
        # Container for pages
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Initialize pages
        self.pages = {}
        self.current_page = None
        
        self.init_pages()
        self.show_page('home')
    
    def init_pages(self):
        self.pages['home'] = HomePage(self.main_frame, self)
        self.pages['booking'] = BookingPage(self.main_frame, self)
        self.pages['reservations'] = ReservationsPage(self.main_frame, self)
        self.pages['edit'] = EditReservationPage(self.main_frame, self)
    
    def show_page(self, page_name, **kwargs):
        
        if self.current_page:
            self.current_page.hide()
        
        # Show new page
        self.current_page = self.pages[page_name]
        self.current_page.show(**kwargs)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FlightReservationApp()
    app.run()