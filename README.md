# AC Tracker

A Streamlit app to keep track of AC units across multiple buildings. The app allows users to log in, view company information, add/edit AC units, and manage maintenance tickets.

## Features

- User authentication
- Home/Dashboard with company information
- Add/Edit AC units
- Add maintenance tickets
- View AC units by building
- Upload images and documents for AC units
- View maintenance history for each unit

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/ac_tracker.git
    cd ac_tracker
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the app:**

    ```sh
    streamlit run app.py
    ```

## Usage

1. **Login:**
   - Access the app and log in using the provided credentials.

2. **Navigate through the app:**
   - Use the sidebar to navigate between the Home/Dashboard, Add/Edit Unit, Add Ticket, and the different building pages.

3. **Add/Edit Units:**
   - Use the form to add new units or edit existing ones.

4. **Add Tickets:**
   - Use the form to add maintenance tickets for any unit.

5. **View Units by Building:**
   - Select a building from the sidebar to view and manage the AC units for that building.

## Folder Structure

