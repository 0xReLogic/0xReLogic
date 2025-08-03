import os
import re

README_PATH = "README.md"

# --- Story Templates ---

SCENE_START = """# The Labyrinth of Logic

<p align="center">
  <img src="https://via.placeholder.com/1200x400.png?text=The+Labyrinth+of+Logic" alt="The Labyrinth of Logic Banner"/>
</p>

### Greetings, Traveler. My name is Allen Elzayn.

You find yourself at the entrance of **The Labyrinth of Logic**, a maze woven from pure reason and paradox. I am the architect of this place. Only those who can navigate its challenges may prove their worth.

Before you lie two doors, each marked with a cryptic statement. One leads to the heart of the labyrinth, the other to an endless loop of confusion.

---

### **The First Trial: The Liar's Doors**

🚪 **Door Alpha:** "The statement on the other door is true."
🚪 **Door Beta:** "The statement on this door is false."

One door speaks the truth, the other lies. Which door will you choose?

---

> To make your choice, click on one of the doors below. This will create an issue in this repository, and the labyrinth will respond to your choice.

<p align="center">
  <a href="https://github.com/0xReLogic/0xReLogic/issues/new?title=logic_game%7Cchoose_door%7Calpha&body=I+choose+Door+Alpha.">
    <img src="https://via.placeholder.com/200x300.png?text=Door+Alpha" alt="Door Alpha" width="200"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/0xReLogic/0xReLogic/issues/new?title=logic_game%7Cchoose_door%7Cbeta&body=I+choose+Door+Beta.">
    <img src="https://via.placeholder.com/200x300.png?text=Door+Beta" alt="Door Beta" width="200"/>
  </a>
</p>

---

### My Stats & Tools

<!-- GitHub Stats will go here -->
"""

SCENE_WRONG_DOOR = """# The Labyrinth of Logic

<p align="center">
  <img src="https://via.placeholder.com/1200x400.png?text=A+Familiar+Place" alt="The Labyrinth of Logic Banner"/>
</p>

### A flicker of light, and you are back where you started.

The door you chose leads to a path that twists back upon itself. The logic was flawed. The architect's voice echoes, *"A paradox unresolved is a loop eternal. Think again."*

Before you lie the same two doors. A new choice awaits.

---

### **The First Trial: The Liar's Doors**

🚪 **Door Alpha:** "The statement on the other door is true."
🚪 **Door Beta:** "The statement on this door is false."

Which door will you choose?

---

> To make your choice, click on one of the doors below.

<p align="center">
  <a href="https://github.com/0xReLogic/0xReLogic/issues/new?title=logic_game%7Cchoose_door%7Calpha&body=I+choose+Door+Alpha.">
    <img src="https://via.placeholder.com/200x300.png?text=Door+Alpha" alt="Door Alpha" width="200"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/0xReLogic/0xReLogic/issues/new?title=logic_game%7Cchoose_door%7Cbeta&body=I+choose+Door+Beta.">
    <img src="https://via.placeholder.com/200x300.png?text=Door+Beta" alt="Door Beta" width="200"/>
  </a>
</p>

---

### My Stats & Tools

<!-- GitHub Stats will go here -->
"""

SCENE_NEXT_CHALLENGE = """# The Labyrinth of Logic

<p align="center">
  <img src="https://via.placeholder.com/1200x400.png?text=The+Path+Forward" alt="The Labyrinth of Logic Banner"/>
</p>

### The door swings open, revealing a path forward.

Correct. Your logic was sound. The paradox was resolved, and the way is now clear. But be warned, the challenges ahead will only grow more complex.

**[This is where the next puzzle will go. To be continued!]**

---

> To reset the game, click the button below.

<p align="center">
  <a href="https://github.com/0xReLogic/0xReLogic/issues/new?title=logic_game%7Creset&body=Reset+the+game.">
    <img src="https://via.placeholder.com/200x100.png?text=Reset+Game" alt="Reset Game" width="200"/>
  </a>
</p>

---

### My Stats & Tools

<!-- GitHub Stats will go here -->
"""

def update_readme(content):
    with open(README_PATH, "w") as f:
        f.write(content)

def main():
    issue_title = os.getenv("ISSUE_TITLE", "")
    
    # Default to start scene if no valid command
    new_content = SCENE_START

    if "logic_game" in issue_title:
        parts = issue_title.split("|")
        if len(parts) == 3:
            _, command, choice = parts
            
            if command == "choose_door":
                if choice == "beta": # The correct choice
                    new_content = SCENE_NEXT_CHALLENGE
                else: # The wrong choice (alpha)
                    new_content = SCENE_WRONG_DOOR

        elif len(parts) == 2 and parts[1] == "reset":
             new_content = SCENE_START

    update_readme(new_content)
    print(f"README.md updated based on issue: {issue_title}")

if __name__ == "__main__":
    main()
