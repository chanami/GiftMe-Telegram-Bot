import settings
from gift_DB import giftList

def initial():
    g = giftList(settings.HOST, settings.DB)
    g.add_gift('Flowers', 20, "http://media4.1800flowers.com/800f_assets/images/flowers/images/shop/catalog/91798Lz.jpg")
    g.add_gift('Flowers', 44, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbJWDvvyoi7hDmMySuvylQqqVbqSTHG0yPECZM4a-ZRZZ0m5sn")
    g.add_gift('Flowers', 26, "http://www.ofer-flowers.co.il/wp-content/uploads/2013/07/Fotolia_44012051_XS.jpg")
    g.add_gift('Flowers', 58, "https://www.ftdimg.com/pics/products/zoom/B4-4785D_600x600.jpg")
    g.add_gift('Flowers', 92, "https://www.ftdimg.com/pics/products/zoom/B4-4785D_600x600.jpg")
    g.add_gift('Flowers', 77, "https://www.ftdimg.com/pics/products/B35_200x225.jpg")
    g.add_gift('Flowers', 86, 'http://green-flower.ru/wa-data/public/shop/products/91/01/191/images/1152/1152.750.jpg')
    g.add_gift('Flowers', 65, "http://green-icon.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/l/r/lr-023.jpg")

    g.add_gift('Balloons', 45, "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")
    g.add_gift('Balloons', 81, "https://cdn.shopify.com/s/files/1/1988/3711/products/Christmas-Layouts-3-F2_1200x.jpg?v=1542889042")
    g.add_gift('Balloons', 47, "https://www.balloonmonkey.co.uk/newimg/cache/5846/4.png")

    g.add_gift('Balloons', 90, "https://www.balloonplanet.com/shop/images/products/product_9316_medium.jpg")
    g.add_gift('Balloons', 28, "https://bridgewaterfloristma.net/wp-content/uploads/2018/08/IDS-B19.jpg")
    g.add_gift('Balloons', 35, "https://www.bigw.com.au/medias/sys_master/images/images/h2c/h76/12154851491870.jpg")
    g.add_gift('Balloons', 62, "https://www.b-loony.co.uk/media/catalog/product/cache/1/image/650x/2d2af058176195dd86a5ae630658753a/i/m/image_265.jpg")
    g.add_gift('Balloons', 75, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPisSI1jHgkbloQg2zZtQ0uJzhCRi0exfjQTsS8lprMbZxvNOQKw")

    g.add_gift('Chocolates', 26, "https://pieceloveandchocolate.com/wp-content/uploads/2014/08/Gift-Baskets-Sm-Files-14.jpg")
    g.add_gift('Chocolates', 81, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBXLgAMpwVFaqFTtM2_uBCds3H0Jl7--EnQ1YIdAhMXhenO5lZCw")
    g.add_gift('Chocolates', 48, "https://cdn2.harryanddavid.com/wcsstore/HarryAndDavid/images/catalog/18_31816_30J_01ex.jpg?height=378&width=345&quality=70")

    g.add_gift('Chocolates', 38, "https://target.scene7.com/is/image/Target/GUEST_a8405d85-47dd-4c69-b79e-684410625106?wid=488&hei=488&fmt=pjpeg")
    g.add_gift('Chocolates', 94, "https://www.giftmandu.com/images/product/P/chocolate-basket01%3Ds.jpg")
    g.add_gift('Chocolates', 77, "https://i9.fnp.com/images/pr/l/loaded-with-chocolates_1.jpg")

    g.add_gift('Surprise Gift', 90, "https://image.freepik.com/free-vector/opened-surprise-gift-box_3446-340.jpg")
    g.add_gift('Surprise Gift', 78, "https://images-na.ssl-images-amazon.com/images/I/61ZcDIo9U0L._SY355_.jpg")
    g.add_gift('Surprise Gift', 47, "https://resources.ediblearrangements.com/Resources/en-us/i/a/12c_Birthday_Surprise_Gift_Set_17_E261_wrev.jpg")
    g.add_gift('Surprise Gift', 30, "https://us.123rf.com/450wm/foodandmore/foodandmore1210/foodandmore121000022/15847543-christmas-surprise-gift-with-blank-tag-and-a-decorative-red-ribbon-and-bow-on-a-white-studio-backgro.jpg?ver=6")


initial()

