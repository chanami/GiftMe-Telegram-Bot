import settings
from gift_DB import giftList

#['Flowers', 'Balloons', 'Chocolates', 'Surprise Gift']
def initial():
    g = giftList(settings.HOST, settings.DB)
    g.add_gift('Flowers', 20, "https://www.ftdimg.com/pics/products/B41_200x225.jpg")
    g.add_gift('Flowers', 40, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXA7DP8Wx8WPl6hwLkxV0exVSX3LfszysZ49DETvC35vWZQsdfmw")
    g.add_gift('Flowers', 26, "http://www.ofer-flowers.co.il/wp-content/uploads/2013/07/Fotolia_44012051_XS.jpg")
    g.add_gift('Flowers', 92, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq66uJYzhragmtvu0Ix-_2YpXXV18w0K7aTdN3p0WuXR4FNL6A")

    g.add_gift('Balloons', 47, "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")
    g.add_gift('Balloons', 80, "https://cdn.shopify.com/s/files/1/1988/3711/products/Christmas-Layouts-3-F2_1200x.jpg?v=1542889042")
    g.add_gift('Balloons', 47, "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")

    g.add_gift('Chocolates', 26, "https://pieceloveandchocolate.com/wp-content/uploads/2014/08/Gift-Baskets-Sm-Files-14.jpg")
    g.add_gift('Chocolates', 81, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBXLgAMpwVFaqFTtM2_uBCds3H0Jl7--EnQ1YIdAhMXhenO5lZCw")
    g.add_gift('Chocolates', 48, "https://cdn2.harryanddavid.com/wcsstore/HarryAndDavid/images/catalog/18_31816_30J_01ex.jpg?height=378&width=345&quality=70")

    g.add_gift('Surprise Gift', 90, "https://image.freepik.com/free-vector/opened-surprise-gift-box_3446-340.jpg")

initial()

