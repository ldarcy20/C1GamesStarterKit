import gamelib
import random
import math
import warnings
from sys import maxsize
import json

uI = "unitInformation"

priorityList = [
       {
        "type": "Build",
        "structure": 2,
        "location": [3, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [24, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [17, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [4, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [23, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [5, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [5, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [22, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [22, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [17, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [3, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [24, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [4, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [23, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [21, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [6, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [9, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [18, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [12, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [13, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [14, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [15, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [4, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [4, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [23, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [23, 12],
        "comment": "Build a turret in the top left corner"
       }
    ]

LPriorityList = [
       {
        "type": "Build",
        "structure": 2,
        "location": [3, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [24, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [17, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [4, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [23, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [5, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [5, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [22, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [4, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [3, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [6, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [9, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [12, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [13, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [14, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [15, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [4, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [4, 12],
        "comment": "Build a turret in the top left corner"
       },
    ]


RPriorityList = [
       {
        "type": "Build",
        "structure": 2,
        "location": [3, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [24, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [17, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [4, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [23, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [5, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [22, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [22, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [10, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [17, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [17, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [10, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [24, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [23, 13],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [21, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [9, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [18, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [18, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [11, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [16, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [12, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [13, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [14, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [15, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [23, 12],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [23, 12],
        "comment": "Build a turret in the top left corner"
       }
    ]



supportList = [
        {
        "type": "Build",
        "structure": 1,
        "location": [12, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [13, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [14, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [15, 9],
        "comment": "Build a turret in the top left corner"
       },
        {
        "type": "Build",
        "structure": 1,
        "location": [12, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [13, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [14, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [15, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [12, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [13, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [14, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [15, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [16, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [16, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [16, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [11, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [11, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 1,
        "location": [11, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [12, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [13, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [14, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [15, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [12, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [13, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [14, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [15, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [12, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [13, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [14, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [15, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [16, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [16, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [16, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [11, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [11, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Upgrade",
        "structure": 1,
        "location": [11, 7],
        "comment": "Build a turret in the top left corner"
       },
]

emergencyDefense = [
        {
        "type": "Build",
        "structure": 0,
        "location": [23, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [22, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [21, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [20, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [20, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [20, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [19, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 6],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 5],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 4],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [4, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [5, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [6, 11],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [7, 10],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [7, 9],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [7, 8],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [8, 7],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 6],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 5],
        "comment": "Build a turret in the top left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 4],
        "comment": "Build a turret in the top left corner"
       }
]
 

class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        seed = random.randrange(maxsize)
        random.seed(seed)
        gamelib.debug_write('Random seed: {}'.format(seed))

        self.defense_priority_list = priorityList
        self.Ldefense_priority_list = LPriorityList
        self.Rdefense_priority_list = RPriorityList
        self.emergency_defense_priority_list = emergencyDefense
        self.support_list = supportList

    def on_game_start(self, config):
        """ 
        Read in config and perform any initial setup here 
        """
        # gamelib.debug_write('Configuring your custom algo strategy...')
        self.config = config
        global WALL, SUPPORT, TURRET, SCOUT, DEMOLISHER, INTERCEPTOR, MP, SP
        WALL = config["unitInformation"][0]["shorthand"]
        SUPPORT = config["unitInformation"][1]["shorthand"]
        TURRET = config["unitInformation"][2]["shorthand"]
        SCOUT = config["unitInformation"][3]["shorthand"]
        DEMOLISHER = config["unitInformation"][4]["shorthand"]
        INTERCEPTOR = config["unitInformation"][5]["shorthand"]
        MP = 1
        SP = 0
        # This is a good place to do initial setup
        self.scored_on_locations = []
        # gamelib.debug_write("Game has started")

        ### DONT PUT SHIT HERE
        # this function seems to be called on a seperate thread as turn which causes it to occasionally
        # overwrite data that is shared between the two functions
        # edit: I dont think thats whats causing this.

    def on_turn(self, turn_state):
        """
        This function is called every turn with the game state wrapper as
        an argument. The wrapper stores the state of the arena and has methods
        for querying its state, allocating your current resources as planned
        unit deployments, and transmitting your intended deployments to the
        game engine.
        """
        game_state = gamelib.GameState(self.config, turn_state)
        gamelib.debug_write('Performing turn {} of your custom algo strategy'.format(game_state.turn_number))
        # game_state.suppress_warnings(True)  #Comment or remove this line to enable warnings.

        self.strategy_manager(game_state)

        game_state.submit_turn()

    """
    NOTE: Code I wrote is below now
    """
    def strategy_manager(self, game_state):
        """
        Function used to manage planning of our custom function
        """
        self.current_SP = game_state.get_resource(0, 0)
        self.current_MP = game_state.get_resource(1, 0)
        self.enemy_MP = game_state.get_resource(1, 1)

        if game_state.turn_number == 5:
            self.scored_on_locations = []

        self.build_base_defenses(game_state)

        self.build_offense(game_state)


    def build_base_defenses(self, game_state):
        """
        Build and reinforce basic defences. This works by going through a priority list in "priority_list.json" and 
        building/upgrading based on this priority.
        """

        
        if (self.enemy_MP >= 7 or game_state.turn_number > 10):
            isAlreadyBuilt = True
            for defense in self.emergency_defense_priority_list:
                defenseCost = self.config[uI][defense["structure"]]["cost1"]
                if defense["type"] == "Build" and len(game_state.game_map[defense["location"]]) == 0 and self.current_SP >= defenseCost:
                    # Create defense and reduce wallet by cost
                    isAlreadyBuilt = False
                    game_state.attempt_spawn(self.config["unitInformation"][defense["structure"]]["shorthand"], [defense["location"]])
                    gamelib.debug_write("Built: " + str(self.config["unitInformation"][defense["structure"]]["shorthand"]))
                    self.current_SP -= defenseCost
            
            

            if self.enemy_focus() <= -3:
                game_state.attempt_spawn(WALL, [6, 9])
                game_state.attempt_remove([6, 9])
                game_state.attempt_spawn(INTERCEPTOR, [[5, 8], [6, 7], [7, 6], [8, 5]])

            elif self.enemy_focus() >= 3:
                game_state.attempt_spawn(WALL, [21, 9])
                game_state.attempt_remove([21, 9])
                game_state.attempt_spawn(INTERCEPTOR, [[22, 8], [21, 7], [20, 6], [19, 5]])
            
            elif self.enemy_focus() <= -2:
                game_state.attempt_spawn(WALL, [6, 10])
                game_state.attempt_spawn(WALL, [21, 10])
                game_state.attempt_remove([6, 10])
                game_state.attempt_remove([21, 10])
                game_state.attempt_spawn(INTERCEPTOR, [20, 6])
                game_state.attempt_spawn(INTERCEPTOR, [[5, 8], [7, 6], [8, 5]])

            elif self.enemy_focus() >= 2:
                game_state.attempt_spawn(WALL, [6, 10])
                game_state.attempt_spawn(WALL, [21, 10])
                game_state.attempt_remove([6, 10])
                game_state.attempt_remove([21, 10])
                game_state.attempt_spawn(INTERCEPTOR, [[22, 8], [20, 6], [19, 5]])
                game_state.attempt_spawn(INTERCEPTOR, [7, 6])



            # Predicting big enemy attack
            elif game_state.turn_number >= 20 and self.enemy_MP >= 12:
                game_state.attempt_spawn(INTERCEPTOR, [20, 6])
                game_state.attempt_spawn(INTERCEPTOR, [7, 6])
                game_state.attempt_spawn(INTERCEPTOR, [22, 8])
                game_state.attempt_spawn(INTERCEPTOR, [5, 8])

            elif self.enemy_focus() == -1:
                game_state.attempt_spawn(INTERCEPTOR, [7, 6])
                game_state.attempt_spawn(INTERCEPTOR, [5, 8])
                game_state.attempt_spawn(WALL, [21, 10])
                game_state.attempt_remove([21, 10])
                game_state.attempt_spawn(INTERCEPTOR, [20, 6])

            elif self.enemy_focus() == 1:
                game_state.attempt_spawn(INTERCEPTOR, [20, 6])
                game_state.attempt_spawn(INTERCEPTOR, [22, 8])
                game_state.attempt_spawn(WALL, [6, 10])
                game_state.attempt_remove([6, 10])
                game_state.attempt_spawn(INTERCEPTOR, [7, 6])

            else:
                game_state.attempt_spawn(WALL, [6, 10])
                game_state.attempt_spawn(WALL, [21, 10])
                game_state.attempt_remove([6, 10])
                game_state.attempt_remove([21, 10])
                game_state.attempt_spawn(INTERCEPTOR, [20, 6])
                game_state.attempt_spawn(INTERCEPTOR, [7, 6])
            

        # gamelib.debug_write(self.current_SP)
        l = []
        if self.enemy_focus() >= 1:
            l = self.Rdefense_priority_list
        elif self.enemy_focus() <= -1:
            l = self.Ldefense_priority_list
        else: 
            l = self.defense_priority_list
        for defense in l:
            # Check if trying to build defense thats already built and that we have the resources to build it
            defenseCost = self.config[uI][defense["structure"]]["cost1"]
            if defense["type"] == "Build" and len(game_state.game_map[defense["location"]]) == 0 and self.current_SP >= defenseCost:
                # Create defense and reduce wallet by cost
                game_state.attempt_spawn(self.config["unitInformation"][defense["structure"]]["shorthand"], [defense["location"]])
                gamelib.debug_write("Built: " + str(self.config["unitInformation"][defense["structure"]]["shorthand"]))
                self.current_SP -= defenseCost

            # Check if trying to upgrade defense thats already upgrade and that we have the resources to upgrade it
            # also you literally cannot lookup the cost of an upgrade in the config it is the dumbest thing
            upgradeCost = 6 if defense["structure"] == 2 else (1.5 if defense["structure"] == 0 else 2)
            if defense["type"] == "Upgrade" and len(game_state.game_map[defense["location"]]) != 0 and not game_state.game_map[defense["location"]][0].upgraded and self.current_SP >= upgradeCost:
                game_state.attempt_upgrade([defense["location"]])
                self.current_SP -= upgradeCost
                gamelib.debug_write("Upgraded: " + str(self.config["unitInformation"][defense["structure"]]["shorthand"]))

            elif self.current_SP <= 5:
                break


        
            # gamelib.debug_write("Start")
            # gamelib.debug_write(defense["location"])
            # gamelib.debug_write(game_state.game_map[defense["location"]])

        """
        # I think these starter turret locations are very important. The first two are to protect the corners, while the
        # last two protect from attacks through the middle.
        base_turret_locations = [[3, 12], [24, 12], [9, 9], [18, 9]]
        game_state.attempt_spawn(TURRET, base_turret_locations)

        # Upgrading these two turrets on the corners is important because enemy attackers can reach corners in a shorter amount of 
        # time
        game_state.attempt_upgrade(base_turret_locations[:2])
        """

    """
    For every relevant tile on the map, count the number of turrets that can reach it. The idea is that this will be a good
    estimate for how vunerable a tile is for the enemy.
    """
    def score_per_tile(self, game_state):
        scores = [[0 for x in range(28)] for y in range(28)]

        # Loop through enemy's tiles
        for y in range(11, 28):
            # These two cases are to deal with the diamond shape of the map, could be achieved using an abs function too
            yVals = range(13 - y, 27 - (13 - y) + 1) if y < 14 else range(y - 14, 27 - (y - 14) + 1)
            for x in yVals:
                # 3.5 is the range of a turret.
                locations1 = game_state.game_map.get_locations_in_range([x, y], 3.5)
                locations2 = game_state.game_map.get_locations_in_range([x, y], 4.5)

                # Loop through each location within 3.5 tiles of each (x,y) pair and count number of turrets within that radius
                for location in locations1:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == TURRET:
                        scores[y][x] += 1.5

                for location in locations2:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == TURRET:
                        scores[y][x] -= 0.3

                for location in locations2:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == SUPPORT:
                        scores[y][x] -= 0.5

                for location in locations2:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == WALL and not structure.upgraded:
                        scores[y][x] -= 0.1
                
                for location in locations2:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == WALL and structure.upgraded:
                        scores[y][x] += 0.2

                for location in locations1:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 0 and structure.unit_type == SUPPORT:
                        scores[y][x] -= 0.2

            

        return scores


    # determine where enemy is focusing their attacks
    def enemy_focus(self):
        # left = negative, right = positive
        num = 0
        for location in self.scored_on_locations:
            if location[0] <= 7:
                num -= 1
            elif location[0] <= 13:
                num += 2
            elif location[0] <= 19:
                num -= 2
            else:
                num += 1
        
        return num


    def build_offense(self, game_state):
        # fix this, this is dumb but im tired
        valid_start_positions =  [[0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3],
                                [17, 3], [18, 4], [19, 5], [20, 6], [21, 7], [22, 8], [23, 9], [24, 10], [25, 11], [26, 12], [27, 13]]
        
        scores = self.score_per_tile(game_state)
        valid_paths = []

        # go through every position possible to place a unit and estimate score for each path
        for index, start_pos in enumerate(valid_start_positions):
            target_edge = game_state.game_map.TOP_RIGHT if index < 14 else game_state.game_map.TOP_LEFT
            path = game_state.find_path_to_edge(start_pos, target_edge)

            # Path is only none when starting point is blocked
            if path is not None and len(path) > 13:
                # Loop through each location and calculate score as average "vulnerability"
                path_score = sum([scores[y][x] for (x, y) in path]) / len(path)        
                valid_paths.append(start_pos + [path_score])
        

        alternatePath1 = game_state.find_path_to_edge([7, 13], game_state.game_map.TOP_RIGHT)
        alternatePath2 = game_state.find_path_to_edge([20, 13], game_state.game_map.TOP_LEFT)
        alternate1Score = (sum([scores[y][x] for (x, y) in alternatePath1]) - 1.5) / len(alternatePath1) 
        alternate2Score = (sum([scores[y][x] for (x, y) in alternatePath2]) - 1.5) / len(alternatePath2) 

        # sort by lowest score
        valid_paths.sort(key=lambda elem: elem[2])
        gamelib.debug_write("Safest Path: ")
        gamelib.debug_write(valid_paths)


        will_attack = False

        if alternate1Score < alternate2Score and alternate1Score < valid_paths[0][2] and alternate1Score < -.5 and self.current_SP >= 2 and game_state.turn_number > 15 and self.current_MP >= 0.15*(game_state.turn_number + 50):
            game_state.attempt_spawn(WALL, [8, 12])
            game_state.attempt_spawn(WALL, [9, 11])
            game_state.attempt_spawn(WALL, [19, 10])
            game_state.attempt_remove([8, 12])
            game_state.attempt_remove([9, 11])
            game_state.attempt_remove([19, 10])
            game_state.attempt_spawn(DEMOLISHER, [10, 3], math.floor(0.05*(game_state.turn_number + 50)))
            will_attack = True

        elif alternate2Score < alternate1Score and alternate2Score < valid_paths[0][2] and alternate2Score < -.5 and self.current_SP >= 2 and game_state.turn_number > 15 and self.current_MP >= 0.15*(game_state.turn_number + 50):
            game_state.attempt_spawn(WALL, [19, 12])
            game_state.attempt_spawn(WALL, [18, 11])
            game_state.attempt_spawn(WALL, [8, 10])
            game_state.attempt_remove([19, 12])
            game_state.attempt_remove([18, 11])
            game_state.attempt_remove([8, 10])
            game_state.attempt_spawn(DEMOLISHER, [17, 3], math.floor(0.05*(game_state.turn_number + 50)))
            will_attack = True

         # if we have at least eight mobile points and there is no threat at all on the lowest path, then attack with all scouts
        elif self.current_MP >= 8 and valid_paths[0][2] == 0:
            game_state.attempt_spawn(SCOUT, [valid_paths[0][0:2]], math.floor(self.current_MP))
            will_attack = True

        # Scale standard attack based on turn number
        elif  valid_paths[0][2] < .1 and self.current_MP >= 0.15*(game_state.turn_number + 50):
            game_state.attempt_spawn(DEMOLISHER, [valid_paths[0][0:2]], math.floor(0.05*(game_state.turn_number + 50)))
            will_attack = True

        elif game_state.turn_number <= 5:
            game_state.attempt_spawn(INTERCEPTOR, [10, 3])
            game_state.attempt_spawn(INTERCEPTOR, [17, 3])

        # When a path has a lot of threats on it, send a large pack of demolishers.
        elif valid_paths[0][2] >= .1 and self.current_MP >= 12 and self.enemy_MP < 8:
            game_state.attempt_spawn(DEMOLISHER, [valid_paths[0][0:2]], 4)
            will_attack = True

        # We have too many mobile points
        elif self.current_MP >= 0.25*(game_state.turn_number + 50) and self.current_MP < 21:
            if self.enemy_focus() >= 1:
                game_state.attempt_spawn(INTERCEPTOR, [[20, 6], [19, 5]])
            elif self.enemy_focus() <= -1:
                game_state.attempt_spawn(INTERCEPTOR, [[7, 6], [8, 5]])
            else:
                game_state.attempt_spawn(INTERCEPTOR, [[7, 6], [8, 5]])
                game_state.attempt_spawn(INTERCEPTOR, [[20, 6], [19, 5]])
                will_attack = True

        # hopefully just end the game
        elif self.current_MP >= 21:
            game_state.attempt_spawn(DEMOLISHER, [valid_paths[0][0:2]], math.floor(self.current_MP / 3))
            will_attack = True



        # If we are trying to build a push and can afford shields, then buy them
        if will_attack:
            for support in self.support_list:
                # Check if trying to build defense thats already built and that we have the resources to build it
                defenseCost = self.config[uI][support["structure"]]["cost1"]
                if support["type"] == "Build" and len(game_state.game_map[support["location"]]) == 0 and self.current_SP >= defenseCost:
                    # Create defense and reduce wallet by cost
                    game_state.attempt_spawn(self.config["unitInformation"][support["structure"]]["shorthand"], [support["location"]])
                    gamelib.debug_write("Built: " + str(self.config["unitInformation"][support["structure"]]["shorthand"]))
                    self.current_SP -= defenseCost

                # Check if trying to upgrade defense thats already upgrade and that we have the resources to upgrade it
                # also you literally cannot lookup the cost of an upgrade in the config it is the dumbest thing
                upgradeCost = 2 if support["structure"] == 1 else 1000000
                if support["type"] == "Upgrade" and len(game_state.game_map[support["location"]]) != 0 and not game_state.game_map[support["location"]][0].upgraded and self.current_SP >= upgradeCost:
                    game_state.attempt_upgrade([support["location"]])
                    self.current_SP -= upgradeCost
                    gamelib.debug_write("Upgraded: " + str(self.config["unitInformation"][support["structure"]]["shorthand"]))



        # Removing this for right now, I think its a good idea though...
        """
        # If there is no path that is extremely vunerable
        if valid_paths[0][2] > 0 and self.current_SP < 2:
            # By setting reserve to 2, we ensure that we have enough SP to build an offense for the next round
            self.reserve = 2

        # either defense is already fully upgraded or we have reserved enough for an offense
        elif self.current_SP >= 2:
            # Take all paths that have been assigned the same (minimum) score and are not on either of the two corners
            valid_paths = filter(valid_paths, lambda x: x[2] == valid_paths[0][2] and (x[0:2] != [0, 13] and x[0:2] != [27, 13]))

            # Ensure that we still have a minimum path, I think the only case this isn't true is if the minimum path is on the
            # corner which should never happen because our defense has a wall on the corner so it shouldn't even be valid
            if len(valid_paths) > 0:
                pathing_walls = 
        """

    def on_action_frame(self, turn_string):
        """
        This is the action frame of the game. This function could be called 
        hundreds of times per turn and could slow the algo down so avoid putting slow code here.
        Processing the action frames is complicated so we only suggest it if you have time and experience.
        Full doc on format of a game frame at in json-docs.html in the root of the Starterkit.
        """
        # Let's record at what position we get scored on
        state = json.loads(turn_string)
        events = state["events"]
        breaches = events["breach"]
        for breach in breaches:
            location = breach[0]
            unit_owner_self = True if breach[4] == 1 else False
            # When parsing the frame data directly, 
            # 1 is integer for yourself, 2 is opponent (StarterKit code uses 0, 1 as player_index instead)
            if not unit_owner_self:
                # gamelib.debug_write("Got scored on at: {}".format(location))
                self.scored_on_locations.append(location)
                gamelib.debug_write("All locations: {}".format(self.scored_on_locations))







if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()