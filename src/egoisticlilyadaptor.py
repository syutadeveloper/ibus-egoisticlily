# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# ibus-egoisticlily - The EgoisticLily engine for IBus
#
# Copyright (c) 2019 Syuta Hashimoto <syuta.hashimoto@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from egoisticlily.converter import Converter

class EgoisticLilyAdaptor:
    def __init__(self, model_path):
        self.__converter = Converter(model_path)

    
    def set_string(self, text):
        self.converted_text = self.__converter(text)

    def get_nr_segments(self):
        return 1

    def get_segment(self, segment_index, candidate_index):
        return self.converted_text

    def get_nr_candidates(self, index):
        return 1

    def commit_segment(self, segment_index, candidate_index):
        pass
