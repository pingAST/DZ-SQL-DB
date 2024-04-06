import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale

DNS = 'postgresql://postgres:XXfeb9i1@localhost:5432/pyDB'
engine = sqlalchemy.create_engine(DNS)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('./tests_data.json', 'r') as file:
    data = json.load(file)

for item in data:
    if item['model'] == 'publisher':
        publisher = Publisher(id=item['pk'], name=item['fields']['name'])
        session.add(publisher)
    elif item['model'] == 'book':
        book = Book(id=item['pk'], title=item['fields']['title'], id_publisher=item['fields']['id_publisher'])
        session.add(book)
    elif item['model'] == 'shop':
        shop = Shop(id=item['pk'], name=item['fields']['name'])
        session.add(shop)
    elif item['model'] == 'stock':
        stock = Stock(id=item['pk'], id_shop=item['fields']['id_shop'], id_book=item['fields']['id_book'],
                      count=item['fields']['count'])
        session.add(stock)
    elif item['model'] == 'sale':
        sale = Sale(id=item['pk'], price=float(item['fields']['price']), date_sale=item['fields']['date_sale'],
                    count=item['fields']['count'], id_stock=item['fields']['id_stock'])
        session.add(sale)

while True:
    publisher_name = input("Введите имя издателя (Для выхода нажмите цифру '1'): ")

    if publisher_name.lower() == '1':
        break

    publisher = session.query(Publisher).filter(Publisher.name == publisher_name).first()

    if publisher:
        # Запрос выборки магазинов, продающих книги целевого издателя
        sales = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).select_from(Book) \
            .join(Stock).join(Shop).join(Sale) \
            .filter(Book.id_publisher == publisher.id).all()

        for sale in sales:
            print(f"{sale[0]} | {sale[1]} | {sale[2]} | {sale[3].strftime('%d-%m-%Y')}")
    else:
        print("Издатель не найден в базе данных.")


session.close()
