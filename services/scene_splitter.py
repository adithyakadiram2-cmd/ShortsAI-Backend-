def split_script(script):
    lines = []

    for sentence in script.split("."):
        sentence = sentence.strip()
        if sentence:
            lines.append(sentence)

    return lines
0

