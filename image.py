from PIL import Image, ImageDraw, ImageFont

def text_to_image(
    text: str,
    filename: str = "output.png",
    size: tuple[int, int] = (3840, 2160),   # high resolution (4K)
    bg: str = "#1e1e2e",
    color: str = "white",
    font_path: str = "/System/Library/Fonts/Supplemental/Arial.ttf",
    font_size: int = 160,
    margin: int = 200,
    line_spacing: float = 1.3,
) -> str:
    img = Image.new("RGB", size, bg)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    # Wrap words so each line fits inside the margins
    max_width = size[0] - 2 * margin
    lines, line = [], ""
    for word in text.split():
        test = f"{line} {word}".strip()
        if draw.textlength(test, font=font) <= max_width:
            line = test
        else:
            lines.append(line)
            line = word
    lines.append(line)

    # Center the whole block vertically
    line_h = int(font_size * line_spacing)
    y = (size[1] - line_h * len(lines)) / 2

    for ln in lines:
        w = draw.textlength(ln, font=font)
        draw.text(((size[0] - w) / 2, y), ln, font=font, fill=color)
        y += line_h

    img.save(filename)
    return filename

text_to_image("Hey man")

# if __name__ == "__main__":
    
    
    