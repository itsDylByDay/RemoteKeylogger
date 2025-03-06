# Remote Keylogger: Network-Based Keystroke Capture Tool

## Objective

Developed a Python-based remote keylogger to capture keystrokes and mouse activity on a target device, sending logs over a TCP network to a designated server. Utilizes `pynput` for input capture, `socket` for networking, and file I/O for timestamped logging. Demonstrates system interaction, network communication, and ethical security testing for educational purposes.

### Skills Learned
- Gained proficiency in system-level input monitoring using `pynput` for keystroke and mouse capture.
- Developed TCP networking skills with `socket` for remote data transmission.
- Enhanced understanding of timestamped logging and file I/O operations in Python.
- Improved ability to simulate attacker techniques ethically for security awareness.

### Tools Used
- Python 3.x for scripting and logic implementation.
- `pynput` library for capturing keyboard and mouse events.
- `socket` module for establishing TCP network communication.
- `datetime` module for adding timestamps to log entries.
- File I/O operations for local and remote logging.

## Steps

*Step 1: Initial Configuration*  
Configured the keylogger with the server IP and port for remote logging, initializing variables for capturing and buffering keystrokes.

*Step 2: Mouse Click Trigger*  
Implemented `on_click()` to detect left mouse clicks, logging click coordinates and starting keystroke capture with `start_listening()`.

*Step 3: Keystroke Capture*  
Used `on_press()` to capture keystrokes, converting special keys (e.g., space, backspace) into readable log entries and storing them in a buffer.

*Step 4: Logging with Timestamps*  
Developed `log_to_file()` to save keystrokes and mouse events to a local file (`keystrokes_log.txt`) with timestamps using `datetime`.

*Step 5: Remote Transmission*  
Created `send_data()` to transmit the log file to a remote server over TCP using `socket`, triggered when the Enter key stops capture.

*Step 6: Server-Side Logging*  
Set up a server script to receive logs, appending the target’s IP and keystroke data to `remote_keystrokes.txt` for analysis.
