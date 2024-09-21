#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

#pylint: disable=attribute-defined-outside-init, missing-function-docstring, missing-module-docstring, missing-class-docstring

import wpilib
import wpilib.drive
import phoenix5
import constants
import math

class MyRobot(wpilib.TimedRobot):
    """
    This is a demo program showing the use of the DifferentialDrive class.
    Runs the motors with arcade steering.
    """  

    def robotInit(self):
        """Robot initialization function"""
        self.pitch_motor = phoenix5.WPI_TalonFX(constants.PITCH_MOTOR_ID)
        self.pov_up_check = False

        left_motor_1 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_1_ID)
        left_motor_2 = phoenix5.WPI_TalonSRX(constants.LEFT_MOTOR_2_ID)
        right_motor_1 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_1_ID)
        right_motor_2 = phoenix5.WPI_TalonSRX(constants.RIGHT_MOTOR_2_ID)
        left_motor_1.follow(left_motor_2)
        right_motor_1.follow(right_motor_2)
        self.robot_drive = wpilib.drive.DifferentialDrive(left_motor_1, right_motor_1)
        self.stick = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)
        pneumatic_hub = wpilib.PneumaticHub(constants.PNEUMATIC_HUB_PORT)
        self.upper_solenoid_1 = pneumatic_hub.makeSolenoid(constants.UPPER_SOLENOID_1_CHANNEL)
        self.upper_solenoid_2 = pneumatic_hub.makeSolenoid(constants.UPPER_SOLENOID_2_CHANNEL)
        self.upper_solenoid_3 = pneumatic_hub.makeSolenoid(constants.UPPER_SOLENOID_3_CHANNEL)
        self.lower_solenoid_1 = pneumatic_hub.makeSolenoid(constants.LOWER_SOLENOID_1_CHANNEL)
        self.lower_solenoid_2 = pneumatic_hub.makeSolenoid(constants.LOWER_SOLENOID_2_CHANNEL)
        self.lower_solenoid_3 = pneumatic_hub.makeSolenoid(constants.LOWER_SOLENOID_3_CHANNEL)

        self.upper_solenoid_1.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
        self.upper_solenoid_2.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
        self.upper_solenoid_3.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
        self.lower_solenoid_1.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
        self.lower_solenoid_2.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
        self.lower_solenoid_3.setPulseDuration(constants.SOLENOID_PULSE_LENGTH)
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

    def fire_upper(self) :
        self.upper_solenoid_1.startPulse()
        self.upper_solenoid_2.startPulse()
        self.upper_solenoid_3.startPulse()

    def fire_lower(self) :
        self.lower_solenoid_1.startPulse()
        self.lower_solenoid_2.startPulse()
        self.lower_solenoid_3.startPulse()


    def teleopPeriodic(self):
        # Drive with arcade drive.
        # That means that the Y axis drives forward
        # and backward, and the X turns left and right.
        self.robot_drive.arcadeDrive(self.stick.getY(), self.stick.getZ())
        if self.stick.getPOV(0) != -1 :
            self.pitch_motor.set(math.cos(self.stick.getPOV(0) * math.pi / 180))
        else :
            self.pitch_motor.set(0)

        if self.stick.getRawButton(constants.FIRE_UPPER_BUTTON_ID) :
            self.fire_upper()
        if self.stick.getRawButton(constants.FIRE_LOWER_BUTTON_ID) :
            self.fire_lower()
