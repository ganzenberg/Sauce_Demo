import logging

class LogGen:
    @staticmethod
    def test_logDemo():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('/Users/ganeshkumar/PycharmProjects/Sauce_Demo/logs/automation.logs')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger