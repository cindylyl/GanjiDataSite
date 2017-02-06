from django.db import models
from mongoengine import *
from mongoengine import connect
connect('ganji', host='127.0.0.1', port=27017)
# Create your models here.


class Info(Document):
    title = StringField()
    pub_date = StringField()
    area = StringField()
    cates = StringField()
    look = StringField()
    url = StringField()
    price = FloatField()
    meta = {
        'collection': 'gj'
    }

# for i in Info.objects:
#     print(i.title,i.date,i.place,i.type,i.extent)

# pipeline = [
#     {'$match': {'$and': [{'pub_date': {'$gte': '2015.12.25', '$lte': '2015.12.27'}}, {'area': '海淀'}]}},
#     {'$group': {'_id': '$cates', 'counts': {'$sum': 1}}},
#     {'$sort': {'counts': -1}},
#     {'$limit': 3}
# ]
#
# for i in Info._get_collection().aggregate(pipeline):
#     data = {
#         'name': i['_id'],
#         'data': [i['counts']],
#         'type': 'column'
#     }
#     print(data)