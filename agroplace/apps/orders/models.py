from django.db import models


class Orders(models.Model):
    """ Model of orders. """

    user = models.ForeignKey('users.Users', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def total_cost(self) -> float:
        offerings = ProductsInOrders.objects.filter(order=self)
        total = 0
        for ofrng in offerings:
            total += ofrng.get_total_cost()
        return total


class ProductsInOrders(models.Model):
    """ Model of Products in order. """

    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    qty = models.PositiveIntegerField(default=1)
    cost = models.FloatField()

    def get_total_cost(self) -> float:
        return self.cost*self.qty


class Cart(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    cost = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
