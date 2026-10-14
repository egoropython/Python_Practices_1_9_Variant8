class StandardStrategy:
    def calculate(self, membership): return membership.price
class DiscountStrategy:
    def calculate(self, membership): return membership.price * 0.9
class FamilyStrategy:
    def calculate(self, membership): return membership.price * 0.8
