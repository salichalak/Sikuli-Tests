# Search for a product
type(Key.WIN)
type("chrome shop.demoqa.com/")
type(Key.ENTER)
sleep(3)
click("SearchBox.png")
type("PINK DROP SHOULDER OVERSIZED T SHIRT")
type(Key.ENTER)
assert exists("ProductLabel.png", 10)