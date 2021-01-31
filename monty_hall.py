import numpy as np
import matplotlib.pyplot as plt
import pathlib


def counter(counts, car, chosen):
    return counts[-1] + 1 if car == chosen else counts[-1]


def main():
    
    not_switched = {'count':[0], 'rate':[.0]}
    switched = {'count':[0], 'rate':[.0]}
    n_doors = 3
    n_trials = 1000

    for i in range(0, n_trials):
        
        doors = np.array([j for j in range(n_doors)])
        car = np.random.randint(0, n_doors)
        first = np.random.randint(0, n_doors)

        # The host must always open a door that was not picked by the contestant.
        # The host must always open a door to reveal a goat and never the car.
        # Monty Hall problem in Wikipedia
        goats = doors[np.where((doors != first) & (doors != car))[0]]
        options = np.array([car, np.random.choice(goats,1)[0]])

        # The host must always offer the chance to switch between the originally
        # chosen door and the remaining closed door.
        # Monty Hall problem in Wikipedia.
        second = options[np.where(options != first)[0]][0]
        
        # Not switched
        not_switched['count'].append(counter(not_switched['count'], car, first))
        switched['count'].append(counter(switched['count'], car, second))

    not_switched['rate'] = [not_switched['count'][i]/(i+1) for i in range(n_trials)]
    switched['rate'] = [switched['count'][i]/(i+1) for i in range(n_trials)]

    fig = plt.figure(figsize=(8, 6))
    plt.rcParams["font.size"] = 14

    label = 'Not switched:' + str(np.round(not_switched['rate'][-1], decimals=5))
    plt.plot(not_switched['rate'], label=label)

    label = 'Switched:' + str(np.round(switched['rate'][-1], decimals=5))
    plt.plot(switched['rate'], label=label)
    plt.legend(loc='upper right')

    plt.ylim(0.0, 1.0)
    plt.ylabel('Rate[0-1]')
    plt.xlabel('The number of trials [N]')

    plt.savefig(pathlib.Path('.').joinpath('monty_hall.png'))
    plt.show()

if __name__ == "__main__":
    main()