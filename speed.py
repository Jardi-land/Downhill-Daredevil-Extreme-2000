# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------


from spritesheet import SpriteSheet
import alias as al
from custom_font import Font


class Speed:
    def __init__(self) -> None:
        self.font_spritesheet = SpriteSheet(al.path(
            "files/font/custom/tilesheet.png"), al.path("files/font/custom/data.json"))

        self.font = Font(self.font_spritesheet, 5)

        self.speed = 10

        self.speed_surface = self.font.render(f"{str(int(self.speed))}M/S", "#")

    def render_text(self):
        self.speed_surface = self.font.render(f"{str(int(self.speed))}M/S", "#")

    def update(self):
        self.render_text()
        return self.speed_surface