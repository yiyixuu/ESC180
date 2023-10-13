import gamify
import unittest

class TestBasicCases(unittest.TestCase):

    def setUp(self):
        gamify.initialize()
    
    def test_function_names(self):
        gamify.get_cur_hedons()
        gamify.get_cur_health()
        gamify.offer_star("running")
        gamify.perform_activity("running", 10)
        gamify.star_can_be_taken("running")
        gamify.most_fun_activity_minute()
 
	
    
    def test1(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.get_cur_health(), 90)
    
    def test2(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.get_cur_hedons(), -20)

    def test3(self):
        gamify.perform_activity("running", 30)
        self.assertEqual(gamify.most_fun_activity_minute(),"resting")

    def test4(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        self.assertEqual(gamify.most_fun_activity_minute(),"running")
    
    def test5(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        self.assertEqual(gamify.get_cur_health(), 150)

    
    def test6(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        self.assertEqual(gamify.get_cur_hedons(), -80)        
    
    def test7(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        self.assertEqual(gamify.get_cur_health(), 210)

    def test8(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        self.assertEqual(gamify.get_cur_hedons(), -90)

    def test9(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        gamify.perform_activity("running", 170)
        self.assertEqual(gamify.get_cur_health(), 700)

    def test10(self):
        gamify.perform_activity("running", 30)
        gamify.perform_activity("resting", 30)
        gamify.offer_star("running")
        gamify.perform_activity("textbooks", 30)
        gamify.offer_star("running")
        gamify.perform_activity("running", 20)
        gamify.perform_activity("running", 170)
        self.assertEqual(gamify.get_cur_hedons(), -430)
    
if __name__ == '__main__':
    unittest.main()
