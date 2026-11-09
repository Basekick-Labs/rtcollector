import io
import unittest

from inputs.exec import _read_bounded_stream


class ReadBoundedStreamTests(unittest.TestCase):
    def test_retains_only_limit_while_counting_all_bytes(self):
        retained, total = _read_bounded_stream(io.BytesIO(b"abcdefghij"), 4)
        self.assertEqual(retained, b"abcd")
        self.assertEqual(total, 10)

    def test_zero_limit_still_drains_and_counts(self):
        retained, total = _read_bounded_stream(io.BytesIO(b"abc"), 0)
        self.assertEqual(retained, b"")
        self.assertEqual(total, 3)


if __name__ == "__main__":
    unittest.main()
