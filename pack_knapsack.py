#! /usr/bin/env python

import sys
import argparse
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(
        description = "Take a knapsack size and a set of items, and return set of items that can fit in the knapsack"
    )
    parser.add_argument(
        "--knapsack_size",
        help = "The maximum weight of objects that can fit in knapsack.",
        required = True
    )
    parser.add_argument(
        "--items_weights",
        help = "The set of items and their associated weights and values in a tab delimited file",
        required = True
    )
    return parser.parse_args()

# def pack_knapsack(...): # recurse or dynamic

def main():
    args = parse_args()

    item_weights = pd.read_csv(args.items_weights, sep='\t')
    # pack_knapsack(args.knapsack_size, items_weights)

if __name__ == '__main__':
    main()