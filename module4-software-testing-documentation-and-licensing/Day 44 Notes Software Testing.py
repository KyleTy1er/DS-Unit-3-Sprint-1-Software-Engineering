

# test/custom_frame_test.py

import unittest
​
from my_lambdata.class3 import CustomFrame
​
class TestCustomFrame(unittest.TestCase):
​
    def test_name_conversion(self):
        #self.assertEqual(enlarge(3), 300)
        custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
        #print(custom_df.head())
        #custom_df.convert_names()
        #print(custom_df.head())
        #breakpoint()
        self.assertEqual(custom_df.columns.tolist(), ["abbrev"])
        custom_df.convert_names()
        self.assertEqual(custom_df.columns.tolist(), ["abbrev", "state_name"])
​
        # todo: consider also testing the actual values (perhaps the first row)
​
if __name__ == "__main__":
