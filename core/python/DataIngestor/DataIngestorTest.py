from DataIngestor import app

import os
import json
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):

    # Our first unit test - We are using the unittest
    # library, calling the generateMyURL route from the app
    # passing a couple of strings, and checking that the
    # returned value, contained on the JSON response, match
    # a valid url.
    def test_generateMyURL(self):
        tester = app.test_client(self)
        response = tester.get('/1996/06/06/KABR/')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"url": "https://noaa-nexrad-level2.s3.amazonaws.com/1996/06/06/KABR/KABR19960606_000202.gz"})

    if __name__ == '__main__':
        unittest.main()