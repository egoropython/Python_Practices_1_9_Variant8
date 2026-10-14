class StandardPricing:
    def calculate(self, kind, months):
        prices={"разовый":500,"месячный":2500,"годовой":24000}
        if kind not in prices: raise ValueError("Неизвестный тип абонемента.")
        return prices[kind] if kind != "годовой" else prices[kind]
class DiscountPricing:
    def calculate(self, kind, months):
        return StandardPricing().calculate(kind, months) * 0.9
class FamilyPricing:
    def calculate(self, kind, months):
        return StandardPricing().calculate(kind, months) * 0.8
