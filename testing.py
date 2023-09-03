import logging
import unittest
from pathlib import Path
logger = logging.getLogger(__name__)
start_dir = f"{Path.cwd()}"


def run():
    """
    Equivalent of running:
        python -m unittest discover -s tests -t tests
    """
    try:
        loader = unittest.TestLoader()
        suite = loader.discover(start_dir, "test*.py")
        # Set buffer=True to save sys.stdout and sys.stderr to buffer (i.e. hide from output during test execution)
        # runner = unittest.TextTestRunner(buffer=True)
        runner = unittest.TextTestRunner()
    except(ImportError, AttributeError) as e:
        logger.error(f"There was an error running the test suite: {e}")
    else:
        logging.captureWarnings(True)
        runner.run(suite)


if __name__ == "__main__":
    run()
