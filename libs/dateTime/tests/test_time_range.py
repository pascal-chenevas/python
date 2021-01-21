#!/usr/bin/python3
############################ Copyrights and license #################################
#                                                                                   #   
# Copyright 2021 Pascal Chenevas-Paule <pascal.chenevas-paule@gmx.de>               #
#                                                                                   #
# datetime_range is free software: you can redistribute it and/or modify it under   #
# the terms of the GNU Lesser General Public License as published by the Free       #
# Software Foundation, either version 3 of the License, or (at your option)         #
# any later version.                                                                #
#                                                                                   #
# datetime_range is distributed in the hope that it will be useful, but WITHOUT ANY #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS         #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more      #
# details.                                                                          #
#                                                                                   #
# You should have received a copy of the GNU Lesser General Public License          #
# along with datetime_range. If not, see <http://www.gnu.org/licenses/>.            #
#                                                                                   #
####################################################################################
import unittest
import ../datetime_range
from datetime import datetime

class TestDateTimeMethods(unittest.TestCase):
    """
    Unit test range of a datetime
    Timestamp values found at url: https://www.epochconverter.com/
    """

    date_time = datetime_range.DateTimeRange()

    def test_get_last_24_hours_range(self):
        to_dt = "2021-10-01 12:00:00"
        from_dt = "2021-09-30 12:00:00"
        expected = from_dt + "," + to_dt
        actual = self.date_time.get_last_24_hours_range(to_dt)
        self.assertEqual(actual, expected)

    def test_get_last_n_hours_range_for_last_78_hours(self):
         to_dt = "1970-03-15 12:00:00"
         from_dt = "1970-03-12 06:00:00"
         expected = from_dt + "," + to_dt
         actual = self.date_time.get_last_n_hours_range(78, to_dt)
         self.assertEqual(actual, expected)

    def test_to_timestamp(self):
        dateTime = "1982-10-04 08:00:01"
        expected = 402562801
        actual = self.date_time.to_timestamp(dateTime)

        self.assertEqual(actual, expected)

    def test_range_to_timestamp(self):
        """
            date = 2022-01-10 09:10:30 => timestamp = 1641802230
            date = 2022-01-12 10:10:30 => timestamp = 1641978630
        """
        range = "2022-01-10 09:10:30,2022-01-12 10:10:30,"
        expected = dict({"from" : 1641802230, "to" : 1641978630})
        actual = self.date_time.range_to_timestamp(range)

        self.assertEqual(actual, expected)

    def test_range_to_timestamp(self):
        """
            date = 2022-01-01 10:10:30 => timestamp = 1641028230
            date = 2022-01-30 16:30:15 => timestamp = 1643556615
        """
        range = "2022-01-30 16:30:15,2022-01-01 10:10:30"
        expected = dict({"from" : 1641028230, "to" : 1643556615})
        actual = self.date_time.range_to_timestamp(range)

        self.assertEqual(actual, expected)

    def test_range_to_timestamp_given_str_failed(self):
        with self.assertRaises(Exception) as cm:
             self.date_time.range_to_timestamp("from_date,to_date")

        exception_thrown = cm.exception
        expected = "Invalid range format! Given: 'from_date,to_date' , want: yyyy-mmm-dd hh:mm:ss,yyyy-mm-dd hh:mm:ss"
        actual = str(exception_thrown)

        self.assertEqual(actual, expected)

    def test_range_to_timestamp_given_wrong_date_time_failed(self):
        with self.assertRaises(Exception) as cm:
             self.date_time.range_to_timestamp("2021-31-12 14:12:00,2021-01-12 00:00:00")

        exception_thrown = cm.exception
        expected = "2021-31-12 14:12:00 is invalid"
        actual = str(exception_thrown)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
