# -*- coding: utf-8 -*-
# @Author: darkshadows123

import copy
from digExtractor.extractor import Extractor
from dig_md5_extractor import DIGMd5Extractor


class Md5Extractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        self.dmd5 = DIGMd5Extractor()

    def extract(self, doc):
        if 'text' in doc:
            return self.dmd5.extract_md5(doc['text'])
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
