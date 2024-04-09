import argparse
import sys
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', metavar='input_file', type=str)
    parser.add_argument('--out', dest='output_file', metavar='output_file', type=str)
    args = parser.parse_args()