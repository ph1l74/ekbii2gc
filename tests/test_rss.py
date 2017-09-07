# -*- encoding: utf-8 -*-

import unittest
import os
import rss
from datetime import datetime

class TestRSS(unittest.TestCase):

    def test_clear_tags_equals(self):
        test_strings = [('<a class="reference internal" href="#organizing-test-code">25.3.4. Organizing test code</a>',
                         '25.3.4. Organizing test code'),
                        (
                        '<a href="http://pythontesting.net/support/" itemprop="url"><span itemprop="name">Support</span></a>',
                        'Support'),
                        ('<a href="../index.html">Documentation</a>', 'Documentation'),
                        ('<a class="reference internal" href="#description">Description</a>', 'Description'),
                        ('<guid isPermaLink="true">http://ekbii.livejournal.com/651113.html</guid>',
                         'http://ekbii.livejournal.com/651113.html'),
                        ('<pubDate>Thu, 22 Jun 2017 07:24:51 GMT</pubDate>', 'Thu, 22 Jun 2017 07:24:51 GMT'),
                        ('<comments>http://ekbii.livejournal.com/651113.html</comments>',
                         'http://ekbii.livejournal.com/651113.html'),
                        ('<lj:poster>the_ob4</lj:poster>', 'the_ob4'),
                        ('<title>Интеллектуальные игры в Екатеринбурге</title>',
                         'Интеллектуальные игры в Екатеринбурге')]
        for raw, expected in test_strings:
            result = rss.clear_tags(raw)
            self.assertEqual(result, expected)

    def test_convert_date_equals(self):
        test_strings = [('понедельник, 26 июня, 19-15', datetime(2017, 6, 26, 19, 15)),
                        ('понедельник, 19 июня, 19-15', datetime(2017, 6, 19, 19, 15)),
                        ('понедельник, 5 июня, 19-20', datetime(2017, 6, 5, 19, 20)),
                        ('понедельник, 29 мая, 19-20', datetime(2017, 5, 29, 19, 20)),
                        ('понедельник, 22 мая, 19-20', datetime(2017, 5, 22, 19, 20)),
                        ('понедельник, 15 мая, 19-20', datetime(2017, 5, 15, 19, 20)),
                        ('понедельник, 24 апреля, 19-20', datetime(2017, 4, 24, 19, 20)),
                        ('суббота, 22 апреля (в день рождения Ленина), 18-00', datetime(2017, 4, 22, 18, 00)),
                        ('понедельник 17 апреля, 19-20', datetime(2017, 4, 17, 19, 20)),
                        ('суббота, 1 апреля, 16-00', datetime(2017, 4, 1, 16, 00))]

        for raw, expected in test_strings:
            result = rss.convert_date(raw)
            self.assertEqual(result, expected)

    def test_get_id_equals(self):
        test_strings = [('http://ekbii.livejournal.com/651113.html', 651113),
                        ('http://ekbii.livejournal.com/651406.html', 651406),
                        ('http://ekbii.livejournal.com/650824.html', 650824),
                        ('http://ekbii.livejournal.com/650468.html', 650468),
                        ('http://ekbii.livejournal.com/650028.html', 650028),
                        ('http://ekbii.livejournal.com/649809.html', 649809),
                        ('http://ekbii.livejournal.com/649612.html', 649612),
                        ('http://ekbii.livejournal.com/649252.html', 649252),
                        ('https://vk.com/12345.html', 12345),
                        ('http://ph1l74.com/post/159561457718.html', 159561457718)]

        for raw, expected in test_strings:
            result = rss.get_id(raw)
            self.assertEqual(result, expected)
