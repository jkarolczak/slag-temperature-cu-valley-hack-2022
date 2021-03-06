import argparse

import cfg
from model import train


def main(args: argparse.Namespace) -> None:
    config = cfg.read(args.cfg)
    train(config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default="../resources/cfg/train.yaml",
                        help="path to the file that contains training parameters")
    arguments = parser.parse_args()
    main(arguments)
