import numpy as np
import matplotlib.pyplot as plt
import pathlib



def counter(counts, car, chosen):
    return counts[-1] + 1 if car == chosen else counts[-1]


def main():
    
    transition = {'not_switched':[],'switched':[]}
    n_doors = 100
    n_trials = 1000

    for door in range(3, n_doors):
        not_switched = {'count':[0], 'rate':[.0]}
        switched = {'count':[0], 'rate':[.0]}

        for i in range(0, n_trials):
            
            doors = np.array([j for j in range(door)])
            car = np.random.randint(0, door)
            first = np.random.randint(0, door)

            # The host must always open a door that was not picked by the contestant.
            # The host must always open a door to reveal a goat and never the car.
            # Monty Hall problem in Wikipedia
            goats = doors[np.where((doors != first) & (doors != car))[0]]
            option = np.array([car, np.random.choice(goats,1)[0]])

            # The host must always offer the chance to switch between the originally
            # chosen door and the remaining closed door.
            # Monty Hall problem in Wikipedia.
            second = option[np.where(option != first)[0]][0]
            
            # Not switched
            not_switched['count'].append(counter(not_switched['count'], car, first))
            switched['count'].append(counter(switched['count'], car, second))

        transition['not_switched'].append(not_switched['count'][-1]/n_trials)
        transition['switched'].append(switched['count'][-1]/n_trials) 

    fig = plt.figure(figsize=(8, 6))
    plt.rcParams["font.size"] = 14

    plt.plot(transition['switched'],label='Switched')
    plt.plot(transition['not_switched'],label='Not switched')
    plt.legend(loc='right')

    plt.ylim(0.0, 1.0)
    plt.ylabel('Rate[0-1]')
    plt.xlabel('The number of doors [N]')

    plt.savefig(pathlib.Path('.').joinpath('monty_hall_transition.png'))
    plt.show()

if __name__ == "__main__":
    main()