"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730544721"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Will return the distance between two points."""
        d: int = sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        return d


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Assign sickness to INFECTED."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Returns True when the cell's sickness attribute is False."""
        outcome: bool
        if self.sickness == constants.VULNERABLE:
            outcome = True
        else:
            outcome = False
        return outcome

    def is_infected(self) -> bool:
        """Returns true if the cell's sickness is equal to INFECTED."""
        result: bool
        if self.sickness >= constants.INFECTED:
            result = True
        else: 
            result = False
        return result

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        color_of_cell: str = " "
        if self.is_vulnerable() is True:
            return "gray"
        elif self.is_infected() is True:
            return "purple"
        else:
            color_of_cell = "red"
        if self.is_immune() is True:
            return "yellow"
        return color_of_cell
    
    def contact_with(self, another: Cell) -> None:
        """If an infected cell comes in contact another cell it will make it infected."""
        if self.is_infected() and another.is_vulnerable() is True:
            another.contract_disease()
        if self.is_vulnerable() and another.is_infected() is True:
            self.contract_disease()

    def immunize(self) -> None:
        """Will assign constant Immune to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> None:
        """Will assign is Immune to a cell sickness attribute if it is equal to the Immune Constant."""
        if self.sickness == constants.IMMUNE:
            return True


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_count: int, immune_count: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_count >= cells or infected_count == 0 or infected_count < 0:
            raise ValueError("Number of infected cells must be at least one and less than the population of cells.")
        if immune_count >= cells or immune_count < 0:
            raise ValueError("Must have at least one immune cell.")
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(infected_count):
            self.population[i].contract_disease()
        for index in range(immune_count):
            self.population[(immune_count) - index - 1].immunize()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x > constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.x > constants.MAX_Y:
            cell.location.x = constants.MAX_Y
            cell.direction.x *= -1.0
        if cell.location.x > constants.MIN_Y:
            cell.direction.x *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete.""" 
        i: int = 0
        while i < len(self.population):
            if self.population[i].is_infected() is True:
                return False
            i += 1
        return True

    def check_contacts(self) -> None:
        """Will check if two cell values come in contact with one another."""
        for i in range(len(self.population)):
            for x in range(i + 1, len(self.population)):
                cell1: Cell = self.population[i]
                cell2: Cell = self.population[x]
                if cell1.location.distance(cell2.location) < constants.CELL_RADIUS:
                    cell1.contact_with(cell2)