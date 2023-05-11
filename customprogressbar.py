
# THIS FILE NEED 3 VALUES - Dynamic values will come with time (maybe), feel free to implement.
# VALUE = LIST( (1, 2, 3)) > NEED EXACTLY THREE NUMBERS !!!
# MAX_VALUE = LIST ( (1, 2, 3)) > NEED EXACTLY THREE NUMBERS !!!
# MAX_VALUE = THE BACKGROUND GRAPH, HE IS THE DESIRED GOAL
# VALUE = CURRENT VALUE IN MAX_VALUE 

# PS: create a widget_size property with _draw() 
# ERRORS:
# U need set size before value or max_values (because widget_size not implemented yet)

example = """
RelativeLayout:
    CustomProgressBar:
        size: (200, 200)
        pos: (100, 100)
        max_value: [100, 150, 130]
        value: [80, 80, 48]
        thickness: 48
        primary_color: "#FFBA13"
        secondary_color: "#1E90FF"
        tertiary_color: "#1CA884"
        #background_color: "#FFFFF6"

"""

# CODE

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.graphics import Color, Ellipse
from kivy.utils import get_color_from_hex as C


class CustomProgressBar(Widget):

    def __init__(self, **kwargs):
        super(CustomProgressBar, self).__init__(**kwargs)

        # Espessura 
        self._thickness = 25
        # Valores
        self._max_value = [2, 2, 2]
        self._value = [1, 1, 1]
        # Cores
        self._background_color = [0,0,0,1]
        self._primary_color = C("#FFBA13")
        self._secondary_color = C("#1E90FF")
        self._tertiary_color = C("#1CA884")
        # Desenhar widget
        self._data_processing()

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if type(value) != int:
            raise TypeError("Progress must be an integer value.")
        elif value != self._thickness:
            self._thickness = value
            self._draw()

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) != list:
            raise TypeError("Progress must be a List.")
        elif len(value) != 3:
            raise KeyError("Exactly three numbers are required.")
        elif len(value) == 3:
            self._value = value
            self._data_processing()

    @property
    def max_value(self):
        return self._max_value
    
    @max_value.setter
    def max_value(self, value):
        if type(value) != list:
            raise TypeError("Progress must be a List.")
        elif len(value) != 3:
            raise KeyError("Exactly three numbers are required.")
        elif len(value) == 3:
            self._max_value = value
            self._data_processing()

    @property
    def background_color(self):
        return self._background_color
    
    @background_color.setter
    def background_color(self, hexcode):
        if type(hexcode) not in [str, list]:
            raise TypeError("Color must be a Hexadecimal code.")
        elif type(hexcode) == str and self._background_color != C(hexcode):
            self._background_color = C(hexcode)
            self._draw()
        elif type(hexcode) == list and self._background_color != hexcode:
            self._background_color = hexcode
            self._draw()


    @property
    def primary_color(self):
        return self._primary_color

    @primary_color.setter
    def primary_color(self, hexcode):
        if type(hexcode) not in [str, list]:
            raise TypeError("Color must be a Hexadecimal code.")
        elif type(hexcode) == str and self._primary_color != C(hexcode):
            self._primary_color = C(hexcode)
            self._draw()
        elif type(hexcode) == list and self._primary_color != hexcode:
            self._primary_color = hexcode
            self._draw()

    @property
    def secondary_color(self):
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, hexcode):
        if type(hexcode) not in [str, list]:
            raise TypeError("Color must be a Hexadecimal code.")
        elif type(hexcode) == str and self._secondary_color != C(hexcode):
            self._secondary_color = C(hexcode)
            self._draw()
        elif type(hexcode) == list and self._secondary_color != hexcode:
            self._secondary_color = hexcode
            self._draw()

    @property
    def tertiary_color(self):
        return self._tertiary_color

    @tertiary_color.setter
    def tertiary_color(self, hexcode):
        if type(hexcode) not in [str, list]:
            raise TypeError("Color must be a Hexadecimal code.")
        elif type(hexcode) == str and self._tertiary_color != C(hexcode):
            self._tertiary_color = C(hexcode)
            self._draw()
        elif type(hexcode) == list and self._tertiary_color != hexcode:
            self._tertiary_color = hexcode
            self._draw()

    def _data_processing(self):

        # max_value = background
        self._mv1 = ((self._max_value[0] * 100) / sum(self._max_value))/100 * 360
        self._mv2 = ((self._max_value[1] * 100) / sum(self._max_value))/100 * 360
        self._mv3 = ((self._max_value[2] * 100) / sum(self._max_value))/100 * 360

        # value = actual value / progress bar
        self._v1 = ((self._value[0] * 100) / self._max_value[0])/100 * self._mv1
        self._v2 = ((self._value[1] * 100) / self._max_value[1])/100 * self._mv2
        self._v3 = ((self._value[2] * 100) / self._max_value[2])/100 * self._mv3

        self._draw()


    def _draw(self):

        with self.canvas:
            
            # Limpar layout
            self.canvas.clear()

            # Base - Cinza para compensar transparencia inicial
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # BACKGROUND VALOR 1
            primary_background_color = self._primary_color.copy()
            primary_background_color[-1] = 0.5

            Color(*primary_background_color)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(self._mv1))
            
            # PROGRESS VALOR 1
            Color(*self._primary_color)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(self._v1))

            # BACKGROUND VALOR 2
            secondary_background_color = self._secondary_color.copy()
            secondary_background_color[-1] = 0.5

            Color(*secondary_background_color)
            Ellipse(pos=self.pos, size=self.size, angle_start=(self._mv1),
                    angle_end=(self._mv1 + self._mv2))
            
            # PROGRESS VALOR 2
            Color(*self._secondary_color)
            Ellipse(pos=self.pos, size=self.size, angle_start=(self._mv1),
                    angle_end=(self._mv1 + self._v2))

            # BACKGROUND VALOR 3
            tertiary_background_color = self._tertiary_color.copy()
            tertiary_background_color[-1] = 0.5

            Color(*tertiary_background_color)
            Ellipse(pos=self.pos, size=self.size, angle_start=(self._mv1+self._mv2),
                    angle_end=(self._mv1 + self._mv2 + self._mv3))
            
            # PROGRESS VALOR 3
            Color(*self._tertiary_color)
            Ellipse(pos=self.pos, size=self.size, angle_start=(self._mv1+self._mv2),
                    angle_end=(self._mv1 + self._mv2 + self._v3))

            # Circulo interno
            Color(*self._background_color)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))



#######EXAMPLE##################################################################EXAMPLE##############
#######################################EXAMPLE#######################################################
#######EXAMPLE##################################################################EXAMPLE###############

if __name__ == '__main__':
    
    class Main(App):

        def build(self):
            main_widget = Builder.load_string(example)
            return main_widget
    Main().run()