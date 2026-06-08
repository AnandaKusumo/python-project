base = {
    "k": "ꦏ", "g": "ꦒ", "n": "ꦤ", "t": "ꦠ", "d": "ꦢ",
    "p": "ꦥ", "b": "ꦧ", "m": "ꦩ",
    "y": "ꦪ", "r": "ꦫ", "l": "ꦭ", "w": "ꦮ",
    "s": "ꦱ", "h": "ꦲ",
    "j": "ꦗ", "c": "ꦕ",
    "ng": "ꦔ", "ny": "ꦚ",
    "dh": "ꦝ", "th": "ꦛ"
}

vowel = {
    "a": "",
    "i": "ꦶ",
    "u": "ꦸ",
    "e": "ꦺ",
    "o": "ꦺꦴ"
}

pangkon = "꧀"

def normalize(text):
    text = text.lower()
    text = text.replace("ng", "ŋ")
    text = text.replace("ny", "ñ")
    text = text.replace("dh", "ð")
    text = text.replace("th", "þ")
    return text

def restore(c):
    return {
        "ŋ": "ng",
        "ñ": "ny",
        "ð": "dh",
        "þ": "th"
    }.get(c, c)

def split_syllables(word):
    syllables = []
    i = 0

    while i < len(word):
        c = word[i]

        if c in vowel:
            syllables.append(c)
            i += 1
            continue

        syll = c

        if i + 1 < len(word) and word[i+1] in vowel:
            syll += word[i+1]
            i += 2
        else:
            i += 1

        syllables.append(syll)

    return syllables

def convert_syllable(s):
    if s in vowel:
        return vowel[s]

    c = s[0]
    v = s[1] if len(s) > 1 else "a"

    if c == "ŋ":
        base_char = "ꦔ"
    elif c == "ñ":
        base_char = "ꦚ"
    elif c == "ð":
        base_char = "ꦝ"
    elif c == "þ":
        base_char = "ꦛ"
    else:
        base_char = base.get(c, c)

    return base_char + vowel.get(v, "")

def apply_pangkon(tokens):
    result = []

    for i, t in enumerate(tokens):
        converted = convert_syllable(t)

        # pangkon HANYA kalau:
        # - bukan vokal
        # - dan di akhir kata
        is_last = (i == len(tokens) - 1)
        is_consonant = t and t[0] not in vowel

        if is_last and is_consonant:
            result.append(converted + pangkon)
        else:
            result.append(converted)

    return result

digits = {
    "0": "꧐",
    "1": "꧑",
    "2": "꧒",
    "3": "꧓",
    "4": "꧔",
    "5": "꧕",
    "6": "꧖",
    "7": "꧗",
    "8": "꧘",
    "9": "꧙"
}

def convert_numbers(text):
    for k, v in digits.items():
        text = text.replace(k, v)
    return text

def latin_to_javanese(text):
    text = convert_numbers(text)
    text = normalize(text)

    words = text.split()
    output = []

    for w in words:
        syllables = split_syllables(w)
        converted = apply_pangkon(syllables)
        output.append("".join(converted))

    return " ".join(output)

if __name__ == "__main__":
    while True:
        txt = input("Masukkan teks: ")
        print("Aksara Jawa:", latin_to_javanese(txt))