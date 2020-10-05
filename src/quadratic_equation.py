import math
import logging
import argparse
import json

logging.basicConfig(level=logging.DEBUG, filename='../log/quadratic_equation_roots.log', filemode='w')


def input_data():
    logging.info('Start input.')

    parser = argparse.ArgumentParser(description='Parse args from json file.')
    parser.add_argument('--path', type=str, required=True, help='Path to file')
    args = parser.parse_args()

    configs = open(args.path)
    config = json.loads(configs.read())

    a = config['a']
    b = config['b']
    c = config['c']

    return [a, b, c]


def discriminant(a, b, c):
    logging.info('Start discriminant.')
    d = b ** 2 - 4 * a * c
    return math.sqrt(d)


def get_roots():
    logging.info('Start getting roots.')

    try:
        a, b, c = input_data()
        d = discriminant(a, b, c)
        x_1 = (-1 * b + d) / (2 * a)
        x_2 = (-1 * b - d) / (2 * a)

        logging.info(f'x1 = {x_1}; x2 = {x_2}')

        return [x_1, x_2]
    except:
        logging.info('No roots.')
        pass
    finally:
        logging.info('Program ends.')
