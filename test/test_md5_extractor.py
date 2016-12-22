import unittest

# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from digExtractor.extractor_processor import ExtractorProcessor
from digMd5Extractor.md5_extractor import Md5Extractor

class TestMd5ExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_md5_extractor(self):
        doc = {'text' : 'sample md5 hash  00236a2ae558018ed13b5222ef1bd987 and 8f6689ae029916841e126e278571794b'}

        extractor = Md5Extractor().set_metadata({'extractor': 'ipaddress'})
        ep = ExtractorProcessor().set_input_fields(['text'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)
        result = updated_doc['extracted'][0]['result']
        self.assertEqual(result[0]['value'],
                         '00236a2ae558018ed13b5222ef1bd987')
        self.assertEqual(result[1]['value'],
                         '8f6689ae029916841e126e278571794b')

if __name__ == '__main__':
    unittest.main()
