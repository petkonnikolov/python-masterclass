def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width -len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)

with open("centered.txt", mode='w') as centered_file:
# call the function
    centre_text("spam and eggs", file=centered_file)
    centre_text("spam, spam and eggs", file=centered_file)
    centre_text(12, file=centered_file)
    centre_text("spam, spam, spam and spam", file=centered_file)
    centre_text("first", "second", 1, 2, "spam", sep=':', file=centered_file)