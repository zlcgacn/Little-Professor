# Little Professor Simulation

This Python script, `professor.py`, simulates the "Little Professor" educational toy. It generates simple addition problems for the user to solve and keeps track of their score.

## How it Works

1.  **Level Selection:** The program first prompts the user to enter a difficulty level (1, 2, or 3).
    *   Level 1: Operands are single digits (0-9).
    *   Level 2: Operands have two digits (10-99).
    *   Level 3: Operands have three digits (100-999).
    If the user enters an invalid level (not 1, 2, or 3, or not an integer), they are prompted again.

2.  **Problem Generation:** The script generates 10 random addition problems in the format `X + Y = ` based on the selected level.

3.  **Solving Problems:** For each problem, the user is prompted for an answer.
    *   If the answer is correct, the program moves to the next problem.
    *   If the answer is incorrect or not a valid integer, the program outputs `EEE` and gives the user another chance.
    *   The user gets up to **three tries** per problem.
    *   If the user fails to answer correctly after three tries, the correct answer is displayed.

4.  **Scoring:** After all 10 problems are presented, the program displays the final score (number of problems answered correctly out of 10).

## How to Run

1.  Make sure you have Python installed.
2.  Navigate to the directory containing `professor.py` in your terminal.
3.  Run the script using the command:
    ```bash
    python professor.py
    ```
4.  Follow the prompts to select a level and solve the math problems. 
