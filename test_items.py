link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_cart(browser):
    browser.get(link)
    button=browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert button.text=="Añadir al carrito"