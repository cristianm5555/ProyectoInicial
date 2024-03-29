from pages.BasePage import BasePage

class HomePage(BasePage):
    SEARCH_CONTAINER = 'searchInput'
    SEARCH_BUTTON = 'searchButton'
    CREATE_ACCOUNT = 'pt-createaccount'
    LOGIN = 'pt-login'

    def set_search_query(self, query: str):
        self._driver.find_element_by_id(HomePage.SEARCH_CONTAINER).send_keys(query)

    def check_search(self):
        return self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).is_displayed()

    def search(self):
        self._driver.find_element_by_id(HomePage.SEARCH_BUTTON).click()

    def check_login(self):
        return self._driver.find_element_by_id(HomePage.LOGIN).is_displayed()

    def login(self):
        self._driver.find_element_by_id(HomePage.LOGIN).click()

    def check_create_account(self):
        return self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).is_displayed()

    def create_account(self):
        self._driver.find_element_by_id(HomePage.CREATE_ACCOUNT).click()