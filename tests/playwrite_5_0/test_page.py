from playwright.sync_api import expect

def test_exactly_one_email_and_password_field(page):
    page.goto("https://demo.opencart.com/index.php?route=account/login")

    email_address_locator = page.get_by_label("E-Mail Address", exact=True)
    password_locator = page.get_by_label("Password", exact=True)

    expect(email_address_locator).to_have_count(1)
    expect(password_locator).to_have_count(1)

