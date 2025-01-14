import constants

import commands2
import commands2.button
import subsystems.drivetrain
import commands.arcadedrive
import wpilib
import autoCmd

# from subsystems.drivetrain import arcadeDrive
# from commands.arcadedrive import ArcadeDrive

from subsystems.limelight import limelightSystem
from commands.limelightdisplay import limelightDisplay


class RobotContainer:
    def __init__(self) -> None:
        self.limelight = limelightSystem()
        self.auto = autoCmd()
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        self.configureButtonBindings()
        

    def configureButtonBindings(self) -> None:
        #self.drivetrain.setDefaultCommand(ArcadeDrive(self.drivetrain, lambda: self.stick.getX(), lambda: self.stick.getY()))
        self.limelight.setDefaultCommand(limelightDisplay(self.limelight))
        
        





