from grid import Grid

if __name__ == "__main__":
    height = 100
    width = 100
    population_size = 1000
    infection_rate = 0.009
    stationary_multiplier = 0.10
    mobility = 0.75
    p_death = 0.06
    infection_duration = 10
    evolutions = 1000
    # initialize grid
    g = Grid(height, width, population_size, infection_rate,
             stationary_multiplier, mobility, p_death, infection_duration)

    # T0
    print(f"TO snapshot")
    g.get_current_snapshot()
    print("")

    for i in range(evolutions):
        print(f"Performing Evolution: {i+1}")
        if g.is_outbreak_stable():
            print("Outbreak Stable")
            g.get_current_snapshot()
            break
        g.perform_evolution()
        g.get_current_snapshot()
        print("")
