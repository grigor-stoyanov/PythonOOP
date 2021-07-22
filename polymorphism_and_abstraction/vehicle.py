#!/usr/bin/env python
"""Exercise for abstract classes"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract class inheriting from abc lib"""

    def __init__(self, fuel_quantity, fuel_consumption):
        """All vehicles inherit fuel parameters"""
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance):
        """1st mandatory method for all vehicles"""

    @abstractmethod
    def refuel(self, fuel):
        """2nd mandatory method for all vehicles"""


CAR_CON_EXTRA = 0.9
TRUCK_CON_EXTRA = 1.6
TRUCK_REDUCED_TANK_CAP = 0.95


class Car(Vehicle):
    """car instance inheriting from vehicle"""

    def drive(self, distance):
        """drive method with increased consumption by air con"""
        fuel_req = (self.fuel_consumption + CAR_CON_EXTRA) * distance
        if self.fuel_quantity >= fuel_req:
            self.fuel_quantity -= fuel_req

    def refuel(self, fuel):
        """increase fuel quantity by fuel parameter"""
        self.fuel_quantity += fuel


class Truck(Vehicle):
    """truck instance inheriting from vehicle"""

    def drive(self, distance):
        """drive method with increased consumption by air con"""
        fuel_req = (self.fuel_consumption + TRUCK_CON_EXTRA) * distance
        if self.fuel_quantity >= fuel_req:
            self.fuel_quantity -= fuel_req

    def refuel(self, fuel):
        """increase fuel quantity with 5% reduction due to hole in tank"""
        self.fuel_quantity += fuel * TRUCK_REDUCED_TANK_CAP
