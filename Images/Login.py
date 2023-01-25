# Log in with valid user
type(Key.WIN)
type("chrome --incognito shop.demoqa.com/my-account/")
type(Key.ENTER)
sleep(10)
click("MyAccountLabel.png")
type(Key.DOWN * 15)
sleep(3)
click("Username.png")
type("salichalak")
find("Login.png").nearby().click("Password.png");
type("TestPassword1234@")
click("Login.png")-