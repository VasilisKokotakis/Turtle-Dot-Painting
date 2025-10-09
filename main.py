import turtle as t
import random
from typing import List, Tuple
import time

# --- Configuration ---
DOT_COLORS: List[Tuple[int, int, int]] = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

GRID_SIZE = 10
DOT_SIZE = 20
SPACING = 50
START_OFFSET = 250

# --- Setup ---
t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

screen = t.Screen()
screen.setup(width=800, height=800)
screen.title("Modern Dot Art 🎨")
screen.bgcolor("#f8f9fa")

# --- Helper functions ---
def draw_dot(color: Tuple[int, int, int]) -> None:
    tim.dot(DOT_SIZE, color)

def move_to_next_row() -> None:
    tim.setheading(90)
    tim.forward(SPACING)
    tim.setheading(180)
    tim.forward(SPACING * GRID_SIZE)
    tim.setheading(0)

def draw_grid() -> None:
    tim.clear()
    tim.penup()
    tim.setheading(225)
    tim.goto(0, 0)
    tim.forward(START_OFFSET)
    tim.setheading(0)

    total_dots = GRID_SIZE * GRID_SIZE
    for dot_count in range(1, total_dots + 1):
        draw_dot(random.choice(DOT_COLORS))
        tim.forward(SPACING)
        if dot_count % GRID_SIZE == 0:
            move_to_next_row()
    show_buttons()

# --- Button system ---
button_drawer = t.Turtle()
button_drawer.hideturtle()
button_drawer.penup()

BUTTONS = {
    "New Painting": (-100, -320, 150, 50),
    "Save Painting": (150, -320, 150, 50),
}

def draw_button(label: str, x: int, y: int, width: int, height: int) -> None:
    """Draw a button rectangle with label."""
    button_drawer.goto(x - width / 2, y - height / 2)
    button_drawer.pendown()
    button_drawer.fillcolor("#e0e0e0")
    button_drawer.begin_fill()
    for _ in range(2):
        button_drawer.forward(width)
        button_drawer.left(90)
        button_drawer.forward(height)
        button_drawer.left(90)
    button_drawer.end_fill()
    button_drawer.penup()
    button_drawer.goto(x, y - 10)
    button_drawer.write(label, align="center", font=("Arial", 14, "bold"))

def show_buttons() -> None:
    """Display the two interactive buttons."""
    button_drawer.clear()
    for label, (x, y, w, h) in BUTTONS.items():
        draw_button(label, x, y, w, h)
    screen.update()

def hide_buttons() -> None:
    """Clear button drawings."""
    button_drawer.clear()
    screen.update()

def save_art() -> None:
    """Save the current turtle screen as an EPS file."""
    filename = f"dot_painting_{int(time.time())}.eps"
    canvas = screen.getcanvas()
    canvas.postscript(file=filename)
    print(f"✅ Saved as {filename}")

def new_art() -> None:
    """Generate a new random painting."""
    hide_buttons()
    print("🎨 Generating a new painting...")
    draw_grid()

def on_click(x: float, y: float) -> None:
    """Handle click events on the buttons."""
    for label, (bx, by, bw, bh) in BUTTONS.items():
        if (bx - bw / 2) <= x <= (bx + bw / 2) and (by - bh / 2) <= y <= (by + bh / 2):
            if label == "New Painting":
                new_art()
            elif label == "Save Painting":
                save_art()
            break

# --- Main ---
def main() -> None:
    draw_grid()
    screen.onclick(on_click)
    screen.mainloop()

if __name__ == "__main__":
    main()
