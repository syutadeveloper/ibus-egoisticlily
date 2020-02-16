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
import grpc
import egoisticlily.proto.egoisticlily_pb2_grpc
import egoisticlily.proto.egoisticlily_pb2

CHANNEL_ADDRESS = "[::]:50055"

class EgoisticLilyAdaptor:
    def __init__(self, model_path):
        """ Egoisticlily adopter.

        :param model_path: now not use.
        """
        self.__channel = grpc.insecure_channel(CHANNEL_ADDRESS)
        self.__stub = egoisticlily.proto.egoisticlily_pb2_grpc.EgoisticLilyServiceStub(self.__channel)
    
    def set_string(self, text):
        response = self.__stub.Convert(egoisticlily.proto.egoisticlily_pb2.ConvertReq(in_str=text))
        self.converted_text = response.out_str

    def get_nr_segments(self):
        return 1

    def get_segment(self, segment_index, candidate_index):
        return self.converted_text

    def get_nr_candidates(self, index):
        return 1

    def commit_segment(self, segment_index, candidate_index):
        pass

    def cleanup(self):
        # debug
        print("cleanup")
        self.__channel.close()
