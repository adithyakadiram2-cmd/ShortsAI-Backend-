def generate_subtitles(script):
    """
    Generate simple subtitles from the script.

    Returns a list of subtitle lines.
    """

    lines = []

    for line in script.split("\n"):
        line = line.strip()
        if line:
            lines.append(line)

    return {
        "status": "success",
        "count": len(lines),
        "subtitles": lines
    }
0

