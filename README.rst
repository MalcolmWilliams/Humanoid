InMoov Humanoid
***************

Open source 3D printed life size robot.

Hardware
========

1. The hardware build instructions can be found on the inmoov website: http://inmoov.fr/
2. There are some useful user designed parts here: http://www.thingiverse.com/Gael_Langevin/collections/inmoov-parts-and-derivatives/
3. Parts I used/made are located in the CAD folder of this repo.
4. The filaments used were `white <https://www.amazon.com/dp/B01EKFV60S/ref=twister_B01EKFV2F2?_encoding=UTF8&th=1>`_ and `black <https://www.amazon.com/dp/B01EKFV4RS/ref=twister_B01EKFV2F2?_encoding=UTF8&psc=1>`_


Default Servo Mapping and Limits
--------------------------------

+--------+-----------+---------+----------+---------+---------+
| Group  | Part Name | Pin Num | Pos Rest | Pos Min | Pos Max |
+========+===========+=========+==========+=========+=========+
| Hand   | Thumb     | 2       |          | 10      | 170     |
|        +-----------+---------+----------+---------+---------+
|        | Index     | 3       |          | 0       | 160     |
|        +-----------+---------+----------+---------+---------+
|        | Middle    | 4       |          | 10      | 170     |
|        +-----------+---------+----------+---------+---------+
|        | 4th       | 5       |          | 170     | 10      |
|        +-----------+---------+----------+---------+---------+
|        | Pinky     | 6       |          | 160     | 20      |
|        +-----------+---------+----------+---------+---------+
|        | Wrist     | 7       |          |         |         |
+--------+-----------+---------+----------+---------+---------+
| Right  | Bicep     | 8       |          | 90      | 0       |
| Arm    +-----------+---------+----------+---------+---------+
|        | Rotate    | 9       |          | 180     | 20      |
|        +-----------+---------+----------+---------+---------+
|        | Shoulder  | 10      |          | 180     | 0       |
|        +-----------+---------+----------+---------+---------+
|        | Omplate   | 11      |          |         |         |
+--------+-----------+---------+----------+---------+---------+
| Left   | Bicep     | 8       |          | 100     | 15      |
| Arm    +-----------+---------+----------+---------+---------+
|        | Rotate    | 9       |          | 180     | 20      |
|        +-----------+---------+----------+---------+---------+
|        | Shoulder  | 10      |          | 180     | 0       |
|        +-----------+---------+----------+---------+---------+
|        | Omplate   | 11      |          | 150     | 95      |
+--------+-----------+---------+----------+---------+---------+


Software
========

The framework that runs the robot is called "MyRobotLab".

This has been tested on windows 10 and ubuntu 16.04


Usage
-----

1. Navigate to the project directory and launch the ``run.bat`` or ``run.sh`` file.
2. This will launch a command prompt window, the mrl application and a chrome tab.
3. In the chrome tab click the microphone to make it red and enable speech recognition.
4. Look in the test.py script to see what commands are recognised. For example, ``ear.addCommand("raise your right arm", "python", "armRightUp")`` will run the ``armRightUp()`` function when you say "raise your right arm"
5. Exit by exiting the mrl application or hitting ``ctrl-c`` on the command window

*Note:* you will have to re-launch the application every time you make a change to ``test.py``


Installation Procedure
----------------------

There is some information online, but a lot of it is confusing or out of date.

1. Clone this repository with ``git clone https://github.com/MalcolmWilliams/Humanoid.git``
2. Download the mrl jar file. (http://myrobotlab.org/download)
3. Put it in a folder called ``mrl`` within this repository. The ``.gitignore`` is setup to ignore changes in this folder
4. Download java if needed (same link)
5. Open command promt at folder with the mrl jar file and run ``java -jar myRobotLab.jar``
6. This will start mrl. go to the runtime tab and click ``system\install all``
7. You can then load and run a python script. Note: the ports defined in the script will likely have to be changed if the computer is different. 

The Arduino firmware can be found in the mrl directory: ``./mrl/resource/Arduino/MRLComm/``. Flash it the same as you would any other Arduino file.
