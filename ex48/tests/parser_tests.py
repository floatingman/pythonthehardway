import unittest
from ex48 import parser


class TestParser(unittest.TestCase):
    def setUp(self):
        self.x = parser.parse_sentence([('verb', 'run'),
                                        ('direction', 'north')])
        self.y = parser.parse_sentence([('noun', 'dragon'),
                                        ('verb', 'eats'),
                                        ('noun', 'hero')])

    def test_no_nouns(self):
        self.assertEqual(self.x.subject, 'player')
        self.assertEqual(self.x.verb, 'run')
        self.assertEqual(self.x.object, 'north')

    def test_nouns(self):
        self.assertEqual(self.y.subject, ('dragon'))
        self.assertEqual(self.y.verb, ('eats'))
        self.assertEqual(self.y.object, ('hero'))


if __name__ == '__main__':
    unittest.main()
