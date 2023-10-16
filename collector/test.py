import unittest

from main import DataCollector


class TestDataCollector(unittest.TestCase):
    def setUp(self):
        self.data_collector = DataCollector()

    # def tearDown(self):
    #     self.data_collector = None

    def test_get_object_ids(self):
        self.assertEqual(0, len(self.data_collector.object_ids))

        self.assertTrue(0 < len(self.data_collector.get_object_ids()))


if __name__ == '__main__':
    unittest.main()
