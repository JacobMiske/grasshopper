"""
API result visualization tools
"""
import numpy as np
import matplotlib.pyplot as plt


class api_visualize(object):
    """
    Object for all APIs to use to pass results towards.

    Able to generate plots and mathematical relations.
    """
    def __init__(self):
        self.desc = "API visualization tools"

    def plot_list(self, list_v, x_s=None, y_s=None, z_s=None):
        """
        Plots list of values given a title and units for x, y, z, etc.
        :param list_v:
        :param x_s: string
        :param y_s: string
        :param z_s: string
        :return:
        """
        fig, ax = plt.subplots(nrows=2, ncols=2)
        for row in ax:
            for col in row:
                col.scatter(range(len(list_v)), list_v)
        plt.show()
        return 0

    def get_metrics_on_list(self, list_v, x_s=None, y_s=None, z_s=None):
        """
        Takes a data stream and converts to comparative values.
        :param list_v:
        :param x_s: string
        :param y_s: string
        :param z_s: string
        :return:
        """
        res_mean = np.mean(list_v)
        return res_mean