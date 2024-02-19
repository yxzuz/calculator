"""Display the calculator user interface."""
from calculator_ui import CalculatorUI
import tkinter as tk
# from tkinter import ttk
from controller import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.run()
