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

		# Amount of blocks over Tb
		blocks = 100000000000000000

		expected = '46566128.73Tb'
		result = diskspace.bytes_to_readable(blocks)

		self.assertEqual(expected, result)

		# Amount of blocks negative
		blocks = -1

		expected = '0.00B'
		result = diskspace.bytes_to_readable(blocks)

		self.assertEqual(expected, result)

	def test_subprocess_check_output(self):
		cmd = 'ls'
		expected = subprocess.check_output(cmd)
		result = diskspace.subprocess_check_output(cmd)

		self.assertEqual(expected, result)

if __name__ == "__main__":
	unittest.main()