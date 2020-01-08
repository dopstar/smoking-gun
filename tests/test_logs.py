import unittest

import smoking_gun.logs


class TestCapturedLogging(unittest.TestCase):
    def test__read_logs(self):
        captured_logging = smoking_gun.logs.CapturedLogging()
        self.assertEqual(captured_logging._read_logs(), "")
