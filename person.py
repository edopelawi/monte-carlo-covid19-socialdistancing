import random
direction_dict = {
    1: {"dir": "TOP_LEFT", "val": [-1, -1]},
    2: {"dir": "TOP_MID", "val": [-1, 0]},
    3: {"dir": "TOP_RIGHT", "val": [-1, 1]},
    4: {"dir": "LEFT", "val": [0, -1]},
    5: {"dir": "RIGHT", "val": [0, 1]},
    6: {"dir": "DOWN_LEFT", "val": [1, -1]},
    7: {"dir": "DOWN_MID", "val": [1, 0]},
    8: {"dir": "DOWN_RIGHT", "val": [1, 1]},
}


class Person:
    def __init__(
        self,
        _id,
        map_size,
        current_location,
        is_infected,
        is_stationary,
        mobility,
        is_alive,
        infected_duration,
        p_death,
    ):
        self._id = _id
        self.map_size = map_size
        self.current_location = current_location
        self.is_infected = is_infected
        self.is_stationary = is_stationary
        self.mobility = mobility
        self.is_alive = is_alive
        self.infected_duration = 0
        # get individual infection duration
        self.infected_duration_max = max(
            1, int(self.get_exponential_dist(infected_duration))
        )
        self.is_immune = False
        self.p_death = p_death

        self.direction = self.switch_direction()

    def switch_direction(self):
        """
        gets available direction to move
            :return index of the direction to be moving  

        """
        while True:
            direction_index = random.choice(range(1, 9))
            # print(f"direction_index - {direction_index}")
            if self.is_valid_direction(direction_index):
                self.direction = direction_index
                return direction_index

    def is_valid_direction(self, direction_index):
        movement_direction = direction_dict[direction_index]['val']
        target_move_location = [
            a_i + b_i for a_i, b_i in zip(self.current_location, movement_direction)]

        if target_move_location[0] < 0:
            return False
        if target_move_location[0] >= self.map_size[0]:
            return False
        if target_move_location[1] < 0:
            return False
        if target_move_location[1] >= self.map_size[1]:
            return False
        return True

    def possible_move(self):
        """
        generates the next move in the current selected direction
            :return [] -> list of location indexes
        """
        if not self.is_valid_direction(self.direction):
            self.direction = self.switch_direction()

        movement_direction = direction_dict[self.direction]['val']
        target_move_location = [
            a_i + b_i for a_i, b_i in zip(self.current_location, movement_direction)]
        return target_move_location

    def set_location(self, new_location):
        self.current_location = new_location

    def is_person_moving(self):
        pbb = random.uniform(0, 1)
        if pbb < self.mobility:
            return True
        return False

    def check_for_infection_duration(self):
        """
        # if person is infected increase the infected duration
        # if reaches the max infection duration make a decision to kill a person or make him immune
            :return void 
        """
        if self.is_immune:
            return
        if self.is_infected:
            self.infected_duration += 1
        if self.infected_duration == self.infected_duration_max:
            pbb = random.uniform(0, 1)
            if pbb < self.p_death:
                self.is_alive = False
            else:
                self.is_immune = True
                self.is_infected = False
                self.infected_duration = 0

    def infect_person(self):
        if self.is_immune:
            return
        self.is_infected = True

    def get_exponential_dist(self, infected_duration):
        return random.expovariate(1/infected_duration)
