from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Car, Category

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_hire.db'
db = SQLAlchemy(app)

def seed_database():
    # Create categories
    sedan = Category(name='Sedan')
    suv = Category(name='SUV')
    truck = Category(name='Truck')

    db.session.add_all([sedan, suv, truck])
    db.session.commit()


    cars = [
        {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'price': 6000.00, 'category_id': sedan.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhtBPG37ndC9bHiGGRaj_h4JgOEj99wR9jQuzk7moy2A&s'},
        {'make': 'Honda', 'model': 'CR-V', 'year': 2019, 'price': 7000.00, 'category_id': suv.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUoD7tuai-N2rHjajm8mA2pTkXviNqdN679AP-_VglGA&s'},
        {'make': 'Ford', 'model': 'F-150', 'year': 2021, 'price': 8000.00, 'category_id': truck.id, 'photo_url': 'https://cars.usnews.com/pics/size/390x290/images/Auto/izmo/i159614477/2021_ford_f_150_angularfront.jpg'},
        {'make': 'Mercedes-Benz', 'model': 'E-Class', 'year': 2020, 'price': 8500.00, 'category_id': sedan.id, 'photo_url': 'https://imgd.aeplcdn.com/370x208/n/cw/ec/47336/e-class-exterior-right-front-three-quarter-27.jpeg?isig=0&q=80'},
        {'make': 'Jeep', 'model': 'Wrangler', 'year': 2018, 'price': 9500.00, 'category_id': suv.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoMeGP4OwQgkYqZW4hfEdUXt84emXzg2_Fj0QgBe7dLA&s'},
        {'make': 'Toyota', 'model': 'Tacoma', 'year': 2019, 'price': 7500.00, 'category_id': truck.id, 'photo_url': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/1da06c3a-d350-48e0-80d5-ce4ed87dc2c8/640e6f66-775c-4779-a565-eb922b215002.png'},
        {'make': 'BMW', 'model': '3 Series', 'year': 2019, 'price': 7800.00, 'category_id': sedan.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPO7zUH03e6Agn_mdR3xQS2mAMJxhh_nUvcWwqu9jKgQ&s'},
        {'make': 'Audi', 'model': 'Q5', 'year': 2020, 'price': 8200.00, 'category_id': suv.id, 'photo_url': 'https://s1.cdn.autoevolution.com/images/models/AUDI_Q5-2020_main.jpg'},
        {'make': 'Chevrolet', 'model': 'Silverado', 'year': 2020, 'price': 8800.00, 'category_id': truck.id, 'photo_url': 'https://platform.cstatic-images.com/xlarge/in/v2/stock_photos/406c2669-2ca9-4db7-9821-1a561504e44c/a1c7ae74-6d51-4f87-856e-f1527ccec20e.png'},
        {'make': 'Lexus', 'model': 'RX', 'year': 2021, 'price': 8900.00, 'category_id': suv.id, 'photo_url': 'https://cars.usnews.com/pics/size/390x290/images/Auto/izmo/i159614467/2021_lexus_rx_angularfront.jpg'},
        {'make': 'Nissan', 'model': 'Altima', 'year': 2019, 'price': 6900.00, 'category_id': sedan.id, 'photo_url': 'https://www-europe.nissan-cdn.net/content/dam/Nissan/nissan_middle_east/experience_nissan/latestnews/February2019/Image%201.jpg.ximg.l_12_m.smart.jpg'},
        {'make': 'GMC', 'model': 'Sierra', 'year': 2020, 'price': 8200.00, 'category_id': truck.id, 'photo_url': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.cars.com%2Fresearch%2Fgmc-sierra_1500-2020%2F&psig=AOvVaw17S5Jx6XOCx4WrsPJh9ZDM&ust=1707981308148000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCNjntKukqoQDFQAAAAAdAAAAABAQ'},
        {'make': 'Toyota', 'model': 'Corolla', 'year': 2018, 'price': 5500.00, 'category_id': sedan.id, 'photo_url': 'https://global.toyota/pages/news/images/2018/11/29/1400/20181129_03_album_images.jpg'},
        {'make': 'Subaru', 'model': 'Outback', 'year': 2019, 'price': 6700.00, 'category_id': suv.id, 'photo_url': 'https://s7d1.scene7.com/is/image/scom/RDB_default_pass_scaled?$900p$'},
        {'make': 'Ram', 'model': '1500', 'year': 2020, 'price': 8300.00, 'category_id': truck.id, 'photo_url': 'https://ymimg1.b8cdn.com/uploads/car_model/8419/pictures/9007333/2019_RAM_1500.png'},
        {'make': 'Volvo', 'model': 'S60', 'year': 2020, 'price': 8000.00, 'category_id': sedan.id, 'photo_url': 'https://media.istockphoto.com/id/1348897749/photo/volvo-s60.jpg?s=612x612&w=0&k=20&c=Bzaw9zmzFTVaoijaO0NVZ5GMphC359zbmPEsHjn9wL4='},
        {'make': 'Honda', 'model': 'Accord', 'year': 2019, 'price': 6700.00, 'category_id': sedan.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf72u85UMP4F4geoRpC4PERe4xz6Sd7KtikYlE8cTzAA&s'},
        {'make': 'Kia', 'model': 'Sorento', 'year': 2019, 'price': 7400.00, 'category_id': suv.id, 'photo_url': 'https://inv.assets.ansira.net/1/8/5/32856549581.jpg'},
        {'make': 'Toyota', 'model': 'Tundra', 'year': 2020, 'price': 9900.00, 'category_id': truck.id, 'photo_url': 'https://cars.usnews.com/static/images/Auto/custom/15105/2023_Toyota_Tundra_Angular_Front_1.jpg'},
        {'make': 'Audi', 'model': 'A4', 'year': 2019, 'price': 7600.00, 'category_id': sedan.id, 'photo_url': 'https://cars.usnews.com/static/images/Auto/izmo/i159614025/2020_audi_a4_sedan_angularfront.jpg'},
        {'make': 'Ford', 'model': 'Escape', 'year': 2020, 'price': 7800.00, 'category_id': suv.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_BJYoAXOSx5CPw2kU2G1yPEAbA-QFVVf6v1Z3sQ7_JA&s'},
        {'make': 'Jeep', 'model': 'Cherokee', 'year': 2018, 'price': 8300.00, 'category_id': suv.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5-CxX4TPRA_srbLlMML9bbjXNExYpXD4_5l1O12LTow&s'},
        {'make': 'Ram', 'model': '3500', 'year': 2021, 'price': 9800.00, 'category_id': truck.id, 'photo_url': 'https://www.shutterstock.com/image-photo/2021-ram-3500-limited-longhorn-260nw-2142148143.jpg'},
        {'make': 'Volvo', 'model': 'XC60', 'year': 2019, 'price': 8600.00, 'category_id': suv.id, 'photo_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGvMSQa0x9GaC6kUxhA1D7uGH6g4zefcv7-n4LU9U-VRHYtASDHWrxUqjMcQ&s'},
        {'make': 'GMC', 'model': 'Acadia', 'year': 2020, 'price': 9100.00, 'category_id': suv.id, 'photo_url': 'https://www.motortrend.com/uploads/sites/10/2019/09/2020-gmc-acadia-at4-4wd-suv-angular-front.png'}
    ]

    for car_data in cars:
        car = Car(**car_data)
        db.session.add(car)
    
    db.session.commit()

if __name__ == '__main__':
    seed_database()
