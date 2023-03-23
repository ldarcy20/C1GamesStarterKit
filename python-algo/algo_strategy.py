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
        "comment": "Build a turret in the top right corner"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [9, 9],
        "comment": "Build a turret to protect the left side in the middle"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [18, 9],
        "comment": "Build a turret to protect the right side in the middle"
       },


       {
        "type": "Upgrade",
        "structure": 2,
        "location": [3, 12],
        "comment": "Upgrade the turret on the left corner"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [24, 12],
        "comment": "Upgrade the turret on the right corner"
       },


       {
        "type": "Build",
        "structure": 0,
        "location": [0, 13],
        "comment": "Build a wall to protect the left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [1, 13],
        "comment": "Build a wall to protect the left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [2, 13],
        "comment": "Build a wall to protect the left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [3, 13],
        "comment": "Build a wall to protect the left corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 13],
        "comment": "Build a wall to protect the right corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 13],
        "comment": "Build a wall to protect the right corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [26, 13],
        "comment": "Build a wall to protect the right corner"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [27, 13],
        "comment": "Build a wall to protect the right corner"
       },


       {
        "type": "Upgrade",
        "structure": 2,
        "location": [9, 9],
        "comment": "Upgrade the turret that protects the left side in the middle"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [18, 9],
        "comment": "Upgrade the turret that protects the left side in the middle"
       }
    ]


class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        seed = random.randrange(maxsize)
        random.seed(seed)
        gamelib.debug_write('Random seed: {}'.format(seed))

        self.defense_priority_list = priorityList

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
        # this function seems to be called on a seperate thread as on_turn which causes it to occasionally
        # overwrite data that is shared between the two functions

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

        self.build_base_defenses(game_state)

        self.build_offense(game_state)


    def build_base_defenses(self, game_state):
        """
        Build and reinforce basic defences. This works by going through a priority list in "priority_list.json" and 
        building/upgrading based on this priority.
        """
        gamelib.debug_write(self.current_SP)
        for defense in self.defense_priority_list:
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

    def score_per_tile(self, game_state):
        for y in range(14, 28):
            for x in range(y - 14, )

    def build_offense(self, game_state):
        valid_start_positions = [[0, 13], [1, 12], [2, 11], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3], [11, 2], [12, 1], [13, 0],
                                [14,0], [15, 1], [16, 2], [17, 3], [18, 4], [19, 5], [20, 6], [21, 7], [22, 8], [23, 9], [24, 10], [25, 11], [26, 12], [27, 13]]
        
        for index, start_pos in enumerate(valid_start_positions):
            target_edge = game_state.game_map.TOP_RIGHT if index < 14 else game_state.game_map.TOP_LEFT
            path = game_state.find_path_to_edge(start_pos, target_edge)
            gamelib.debug_write(path)




if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()