from django.core.management.base import BaseCommand, CommandError
from order.models import Product


class Command(BaseCommand):
    help = "Creates product with the given information like productName productPrice"

    def add_arguments(self, parser):
        parser.add_argument('productName', nargs="+", type=str)

    def handle(self, *args, **kwargs):
        product_name = kwargs['productName'][0]
        Product.objects.create(name=product_name, price=1500)
        self.stdout.write("Product successfully created, cheers,👍👍👍")
