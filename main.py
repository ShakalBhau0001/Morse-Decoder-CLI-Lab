MORSE_CODE = {
    # Letters
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Punctuation
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    # Space
    " ": "/",
}


# Conversion Of Text Message Into Morse Code

def text_to_morse(text):
    text = text.upper()
    morse_output = []

    for char in text:
        if char in MORSE_CODE:
            morse_output.append(MORSE_CODE[char])
        else:
            # For Ignoring Unsupported Characters
            pass

    return " ".join(morse_output)


# Conversion Of Morse Code Into Text Message

def morse_to_text(morse):
    reverse_morse = {value: key for key, value in MORSE_CODE.items()}
    decoded_text = ""

    for code in morse.split(" "):
        if code in reverse_morse:
            decoded_text += reverse_morse[code]
        else:
            decoded_text += ""

    return decoded_text


def main():
    print("🔤 International Morse Code 🔤")
    print("--------------------")
    print("1. Text → Morse")
    print("2. Morse → Text")
    print("3. Exit")
    print("--------------------")

    choice = input("Choose (1 , 2 or 3): ").strip()

    if choice == "1":
        text = input("Enter text: ")
        morse = text_to_morse(text)
        print("\n🔐 Morse Code:")
        print(morse)
    elif choice == "2":
        morse = input("Enter Morse code (space separated, / for space): ")
        text = morse_to_text(morse)
        print("\n🔓 Decoded Text:")
        print(text)
    elif choice == "3":
        print("❌ Exiting... See You Soon!")
    else:
        print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
