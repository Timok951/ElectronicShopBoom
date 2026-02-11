from django.conf import settings
from decimal import Decimal
from shop.models import Good

class Cart(object):
    def __init__(self, request):
        #initializing cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, good, amount=1, override_quantity=False):
        good_id = str(good["id"])
        if good_id not in self.cart:
            self.cart[good_id] = {'amount': 0,
                                     'price_at_purchase': str(good["price"])
                                     }
        if override_quantity:
            self.cart[good_id]['amount'] = amount
        else:
            self.cart[good_id]['amount'] += amount
        self.save()
    
    def remove(self,good):
        good_id = set(good["id"])
        
        if good_id in self.cart:
            del self.cart[good_id]
        self.save()
    
    def __iter__(self):
        #Loop throught cart items and fetch the products from the database
        good_ids = self.cart.keys()
        # get the product objects and add them to the cart
        goods = Good.objects.filter(id__in=good_ids)
        cart = self.cart.copy()
        for good in goods:
            cart[str(good.id)]['good'] = good
        for item in cart.values():
            item['price_at_purchase'] = Decimal(item['price'])
            yield item 
            
    def __len__(self):
        return sum(item['amount'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values)
    
    def clear(self):
        #revove cart form session
        del self.session[settings.CART_SESSION_ID]
        self.save()