# ArduPlot - Arduino sensor data visualizer

[ArduPlot](https://github.com/VP1147/arduplot) is a tool for visualize data from Arduino-connected sensors using [TeenyGraph](https://github.com/VP1147/tg).

![Image](da70de4a-9f29-480b-99ac-360f7214c334.jpg)

## Requiremments
> As of now, this program only works on Linux
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Python3](https://www.python.org/downloads/)
- And Python Libraries
  - pyserial
  - getch
  - graphics.py
  ```
  $ python3 -m pip install pyserial getch graphics.py
  ```
- Python3-tk
  ```
  $ sudo apt install python3-tk
  ```
## Instructions

### Load code to Arduino
- Open `arduplot.ino` with Arduino IDE
- Click **load**
- If any error, please check 

### Start the program
- Please make sure all libraries are installed
- open `arduplot.py` with Python
  ```
  $ python3 arduplot.py
  ```

## Support and Contact

For any bugs or suggestions, feel free to [open a issue](https://github.com/VP1147/arduplot/issues) and describe it. We'll sure appreciate your help.

