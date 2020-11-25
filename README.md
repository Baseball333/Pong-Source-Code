# Pong-Source-Code
Source code for a Pong variant I wrote about a year ago. I'll explain the logical structure later.

Second Commit:
I'm not explaining the logical structure right now.

Third Commit:
This repository hosts the source code for a Pong variant written in Python with the turtle and os libraries. The final game is accessible through a graphical shell which is easily written if Python is installed on a user's operating system(UNIX opr UNIX-like systems). Anyway, notice how the logical structure of the source code is not convenitonal OOP, instead something more like imperative instruction. For example, here is the graphical shell.

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=500)

Notice how direct instruction is provided instead of object orientation. This might appear deliberated although at the time I was not familiar with OOP and simply sought to create something. Be wary, this is not oppostion towards OOP, I was just explaining context.
