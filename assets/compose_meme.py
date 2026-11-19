#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme: scene + Impact-style captions + real make.fun ghost."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SCENE = "/home/hatch/workspace/makefun/gta6-meme-x-01/assets/media-generation-gta6-download-scene-0-bab41e0b-c9d7-4620-abf3-57c0fd673d9c.png"
MARK = "/tmp/mark-1024.png"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01/meme-gta6-download.png"

FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

img = Image.open(SCENE).convert("RGBA")
W, H = img.size  # 1600x1600

def text_w(draw, s, font):
    b = draw.textbbox((0, 0), s, font=font, stroke_width=10)
    return b[2] - b[0]

def draw_caption(draw, lines, y_top, size):
    font = ImageFont.truetype(FONT, size)
    y = y_top
    for line in lines:
        w = text_w(draw, line, font)
        draw.text(((W - w) / 2, y), line, font=font, fill="white",
                  stroke_width=10, stroke_fill="black")
        y += int(size * 1.18)
    return y

d = ImageDraw.Draw(img)
# Top caption in the dark band
draw_caption(d, ["WAITED 13 YEARS", "FOR GTA 6"], 60, 118)
# Bottom caption in the dark band
draw_caption(d, ["DOWNLOAD: 47 HOURS LEFT"], 1330, 100)

# Ghost: sit it on the couch's right armrest (bottom-right), with a soft contact shadow.
mark = Image.open(MARK).convert("RGBA")
ghost_w = 240
mark = mark.resize((ghost_w, ghost_w), Image.LANCZOS)
gx, gy = 1465 - ghost_w // 2, 890  # center x ~1465, top y 890 -> bottom ~1130 on armrest

# soft shadow: dark ellipse under the ghost, blurred
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([gx + 15, gy + ghost_w - 18, gx + ghost_w - 15, gy + ghost_w + 22], fill=(0, 0, 0, 140))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
img = Image.alpha_composite(img, shadow)

img.paste(mark, (gx, gy), mark)

img = img.convert("RGB").resize((1024, 1024), Image.LANCZOS)
img.save(OUT, "PNG")
print("saved", OUT, img.size)
