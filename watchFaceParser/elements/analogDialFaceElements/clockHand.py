﻿from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.basicElements.image import Image

class ClockHand:
    definitions = {
        1: { 'Name': 'unknown1', 'Type': 'long'},
        2: { 'Name': 'unknown2', 'Type': 'long'},
        3: { 'Name': 'unknown3', 'Type': Coordinates},
        4: { 'Name': 'unknown4', 'Type': Coordinates},
        5: { 'Name': 'CenterImage', 'Type': Image},
    }

