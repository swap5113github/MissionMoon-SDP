import random
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.vertex_instructions import Triangle
from kivy.graphics import Color
from kivy.properties import ObjectProperty

def keyboard_is_closed(self):
    self._keyboard.unbind(on_key_down=self.on_press_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_press_keyboard_up)
    self._keyboard = None

def on_press_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.present_speed_x = self.speed_along_X
    elif keycode[1] == 'right':
        self.present_speed_x = -self.speed_along_X
    return True

def on_press_keyboard_up(self, keyboard, keycode):
    self.present_speed_x = 0
    return True

def on_touching_down(self, touch):
    if touch.x < self.width/2:
        self.present_speed_x = self.speed_along_X
    else:
        self.present_speed_x = -self.speed_along_X
    return super(RelativeLayout,self).on_touching_down(touch)
    
def on_touching_up(self, touch):
    self.present_speed_x = 0