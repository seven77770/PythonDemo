from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import unittest

class NewVisitorTest(unittest.TestCase):
	"""docstring for NewVisitorTest"""
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')

		self.assertIn('To-Do',self.browser.title)
		#找到h1元素，判断其包含‘To-Do’字符串
		header_text = self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('To-Do',header_text)

		#找到id = id_new_item 元素，是个输入框
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			#判断输入框的placeholder内容
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)


		inputbox.send_keys('Buy peacock feathers')

		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1:Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
		)

		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')

		

