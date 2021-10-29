from django.core.management.base import BaseCommand, CommandError
from order.models import Product


class Command(BaseCommand):

    help = "shows price of the specified product in database."

    def add_arguments(self, parser):
        parser.add_argument('productName', type=str)

    def handle(self, *args, **kwargs):
        product_name = kwargs['productName']
        try:
            product_price = Product.objects.get(name=product_name).price
        except Product.DoesNotExist:
            self.stdout.write(f"Product with name {product_name} was not found in our database😥")
        else:
            self.stdout.write(f"Product {product_name} costs {product_price}")
