from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    """Special version of Taxi that include fanciness which influence kilometer price"""

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # The base kilometer price depends on all Taxi's kilometer price
        # Base kilometer price multiple by fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return super().__str__() + " plus flagfall of ${:.2f}".format(self.flagfall)

    def get_fare(self):
        # Kilometer price plus flagfall price
        fancy_taxi_fare = super().get_fare() + self.flagfall
        return fancy_taxi_fare
