from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


    def keys_for_inputbox(self,check_text):
        inputbox= self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(check_text)
        inputbox.send_keys(Keys.ENTER)


    def check_for_row_in_list_table(self, row_text):
        table= self.browser.find_element_by_id('id_list_table')
        rows= table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a coll new online to-do app.
        # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text= self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        # She is invited to enter a to-do item straight away
        inputbox= self.browser.find_element_by_id('id_new_item')
        # place holder
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do lists
        self.keys_for_inputbox('Buy peacock feathers')

        self.check_for_row_in_list_table('1. Buy peacock feathers')

        # There is still a text box inviting her to add another item.
        # She enters 'Use peacock feathers to make fly'
        # (Edith is very methodolical)

        self.keys_for_inputbox('Use peacock feathers to make fly')


        # The homepage updates again, and now shows both items on her lists
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make fly')


        # Edith wonders whether the site will remember her list. Then she sees
        # That the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.
        self.fail('Finish the app!')

if __name__ == '__main__':
    unittest.main()
