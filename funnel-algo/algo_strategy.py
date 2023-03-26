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
        "structure": 0,
        "location": [0, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [1, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [2, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [3, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [4, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [23, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [26, 13],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [27, 13],
       },


       {
        "type": "Build",
        "structure": 2,
        "location": [3, 12],
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [24, 12],
       },


       {
        "type": "Build",
        "structure": 0,
        "location": [26, 12],
        "comment": "These are to create the funnel"
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [25, 11],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 10],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [23, 9],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [22, 8],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [21, 7],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [20, 6],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [19, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [6, 11],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [7, 9],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [8, 8],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [9, 7],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [10, 6],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [11, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [12, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [13, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [14, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [15, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [16, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [17, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [18, 5],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [19, 5],
       },


       {
        "type": "Build",
        "structure": 2,
        "location": [5, 10],
        "comment": "Turret protecting entrance of funnel"
       },
       {
        "type": "Build",
        "structure": 2,
        "location": [6, 10],
        "comment": "Turret protecting entrance of funnel"
       },



       {
        "type": "Upgrade",
        "structure": 0,
        "location": [3, 13],
        "comment": "These are to upgrade the front walls"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [4, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [23, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [24, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [2, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [25, 13],
       },


       {
        "type": "Upgrade",
        "structure": 2,
        "location": [3, 12],
        "comment": "These are to upgrade turrets"
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [24, 12],
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [5, 10],
       },
       {
        "type": "Upgrade",
        "structure": 2,
        "location": [6, 10],
       },


       {
        "type": "Upgrade",
        "structure": 0,
        "location": [0, 13],
        "comment": "These are to upgrade walls on the very corners"
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [1, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [26, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [27, 13],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [6, 11],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [7, 9],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [8, 8],
       },


       {
        "type": "Build",
        "structure": 0,
        "location": [23, 12],
       },
       {
        "type": "Build",
        "structure": 0,
        "location": [24, 11],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [23, 12],
       },
       {
        "type": "Upgrade",
        "structure": 0,
        "location": [24, 11],
       },


    ]


class AlgoStrategy(gamelib.AlgoCore):
    def __init__(self):
        super().__init__()
        seed = random.randrange(maxsize)
        random.seed(seed)
        gamelib.debug_write('Random seed: {}'.format(seed))

        self.defense_priority_list = priorityList
        self.prev_defense_priority_list = None
        self.last_attack_round = 0
        self.completed_infiltrate_attack = False
        self.do_not_attack = False

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

        self.build_base_defenses(game_state)

        self.build_shields(game_state)

        self.build_offense(game_state)

    def build_self_destruct_defense(self, game_state):
        # TODO: if it just recently changed rounds to a new multiple of 10, this will be wrong
        mp_per_round = (5 + game_state.turn_number // 10)
        savings_3_rounds = (((mp_per_round * .75) + mp_per_round) * .75) + mp_per_round
        savings_4_rounds = (((((mp_per_round * .75) + mp_per_round) * .75) + mp_per_round) * .75) + mp_per_round

        if self.enemy_MP >= savings_3_rounds:
            self.do_not_attack = True
            game_state.attempt_spawn(WALL, [[4, 10]])
            game_state.attempt_remove([[4, 10]])
            self.current_SP -= .5

            game_state.attempt_spawn(INTERCEPTOR, [[7, 6]], 1)
            self.current_SP -= 1
            if self.enemy_MP >= savings_4_rounds:
                game_state.attempt_spawn(INTERCEPTOR, [[5, 8]], 1)
                self.current_SP -= 1
        else:
            self.do_not_attack = False



    def build_base_defenses(self, game_state):
        """
        Build and reinforce basic defences. This works by going through a priority list in "priority_list.json" and 
        building/upgrading based on this priority.
        """
        if self.completed_infiltrate_attack:
            self.defense_priority_list = self.prev_defense_priority_list
            self.completed_infiltrate_attack = False
            self.attempt_infiltrate_attack = False


        # Try to build self-destruct defense, pretty powerful.
        self.build_self_destruct_defense(game_state)

        # gamelib.debug_write(self.current_SP)
        for defense in self.defense_priority_list:
            # Check if trying to build defense thats already built and that we have the resources to build it
            defenseCost = self.config[uI][defense["structure"]]["cost1"]
            if defense["type"] == "Build" and len(game_state.game_map[defense["location"]]) == 0 and self.current_SP >= defenseCost:
                # Create defense and reduce wallet by cost
                game_state.attempt_spawn(self.config["unitInformation"][defense["structure"]]["shorthand"], [defense["location"]])
                # gamelib.debug_write("Built: " + str(self.config["unitInformation"][defense["structure"]]["shorthand"]))
                self.current_SP -= defenseCost

            # Check if trying to upgrade defense thats already upgrade and that we have the resources to upgrade it
            # also you literally cannot lookup the cost of an upgrade in the config it is the dumbest thing
            upgradeCost = 6 if defense["structure"] == 2 else (1.5 if defense["structure"] == 0 else 2)
            if defense["type"] == "Upgrade" and len(game_state.game_map[defense["location"]]) != 0 and not game_state.game_map[defense["location"]][0].upgraded and self.current_SP >= upgradeCost:
                game_state.attempt_upgrade([defense["location"]])
                self.current_SP -= upgradeCost
                # gamelib.debug_write("Upgraded: " + str(self.config["unitInformation"][defense["structure"]]["shorthand"]))

        """
        # I think these starter turret locations are very important. The first two are to protect the corners, while the
        # last two protect from attacks through the middle.
        base_turret_locations = [[3, 12], [24, 12], [9, 9], [18, 9]]
        game_state.attempt_spawn(TURRET, base_turret_locations)

        # Upgrading these two turrets on the corners is important because enemy attackers can reach corners in a shorter amount of 
        # time
        game_state.attempt_upgrade(base_turret_locations[:2])
        """
    
    def build_shields(self, game_state):
        shield_spots = [[17, 6], [16, 4], [16, 6], [15, 4], [15, 6], [14, 4], [14, 6], [13, 4], [13, 6], [12, 4], [12, 6], [11, 4], [11, 6]]
        # Build shields
        for shield_spot in shield_spots:
            if self.current_SP >= 6 and len(game_state.game_map[shield_spot]) == 0:
                game_state.attempt_spawn(SUPPORT, [shield_spot], 1)
                self.current_SP -= 4

        # Upgrade shields
        for shield_spot in shield_spots:
            if self.current_SP >= 6 and len(game_state.game_map[shield_spot]) != 0:
                game_state.attempt_upgrade([shield_spot])
                self.current_SP -= 2

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
                locations = game_state.game_map.get_locations_in_range([x, y], 3.5)

                # Loop through each location within 3.5 tiles of each (x,y) pair and count number of turrets within that radius
                for location in locations:
                    structure = None if len(game_state.game_map[location]) == 0 else game_state.game_map[location][0]
                    if structure is not None and structure.player_index == 1 and structure.unit_type == "DF":
                        scores[y][x] += 1
        return scores
    
    # Try to estimate the value of a path from the amount of units it will destroy.
    def path_value(self, game_state, path):
        value = 0
        visited = set()
        for location in path:
            # If y is less than 11 then a demolisher could not hit anything anyways
            if location[1] >= 11:
                neighbor_locations = game_state.game_map.get_locations_in_range(location, 4.5)
                for neighbor_location in neighbor_locations:
                    structure = None if len(game_state.game_map[neighbor_location]) == 0 else game_state.game_map[neighbor_location][0]

                    # In the case there is a turret in range of this tile, just return current value as this unit will die.
                    if structure is not None and structure.unit_type == "DF" and structure.player_index == 1 and math.dist(location, neighbor_location) <= 3.5:
                        return value
                    # Only occurs when structure is a turret or a shield and ensure we aren't double counting
                    elif structure is not None and structure.player_index == 1 and tuple(neighbor_location) not in visited:
                        value += .5 if structure.unit_type == "FF" else 4
                        visited.add(tuple(neighbor_location))

        return value
    
    def can_infiltrate(self, game_state):
        structure1 = game_state.game_map[[0, 14]]
        structure2 = game_state.game_map[[1, 14]]
        if len(structure1) == 0 and len(structure2) == 0:
            return True
        structure3 = game_state.game_map[[2, 14]]
        structure4 = game_state.game_map[[3, 14]]
        structure5 = game_state.game_map[[4, 14]]
        upgraded_wall_1 = True if len(structure1) == 0 or structure1[0].unit_type != "FF" or not structure1[0].upgraded else False
        upgraded_wall_2 = True if len(structure2) == 0 or structure2[0].unit_type != "FF" or not structure2[0].upgraded else False
        upgraded_wall_3 = True if len(structure3) == 0 or structure3[0].unit_type != "FF" or not structure3[0].upgraded else False
        upgraded_wall_4 = True if len(structure4) == 0 or structure4[0].unit_type != "FF" or not structure4[0].upgraded else False
        upgraded_wall_5 = True if len(structure5) == 0 or structure5[0].unit_type != "FF" or not structure5[0].upgraded else False
        if upgraded_wall_1 and upgraded_wall_2 and upgraded_wall_3 and upgraded_wall_4 and upgraded_wall_5:
            return True
        
        return False


    def build_offense(self, game_state):
        # Check for infiltrate attack
        if self.do_not_attack:
            return
        
        if game_state.turn_number > 20:
            gamelib.debug_write("Can Infiltrate:")
            gamelib.debug_write(self.can_infiltrate(game_state))
            can_infiltrate = self.can_infiltrate(game_state)

            if can_infiltrate and self.current_MP >= 25:
                game_state.attempt_remove([[0, 13], [1, 13]])
                self.prev_defense_priority_list = self.defense_priority_list.copy()
                self.defense_priority_list = [i for i in self.defense_priority_list if i["location"] not in [[0, 13], [1, 13]]]

            if len(game_state.game_map[[0, 13]]) == 0 and len(game_state.game_map[[1, 13]]) == 0 and self.current_MP >= 25:
                # Check if both inner two walls are not upgraded
                structure1 = game_state.game_map[[0, 14]]
                structure2 = game_state.game_map[[1, 14]]
                upgraded_wall_1 = False if len(structure1) == 0 or structure1[0].unit_type != "FF" or not structure1[0].upgraded else True
                upgraded_wall_2 = False if len(structure2) == 0 or structure2[0].unit_type != "FF" or not structure2[0].upgraded else True
                if upgraded_wall_1 or upgraded_wall_2:
                    game_state.attempt_spawn(DEMOLISHER, [0, 13], 5)
                    self.current_MP -= 15
                else:
                    game_state.attempt_spawn(DEMOLISHER, [0, 13], 2)
                    self.current_MP -= 6

                game_state.attempt_spawn(SCOUT, [14, 0], math.floor(self.current_MP))
                self.completed_infiltrate_attack = True

            if can_infiltrate:
                return 

        # fix this, this is dumb but im tired
        valid_start_positions = [[2, 11], [3, 10], [4, 9], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3], [11, 2], [12, 1], [13, 0],
                                [14,0], [15, 1], [16, 2], [17, 3], [18, 4], [19, 5], [20, 6], [21, 7], [22, 8], [23, 9], [24, 10], [25, 11], [26, 12], [27, 13]]
        
        scores = self.score_per_tile(game_state)
        valid_paths = []

        # go through every position possible to place a unit and estimate score for each path
        for index, start_pos in enumerate(valid_start_positions):
            target_edge = game_state.game_map.TOP_RIGHT if index < 14 else game_state.game_map.TOP_LEFT
            path = game_state.find_path_to_edge(start_pos, target_edge)

            # Path is only none when starting point is blocked
            if path is not None:
                # Loop through each location and calculate score as average "vulnerability"
                path_score = sum([scores[y][x] for (x, y) in path]) / len(path)        
                path_value = self.path_value(game_state, path)
                valid_paths.append(start_pos + [path_score, path_value])

        # sort by lowest score
        valid_paths.sort(key=lambda elem: elem[2])
        gamelib.debug_write("Safest Path: ")
        gamelib.debug_write(valid_paths)

        highest_value_paths = valid_paths.copy()
        highest_value_paths.sort(key=lambda elem: -elem[3])
        gamelib.debug_write("Highest Value Paths:")
        gamelib.debug_write(highest_value_paths)

        will_attack = False

        """
        if self.current_MP >= 3 and highest_value_paths[0][3] > 5:
            game_state.attempt_spawn(DEMOLISHER, [highest_value_paths[0][0:2]], 1)
            will_attack = True
            self.current_MP -= 3
        """

        # if we have at least eight mobile points and there is no threat at all on the lowest path, then attack with all scouts
        if (self.current_MP >= 8 and valid_paths[0][2] == 0) or game_state.turn_number >= (self.last_attack_round + 10):
            game_state.attempt_spawn(SCOUT, [valid_paths[0][0:2]], math.floor(self.current_MP))
            will_attack = True

            self.last_attack_round = game_state.turn_number
        

        """
        # After a lot of testing, I found that spawning 3 scouts and 2 demolishers works pretty well.
        if 0 < valid_paths[0][2] < .3 and self.current_MP >= 9:
            game_state.attempt_spawn(SCOUT, [valid_paths[0][0:2]], 3)
            game_state.attempt_spawn(DEMOLISHER, [valid_paths[0][0:2]], 2)
            will_attack = True
        """

        # When a path has a lot of threats on it, send a large pack of demolishers.
        mp_per_round = (5 + game_state.turn_number // 10)
        savings_3_rounds = (((mp_per_round * .75) + mp_per_round) * .75) + mp_per_round
        savings_2_rounds = (mp_per_round * .75) + mp_per_round
        gamelib.debug_write("MP per round:")
        gamelib.debug_write(savings_3_rounds)
        gamelib.debug_write(savings_2_rounds)
        if self.current_MP >= savings_3_rounds and self.enemy_MP < (savings_2_rounds + 1):
            game_state.attempt_spawn(DEMOLISHER, [[18, 4]], int(self.current_MP // 3))
            will_attack = True

            self.last_attack_round = game_state.turn_number

        """
        # If we are trying to build a push and can afford shields, then buy them
        if will_attack and self.current_SP >= 4:
            # This is to deal with attacks from both sides, to ensure that support can reach
            shield_location = [10, 9] if (valid_paths[0][0] < 9 or 14 < valid_paths[0][0] < 18) else [17, 9]

            game_state.attempt_spawn(SUPPORT, [shield_location])
            self.current_SP -= 4

            if self.current_SP >= 2:
                game_state.attempt_upgrade([shield_location])
        """



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






if __name__ == "__main__":
    algo = AlgoStrategy()
    algo.start()