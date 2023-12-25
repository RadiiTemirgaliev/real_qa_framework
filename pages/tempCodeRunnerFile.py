  def click_random_checkbox(self):
        item_list = self.element_are_visible(self.locators.ITEM_LIST)
        for item in item_list:
            self.go_to_element(item)
            print(item.text)