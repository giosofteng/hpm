import unittest

from collector.source.data_collector import DataCollector


class TestDataCollector(unittest.TestCase):
    def setUp(self):
        self.data_collector = DataCollector()

    # def tearDown(self):
    #     self.data_collector = None

    def test_get_object_ids(self):
        self.assertEqual(0, len(self.data_collector.object_ids))

        self.assertTrue(0 < len(self.data_collector.get_object_ids()))

    def test_get_object_data(self):
        # The API only returns the `message` when an error occurs
        self.assertIsNotNone(self.data_collector.get_object_data(0)['message'])

        object_id = self.data_collector.get_object_ids()[0]
        self.assertIsNotNone(self.data_collector.get_object_data(object_id)['title'])


if __name__ == '__main__':
    unittest.main()
