# MAX_VALUE = THE BACKGROUND GRAPH, HE IS THE DESIRED GOAL
# VALUE = CURRENT VALUE IN MAX_VALUE 
#
#
# ERRORS:
# U need set size before value or max_values (because widget_size not implemented yet)
#
# FUTURE: create a size property with _data_processing() 

example = """
RelativeLayout:
    CustomProgressBar:
        size: (200, 200)
        pos: (100, 100)
        max_value: [100, 140, 90, 100, 110]
        value: [80, 60, 50, 40, 32]
        thickness: 48
        #colors: ["#008000","A75EC1","1CA884", "DC772D", "DC2D42"]
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
        self._max_value = [2]
        self._value = [1]
        # Cores
        self._background_color = [0,0,0,1]
        self._colors = [C("#FFBA13"), C("#1E90FF"), C("#1CA884"), C("#A75EC1"),
                       C("17973AC"), C("791644"), C("5553D3"), C("A59575")]
        # Desenhar widget
        #self._data_processing()

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):
        if type(value) != int:
            raise TypeError("Progress must be an integer value.")
        elif value != self._thickness:
            self._thickness = value
            self._data_processing()

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if type(value) != list:
            raise TypeError("Progress must be a List.")
        else:
            self._value = value

    @property
    def max_value(self):
        return self._max_value
    
    @max_value.setter
    def max_value(self, value):
        if type(value) != list:
            raise TypeError("Progress must be a List.")
        else:
            self._max_value = value

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
    def colors(self):
        return self._colors

    @colors.setter
    def colors(self, hexlist):
        
        if type(hexlist) != list:
            raise TypeError("Colors must be a Hexadecimal code in a List.")
        
        conversion = list()
        for x in hexlist:
            if type(x) != str:
                raise TypeError("Colors must be a Hexadecimal Code.")
            else:
                conversion.append(C(x))
        self._colors = conversion
        self._data_processing()


    def _data_processing(self):

        if len(self._max_value) != len(self._value):
            raise IndexError("'max_value' and 'value' must have the same amount of values.")

        elif len(self._colors) < len(self._max_value):
            raise IndexError("Insufficient colors. Assign colors propertie with a list with same number of values as in 'max_value'.")
        else:
            i= 0
            for x in self._max_value:
                print("{} < {}".format(x, self._value[i]))
                if x < self._value[i]:
                    raise ValueError("'value' cannot be greater than 'max_value'.")
                i+= 1
            self._draw()


    def _draw(self):

        with self.canvas:
            # Limpar layout
            self.canvas.clear()

            # Base - Cinza para compensar transparencia inicial
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # DRAWING MAX VALUE AND VALUE 

            previous_value = 0
            progress_value = 0
            i = 0 
            for x in self._max_value:
                
                # 'max_value' calc
                actual_value = ((x * 100) / sum(self._max_value))/100 * 360
                # 'value' calc
                actual_progress = ((self._value[i] * 100) / sum(self._max_value))/100 * 360
                # bk color
                actual_color = self._colors[i]
                actual_color[-1] = 0.5

                # background
                Color(*actual_color)
                Ellipse(pos=self.pos, size=self.size, angle_start=(previous_value), angle_end=(progress_value+actual_value))

                # progress
                Color(*self._colors[i])
                Ellipse(pos=self.pos, size=self.size, angle_start=(previous_value), angle_end=(progress_value+actual_progress))

                progress_value += actual_value
                previous_value = progress_value
                i += 1


            # Circulo interno
            Color(*self._background_color)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))



#######EXAMPLE##################################################################EXAMPLE##############
#######################################EXAMPLE#######################################################
#######EXAMPLE##################################################################EXAMPLE###############

# EXAMPLE KV CODE IN LINE 10
if __name__ == '__main__':
    
    class Main(App):

        def build(self):
            main_widget = Builder.load_string(example)
            return main_widget
    Main().run()