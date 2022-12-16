emoji_dict = {
    "happy": "😃",
    "heart": "😍",
    "rotfl": "🤣",
    "smile": "😊",
    "crying": "😭",
    "kiss": "😘",
    "clap": "👏",
    "grin": "😁",
    "fire": "🔥",
    "broken": "💔",
    "think": "🤔",
    "excited": "🤩",
    "boring": "🙄",
    "winking": "😉",
    "ok": "👌",
    "hug": "🤗",
    "cool": "😎",
    "angry": "😠",
    "python": "🐍",
}

sentence = input("Please enter a sentence:")
sentence = sentence.split()
new_sentence = ""
for word in sentence:
    for emoji in emoji_dict:
        if word == emoji:
            word = emoji_dict[emoji]
    if sentence[-1] != word:
        new_sentence = new_sentence + word + " "
    else:
        new_sentence = new_sentence + word
print(new_sentence)
    
