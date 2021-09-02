from resources import pages
from robot.libraries.BuiltIn import BuiltIn
import config


def robot_log(message):
    BuiltIn().log(message)


def setup_browser():
    feta = pages.BasePage().selib
    options = ''
    options += 'add_argument("--headless")' if config.headless else ''
    options += '; ' if options and config.maximized else ''
    options += 'add_argument("--start-maximized")' if config.maximized else ''
    options += '; ' if options and config.fixed_size else ''
    options += f'add_argument("--window-size={config.horizontal},{config.vertical}")' if config.fixed_size else ''
    feta.open_browser(browser=config.browser, options=options)
    feta.set_selenium_timeout(config.selenium_timeout)


def open_page(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    page.selib.go_to(page.PAGE_URL)
    page.selib.wait_until_element_is_visible(page.header)
    page.selib.wait_until_element_is_visible(page.ad_banner_close)
    page.click(page.ad_banner_close)
    page.selib.wait_until_element_is_not_visible(page.ad_banner)


def happy_elements_should_be_visible(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    for element in page.happy_elements:
        page.selib.element_should_be_visible(element)


def page_heading_should_be_correct(page_name):
    page = getattr(pages, page_name.replace(' ', ''))()
    heading = True if getattr(page, 'page_heading_text', '') else False
    subheading = True if getattr(page, 'page_subheading_text', '') else False
    subheading1 = True if getattr(page, 'page_subheading1_text', '') else False
    subheading2 = True if getattr(page, 'page_subheading2_text', '') else False
    page.selib.element_text_should_be(page.page_heading, page.page_heading_text) if heading else None
    page.selib.element_text_should_be(page.page_subheading, page.page_subheading_text) if subheading else None
    page.selib.element_text_should_be(page.page_subheading1, page.page_subheading1_text) if subheading1 else None
    page.selib.element_text_should_be(page.page_subheading2, page.page_subheading2_text) if subheading2 else None
