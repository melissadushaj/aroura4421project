# Hardware/display.py
from PIL import Image, ImageDraw, ImageFont
from Config.settings import FACE_COLS, FACE_ROWS   
from .waveshare_lcd import LCD_2inch, lcdconfig


class RobotDisplay:
    def __init__(self, rotation: int = 180):
        if hasattr(lcdconfig, "module_init"):
            try:
                lcdconfig.module_init()
            except Exception:
                pass

        self.lcd = LCD_2inch.LCD_2inch()
        self.lcd.Init()

        raw_w = getattr(self.lcd, "width", 240)
        raw_h = getattr(self.lcd, "height", 320)

        self.WIDTH = raw_h     
        self.HEIGHT = raw_w    

        try:
            self.lcd.rotation = rotation
        except AttributeError:
            pass

        if hasattr(self.lcd, "bl_DutyCycle"):
            try:
                self.lcd.bl_DutyCycle(60)  
            except Exception:
                pass

        self.image = Image.new("RGB", (self.WIDTH, self.HEIGHT), "black")
        self.draw = ImageDraw.Draw(self.image)
        self.font = self._load_default_font()

        self._rotation = rotation
        self.clear()

    def _load_default_font(self):
        try_paths = [
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        ]
        for p in try_paths:
            try:
                return ImageFont.truetype(p, 20)
            except Exception:
                continue
        return ImageFont.load_default()
    
    def _wrap_text(self, text: str, max_width: int):
        words = text.split()
        if not words:
            return []

        lines = []
        current = words[0]
        for word in words[1:]:
            test = current + " " + word
            bbox = self.draw.textbbox((0, 0), test, font=self.font)
            line_width = bbox[2] - bbox[0]
            if line_width <= max_width:
                current = test
            else:
                lines.append(current)
                current = word
        lines.append(current)
        return lines


    def clear(self, color="black"):
        self.image = Image.new("RGB", (self.WIDTH, self.HEIGHT), color)
        self.draw = ImageDraw.Draw(self.image)
        self.show()

    def show(self):
        img = self.image
        if self._rotation:
            img = img.rotate(self._rotation)
        self.lcd.ShowImage(img)

    def show_test_pattern(self):
        self.clear("black")
        w, h = self.WIDTH, self.HEIGHT

        self.draw.rectangle((0, 0, w // 2, h // 2), fill="red")
        self.draw.rectangle((w // 2, 0, w, h // 2), fill="green")
        self.draw.rectangle((0, h // 2, w // 2, h), fill="blue")
        self.draw.rectangle((w // 2, h // 2, w, h), fill="yellow")

        self.show()

    def show_text_center(self, text: str, fg="white", bg="black"):
        self.clear(bg)

        bbox = self.draw.textbbox((0, 0), text, font=self.font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (self.WIDTH - text_w) // 2
        y = (self.HEIGHT - text_h) // 2

        self.draw.text((x, y), text, font=self.font, fill=fg)
        self.show()

    def shutdown(self):
        if hasattr(self.lcd, "clear"):
            try:
                self.lcd.clear()
            except Exception:
                pass

        if hasattr(lcdconfig, "module_exit"):
            try:
                lcdconfig.module_exit()
            except Exception:
                pass

    def show_face(self, face_grid, emotion: str | None = None):

        emotion_colors = {
            "happy": ("yellow", "black"),
            "surprised": ("cyan", "black"),
            "empathetic": ("magenta", "black"),
            "confused": ("orange", "black"),
            "sad": ("blue", "black"),
            "sleeping": ("white", "black"),
        }

        fg, bg = emotion_colors.get(emotion, ("white", "black"))

        self.clear(bg)

        cols = FACE_COLS
        rows = FACE_ROWS

        cell_w = self.WIDTH // cols
        cell_h = self.HEIGHT // rows

        grid_w = cell_w * cols
        grid_h = cell_h * rows

        offset_x = (self.WIDTH - grid_w) // 2
        offset_y = (self.HEIGHT - grid_h) // 2

        for y in range(rows):
            for x in range(cols):
                if not face_grid[y][x]:
                    continue
                x0 = offset_x + x * cell_w
                y0 = offset_y + y * cell_h
                x1 = x0 + cell_w - 1
                y1 = y0 + cell_h - 1
                self.draw.rectangle((x0, y0, x1, y1), fill=fg)

        self.show()

    def show_notification(self, text: str):

        self.clear("navy")  

        title = "Notification <3"
        title_bbox = self.draw.textbbox((0, 0), title, font=self.font)
        title_w = title_bbox[2] - title_bbox[0]
        title_h = title_bbox[3] - title_bbox[1]
        title_x = (self.WIDTH - title_w) // 2
        title_y = 10
        self.draw.text((title_x, title_y), title, font=self.font, fill="white")

        margin = 10
        max_body_width = self.WIDTH - 2 * margin
        body_y = title_y + title_h + 15

        lines = self._wrap_text(text, max_body_width)

        sample_bbox = self.draw.textbbox((0, 0), "Ag", font=self.font)
        line_height = sample_bbox[3] - sample_bbox[1]

        for i, line in enumerate(lines):
            y = body_y + i * (line_height + 4)  
            self.draw.text((margin, y), line, font=self.font, fill="white")

        self.show()

    def show_music_screen(self, title: str, elapsed_s: int, total_s: int):

        self.clear("black")

        title_text = f"♪ {title}"
        title_bbox = self.draw.textbbox((0, 0), title_text, font=self.font)
        title_w = title_bbox[2] - title_bbox[0]
        title_x = (self.WIDTH - title_w) // 2
        self.draw.text((title_x, 10), title_text, font=self.font, fill="white")

        def fmt(t):
            m = t // 60
            s = t % 60
            return f"{m:02d}:{s:02d}"

        elapsed_s = max(0, elapsed_s)
        total_s = max(elapsed_s + 1, total_s) 
        time_text = f"{fmt(elapsed_s)} / {fmt(total_s)}"
        time_bbox = self.draw.textbbox((0, 0), time_text, font=self.font)
        time_w = time_bbox[2] - time_bbox[0]
        time_x = (self.WIDTH - time_w) // 2
        self.draw.text((time_x, 50), time_text, font=self.font, fill="white")

        bar_margin = 20
        bar_top = 80
        bar_bottom = bar_top + 10
        bar_left = bar_margin
        bar_right = self.WIDTH - bar_margin

        self.draw.rectangle((bar_left, bar_top, bar_right, bar_bottom), outline="white")

        progress = min(1.0, elapsed_s / total_s)
        fill_right = bar_left + int((bar_right - bar_left) * progress)
        self.draw.rectangle((bar_left, bar_top, fill_right, bar_bottom), fill="white")

        self.show()

