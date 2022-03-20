from utils import Utils
import tkinter as tk
import tkinter.ttk as ttk


class Button:

    ready = False
    job = None

    def __init__(self, root, row=0, column=0, text="Button", color=[0, 0, 0], onClick=None) -> None:
        self.root = root
        self.btn = None
        self.row = row
        self.column = column

        self.setColor(color)
        self.setText(text)
        self.onClick(onClick)
        self.build()

    def setText(self, text):
        self.text = text
        self.update()

    def setTextDelay(self, delay, text):
        self.delay(delay, lambda: self.setText(text))

    def cancelJob(self):
        if self.job != None:
            self.root.after_cancel(self.job)
            self.job = None

    def delay(self, delay, func):
        self.cancelJob()
        self.job = self.root.after(delay, func)

    def update(self):
        if self.ready == False or not self.btn:
            return
        self.btn.config(text=self.text, command=self.command, bg=Utils.fromRGB(*self.color))

    def build(self):
        if self.btn:
            print("[WARNING] Tried to build button that is already built. Use btn.update() instead.")
            return

        self.btn = tk.Button(
            self.root,
            text=self.text,
            background=Utils.fromRGB(*self.color),
            #  width=16,
            #  height=4,
            wraplength=100,
            fg=Utils.fromRGB(*self.textColor()))
        # self.btn.pack(fill="both", pady=2, padx=5)
        self.btn.grid(row=self.row, column=self.column, padx=5, pady=2, sticky=tk.NSEW)
        self.ready = True

    def setColor(self, color):
        self.color = color
        self.update()

    def onClick(self, func):
        self.command = Utils.passProps(func, self)
        self.update()

    def textColor(self):
        bgLuminance = Utils.luminance(*self.color)
        txtLuminance = Utils.luminance(255, 255, 255)
        if bgLuminance > txtLuminance:
            ratio = ((txtLuminance + 0.05) / (bgLuminance + 0.05))
        else:
            ratio = ((bgLuminance + 0.05) / (txtLuminance + 0.05))

        if ratio > 1 / 3:
            self.textColor = [0, 0, 0]
        else:
            self.textColor = [255, 255, 255]
        return self.textColor
