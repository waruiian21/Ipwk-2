import unittest
from app.models import Source, Article


class SourceArticleTest(unittest.TestCase):
    '''
      Test Class to test the behaviour of the Source class
    '''
    def setUp(self):
        '''
         Set up method that will run before every Test
        '''
        self.new_source = Source('abc-news','Abc News','A world class news channel')
        self.new_article = Article('dummy_article','john doe','https://s.image.com','2019-10-12T03:11:28Z',"http://abc.com",'abc-news')


    def test_instance(self):

        print(self.new_source.__class__)
        self.assertTrue(isinstance(self.new_source,Source))

    def test_article_instance(self):
        print(self.new_article.__class__)
        self.assertTrue((isinstance(self.new_article,Article)))

