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

Fourth Commit:
This Pong variant was written with simple instruction, which is evident in the game's components. Of the 172 lines all were written with the completion of components. Pong requires two paddles, a ball and their derived operations. A pen is also specified to write graphical components, although it is eventually retired through the pen.penup() method. Operations are described in the next commit.

Fifth Commit:
Functions for component movement are defined in these functions, specifically their limitations in the graphical shell(a Cartesian Plane). These components are established at a point in the Cartesian Plane by variable assignment.

Sixth Commit:
After the functions are defined and verified in runtime, the keyboard bindings are written. Keyboard bindings are especially important in Pong as during the 1970s terminals were the primary source of computing. As such, this Python variant is created to simulate the Pong experience of the mid-1970s. Keyboard bindings were also written with imperative instruction.

