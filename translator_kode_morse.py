MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

MORSE_REVERSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text):
    text = text.upper()
    result = []

    for char in text:
        if char == ' ':
            result.append('/')
        elif char in MORSE_CODE:
            result.append(MORSE_CODE[char])

    return ' '.join(result)

def morse_to_text(morse):
    result = []
    words = morse.split(' / ')

    for word in words:
        letters = word.split()
        decoded = ''

        for code in letters:
            if code in MORSE_REVERSE:
                decoded += MORSE_REVERSE[code]

        result.append(decoded)

    return ' '.join(result)

def translate(input_text):
    if all(c in ".- /" for c in input_text.strip()):
        return morse_to_text(input_text)
    else:
        return text_to_morse(input_text)

while True:
    user_input = input("\nMasukkan teks/morse (atau 'exit'): ")

    if user_input.lower() == 'exit':
        print("Keluar dari translator ⚡")
        break

    print("Hasil:", translate(user_input))