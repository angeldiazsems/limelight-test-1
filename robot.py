#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import math
import wpilib
import wpilib.drive
import phoenix5
import constants
import math
import limelight 
import commands2
import typing
import commands.arcadedrive
import autoCmd

from robotcontainer import RobotContainer
from commands.limelightdisplay import limelightDisplay


class MyRobot(commands2.TimedCommandRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with arcade steering.
    """  

    autonomousCommand: typing.Optional[commands2.Command] = None

    def robotInit(self):
        """Robot initialization function"""
        self.container = RobotContainer()


    def teleopPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def autonomousPeriodic(self):
        commands2.CommandScheduler.getInstance().run()

    def autonomousInit(self):
        self.container.auto.schedule()


