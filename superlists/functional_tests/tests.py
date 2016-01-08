from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
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
        self.browser.get(self.live_server_url)

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
        # When she hits enter, she is taken to a new URL.
        # and now the page lists "Buy peacock feathers"
        # as an item in a to-do list
        edith_list_url= self.browser.current_url
        self.assertRegexpMatches(edith_list_url,'/lists/.+')

        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.keys_for_inputbox('Buy peacock feathers')



        # There is still a text box inviting her to add another item.
        # She enters 'Use peacock feathers to make fly'
        # (Edith is very methodolical)

        self.keys_for_inputbox('Use peacock feathers to make fly')


        # The homepage updates again, and now shows both items on her lists
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table('2. Use peacock feathers to make fly')

        # Now a new user Farncis comes along

        ## We use a new browser session to make sure no information
        ## of Edith's comes along (EG cookies, localStorage)
        self.browser.quit()
        self.browser= webdriver.Firefox()

        # Francis visits the homepage. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text= self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

    def test_layout_and_styling(self):
        # Edith has heard about a coll new online to-do app.
        # She goes to check out its homepage.
        self.browser.set_window_size(1024, 768)
        self.browser.get(self.live_server_url)

        # She notices the inputbox is nicely centered
        inputbox= self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
        inputbox.location['x']+(inputbox.size['width']/2),
        512,
        delta=5
        )

    def check_input_box_is_centered(self):
        inputbox= self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            input.location['x'] + (inputbox.size['width']/2)
            512,
            delta=5
        )

        # Francis starts a new list  by entering a new item
        # He is less interesting than Edith's
        self.keys_for_inputbox('Buy milk')

        # Francis gets his own URL
        francis_list_url= self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        # There is still no trace of Edith's list
        page_text= self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Satisfied they both go back to sleep
