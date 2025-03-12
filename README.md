# Battle of the Hero's Game

Welcome to the "Battle of the Hero's" game! This is a game where two players strategize and battle to see who the true hero is. The game supports different characters, each with unique abilities.

## Prerequisites

- `Python` (3.x)
- `pip` (Python package manager)
- `virtualenv` (for creating Python environments)

## Setup Instructions

### 1. Create a Virtual Environment

To get started, you'll need to create a virtual environment. This ensures that the dependencies are isolated from your global Python environment.

Open a terminal and run the following commands to create and run a virtual environment:

```bash
    python3 -m venv venv
```

Mac OS:
```bash
    source venv/bin/activate
```

You should now see `(venv)` at the beginning of your terminal prompt.

### 2. Running the Game

#### Option 1:
- **Install Dependencies & Play The Game**
    - Run the Game using `game.sh` to install the dependencies and run the game using one script.
```bash
    bash game.sh
```

#### Option 2:
- **Install Dependencies**
    - Once the virtual environment is activated, you need to install the required dependencies. These are listed in the requirements.txt file. 
```bash
    pip install -r requirements.txt
```

- **Play the Game**
    - Run the Python Script Directly
```bash
    python3 game.py
```
This will run the game script and allow you to play directly in the terminal.

### 3. Deactivate the Virtual Environment
When you're done, you can deactivate the virtual environment by running:

```bash
    deactivate
```