import commands2
import typing

from subsystems.drivetrain import arcadeDrive
from subsystems.limelight import limelightSystem

class autoCmd(commands2.CommandBase):
    def __init__(self, arcade_drive: arcadeDrive, limelight : limelightSystem) -> None:
        super().__init__()
        self.arcade_drive = arcade_drive
        self.y = y
        self.z = z
        self.addRequirements(arcade_drive)
        self.addRequirements(limelight)

    def execute(self) -> None:
        results = self.limelight.get_results()
        tag = results.tagId if results else -1
        if(tag != -1):
            if(tag % 2 ==0):
                arcade_drive.drive(.5,0)
            else:
                arcade_drive.drive(.9,.5)

    def isFinished(self) -> bool:
        return False
    
    def end(self) -> None:
        pass
