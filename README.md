# Chess-Game

We all know about the chess game if not please first read about chess.  
In the chess game there are total 8x8=64 blocks and 2 teams. First = White and second = Black

# Prerequisites:
 1. Python
 2. Basic knowlage about chess-game

# Python libraries included are:
In game we are use one librarie.
 1. Numpy Array

# Follow Below steps to run game.
 1. Create folder and clone repo.
 2. Create environment.
    ```bash
    python3 -m venv env
    ```
 3. Activate environment.
    ```bash
    source env/bin/activate
    ```
 4. Install requirement.txt.
    ```bash
    pip install requirement.txt
    ```
 5. Run game.
    ```bash
    python chess_game.py
    ```
 6. In terminal.
    ```bash
    [['S' '1' '2' '3' '4' '5' '6' '7' '8']
    ['a' '♖' '♙' '-' '-' '-' '-' '♟' '♜']
    ['b' '♘' '♙' '-' '-' '-' '-' '♟' '♞']
    ['c' '♗' '♙' '-' '-' '-' '-' '♟' '♝']
    ['d' '♔' '♙' '-' '-' '-' '-' '♟' '♚']
    ['e' '♕' '♙' '-' '-' '-' '-' '♟' '♛']
    ['f' '♗' '♙' '-' '-' '-' '-' '♟' '♝']
    ['g' '♘' '♙' '-' '-' '-' '-' '♟' '♞']
    ['h' '♖' '♙' '-' '-' '-' '-' '♟' '♜']]

    $ current_row : 
    $ current_col :
    $ next_row :
    $ next_col :
    ```
~ Please make sure you need to enter Four values.\
~ ex: 
     ```bash
    [['S' '1' '2' '3' '4' '5' '6' '7' '8']
    ['a' '♖' '-' '♙' '-' '-' '-' '♟' '♜']
    ['b' '♘' '♙' '-' '-' '-' '-' '♟' '♞']
    ['c' '♗' '♙' '-' '-' '-' '-' '♟' '♝']
    ['d' '♔' '♙' '-' '-' '-' '-' '♟' '♚']
    ['e' '♕' '♙' '-' '-' '-' '-' '♟' '♛']
    ['f' '♗' '♙' '-' '-' '-' '-' '♟' '♝']
    ['g' '♘' '♙' '-' '-' '-' '-' '♟' '♞']
    ['h' '♖' '♙' '-' '-' '-' '-' '♟' '♜']]

    $ current_row : 1
    $ current_col : 2
    $ next_row : 1
    $ next_col : 3
    ```
# Note: 

 1. if current_row or next_col enter 0 so, you out of the game.
 2. if user enter more than 8 number so, you out of the game.
 3. if current_row, current_col, next_row and next_col match same value so, you out of the game.
