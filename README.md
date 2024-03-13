# 2024-Season: Buckeye Regional

## Robotpy Setup

BC Robotics (Team #4504) has designed their 2024 FIRST Robotics submission using [Robotpy](https://robotpy.readthedocs.io/en/stable/install/robot.html) with the [MagicBot Framework](https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html). To keep the relevant libraries current, the following code will need to be run regularly in a terminal interface:

```bash
python -m pip install --upgrade pip
python -m pip install robotpy wpilib
robotpy installer download-python
robotpy installer install-python
robotpy sync
robotpy installer download robotpy[all]
robotpy installer install robotpy[all]
```

## Hardware Configuration

### Swerve Drive

- **[SparkMax](https://www.revrobotics.com/rev-11-2158/)** (8x):
  - Drives [MK4i Swerve Module](https://www.swervedrivespecialties.com/products/mk4i-swerve-module) (4x)

| Component                 | Type             | ID/Details | Inverted | Gear Ratio | Wheel Diameter | Absolute Encoder | Z-Offset   |
|---------------------------|------------------|------------|----------|------------|----------------|------------------|------------|
| Front Left Angle Motor    | SparkMaxTurning  | 6          | No       | 1          | 1              | Yes              | 5.7535123  |
| Front Left Speed Motor    | SparkMaxDriving  | 5          | No       | 1          | 0.1143         |                  |            |
| Rear Left Angle Motor     | SparkMaxTurning  | 8          | No       | 1          | 1              | Yes              | 5.6867370  |
| Rear Left Speed Motor     | SparkMaxDriving  | 7          | No       | 1          | 0.1143         |                  |            |
| Rear Right Angle Motor    | SparkMaxTurning  | 2          | No       | 1          | 1              | Yes              | 5.5975077  |
| Rear Right Speed Motor    | SparkMaxDriving  | 1          | No       | 1          | 0.1143         |                  |            |
| Front Right Angle Motor   | SparkMaxTurning  | 4          | No       | 1          | 1              | Yes              | 0.0182671  |
| Front Right Speed Motor   | SparkMaxDriving  | 3          | No       | 1          | 0.1143         |                  |            |

### Launcher

- **[SparkMax](https://www.revrobotics.com/rev-11-2158/)** ():
  - Drives [Neo 550 Brushless Motor](https://www.revrobotics.com/rev-21-1651/)

| Component            | Type                | ID/Details | Inverted | Gear Ratio | Follower CAN ID |
|----------------------|---------------------|------------|----------|------------|-----------------|
| Launcher Spinner Left | SparkMaxDualSpinner | 10         | Yes      |            |                 |
| Launcher Spinner Right | SparkMaxDualSpinner | 12        | No       |            |                 |
| Intake Spinner Left  | SparkMaxDualSpinner | 14         | Yes      |            |                 |
| Intake Spinner Right | SparkMaxDualSpinner | 13         | Yes      |            |                 |
| Intake Pivot         | SparkMaxPivot       | 9          | No       | 4          | 15              |

### Climber

- **[SparkMax](https://www.revrobotics.com/rev-11-2158/)** (2x):
  
| Component            | Type          | ID/Details | Inverted |
|----------------------|---------------|------------|----------|
| Climber Motor Left   | SparkMaxClimb | 16         | No       |
| Climber Motor Right  | SparkMaxClimb | 17         | Yes      |

### Robot IP Address

`10.45.4.1`  

### Vision

- **[Limelight 2.0](https://docs.limelightvision.io/en/latest/)**:
  - Static IP address (Front) `10.4.45.11`
  - Static IP address (Rear)  `10.4.45.12`
  
| Component       | Type      | IP         | Name           |
|-----------------|-----------|------------|----------------|
| Limelight       | Limelight |`10.4.45.11`| limelight      |
| Limelight Front | Limelight |`10.4.45.12`| limelight-front|

## Robot Controls

### **[GameSir G7 Wired Controller](https://www.amazon.com/dp/B0BM9HRCCV?ref_=cm_sw_r_apin_dp_ER34REM3C1FQSY0W5MQR)**

- Input device ID `0`
- **Left Joystick (Lx, Ly)**: Controls the robot's movement in the field. The X-axis (Lx) translates to movement in the x-direction while the Y-axis translates to movement in the y-direction.
- **Right Joystick (Rx)**: Controls the robot's rotation on the field. The X-axis (Rx) influences the angular velocity of the robot.
- **Right Trigger (RT)**: Engages the launcher to shoot.
- **Left Trigger (LT)**: Engages auto-alignment with the AprilTag. When pressed beyond a certain threshold(.35), it activates the alignment process for precise targeting.
- **Y Button**: Positions the intake to score in the amp.
- **B Button**: Deactivates the front camera, raises the intake.
- **A Button**: Activates the front camera and lowers the intake.

## Autonomous Operation

  **Our autonomous plan is as follows...**

  1. Backup to shooting positon
  2. Shoot preloaded game piece
  3. Backup 2.75844 meters to exit community
  