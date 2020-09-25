
# RL Humanoid Maze Solver

Demo Video [here](https://drive.google.com/file/d/1R7KlKXhLdm0ZP_DaYa8dCx3IvxafaMwd/view?usp=sharing)

### 15CS496L MAJOR PROJECT <br>
CSE Dept. May 2019 <br>
ProjectID CSE532744

Guide - Dr. T Sujithra, Assistant Professor (CSE Dept, SRM Institute of Science and Technology, Chennai)

## Contents
1. Videos folder contains the final implementation video.
2. Report folder contains the final report pdf, latex source and final review ppt
3. Codes folder contains required scripts to run the code


## Code Instructions
### System Requirements - 
 - OS: Ubuntu 16.04/18.04
 - RAM: 8GB
 - GPU above GTX950 is preferred

### System Setup - 
1. Install Anaconda Python 3.6
2. Create new conda env named "rl"
3. In this conda env, install the following python libraries -
	- Numpy
	- Tensorflow
	- Roboschool
	- Squaternion
	- OpenAI Gym

*Extract Builds.rar from [here](https://drive.google.com/file/d/1qSRSU-h1TGCtWEeZc_R7P6xybK-40CRA/view?usp=sharing) into the Scripts directory*

### Execution - 
1. Go to Scripts/Builds/MazeHumanoid folder.
2. Run ./MazeHumanoid.x86_64 in a terminal. Ensure it has execute permission.
3. Unity Window will open. Select Resolution and Quality.
4. Finally Unity Environment will start with a humanoid and a maze.
5. Open another terminal and go to Codes Folder.
5. Activate Conda Environment
6. Run "python humanoid.py"
7. The humanoid will attempt to solve the maze


