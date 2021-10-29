from django.db import models
from django.db.models.fields.related import OneToOneField
from django.db.models import Count, Subquery, OuterRef
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=255)  


class Follow(models.Model):
    from_user = models.ForeignKey(User, models.CASCADE, related_name='following')
    to_user = models.ForeignKey(User, models.CASCADE, related_name='followers')

# users = User.objects.all()
# follow = Follow.objects.filter(from_user=OuterRef('pk'))
# follow = follow.values(sum=Count('*')).order_by()
# follow.query.group_by = []
#
# users = users.annotate(follow_count=Subquery(follow[:1]))
#
# # result = [{
#     'id': 1,
#     'name': 'bob',
#     'follower_count': 12
# }]
#
#
# result = [
#     {
#         'name':'Apple',
#         'total_count':18,
#         'total_price':150000,
#         'date':'2021-10-22'
#     },
#     {
#         'name': 'Cherry',
#         'total_count':15,
#         'total_price':130000,
#         'date':'2021-10-21'
#     },
#     {
#
#         'name':'Banana',
#         'total_count':11,
#         'total_price':10000,
#         'date':'2021-10-22'
#     }
# ]
