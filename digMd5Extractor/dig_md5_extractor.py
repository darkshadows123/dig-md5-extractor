# -*- coding: utf-8 -*-
# @Author: darkshadows123

import re
from sets import Set

################################################
# Main
################################################

class DIGMd5Extractor(object):
    """Extractor of md5 hash from text.

    Users of this class should call DIGIpAddressExtractor.extract_ipaddress(), see documentation.
    """

    def extract_md5(self, string):
        """Extract md5 hash from string.
        :param string: the text to extract from
        """
        pattern = r"[a-f0-9]{32}"
        md5s = re.findall(pattern, string)

        return md5s


