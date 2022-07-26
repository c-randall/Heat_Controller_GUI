# Heat_Controller_GUI
GUI for Watlow EHG-SL10 heat controller, uses Modbus RTU serial connection.

## Project description:
The Watlow EHG-SL10 heat controller uses Modbus RTU serial connection protocols. Communication and control of the controller was originally supported directly by Watlow through their proprietary EHG-soft software. This software was discontinued in 2007 and was only supported on Windows XP. In order to communicate and control the device on newer opperating systems, this GUI was developed. The GUI is a self-contained program that was originally written using python. The tool can be used without any knowledge of Python, however, modifications for your own applications will require a moderate amount of Python knowledge. A visual of the app window is shown below:

<p algin="center">
<img width="845" alt="Untitled" src="https://user-images.githubusercontent.com/39809042/180931114-602f84e8-9745-4262-81de-3a54b60d6332.png">
</p>

## File descriptions:
-`main_windows.exe`: executable application compiled for Windows PCs, tested on Windows 10
-`main_macos.app`: executable application compiled for macOs computers, tested on macOS Monterey (ver: 12.4)
- `gui.ui`: user interface file (created using the PyQt5 Designer), this file only needs to be edited if HEAVY changes to the visual parts of the GUI are desired
- `main.py`: Python script that incorporates code for both the GUI and the app functionality, this is the file that would need to be modified to change smaller visuals in the GUI and/or any app functionality
- `dummy_serial.py`: functions to initialize a dummy RTU serial slave for testing purposes, taken from the tests folder of the minimalmodbus module on GitHub
- `test_minimalmodbus.py`: data from a serial slave, taken from the tests folder of the minimalmodbus module on GitHub

## How to use:
1) Download the `main_windows` or `main_macos` file depending on your operating system 
2) Launch the application by clicking on it 
3) Go into your device manager to determine the COM port that your controller is plugged into
4) Select the correct COM port using the drop down in the GUI
5) Click the "START" button to begin reading the set point (SP) and proces variable (PV)
6) To change the SP, type in a number or use the arrows to adjust the value in the editable box above the "Engage" button
7) Click the "Engage" button to write the new SP to the controller
9) Click the "STOP" button to stop reading the temperatures and to reset the SP back to 20 C

NOTE: If the "DUMMY" COM port is selected, the app will simulate a heat controller by adjusting the PV up or down to match the current SP. Additionally, if the incorrect COM port is selected or a connection cannot be established with your device, the COM port will automatically switch back to the "DUMMY" port. 

## Modification instructions:
This project was completed using Python 3.9. An environment was built using Anaconda that included the following packages: pyqt5-tools (ver: 5.15.4.2.2), minimalmodbus (ver: 2.0.1), and pyinstaller (ver: 5.2). 

The `gui.ui` file can be read back into the PyQt5 Designer tool if you would like to make heavy modifications to the visual part of the GUI. Afterward, you would need to extract the functions from the `main.py` file to keep the GUI operational. 

If you are satisfied with the visual aspect of the GUI, the `main.py` file only has a few lines of code that could be edited to make this program more functional for other heat controllers. Mainly, you would need to update the "read" and "write" registers. These are hard-coded in as "20" and "34" respectively. Do a search for these numbers and replace them where necessary with the registers that match your device, taken from the manual. 

Other desired modifications may include changing the min/max set points, which are set to 20 and 99 C, respectively. Additionally, Be the "STOP" button automatically resets the controller temperature to 20 C, which may not be desired by other users. 

After any modifications have been made, another executable file can be generated using the pyinstaller module. Open a command terminal in your Python environment and navigate to the directory that contains your new `main.py` file. Afterward, enter the code:

```
pyinstaller --onefile --windowed
```

which will compile your app into a standalone program that can be run from a single file and that opens without the need to have the command terminal running in the background.
