from .base import TodoFunctionalTest

class ItemValidationTest(TodoFunctionalTest):
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page, and accidentally tries
        # to submit an empty item
        # She hits 'enter' on the empty item input box
        self.browser.get(self.live_server_url)
        self.enter_a_new_item('')

        # The home page refreshes, and there is am error message
        # saying that list items cannot be blanck
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some test for the item
        # which now works
        self.enter_a_new_item('Buy milk')
        self.check_for_row_in_list_table('1. Buy milk')

        # Perversely tries to enter a second item
        self.enter_a_new_item('')

        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1. Buy milk')
        error=self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling in with some test
        self.enter_a_new_item('Make tea')
        self.check_for_row_in_list_table('1. Buy milk')
        self.check_for_row_in_list_table('2. Make tea')
