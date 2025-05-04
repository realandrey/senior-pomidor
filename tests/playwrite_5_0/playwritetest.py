from playwright.sync_api import sync_playwright
import time

# Создаем экземпляр Playwright и запускаем его
playwright = sync_playwright().start()

# Далее, используя объект playwright, можно запускать браузер и работать с ним
browser = playwright.chromium.launch(headless=False, slow_mo=1000)
page = browser.new_page()

page.goto('https://www.saucedemo.com/')
page.type(selector='[id="user-name"]', text = 'standard_user', delay = 100)
page.fill(selector='#password', value = 'secret_sauce')
page.click(selector='.submit-button')

page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout= 10000)
page.wait_for_selector('#inventory_container')

button_add_card = '[data-test="add-to-cart-sauce-labs-fleece-jacket"]'
alt_locator_for_card = '.inventory_item a:has-text("Sauce Labs Fleece Jacket")'
card_button = '.inventory_item_description:has-text("Sauce Labs Fleece Jacket") button:has-text("Add to cart")'

page.is_visible(selector=button_add_card)
page.is_enabled(selector=button_add_card)
#page.click(selector=button_add_card)
#page.click(selector=alt_locator_for_card)
page.click(card_button)
page.is_visible('[data-test="shopping-cart-link"]')
page.click('[data-test="shopping-cart-link"]')
page.wait_for_url('https://www.saucedemo.com/cart.html', timeout= 10000)

button_checkout = '#checkout'
page.wait_for_selector(button_checkout)
page.is_visible(button_checkout)
page.is_enabled(button_checkout)
page.click(button_checkout)
page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html')


page.fill(selector='#first-name', value='FirstName')
page.fill(selector='#last-name', value='LastName')
page.fill(selector='#postal-code', value='6795795')

page.click('[id="continue"][type="submit"]')

page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html')
page.wait_for_selector('button:has-text("Finish")')
page.click('[id="finish"]')
page.wait_for_url('https://www.saucedemo.com/checkout-complete.html')

time.sleep(5)

# После выполнения необходимых действий, следует явно закрыть браузер
browser.close()

# И остановить Playwright, чтобы освободить ресурсы
playwright.stop()
