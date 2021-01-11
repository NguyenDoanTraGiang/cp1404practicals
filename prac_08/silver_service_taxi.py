from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Special version of Taxi that include fanciness which influence kilometer price"""
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # The base kilometer price depends on all Taxi's kilometer price
        # Base kilometer price multiple by fanciness
        self.price_per_km = Taxi.price_per_km * fanciness



