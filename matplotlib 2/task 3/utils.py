class Utils:

    ## lambda so I can pass props into the command
    ## function for buttons in tkinter
    ## *_ stops python complaining about passing a prop
    ## When the function doesnt need one
    @staticmethod
    def passProps(func, *x):
        """Pass props into function"""
        return lambda *_: func(*x)

    @staticmethod
    def fromRGB(r, g, b):
        """Converts rgb to format for tkinter"""
        return f'#{r:02x}{g:02x}{b:02x}'

    @staticmethod
    def luminance(r, g, b):
        a = []
        for c in [r, g, b]:
            c /= 255
            if c <= 0.03928:
                a.append(c / 12.92)
            else:
                a.append(pow((c + 0.055) / 1.055, 2.4))
        return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722
