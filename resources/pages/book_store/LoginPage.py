from resources.pages.BasePage import BasePage


class LoginPage(BasePage):
    uri = "/login"
    page_heading_text = 'Login'
    user_form = '//form[@id="userForm"]'
    page_subheading1 = f'{user_form}//h2'
    page_subheading1_text = 'Welcome,'
    page_subheading2 = f'{user_form}//h5'
    page_subheading2_text = 'Login in Book Store'
    username_field = '//input[@id="userName"]'
    password_field = '//input[@id="password"]'
    login_button = '//button[@id="login"]'
    new_user_button = '//button[@id="newUser"]'

    def __init__(self):
        super().__init__()
        self.PAGE_URL = f'{super().PAGE_URL}{self.uri}'
        self.happy_elements = super().happy_elements + [self.page_heading, self.page_subheading1, self.page_subheading2,
                                                        self.username_field, self.password_field, self.login_button,
                                                        self.new_user_button]