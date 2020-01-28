"""
Sample Code for Lab2 for testing the sonar
Use "run.py [--sim] lab2_sonar_test" to execute
"""
import numpy as np
import matplotlib.pyplot as plt


class Run:
    def __init__(self, factory):
        """Constructor.

        Args:
            factory (factory.FactoryCreate)
        """
        self.create = factory.create_create()
        self.time = factory.create_time_helper()
        self.sonar = factory.create_sonar()

    def run(self):
        data = []
        for i in range(0, 101):
            new_data = self.sonar.get_distance()
            data.append(new_data)
            print(new_data)
            self.time.sleep(0.1)
        # First element gets 3.3
        data.pop(0)
        print(data)
        correct_res = 0.53
        Utils.show_stat(np.asarray(data), correct_res)
        Utils.plot_hist(np.asarray(data))
        self.create.stop()

        # while True:
        #     print(self.sonar.get_distance())
        #     self.time.sleep(0.1)

class Utils:
    def plot_hist(s, num_bins: int = 20):
        mu, sigma = 0, 0.5
        # s = np.random.normal(mu, sigma, 10000)

        plt.hist(s, 20, density=False, linewidth=1.0)
        plt.savefig('test.png')
        plt.show()

    def show_stat(s, correct_res: float = 0):
        print("Mean: " + str(np.mean(s - correct_res)))
        print("SD: " + str(np.std(s)))

    # def run(self):
    #     data = np.zeros(100, dtype=float)
    #     for i in range(0, 100):
    #         data[i] = self.sonar.get_distance()
    #         print(data[i])
    #         self.time.sleep(0.1)
    #
    #     print("Stats: ")
    #     correct_res = input("Enter correct distance")
    #     show_stat(data, float(correct_res))
    #     plot_hist(data)


# def plot_hist(data=None, num_bins: int = 20) -> None:
#     if data is None:
#         data = np.random.normal(0, 0.5, 10000)
#
#     plt.hist(data, bins=num_bins, edgecolor='black', linewidth=1.0)
#     plt.show()
#
#
# def show_stat(data, correct_res: float = 0) -> None:
#     print("Mean: " + str(np.mean(data - correct_res)))
#     print("SD: " + str(np.std(data)))
