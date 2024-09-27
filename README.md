# quiz_game

**Quiz Game**
A simple Quiz Game built using Python, where the player answers a series of True/False questions. The game tracks the player's progress and continues asking questions until the quiz is complete.

**Features**
Displays questions with a True/False prompt.
Tracks the current question number.
Allows players to continue until all questions are answered.
Project Structure
The project contains the following files:

main.py: The main driver file that runs the quiz game.
question_model.py: Defines the Question class used to represent individual questions in the quiz.
quiz_brain.py: Handles the game logic, including question progression and checking if more questions remain.
data.py: A file that contains the question_data - a list of dictionaries, each containing a question and its answer.
**How to Run**
Prerequisites
Could you make sure that you have Python installed on your system?

Clone the repository or download the files to your local machine.
You can open the project folder in a terminal or command prompt.
Run the following command to start the quiz:
python main.py
Gameplay
The game will display a question followed by a prompt asking for your answer (True/False).
Type True or False and hit enter.
The game will continue until there are no more questions left.
**Example Questions**

Q.1: The sky is blue. (True/False):
Q.2: Python is a snake. (True/False):
**Customization**
You can modify the quiz data by editing the data.py file. The data is represented as a list of dictionaries, where each dictionary contains the following keys:

"text": The question text.
"answer": The correct answer (True/False).
**Example:**


question_data = [
    {"text": "The sky is blue.", "answer": "True"},
    {"text": "Python is a programming language.", "answer": "True"},
    {"text": "The sun sets in the east.", "answer": "False"},
]
**Future Enhancements**

Implement score tracking to show how many questions the player answered correctly.
Add a user interface using a library like Tkinter for a graphical quiz game.


**Notes**
You can add more details about specific features, future improvements, or how users can contribute, depending on your preference. If you upload this on GitHub, this README.md will display nicely on the repository's main page.
