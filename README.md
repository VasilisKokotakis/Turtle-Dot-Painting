
# 🎨 Turtle Dot Painting — Interactive Edition

Bring **Damien Hirst vibes** to your Python screen with a splash of colors and a touch of interactivity 🐢✨

This upgraded version of *Turtle Dot Painting* lets you **generate new artworks** and **save them** right from inside the window — no keyboard shortcuts needed!

---

## 🌟 Features

✅ Generates a **10 × 10 grid** of vibrant, randomly colored dots
✅ **Interactive buttons** to create new paintings or save your artwork
✅ **No external libraries** — pure Python and turtle magic
✅ Each artwork is unique and instantly re-generatable
✅ Saved paintings are timestamped as `.eps` files for easy export

---

## 🖱️ New Interactive Controls

After each painting finishes, two buttons appear at the bottom:

| Button               | Action                                                      |
| -------------------- | ----------------------------------------------------------- |
| 🖼 **Save Painting** | Exports your current artwork as an `.eps` image file        |
| 🔁 **New Painting**  | Clears the canvas and generates a brand-new random painting |

Just click the buttons inside the Turtle window — no need to type anything in the console!

---

## 🖼️ Demo

Every click of “New Painting” gives you something new and colorful:

```
🔴 🔵 🟢 🟣 🟡
🟣 🟡 🔵 🟢 🔴
...
```

*(...but way prettier and smoother in the Turtle window 😄)*

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/VasilisKokotakis/turtle-dot-painting.git
   cd turtle-dot-painting
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. Wait for the painting to complete, then click a button:

   * **Save Painting** 💾 → save it to your folder
   * **New Painting** 🎨 → make another masterpiece

---

## 🛠️ Requirements

* Python 3.7+
* `turtle` (built-in)
* `random` (standard library)
* No extra installs required 🚫📦

---

## 💡 Tips & Customization

You can tweak these constants at the top of the script:

```python
GRID_SIZE = 10       # Grid size (10x10)
DOT_SIZE = 20        # Dot diameter
SPACING = 50         # Distance between dots
START_OFFSET = 250   # Canvas offset from center
```

Try experimenting with different values for your own style!

---

## 🧠 Fun Fact

The **turtle** module was inspired by the 1960s **Logo Turtle Robot**, a real machine that moved on the floor and drew with a pen! 🐢🖊️

---

## 📜 License

MIT — share the colors, spread the joy 🌈✨

