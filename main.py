import logging
import multiprocessing
import sys

import fix_machine as fm

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s', stream=sys.stderr, level=logging.DEBUG, datefmt='%Y-%m-%d,%H:%M:%S')
logger = logging.getLogger(__name__)


def main():
    """Main Entry Point

    :return:
    """
    logger.debug('startup')

    # Allocate a pool of heavy weight processes
    logger.debug(f'creating multiprocessing pool')
    pool = multiprocessing.Pool(50)
    logger.debug(f'{pool._processes}')

    # Allocate the queue that tasks will be consumed and run.
    process_queue = multiprocessing.Queue()

    # Create Semaphore for step 3 allowing 2 processes to run at a time
    step_3_semaphore = multiprocessing.Manager().Semaphore(2)

    # Add some tasks
    for target_number in range(10):
        process_queue.put(('fix_machine', f'target-{target_number}', step_3_semaphore,))

    # kick off all the jobs into the pool for execution and then just wait 60 secs for everything to complete
    while True:
        item = process_queue.get(timeout=60)
        if item[0] == 'fix_machine':
            logger.debug(f'starting up {item[1]}')
            pool.apply_async(fm.fix_target_machine, args=(item[1], item[2]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

