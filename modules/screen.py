''' 
Screen module

Controls LCD-screen
'''
import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
import board


class Screen:
    lcd_columns = 16
    lcd_rows = 2

    lcd_rs = digitalio.DigitalInOut(board.D5)
    lcd_en = digitalio.DigitalInOut(board.D17)
    lcd_d7 = digitalio.DigitalInOut(board.D18)
    lcd_d6 = digitalio.DigitalInOut(board.D12)
    lcd_d5 = digitalio.DigitalInOut(board.D16)
    lcd_d4 = digitalio.DigitalInOut(board.D25)

    def __init__(self):
        self.screen = characterlcd.Character_LCD_Mono(
            self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5,
            self.lcd_d6, self.lcd_d7, self.lcd_columns, self.lcd_rows)
        self.screen.clear()

    def write(self, text):
        self.screen.message = text
