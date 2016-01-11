from .base import TodoFunctionalTest
from unittest import skip 

class ItemValidationTest(TodoFunctionalTest):
    @skip("Haven't implemented this")
    def test_cannot_add_empty_list_item(self):
        # Edith goes to the home page, and accidentally tries
        # to submit an empty item
        # She hits 'enter' on the empty item input box

        # The home page refreshes, and there is am error message
        # saying that list items cannot be blanck

        # She tries again with some test for the item
        # which now works

        # Perversely tries to enter a second item

        #

        # And she can correct it by filling in with some test
        self.fail('Finish the test')
