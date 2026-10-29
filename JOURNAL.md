**2026.10.27**

-I started the project with the goal of creating an application that can start up on Windows within a few seconds, has a simple, old-school CLI vibe, and consumes little memory. Then I implemented printing the ASCII art to the screen from the art.dat file, and used the getattr() function to read the art and menu colors from settings.conf.
-As an idea, I would have read the application names and execution paths from the apps.conf file, but that would have been difficult to edit, so I started thinking about other solutions.
-I wanted to organize the code, so I solved it using def() functions.

**2026.10.27**

-As a solution, I am now reading the .lnk files from the apps folder.
-I add the execution paths to the apps list, and print the names of the games/apps character by character using (f" [{count}]"), while trimming the end of the name at the extension dots, so e.g. control.exe.lnk becomes control.
-I added a rudimentary launching and option-checking mechanism.

**2026.10.27**

-I abandoned the def() structure because it makes the readability and comprehension of the program harder for me.
-Due to a few bugs, I replaced os.system() with the more reliable os.startfile().
-I added a "UI" made of box-drawing characters; as a solution, I created an m variable representing the desired box length. I tried to crudely align the right edge of the box with the others using print(" " * ((m-3)-len(app)), end="") and print("║").
-It hadn't stood out to me until now, but the ASCII art was displaying incorrectly due to i = i.strip().split(";"). I replaced this with print(artcolor + i.rstrip("\n")).
-I fixed a few minor bugs originating from app launching or selection (e.g. if count only had 10 elements, the 11th non-existent element could still be selected).
-I eventually changed art.dat to art.txt.
-I added background colorization (although I think it looks pretty ugly except for black :D).
-Writing Readme.md and Journal.md.
-In this project, I learned how to use a few new functions like getattr(), which will likely be useful to me. Currently, unfortunately, I have run out of ideas and things to fix in the code (or maybe I just don't notice the bugs), so I am putting this project aside for a while. If I get any new ideas, I will likely return to it; building this project was a really great experience.