'''
Traffic Lights

Write a simulation of traffic lights. There are 2 traffic lights. One light controls north-south traffic. The second controls east-west traffic.

One light is red while the other light goes through the following cycle:

Green for 8 seconds.
Yellow for 3 seconds.
Red for 2 seconds (Thus, both lights will be red for these 2 seconds).

After this, the second light goes through this same cycle while the first light remains red.

Desired output: Print out the state of both lights at each second.

- The system must be unit-testable.
- For time, use simulated time (not real time -- don't use setInterval or setTimeout) -- a simple integer that increments is sufficient for simulating the seconds.
'''

import pytest
from enum import Enum

class Color(Enum):
    Red =  2
    Green = 8
    Yellow = 3

class StreetLight:
    def __init__(self, name, controller, adjacent_light=None, light_states=None):
        self._name = name
        self._controller = controller
        self._adjacent_light = adjacent_light
        self._list_states = []
        if light_states is None:
            self._light_states = list(Color)
        self._light_state = Color.Red

    def __str__(self):
        return f'{self._name}: {self._light_state}'

    def setLightState(self, color):
        self._light_state = color
        self._list_states.append((self._controller.getCurrentTime(), color))
        print(self)

    def getListStates(self):
        return self._list_states

    def setAdjacentLight(self, adjacent_light):
        self._adjacent_light = adjacent_light

    def startCycle(self):
        for state in self._light_states:
            for i in range(state.value):
                self.setLightState(state.name)
                if self._adjacent_light is not None:
                    print(self._adjacent_light)
                self._controller.incrCurrentTime()
        self.setLightState(Color.Red.name)
        if self._adjacent_light is not None:
            self._adjacent_light.startCycle()


class IntersectionController:
    def __init__(self):
        self._current_time = 0
        self._runCycle = True

    def getCurrentTime(self):
        return self._current_time

    def incrCurrentTime(self):
        self._current_time += 1

    def cycleRunning(self):
        return self._runCycle

    def stopCycle(self):
        self._runCycle = True


class Intersection:
    def __init__(self, streetlightName1, streetlightName2):
        self._controller = IntersectionController()
        self._streetlight2 = StreetLight(streetlightName2, self._controller)
        self._streetlight1 = StreetLight(streetlightName1, self._controller, self._streetlight2)

    def cycleLights(self):
        self._streetlight1.startCycle()
        states1 = self._streetlight1.getListStates()
        states2 = self._streetlight2.getListStates()
        return states1, states2


def test_lights():
    intersection = Intersection('north-south', 'east-west')
    states1, states2 = intersection.cycleLights()
    print(f'states1 = {states1}')
    print(f'states2 = {states2}')
    assert [ (x,y) for x, y in states1 if y  == 'Red' ] == [(0, 'Red'), (1, 'Red'), (13, 'Red')]
    assert len([ (x,y) for x, y in states1 if y  == 'Yellow' ] ) == Color.Yellow.value
    assert len([ (x,y) for x, y in states1 if y  == 'Green' ] ) == Color.Green.value

    assert [ (x,y) for x, y in states2 if y  == 'Red' ] == [(13, 'Red'), (14, 'Red'), (26, 'Red')]
    assert len([ (x,y) for x, y in states2 if y  == 'Yellow' ] ) == Color.Yellow.value
    assert len([ (x,y) for x, y in states2 if y  == 'Green' ] ) == Color.Green.value

    # assert states1 == [(0, Color.Red), (1, Color.Red), (2, Color.Green)]
    # assert states2 == []