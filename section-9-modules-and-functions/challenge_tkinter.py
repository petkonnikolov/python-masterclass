# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480-8-200")
mainWindowPadding = 8
mainWindow['padx'] = mainWindowPadding

# mainWindow.columnconfigure(0, weight=1)
# mainWindow.columnconfigure(1, weight=1)
# mainWindow.columnconfigure(2, weight=1)
# mainWindow.columnconfigure(3, weight=1)
# mainWindow.columnconfigure(4, weight=1)
# mainWindow.rowconfigure(0, weight=1)
# mainWindow.rowconfigure(1, weight=1)
# mainWindow.rowconfigure(2, weight=1)
# mainWindow.rowconfigure(3, weight=1)
# mainWindow.rowconfigure(4, weight=1)
# mainWindow.rowconfigure(5, weight=1)
# mainWindow.rowconfigure(6, weight=1)

# widget to display calc display
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# key pad
key_pad = tkinter.Frame(mainWindow)
key_pad.grid(row=1, column=0, sticky='nsew')

# button widget
keys_dict = [
    [('C', 1), ('CE', 1)], 
    [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
    [('4', 1), ('5', 1), ('6', 1), ('-', 1)], 
    [('1', 1), ('2', 1), ('3', 1), ('*', 1)], 
    [('0', 1), ('=', 2), ('/', 1)]]

row = 0
for keyRoll in keys_dict:
    column = 0
    for key in keyRoll:
        tkinter.Button(key_pad, text=key[0]).grid(row=row, column=column, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        column += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(key_pad.winfo_width() + mainWindowPadding, result.winfo_height() + key_pad.winfo_height())
mainWindow.maxsize(key_pad.winfo_width() + mainWindowPadding, result.winfo_height() + key_pad.winfo_height())

mainWindow.mainloop()