import unittest

import smoking_gun.logs


class TestCapturedLogging(unittest.TestCase):
    def test_get_logs(self):
        captured_logging = smoking_gun.logs.CapturedLogging()
        self.assertEqual(captured_logging.get_logs(), "")
