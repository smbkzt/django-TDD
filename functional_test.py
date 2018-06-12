from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)

        self.fail("Finish the rest test cases.")

        # She is invited to enter a to-do item straight away
        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the pages updates, and now the page list
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.
        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings="ignore")
