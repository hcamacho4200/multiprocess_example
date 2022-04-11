import logging
import multiprocessing
import os
import random
import time


logger = logging.getLogger(__name__)


def fix_target_machine(target_machine_name, step_3_lock: multiprocessing.Semaphore = None):
    """Fixes a target machine
    - step 1 - print the target_machine_name and wait random time
    - step 2 - perform an ls -la and wait a random time
    - step 3 - obtain semaphore, then wait sometime.
    - return results

    :param machine_name:
    :param step_3_lock:
    :return:
    """
    logger.debug(f'starting fix for {target_machine_name}')

    # step 1
    logger.debug(f'step 1 for {target_machine_name}')
    print(target_machine_name)
    _wait_random_time(target_machine_name)

    # step 2
    logger.debug(f'step 2 for {target_machine_name}')
    stream = os.popen('ls -la')
    output = stream.read()
    _wait_random_time(target_machine_name)

    # step 3
    logger.debug(f'step 3 for {target_machine_name}')
    with step_3_lock:
        logger.debug(f'step 3 for {target_machine_name} semaphore obtained')
        _wait_random_time(target_machine_name, 5, 5)
    logger.debug(f'step 3 for {target_machine_name} semaphore released')

    return True


def _wait_random_time(name, lower_bound=1, upper_bound=10):
    """Wait a random time period

    :return:
    """
    logger.debug(f'starting wait for {name}')
    time.sleep(random.randint(lower_bound, upper_bound))
    logger.debug(f'ending wait for {name}')