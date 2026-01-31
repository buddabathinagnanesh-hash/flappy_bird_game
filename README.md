# 🐦 Flappy Bird – Advanced Edition

An advanced version of the classic **Flappy Bird** game built using **Python** and **Pygame**.  
This project focuses on **gameplay balance, clean architecture, and user experience** rather than just basic functionality.

---

## 🎮 Features

- ✅ Smooth bird physics (balanced gravity & jump)
- ✅ Bird rotation based on velocity
- ✅ Dynamic difficulty with Levels 1, 2, and 3
- ✅ Beginner-friendly slow-motion start (first 3 seconds)
- ✅ Pause & Resume feature (Press **P**)
- ✅ Score and Best Score system
- ✅ Clean Game Over screen
- ✅ Modular and well-structured code
- ✅ Custom bird sprite

---

## 🧠 Game Design Highlights

- The game starts **easy** and becomes harder gradually.
- Difficulty increases smoothly by adjusting pipe speed.
- Visual clarity and player comfort were prioritized.
- Game states are clearly separated:
  - Start
  - Playing
  - Paused
  - Game Over

---

## 📁 Project Structure

```text
flappy_bird_game/
│
├── main.py        # Main game loop and game states
├── bird.py        # Bird physics, movement, and sprite
├── pipes.py       # Pipe generation and movement
├── settings.py    # Game constants and tuning values
├── bird.png       # Bird sprite image
├── README.md      # Project documentation
└── .gitignore     # Git ignore file
🕹️ Controls
Key	Action
SPACE	Make the bird jump
P	Pause / Resume the game
R	Restart after Game Over
ESC	Quit the game
1️⃣ Install dependencies

Make sure Python is installed, then run:

pip install pygame

2️⃣ Run the game
python main.py

🛠️ Technologies Used

Python 3

Pygame

🎯 Learning Outcomes

This project helped me learn:

Game physics tuning

Game state management

Modular Python programming

Debugging real-time applications

Using Git & GitHub for version control

📌 Notes

No external assets or sound libraries are used.

The project is designed for educational purposes.

Code is written to be readable and beginner-friendly.

👨‍💻 Author

Gnaniii
Flappy Bird – Advanced Edition (Python + Pygame)

⭐ If you like this project, feel free to explore and improve it further!


---

## ✅ NEXT STEPS (DO THIS NOW)

After saving `README.md`, run:

```bash
git add README.md
git commit -m "Add README documentation"
git push
