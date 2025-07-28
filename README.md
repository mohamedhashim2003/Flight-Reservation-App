# Flight Reservation Desktop App

A simple desktop application for managing flight reservations built with Python

## Features
- Book new flight reservations
- View all reservations
- Edit existing reservations
- Delete reservations
- SQLite database storage

## Installation and Usage

### Running from Source
1. Ensure Python 3.6+ is installed
2. Clone this repository
3. Navigate to the project directory
4. Run: `python main.py`

### Running the Executable
1. Download the `main.exe` file from the releases
2. Double-click to run the application

## Database
The application uses SQLite database (`flights.db`).

## Project Structure
- `main.py` - Main application entry point
- `database.py` - Database operations
- `home.py` - Home page interface
- `booking.py` - Flight booking form
- `reservations.py` - View reservations
- `edit_reservation.py` - Edit/delete functionality