from tkinter import *
from typing import Callable


class Model:
    def __init__(self):
        self.input_str: str = ""

    @property
    def data(self) -> str:
        return self.input_str

    @data.setter
    def data(self, value) -> None:
        self.input_str = value


class View:
    def __init__(self):
        self.root = Tk()
        self.equation = StringVar()

    def set_equation(self, value: str) -> None:
        self.equation.set(value)

    def setup_view(self, callback: Callable) -> None:
        calculation = Label(self.root, textvariable=self.equation)
        self.set_equation("0")
        calculation.grid(columnspan=4)
        self.setup_buttons(callback)

    def setup_buttons(self, callback: Callable) -> None:
        button_1 = Button(self.root, text="1", command=lambda: callback("1"))
        button_1.grid(row=1, column=0)

        button_2 = Button(self.root, text="2", command=lambda: callback("2"))
        button_2.grid(row=1, column=1)

        button_3 = Button(self.root, text="3", command=lambda: callback("3"))
        button_3.grid(row=1, column=2)

        button_4 = Button(self.root, text="4", command=lambda: callback("4"))
        button_4.grid(row=2, column=0)

        button_5 = Button(self.root, text="5", command=lambda: callback("5"))
        button_5.grid(row=2, column=1)

        button_6 = Button(self.root, text="6", command=lambda: callback("6"))
        button_6.grid(row=2, column=2)

        button_7 = Button(self.root, text="7", command=lambda: callback("7"))
        button_7.grid(row=3, column=0)

        button_8 = Button(self.root, text="8", command=lambda: callback("8"))
        button_8.grid(row=3, column=1)

        button_9 = Button(self.root, text="9", command=lambda: callback("9"))
        button_9.grid(row=3, column=2)

        button_0 = Button(self.root, text="0", command=lambda: callback("0"))
        button_0.grid(row=4, column=0)

        button_plus = Button(self.root, text="+", command=lambda: callback("+"))
        button_plus.grid(row=1, column=3)

        button_minus = Button(self.root, text="-", command=lambda: callback("-"))
        button_minus.grid(row=2, column=3)

        button_multi = Button(self.root, text="*", command=lambda: callback("*"))
        button_multi.grid(row=3, column=3)

        button_divide = Button(self.root, text="/", command=lambda: callback("/"))
        button_divide.grid(row=4, column=3)

        button_equal = Button(self.root, text="=", command=lambda: callback("="))
        button_equal.grid(row=4, column=2)

        button_clear = Button(self.root, text="C", command=lambda: callback("C"))
        button_clear.grid(row=4, column=1)

    def start_main_loop(self) -> None:
        self.root.mainloop()


class Controller:
    def __init__(self, view: View, model: Model):
        self.model = model
        self.view = view

    def start(self) -> None:
        """Set up and start the view"""
        self.view.setup_view(self.button_click_handler)
        self.view.start_main_loop()

    def button_click_handler(self, value: str) -> None:
        """Redirect to the suitable handler function base on the value of the clicked button"""
        if value == "=":
            self._equal_button()
        elif value == "C":
            self._clear_button()
        else:
            self._button_pressed(value)

    def _button_pressed(self, num: str) -> None:
        """Add the value of the clicked button to the equation"""
        self.model.data += str(num)
        self.view.set_equation(self.model.data)

    def _equal_button(self) -> None:
        """Evaluate the equation and show the result"""
        total = str(eval(self.model.data))
        self.view.set_equation(total)
        self.model.data = ""

    def _clear_button(self) -> None:
        """Clear out the sreen of the calculator"""
        self.model.data = ""
        self.view.set_equation(self.model.data)


if __name__ == "__main__":
    controller = Controller(View(), Model())
    controller.start()
