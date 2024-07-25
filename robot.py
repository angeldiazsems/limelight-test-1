#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import wpilib
import wpilib.drive
import phoenix5
import constants

class MyRobot(wpilib.TimedRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with arcade steering.
    """

    def robotInit(self):
        """Robot initialization function"""

        left_motor_1 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_1_ID)
        left_motor_2 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_2_ID)
        right_motor_1 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_1_ID)
        right_motor_2 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_2_ID)
        left_motor_1.follow(left_motor_2)
        right_motor_1.follow(right_motor_2)
        self.robot_drive = wpilib.drive.DifferentialDrive(left_motor_1, right_motor_1)
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        right_motor_1.setInverted(True)

    # def RobotPeriodic(self):
    #     # Drive with arcade drive.
    #     # That means that the Y axis drives forward
    #     # and backward, and the X turns left and right.
    #     self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        # self.left_motor_1.set(self.stick.getY())


    def teleopPeriodic(self):
        # Drive with arcade drive.
        # That means that the Y axis drives forward
        # and backward, and the X turns left and right.
        self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getZ())
        # self.left_motor_1.set(self.stick.getY())
