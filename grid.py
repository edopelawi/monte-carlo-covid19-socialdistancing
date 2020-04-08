import random
from person import Person


class Grid:
    def __init__(
        self,
        height,
        width,
        population_size,
        infection_rate,
        stationary_multiplier,
        mobility,
        p_death,
        infection_duration,
    ):
        """
        Initializes the gridmap with the parameters
            :param height: height of grid
            :param width: width of grid
            :param population_size: population size
            :param infection_rate: infection rate of the initialized population
            :param stationary_multiplier: stationary population rate
            :param mobility: movement probability of each ind person
            :param p_death: probability of death after infection period
            :param infection_duration: exp mean duration of infection after which individual survives(immunity) or dies.
        """

        self.height = height  # 100
        self.width = width  # 100
        self.population_size = population_size  # 1000
        self.infection_rate = infection_rate  # 0.9% - 0.009
        self.stationary_multiplier = stationary_multiplier  # variable 0-100%
        self.mobility = mobility  # 75% -> 0.75
        self.p_death = p_death  # 6% -> 0.06
        self.infection_duration = infection_duration  # 4

        population_indexes = random.sample(
            range(height * width), population_size)
        infected_pop_indexes = random.sample(
            population_indexes, int(population_size * infection_rate)
        )
        stationary_pop_indexes = random.sample(
            population_indexes, int(population_size * stationary_multiplier)
        )

        map = [[None for x in range(height)] for y in range(width)]

        for pop_idx in population_indexes:
            [row_idx, col_idx] = divmod(pop_idx, height)

            is_infected = pop_idx in infected_pop_indexes
            is_stationary = pop_idx in stationary_pop_indexes

            # create person
            p = Person(
                _id=pop_idx,
                map_size=[height, width],
                current_location=[row_idx, col_idx],
                is_infected=is_infected,
                is_stationary=is_stationary,
                mobility=mobility,
                is_alive=True,
                infected_duration=infection_duration,
                p_death=p_death,
            )

            # puts on the map
            map[row_idx][col_idx] = p
        self.map = map

    def perform_evolution(self):
        no_of_peeps = 0
        moved_persons = []
        for row in range(self.height):
            for col in range(self.width):

                if self.map[row][col] is None:
                    continue

                # person to be moved
                p = self.map[row][col]

                # handling multiple movement of same person
                if p._id in moved_persons:
                    continue
                moved_persons.append(p._id)

                ###########################
                # INFECTION DURATION LOGIC#
                ###########################
                # if person is infected increase the infected duration
                # if reaches the max infection duration make a decision to kill a person or make him immune
                p.check_for_infection_duration()

                ##########################
                # MOVEMENT RELATED LOGIC #
                # get the person to move #
                ##########################
                if not p.is_alive:
                    # person is dead LOL cant move him
                    continue
                if p.is_stationary:
                    # person is stationary, continue to next person
                    continue
                if not p.is_person_moving():
                    # person doest not want to move, continue to next person
                    continue

                # person wants to move
                [p_row_idx, p_col_idx] = p.possible_move()

                target_move_location_person = self.map[p_row_idx][p_col_idx]

                # if the possible move direction is available, move that person to newlocation
                if target_move_location_person is None:
                    self.map[p_row_idx][p_col_idx] = self.map[row][col]
                    self.map[row][col] = None
                    # move the person on the object level
                    p.set_location([p_row_idx, p_col_idx])
                else:
                    # if there is another person, COLLISION!
                    if p.is_infected or target_move_location_person.is_infected:
                        # infection is spreading
                        # accounts for immunity of the person
                        p.infect_person()
                        # switch the persons direction after collision
                        p.switch_direction()
                        # accounts for immunity of the person
                        target_move_location_person.infect_person()

    def is_outbreak_stable(self):
        """
        checks the current outbreak status
        return: boolean 
        """
        no_of_infected_person = 0
        no_of_dead_person = 0
        no_of_immune_person = 0
        no_of_healthy_person = 0
        population_count = 0

        for row in range(self.height):
            for col in range(self.width):
                if self.map[row][col] is None:
                    continue
                population_count += 1
                p = self.map[row][col]

                if not p.is_alive:
                    no_of_dead_person += 1
                else:
                    if p.is_infected:
                        no_of_infected_person += 1
                    else:
                        no_of_healthy_person += 1

        if no_of_healthy_person + no_of_dead_person == self.population_size:
            return True

        return False

    def get_current_snapshot(self):
        """
        used to get stats for the current period.
        TODO: dictionary interface 
        """
        no_of_infected_person = 0
        no_of_dead_person = 0
        no_of_immune_person = 0
        population_count = 0

        for row in range(self.height):
            for col in range(self.width):
                if self.map[row][col] is None:
                    continue
                population_count += 1
                p = self.map[row][col]

                if not p.is_alive:
                    no_of_dead_person += 1
                if p.is_alive and p.is_infected:
                    no_of_infected_person += 1
                if p.is_immune:
                    no_of_immune_person += 1

        print(f"total_population: {self.population_size}")
        # print(f"population_count: {population_count}")
        print(f"no_of_infected_person: {no_of_infected_person}")
        print(f"no_of_dead_person: {no_of_dead_person}")
        print(f"no_of_immune_person: {no_of_immune_person}")
