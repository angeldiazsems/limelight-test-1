import commands2
import phoenix5
import constants
import wpilib
import wpilib.drive

class arcadeDrive(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.left_motor_1 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_1_ID)
        self.left_motor_2 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_2_ID)
        self.right_motor_1 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_1_ID)
        self.right_motor_2 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_2_ID)
        self.left_motor_1.follow(self.left_motor_2)
        self.right_motor_1.follow(self.right_motor_2)
        self.robot_drive = wpilib.drive.DifferentialDrive(self.left_motor_1, self.right_motor_1)

    def arcadeDrive(self, y: float, z: float) -> None:
        self.robot_drive.arcadeDrive(y, z)