class LTLocator(object):

    # Locators for HomePage
    login_link = "//a[normalize-space()='Login']"
    signup_link = "//a[contains(text(), 'Sign Up')]"
    logo = "//a[@href='https://www.lambdatest.com/']/img"

    # Locators for LoginPage
    email_field = "//input[@id='email']"
    password_field = "//input[@id='password']"
    login_button = "//button[@id='login-button']"
