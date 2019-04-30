# -*- coding: utf-8 -*-
import  argparse
import random


class generate_random:

    def __init__(self):

        print "Flag value: " + str(custom_variable)

        for i in range(10):
            x = random.randint(0,10)
            print "Random number " + str(i) + ": " + str(x)

        print "End of program"

        #generate random 

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument(   "-f",
                                "--flag",
                                help="dummy flag variable",
                                action="store_true",
                                default = False)

    args = args_parser.parse_args()

    custom_variable = args.flag

    APP = generate_random()
