"""Extract the original eight-view OpenGFX passenger bus sprites.

Source: OpenTTD/OpenGFX sprites/png/roadvehicles/vehiclesroad01.png
Original coordinates: base-3092-road-vehicles.pnml (spr3092).
License: GPL-2.0, copyright OpenGFX contributors.
"""
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen

from PIL import Image

url = "https://raw.githubusercontent.com/OpenTTD/OpenGFX/master/sprites/png/roadvehicles/vehiclesroad01.png"
original = Image.open(BytesIO(urlopen(url, timeout=45).read()))
if original.mode != "P":
    raise RuntimeError("Expected original OpenGFX indexed 8bpp sprites")

views = [
    (82, 8, 8, 18), (98, 8, 20, 16), (130, 8, 28, 12), (178, 8, 20, 16),
    (210, 8, 8, 18), (226, 8, 20, 16), (258, 8, 28, 12), (306, 8, 20, 16),
]
sheet = Image.new("P", (256, 20), 0)
sheet.putpalette(original.getpalette())
for i, (x, y, w, h) in enumerate(views):
    sheet.paste(original.crop((x, y, x + w, y + h)), (i * 32, 0))
out = Path("graphics")
out.mkdir(exist_ok=True)
sheet.save(out / "megabus_opengfx.png")
print("Generated original OpenGFX bus sprite sheet")
