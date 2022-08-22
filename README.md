# Heat_Controller_GUI
GUI for Watlow EHG-SL10 heat controller, uses Modbus RTU serial connection.

## Project description:
The Watlow EHG-SL10 heat controller uses Modbus RTU serial connection protocols. Communication and control of the controller was originally supported directly by Watlow through their proprietary EHG-soft software. This software was discontinued in 2007 and was only supported on Windows XP. In order to communicate and control the device on newer opperating systems, this GUI was developed. The GUI is a self-contained program that was originally written using python. The tool can be used without any knowledge of Python, however, modifications for your own applications will require a moderate amount of Python knowledge. A visual of the app window is shown below:

![MainWindowScreenShot](https://user-images.githubusercontent.com/39809042/181647247-416492c4-e638-4758-93f5-1f16a6642867.png)

![ConfigureScreenShot](https://user-images.githubusercontent.com/39809042/181647263-f6c24831-ef6c-4488-a342-e9f5abf82610.png)

The first image shows the "Main Window" tab, where the widgets are used to show the continuously read (updated every 1 second) temperatures for the set point (SP) and process variable (PV). The second image shows the "Configure" tab, which is where the read/write registers and function codes can be modified. This tab allows this app to work for more than just the Watlow EHG-SL10. It can work with any Modbus RTU supported controller, so long as you input the correct registers/function codes from your device. The app is set up to automatically save and load your configuration, so you should only need to modify the values once if you are always using it with the same controller. There are also tabs for "Directions" and "About" which include valuable information, but are not fully pictured here.

## File descriptions:
- `main_windows.exe`: executable application compiled for Windows PCs, tested on Windows 10
- `main_macos.app`: executable application compiled for macOs computers, tested on macOS Monterey (ver: 12.4)
- `gui.ui`: user interface file (created using the PyQt5 Designer), if you wish to build your own temperature controller, you may wish to start with this GUI file
- `main.py`: Python script that incorporates code for both the GUI and the app functionality, this is the file that would need to be modified to change any app functionality
- `dummy_serial.py`: functions to initialize a dummy RTU serial slave for testing purposes, taken from the tests folder of the minimalmodbus module on GitHub
- `test_minimalmodbus.py`: data from a serial slave, taken from the tests folder of the minimalmodbus module on GitHub

## How to use:
1) Download the `main_windows` or `main_macos` file depending on your operating system 
2) Launch the application by clicking on it 
3) Go into your device manager to determine the COM port that your controller is plugged into
4) Select the correct COM port using the drop down in the GUI's "Main Window" tab
5) Click the "START" button to begin reading the set point (SP) and proces variable (PV)
6) To change the SP, type in a number or use the arrows to adjust the value in the editable box above the "Engage" button
7) Click the "Engage" button to write the new SP to the controller
9) Click the "STOP" button to stop reading the temperatures and to reset the SP back to the minimum SP temperature

NOTE: If you are not using the app with a Watlow EHG-SL10 controller, you may need to first select the "Configure" tab and input the read/write registers and read/write function codes for the SP and PV. These values can be found in the detailed manual of any controller that supports Modbus RTU. Once correctly configured, follow the above instructions.

NOTE: If the "DUMMY" COM port is selected, the app will simulate a heat controller by adjusting the PV up or down to match the current SP. Additionally, if the incorrect COM port is selected or a connection cannot be established with your device, the COM port will automatically switch back to the "DUMMY" port. 

## Modification instructions:
This project was completed using Python 3.9. An environment was built using Anaconda that included the following packages: pyqt5-tools (ver: 5.15.4.2.2), minimalmodbus (ver: 2.0.1), and pyinstaller (ver: 5.2). 

The `gui.ui` file can be read back into the PyQt5 Designer tool if you would like to make heavy modifications to the visual part of the GUI. Afterward, you can convert the newly saved file into a python script using

```
pyuic5 -x gui.ui -o gui.py
```

which will gernate a new file called `gui.py` with the Python code that creates the GUI. This code can be copied into the `main.py` file to replace the current GUI lines (prior to the logic building). NOTE: the `Ui_MainWindow` class was updated to inherit the attributes from `QtWidgets.QtMainWindow` rather than from `object`. This was done in order to preserve the `QtSettings` capabilities, which save and load the settings from the "Configure" tab every time the app is closed and opened, respectively. This means that everywhere the `gui.py` file uses `MainWindow`, the code needs to be replaced with `self.` instead. I would highly recommend not making heavy modifications to the GUI part of the code if you are not very familiar with classes and the Qt widgets. 

If you are satisfied with the visual aspect of the GUI, the `main.py` file can directly be edited to change any logic capabilities. There are multiple functions defined near the end of the file, e.g. `read_SP()` and `write_SP()`. Making changes to these functions to suit your needs should be fairly simple. 

After any modifications have been made to the `main.py` file, another executable application can be generated using the pyinstaller module. Open a command terminal in your Python environment and navigate to the directory that contains your new `main.py` file. Afterward, enter the code:

```
pyinstaller --onefile --windowed main.py
```

which will compile your app into a standalone program that can be run from a single file and that opens without the need to have the command terminal running in the background. Pyinstaller will only compile an app that is compatible with the OS that you build it on. If you wish to create both a windows and macos version, you will need access to two different computers that run the separate operating systems.

NOTE: Although the `dummy_serial.py` and `test_minimalmodbus.py` files do not need to be modified at all, they are still required in order to build the "DUMMY" serial slave. Make sure to download them and keep them in the same directory as your `main.py` file while working on modifications or compiling a new version of this program.
