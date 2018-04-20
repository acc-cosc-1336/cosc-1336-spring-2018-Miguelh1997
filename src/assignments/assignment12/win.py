from tkinter import Tk, Label
from src.assignments.assignment12.converter import Converter


class Win(Tk):

    def __init__(self):

        self.miles = Converter()
        km = 100
        Tk.__init__(self, None, None)

        self.wm_title('Miles to Kilometers converter')
        self.label = Label(self, text='Km:' + str(km)).grid(row=0, column=1, sticky="w")
        self.label = Label(self, text='Miles:' + str(self.miles.get_miles_from_km(km))).grid(row=1, column=1, sticky="w")
        self.mainloop()