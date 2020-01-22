# Copyright 2019
"""
For development of grasshopper Project Shell
"""

import os
from pyfiglet import Figlet             # For printing ascii art
from terminaltables import SingleTable, ascii_table, AsciiTable  # For creating tables
import json


class RunSim:
    """
    Class for functions associated with jarvis shell script list sensors feature
    """
    def __init__(self):
        self.questions = ["How many unique materials are used in the simulation? ",
                          "What is particle type being used? (proton, neutron, electron, photon...)",
                          "How many kgs of that item are there? [kg]",
                          "What is the density of that item? [kg/m^3]"
                          ]

    def get_sim(self):
        """
        This function prepares the questions for populating a GDML file.
        :return:
        """
        answers = self.set_questions()

    def set_questions(self):
        """
        Has the user set answers to a variety of questions
        :return:
        """
        answer_list = []
        print(' This tool will ask you a set of questions to generate a simulation input. \n')
        while True:
            try:
                for question in self.questions:
                    print(question)
                    q_answer = input()
                    answer_list.append(q_answer)
            except TypeError:
                print("Please try again")
                continue
            except ValueError:
                print("Please try again")
                continue
            else:
                break

        # TODO: work this out to utilize the *.json which drives CLI input
        return answer_list

    def generate_input_GDML(self):
        """

        :return:
        """
        pass

    def start_grasshopper_sim(self):
        """

        :return:
        """
        pass

