InMoov Humanoid
***************

3D printable open-source humanoid robot

Hardware
========

The hardware build instructions can be found on the inmoov website: http://inmoov.fr/
There are some useful user designed parts here: http://www.thingiverse.com/Gael_Langevin/collections/inmoov-parts-and-derivatives/
Parts I used/made are located in the CAD folder of this repo.


Default Servo Mapping and Limits
--------------------------------

+--------+-----------+---------+----------+---------+---------+
| Group  | Part Name | Pin Num | Pos Rest | Pos Min | Pos Max |
+========+===========+=========+==========+=========+=========+
| Hand   | Thumb     | 2       |          | 10      | 170     |
|        +-----------+---------+----------+---------+---------+
|        | Index     | 3       |          | 0       | 160     |
|        +-----------+---------+----------+---------+---------+
|        | middle    | 4       |          | 10      | 170     |
|        +-----------+---------+----------+---------+---------+
|        | 4th       | 5       |          | 170     | 10      |
|        +-----------+---------+----------+---------+---------+
|        | Pinky     | 6       |          | 160     | 20      |
|        +-----------+---------+----------+---------+---------+
|        | wrist     | 7       |          | -   	| -       |
+--------+-----------+---------+----------+---------+---------+
| Right  | Bicep     | 8       |          | 90      | 0       |
| Arm    +-----------+---------+----------+---------+---------+
|        | Rotate    | 9       |          | 180     | 20      |
|        +-----------+---------+----------+---------+---------+
|        | Shoulder  | 10      |          | 180     | 0       |
|        +-----------+---------+----------+---------+---------+
|        | Omplate   | 11      |          | -       | -       |
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

Installation Procedure
----------------------

There is some information online, but a lot of it is confusing or out of date.

1. Download the mrl jar file. (http://myrobotlab.org/download)
2. Put it in a folder called ``mrl`` within this repository. The ``.gitignore`` is setup to ignore changes in this folder.
2. Download java if needed (same link)
3. Open command promt at folder with the mrl jar file and run ``java -jar myRobotLab.jar``
4. This will start mrl. go to the runtime tab and click ``system\install all``
5. You can then load and run a python script. note the ports defined in the script will likely have to be changed if the computer is different. 

If the arduino has not had the mrlComm firmware flashed, it can be found in the mrl directory: ``.mrl/resource/Arduino/MRLComm/``. flash it the same as you would any other arduino file.
'''