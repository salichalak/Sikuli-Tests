# Purchase a product
type(Key.WIN)
type("chrome --incognito shop.demoqa.com/")
type(Key.ENTER)
sleep(5)
click("searchButton.png")
type("PINK DROP SHOULDER OVERSIZED T SHIRT")
type(Key.ENTER)
sleep(5)

click("ProductTitle.png")
type(Key.DOWN * 15)
sleep(3)
find("Color.png").right().click("ChooseColor.png")
click("ColorToSelect.png")
sleep(3)
find("FavouriteButton.png").nearby(100).click("ChooseSize.png")
click("1674597484959.png")
sleep(5)
click("AddToCartButton.png")
assert exists("SuccessfullyAddedToCartMessage.png", 10) 
click("MyCartButton.png")
sleep(3)
click("1674675918372.png")
type(Key.PAGE_DOWN)
click("CheckoutButton.png")
click("CheckoutButton2.png")
type(Key.PAGE_DOWN)
click("FirstName.png")
type("Sali")
click("LastName.png")
type("Chalak")
click("CompanyName.png")
type("Progress Telerik")
click("StreetAddress.png")
type("Sofia Tsarigradsko Shose 54B")
type(Key.PAGE_DOWN)
click("City.png")
type("Sofia")
click("PinCode.png")
type("1000")
click("Phone.png")
type("12345678990")
click("Email.png")
type("sali.chalak@gmail.com")
click("TermsAndConditions.png")
click("PlaceOrderButton.png")
click("CheckoutButton2.png")
type(Key.DOWN * 5)
assert exist("OrderReceivedMessage.png", 10)