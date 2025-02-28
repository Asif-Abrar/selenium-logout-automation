# Facebook, Google, and GitHub Auto Logout Script

This Python script uses Selenium to automatically log out from Facebook, Google, and GitHub when you are logged into your current Chrome profile.

## Features

- Detects whether you are logged into Facebook, Google, and GitHub.
- Logs out from these accounts automatically.
- Uses your existing Chrome profile for seamless login detection.

## Prerequisites

1. Install **Google Chrome version 133.0.6943.*** (if not already installed).
2. Install **Python (3.x recommended)**.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/Asif-Abrar/selenium-logout-automation.git
   cd selenium-logout-automation
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```sh
   python -m venv venv
   ```

   - Activate the environment:
     - **Windows:** `venv\Scripts\activate`
     - **Mac/Linux:** `source venv/bin/activate`

3. **Install Required Packages**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Update the Chrome Profile Path**

   - Check path in chrome `chrome://version`
   - Open `main.py`
   - Update the `chrome_profile_path` variable with the path to your Chrome profile.

2. **Run the Script**

   - If using a virtual environment:
     ```sh
     python main.py
     ```
   - If using the batch script (Windows only):
     ```sh
     autoenv.bat
     ```

## Notes

- This script **requires** your Chrome profile path to be set correctly for it to work.
- If Google or GitHub modifies their logout process, the script might need updates.
- Running this script while Chrome is already open may cause conflicts. Close Chrome before running the script.

## Contributions

Feel free to submit a pull request or report issues!

## Author

Asif Abrar - [GitHub Profile](https://github.com/Asif-Abrar)
