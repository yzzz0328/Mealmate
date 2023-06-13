from decimal import Decimal
from django.conf import settings
from database.models import foodinfo

class Cart(object):

    def __init__(self, request):
        # Initialize the cart.
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, foodinfo, quantity=1, update_quantity=False):
        # Add a food to the cart or update its quantity.
        foodinfo_id = str(foodinfo.id)
        if foodinfo_id not in self.cart:
            self.cart[foodinfo_id] = {
                                        'quantity': 0,
                                        'calories': str(foodinfo.calories),
                                       }
        if update_quantity:
            self.cart[foodinfo_id]['quantity'] = quantity
        else:
            self.cart[foodinfo_id]['quantity'] += quantity
        self.save()


    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, foodinfo):
        foodinfo_id = str(foodinfo.id)
        if foodinfo_id in self.cart:
            del self.cart[foodinfo_id]
            self.save()

    def __iter__(self):

        # Iterate over the items in the cart and get the foods from the database.

        foodinfo_ids = self.cart.keys()
        # get the foods and add them to the cart
        foods = foodinfo.objects.filter(id__in=foodinfo_ids)
        for food in foods:
            self.cart[str(food.id)]['foodinfo'] = food

        for item in self.cart.values():
            item['calories'] = Decimal(item['calories'])
            item['total_calories'] = item['calories'] * item['quantity']
            yield item

    def __len__(self):
        # Count all items in the cart.
        return sum(item['quantity'] for item in self.cart.values())

    def get_sum_calories(self):
        return sum(Decimal(item['calories']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
