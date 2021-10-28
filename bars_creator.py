from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import re

def drawProgressBar(d, x, y, w, h, progress, bg="black", fg="green"):
    # draw background
    d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
    d.ellipse((x, y, x+h, y+h), fill=bg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

    # draw progress bar
    if progress == 0:
        return d
    w *= progress
    d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
    d.ellipse((x, y, x+h, y+h),fill=fg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

    return d

def create(fname, iname):
    out = Image.new("RGBA", (400, 38), (255, 255, 255, 0))
    Image.new
    d = ImageDraw.Draw(out)
    tested = 0
    for line in open(fname):
        match = re.search('Tested: (\d+)', line)
        if match:
            tested = int(match.group(1))
    passing = 0
    for line in open(fname):
        match = re.search('Passing: (\d+)', line)
        if match:
            passing = int(match.group(1))
    percent = 0
    if tested != 0:
        percent = passing / tested
    d = drawProgressBar(d, 0, 0, 150, 38, percent)
    out.save(iname)

def create_gcovr(fname, iname):
    out = Image.new("RGBA", (200, 38), (255, 255, 255, 0))
    Image.new
    d = ImageDraw.Draw(out)
    value = 0
    for line in open(fname):
        match = re.search('(\d+)%', line)
        stot = re.search('TOTAL', line)
        if match and stot:
            value = int(match.group(1))
    percent = value / 100
    d = drawProgressBar(d, 0, 0, 150, 38, percent)
    out.save(iname)

create("eca_sync", "tests.png")
create_gcovr("eca_lc", "lines.png")
create_gcovr("eca_lb", "branches.png")