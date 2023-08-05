"""
Unit tests for stem.client.Size.
"""

import unittest

from stem.client.datatype import Size


class TestSize(unittest.TestCase):
  def test_attributes(self):
    self.assertEqual('CHAR', Size.CHAR.name)
    self.assertEqual(1, Size.CHAR.size)
    self.assertEqual(2, Size.SHORT.size)
    self.assertEqual(4, Size.LONG.size)
    self.assertEqual(8, Size.LONG_LONG.size)

  def test_pack(self):
    self.assertEqual(b'\x12', Size.CHAR.pack(18))
    self.assertEqual(b'\x00\x12', Size.SHORT.pack(18))
    self.assertEqual(b'\x00\x00\x00\x12', Size.LONG.pack(18))
    self.assertEqual(b'\x00\x00\x00\x00\x00\x00\x00\x12', Size.LONG_LONG.pack(18))

    self.assertRaisesWith(ValueError, 'Size.pack encodes an integer, but was a str', Size.CHAR.pack, 'hi')
    self.assertRaisesWith(ValueError, 'Packed values must be positive (attempted to pack -1 as a CHAR)', Size.CHAR.pack, -1)

    too_small = Size('TOO_SMALL', 1)
    self.assertRaises(OverflowError, too_small.pack, 1800)

  def test_unpack(self):
    self.assertEqual(18, Size.CHAR.unpack(b'\x12'))
    self.assertEqual(18, Size.SHORT.unpack(b'\x00\x12'))
    self.assertEqual(18, Size.LONG.unpack(b'\x00\x00\x00\x12'))
    self.assertEqual(18, Size.LONG_LONG.unpack(b'\x00\x00\x00\x00\x00\x00\x00\x12'))

    self.assertEqual(ord('a'), Size.CHAR.unpack(b'a'))
    self.assertEqual(24930, Size.SHORT.unpack(b'ab'))

    self.assertRaisesWith(ValueError, "'\\x00\\x12' is the wrong size for a CHAR field", Size.CHAR.unpack, '\x00\x12')

  def test_pop(self):
    self.assertEqual((18, b''), Size.CHAR.pop(b'\x12'))

    self.assertEqual((0, b'\x12'), Size.CHAR.pop(b'\x00\x12'))
    self.assertEqual((18, b''), Size.SHORT.pop(b'\x00\x12'))

    self.assertRaisesWith(ValueError, "'' is the wrong size for a CHAR field", Size.CHAR.pop, '')
    self.assertRaisesWith(ValueError, "'\\x12' is the wrong size for a SHORT field", Size.SHORT.pop, '\x12')
