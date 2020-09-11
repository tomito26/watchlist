import unittest
from app.models import Review

class TestReview(unittest.TestCase):
    
    def  setUp(self):
        self.new_review = Review('1235','Review for movies','https://image.tmd.org/t/p/w500/hjejhggsf' 'This the best movie so far')
        
    def tearDown(self):
        Review.clear_views()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Review))
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,1235)
        self.assertEquals(self.new_review.title,'Review for movies')
        self.assertEquals(self.new_review.imageurl,'https://image.tmdeb.org/n/g/w500/webhbcc')

    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.all_reviews)>0)

    def test_get_review_by_id(self):
        
        self.new_review.save_review()
        got_reviews = Review.get_reviews(1235)
        self.assertTrue(len(got_reviews)== 1)