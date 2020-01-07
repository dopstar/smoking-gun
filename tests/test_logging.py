import unittest

import smoking_gun.logging


class TestCapturedLogging(unittest.TestCase):
    def test_get_logs(self):
        captured_logging = smoking_gun.logging.CapturedLogging()
        self.assertEqual(captured_logging.get_logs(), "")
