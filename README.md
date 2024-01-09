# World Clock Application

This is a simple Python application that displays the current time in different time zones. The time zones included are Sydney, Tokyo, Singapore, London, New York, and Los Angeles.

### Requirements

- Python 3.x
- tkinter
- pytz

You can install the necessary libraries by running the following command:

```bash
pip install pytz tkinter
```

## Usage
To run the application, simply execute the Python script:
python world_clock.py
This will open a new window displaying the current time in each of the specified time zones. The time is updated every second.

## Packaging the World Clock Application
This part of the project involves packaging the World Clock Python script into a standalone executable using `pyinstaller`. Here are the steps to do it:

### Requirements

- Python 3.x
- pyinstaller

You can install `pyinstaller` by running the following command:

```bash
pip install pyinstaller
```

## Creating a Custom Icon for the World Clock Application

This part of the project involves creating a custom icon for the World Clock application and using it for a desktop shortcut.

### Requirements

- An `.ico` file for the icon
- PyInstaller

## Creating or Choosing an Icon

The icon should be a `.ico` file. You can create one using an image editing software or find free icons online. Make sure the icon is square and at least 32x32 pixels for best results.

### Adding the Icon to the PyInstaller Script

You can specify the icon when creating the standalone executable with PyInstaller by adding the `--icon` option followed by the path to your `.ico` file. For example:

```bash
pyinstaller --onefile --windowed --icon=path/to/your_icon.ico your_script.py
```
Replace path/to/your_icon.ico with the actual path to your .ico file and your_script.py with the name of your Python script.

## Creating a Shortcut on Your Desktop
After you’ve created the standalone executable with the custom icon, you can create a shortcut to it on your desktop. Here’s how you can do it on Windows:
Right-click on the desktop and select New > Shortcut.
Click Browse and navigate to the dist folder created by PyInstaller. Select the executable and click OK.
Click Next, give your shortcut a name, and click Finish.
Your new shortcut should appear on your desktop with the custom icon.

## Adding a Bitcoin Ticker to the World Clock Application
This part of the project involves adding a Bitcoin ticker to the World Clock application. The ticker displays the current Bitcoin price in USD, updated every second.

### Requirements

- Python 3.x
- tkinter
- pytz
- requests

You can install the necessary libraries by running the following command:

```bash
pip install tkinter pytz requests
```

The Bitcoin ticker is implemented as a label in the tkinter application. The requests library is used to make HTTP requests to the CoinDesk API, which provides the current Bitcoin price in various currencies.
The ticker is updated every second along with the times in the time zones. The update function makes a GET request to the CoinDesk API, parses the response to extract the current Bitcoin price, and updates the Bitcoin label with the new price.

## Troubleshooting
Please replace "path/to/my_project" and "world_clock.py" with the actual path to your project directory and the name of your Python script, respectively. 
