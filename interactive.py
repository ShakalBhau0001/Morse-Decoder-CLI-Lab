from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

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
    console.print(
        Panel.fit(
            "[bold cyan]🔤 International Morse Code 🔤[/bold cyan]",
            border_style="cyan",
        )
    )
    console.print(
        Panel(
            "1️⃣  Text → Morse\n" "2️⃣  Morse → Text\n" "3️⃣  Exit",
            title="📋 Menu",
            border_style="blue",
        )
    )
    choice = Prompt.ask(
        "[bold yellow]Choose an option[/bold yellow]",
        choices=["1", "2", "3"],
    )

    if choice == "1":
        text = Prompt.ask("[bold yellow]Enter text[/bold yellow]")
        morse = text_to_morse(text)
        console.print(
            Panel(
                morse,
                title="🔐 Morse Code",
                border_style="green",
            )
        )
    elif choice == "2":
        morse = Prompt.ask(
            "[bold yellow]Enter Morse code[/bold yellow]\n"
            "[dim](space separated, / for space)[/dim]"
        )
        text = morse_to_text(morse)
        console.print(
            Panel(
                text,
                title="🔓 Decoded Text",
                border_style="green",
            )
        )
    elif choice == "3":
        console.print("[bold red]Exiting... See You Soon![/bold red]")


if __name__ == "__main__":
    main()
