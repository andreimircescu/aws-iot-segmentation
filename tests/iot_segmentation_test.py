# -*- coding: utf-8 -*-
import unittest
from aws_iot_segmentation import iot_segmentation


class IotSegmentationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_normal_message(self):
        msg = "this is a normal message dooh"
        for seg_msg in iot_segmentation.segment_message(msg):
            self.assertEqual(msg, seg_msg)
            return

    def test_bad_input(self):
        bad_input = None
        iterator = iot_segmentation.segment_message(bad_input)
        with self.assertRaises(Exception):
            iterator.next()

    def test_big_input_same_message(self):
        big_input = self._get_big_input()
        # feed it to be segmented
        iterator = iot_segmentation.segment_message(big_input)
        is_equal = False
        for msg in iterator:
            # feed it back to reconstruct
            full_msg = iot_segmentation.get_message(msg)
            if full_msg:
                is_equal = full_msg == big_input
        self.assertTrue(is_equal)

    def _get_big_input(self):
        return " dummy string " * iot_segmentation.MAX_SIZE


if __name__ == '__main__':
    unittest.main()
