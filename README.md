# AI-Game-Collection
A collection of classic games enhanced with AI algorithms like Minimax, Pathfinding, Backtracking, and Vision AI.

# AI Game Collection 🎮🤖

**Live Demo**: [ai-games-by-riya.netlify.app](https:https://ai-game-collection-byriya.netlify.app/)  

A web-based collection of classic games powered by AI algorithms. Each game demonstrates a different AI technique — from search algorithms and heuristics to computer vision and rule‑based reasoning.

---

## 🕹️ Games in this Collection

| Game | AI Technique / Algorithm | Description |
|------|---------------------------|-------------|
| **Snake** | Pathfinding (e.g. A*) | The AI finds the optimal path to food while avoiding collisions with itself and the walls. |
| **Tic Tac Toe** | Minimax | The AI explores possible moves to choose the optimal play (win or draw). |
| **Connect Four** | Minimax + Alpha‑Beta Pruning | The AI efficiently searches the game tree, pruning branches to make decisions faster. |
| **Rock Paper Scissors** | Vision AI (Gesture Recognition) | Uses webcam input and computer vision to detect the player’s hand gesture, then plays accordingly. |
| **Guess the Word** | Knowledge Representation / Rule-based Inference | The AI uses a knowledge base and logic rules to guess the target word. |
| **2048 Game AI** | Heuristic Search | The AI uses heuristic evaluation and search techniques to try to reach the 2048 tile. |
| **Sudoku Solver** | Backtracking | The AI fills the board systematically by trying possibilities and backtracking when invalid. |

---

## 📂 Project Structure

```
├── README.md  
├── /public  
│   └── <static assets like images, CSS>  
├── /src  
│   ├── snake/  
│   ├── tic_tac_toe/  
│   ├── connect_four/  
│   ├── rock_paper_scissors/  
│   ├── guess_the_word/  
│   ├── game_2048_ai/  
│   └── sudoku_solver/  
├── requirements.txt    # (if using Python)  
├── package.json        # (if using Node / frontend dependencies)  
└── index.html           # main homepage linking to all games  
```

---

## 🛠 Setup & Installation

Below are general instructions. Adjust depending on whether you used pure frontend, Python backend, or hybrid.

### Prerequisites

- Python ≥ 3.x  
- (Optional) Node.js & npm  
- Web browser with webcam support (for Rock Paper Scissors)  

### Steps

1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/ai-game-collection.git
   cd ai-game-collection
   ```

2. Install dependencies (if using Python / backend):  
   ```bash
   pip install -r requirements.txt
   ```

3. (If applicable) Install frontend dependencies:  
   ```bash
   npm install
   ```

4. Run the application:  
   - If backend + frontend:  
     ```bash
     python app.py         # or your main server file
     ```
   - Or for a static frontend: open `index.html` or run a simple HTTP server, e.g.:  
     ```bash
     npx http-server .  
     ```

5. Navigate to `http://localhost:8000` (or your server’s address) to access the games.

---

## 💡 Usage

- From the homepage, select the game you want to play.  
- For **Rock Paper Scissors**, allow the browser to access your webcam.  
- Enter inputs or make moves as required; the AI will respond accordingly.  
- For **Sudoku**, you can input a puzzle and click “Solve” to see the AI solution.

---

## 📊 Performance & Results

- **Tic Tac Toe**: AI plays optimally; it should never lose.  
- **Connect Four**: With alpha-beta pruning, AI responds within acceptable time even on deeper search trees.  
- **2048 AI**: It consistently reaches the 2048 tile; sometimes higher depending on luck & heuristics.  
- **Rock Paper Scissors**: Gesture recognition achieves good accuracy (subject to lighting, clarity).  
- **Sudoku Solver**: Solves moderate puzzles in under a second.  
- **Snake**: AI pathfinding efficiently avoids collisions and reaches food.  
- **Guess the Word**: Uses inference rules to narrow down possible words intelligently.

---

## 🚀 Future Improvements

- Add **machine learning / reinforcement learning** for adaptive AI that improves with more gameplay data  
- Introduce **multi‑player modes**  
- Add **leaderboards / scoring systems**  
- Turn this into a **mobile app** (React Native, Flutter, etc.)  
- Expand the collection with additional AI game demos (e.g. Chess, Reversi, Maze Solving, etc.)  

---

## 📚 References & Further Reading

- Russell, S., & Norvig, *Artificial Intelligence: A Modern Approach*  
- TensorFlow.js / OpenCV.js documentation  
- Online tutorials & algorithm references (e.g. minimax, A*, backtracking)  
- Relevant blog posts, research papers, and implementation guides  

---

## 🧡 Acknowledgments

Thanks to all open‑source libraries, tutorials, and community resources that helped in building this collection.  
Built with ❤️ by **Riya**
