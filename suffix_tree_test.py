import unittest
from suffix_tree_v2 import SuffixTree
import MiniProject3

class MyTestCase(unittest.TestCase):
    def test_empty_string(self):
        st = SuffixTree('')
        self.assertEqual(st.find_substring('not there'), -1)
        self.assertEqual(st.find_substring(''), -1)
        self.assertFalse(st.has_substring('not there'))
        self.assertFalse(st.has_substring(''))

    def test_repeated_string(self):
        st = SuffixTree("aaa")
        self.assertEqual(st.find_substring('a'), 0)
        self.assertEqual(st.find_substring('aa'), 0)
        self.assertEqual(st.find_substring('aaa'), 0)
        self.assertEqual(st.find_substring('b'), -1)
        self.assertTrue(st.has_substring('a'))
        self.assertTrue(st.has_substring('aa'))
        self.assertTrue(st.has_substring('aaa'))
        self.assertFalse(st.has_substring('aaaa'))
        self.assertFalse(st.has_substring('b'))
        # case sensitive by default
        self.assertFalse(st.has_substring('A'))

    def test_the_old_testament(self):
        text = MiniProject3.read_file('king-james-bible.txt')
        st = SuffixTree(text)

        books = ['The Old Testament', 'The First Book of Moses: Called Genesis',
                 'The Second Book of Moses: Called Exodus', 'The Third Book of Moses: Called Leviticus',
                 'The Fourth Book of Moses: Called Numbers', 'The Fifth Book of Moses: Called Deuteronomy',
                 'The Book of Joshua', 'The Book of Judges', 'The Book of Ruth', 'The First Book of the Kings',
                 'The Second Book of the Kings', 'The Third Book of the Kings', 'The Fourth Book of the Kings',
                 'The First Book of the Chronicles', 'The Second Book of the Chronicles', 'The Book of Ezra',
                 'The Book of Nehemiah', 'The Book of Esther', 'The Book of Job', 'The Book of Psalms', 'The Proverbs',
                 'The Preacher', 'The Song of Solomon', 'The Book of the Prophet Isaiah',
                 'The Book of the Prophet Jeremiah', 'The Lamentations of Jeremiah', 'The Book of the Prophet Ezekiel',
                 'The Book of Daniel', 'The Book of Hosea', 'The Book of Joel', 'The Book of Amos',
                 'The Book of Obadiah', 'The Book of Jonah', 'The Book of Micah', 'The Book of Nahum',
                 'The Book of Habakkuk', 'The Book of Zephaniah', 'The Book of Haggai', 'The Book of Zechariah',
                 'The Book of Malachi']
        expected = [0, 43, 205455, 381577, 513187, 695893, 847557, 951250, 1053192, 1066606, 1200296, 1310466, 1441831,
                    1566453, 1682457, 1825987, 1867755, 1926972, 1957973, 2058091, 2296357, 2381328, 2410764, 2424992,
                    2626050, 2857300, 2876144, 3088520, 3152183, 3180258, 3191332, 3213867, 3217563, 3224419, 3241236,
                    3248378, 3256578, 3265343, 3271271, 3305264]
        actual = list(map(st.find_substring, books))
        self.assertEqual(expected, actual)

    def test_the_new_testament(self):
        text = MiniProject3.read_file('king-james-bible.txt')
        st = SuffixTree(text)

        books = ['The New Testament', 'The Gospel According to Saint Matthew',
                 'The Gospel According to Saint Mark', 'The Gospel According to Saint Luke',
                 'The Gospel According to Saint John', 'The Acts of the Apostles',
                 'The Epistle of Paul the Apostle to the Romans',
                 'The First Epistle of Paul the Apostle to the Corinthians',
                 'The Second Epistle of Paul the Apostle to the Corinthians',
                 'The Epistle of Paul the Apostle to the Galatians',
                 'The Epistle of Paul the Apostle to the Ephesians',
                 'The Epistle of Paul the Apostle to the Philippians',
                 'The Epistle of Paul the Apostle to the Colossians',
                 'The First Epistle of Paul the Apostle to the Thessalonians',
                 'The Second Epistle of Paul the Apostle to the Thessalonians',
                 'The First Epistle of Paul the Apostle to Timothy',
                 'The Second Epistle of Paul the Apostle to Timothy',
                 'The Epistle of Paul the Apostle to Titus', 'The Epistle of Paul the Apostle to Philemon',
                 'The Epistle of Paul the Apostle to the Hebrews', 'The General Epistle of James',
                 'The First General Epistle of Peter', 'The Second General Epistle of Peter',
                 'The First General Epistle of John', 'The Second General Epistle of John',
                 'The Third General Epistle of John', 'The General Epistle of Jude',
                 'The Revelation of Saint John the Devine']
        expected = [3314727, 3314770, 3445153, 3527877, 3668828, 3771564, 3906908, 3959393, 4010670, 4044000, 4060979,
                    4078038, 4090136, 4101350, 4111478, 4117192, 4130456, 4140080, 4145459, 4147941, 4186739, 4199406,
                    4213386, 4222404, 4235678, 4237324, 4239014, 4242683]
        actual = list(map(st.find_substring, books))
        self.assertEqual(expected, actual)

    def test_characters(self):
        text = MiniProject3.read_file('king-james-bible.txt')
        st = SuffixTree(text)

        self.assertTrue(st.has_substring('God'))
        self.assertTrue(st.has_substring('Satan'))
        self.assertTrue(st.has_substring('Moses'))
        self.assertTrue(st.has_substring('Noah'))
        self.assertTrue(st.has_substring('Adam'))
        self.assertTrue(st.has_substring('Eve'))
        self.assertTrue(st.has_substring('Jesus'))
        self.assertTrue(st.has_substring('Mary'))
        self.assertTrue(st.has_substring('Joseph'))
        self.assertTrue(st.has_substring('antichrist'))


if __name__ == '__main__':
    unittest.main()
