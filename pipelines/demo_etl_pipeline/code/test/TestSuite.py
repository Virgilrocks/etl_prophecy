import unittest

from test.demo_etl_pipeline.graph.test_Reformat_1 import *
from test.demo_etl_pipeline.graph.test_Filter_1 import *
from test.demo_etl_pipeline.graph.test_OrderBy_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
