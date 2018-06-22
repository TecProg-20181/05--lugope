import unittest
import diskspace
import subprocess

class DiskSpaceTest(unittest.TestCase):
	"""docstring for DiskSpaceTest"""

	def test_bytes_to_readable(self):
		# Lower amount of blocks 
		blocks = 0

		expected = '0.00B'
		result = diskspace.bytes_to_readable(blocks)

		self.assertEqual(expected, result)

		# High amount of blocks
		blocks = 10000000000

		expected = '4.66Tb'
		result = diskspace.bytes_to_readable(blocks)

		self.assertEqual(expected, result)

if __name__ == "__main__":
	unittest.main()