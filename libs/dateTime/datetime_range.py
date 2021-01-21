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
#####################################################################################
import time
import datetime
from datetime import datetime as date_time
import re

class DateTimeRange:

    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def to_timestamp(self, dateTime):
        dt = date_time.strptime(dateTime, self.DATE_TIME_FORMAT)
        return int(date_time.timestamp(dt))

    def get_last_n_hours_range(self, n_hours, date_time_str="", output_format= ""):
            if len(output_format.strip()) > 0 :
                output_format = self.DATE_TIME_FORMAT

            now = date_time.now()
            dt_to = date_time.now()
            if len(date_time_str.strip()) > 0 :
                dt_to = date_time.strptime(date_time_str, self.DATE_TIME_FORMAT)

            dt_from = dt_to -  datetime.timedelta(hours = n_hours)
            return dt_from.strftime(self.DATE_TIME_FORMAT) + "," + dt_to.strftime(self.DATE_TIME_FORMAT)

    def get_last_24_hours_range(self, date_time_str="", output_format= ""):
        return self.get_last_n_hours_range(24, date_time_str, output_format)

    def range_to_timestamp(self, datetime_range):
        dtr = datetime_range.rstrip(",")
        self.__assert_range(dtr)
        dt_from, dt_to = self.__extract_range(dtr)

        timestamp_from = self.to_timestamp(dt_from)
        timestamp_to = self.to_timestamp(dt_to)

        dt_to_timestamp = dict({"from" : timestamp_from, "to" : timestamp_to })

        if timestamp_to < timestamp_from:
            dt_to_timestamp['from'] = timestamp_to
            dt_to_timestamp['to'] = timestamp_from

        return dt_to_timestamp

    def __assert_format(self, datetime_range):
        "format checker 2020-01-10 hh:mm:ss,2020-01-10 hh:mm:ss"
        pattern = re.compile("^([0-9]{4}\-[0-9]{2}\-[0-9]{2} [0-9]{1,2}\:[0-9]{1,2}\:[0-9]{1,2},?){2}$")

        if not pattern.fullmatch(datetime_range):
               raise Exception("Invalid range format! Given: '" + datetime_range + "' , want: yyyy-mmm-dd hh:mm:ss,yyyy-mm-dd hh:mm:ss")

    def __extract_range(self, datetime_range):
        range_values = datetime_range.split(",")
        from_date_time = range_values[0]
        to_date_time = range_values[1]

        return from_date_time, to_date_time

    def __assert_datetime(self, dt):
        try:
            date_time.strptime(dt, self.DATE_TIME_FORMAT)
        except ValueError as err:
            raise Exception(dt + " is invalid")

    def __assert_range(self, datetime_range):
        self.__assert_format(datetime_range)
        dt_from, dt_to = self.__extract_range(datetime_range)
        self.__assert_datetime(dt_from)
        self.__assert_datetime(dt_to)
