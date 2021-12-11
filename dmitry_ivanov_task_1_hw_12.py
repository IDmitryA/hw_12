class Cat:
    age = 1

    def __init__(self, breed='Oriental cat', mood='active', causes_allergies='no', meal='milk'):
        self.breed = breed
        self.mood = mood
        self.causes_allergies = causes_allergies
        self.meal = meal

    def __repr__(self) -> str:
        return f"{self.breed} can't be cause allergy"  # and it's really true

    def __call__(self, mood='sleep') -> str:  # return cat conditional
        if mood == 'active':
            return 'cat is playing'
        elif mood == 'hungry':
            return 'cat is eating'
        elif mood == 'gentle':
            return 'cat is purring'
        else:
            return 'cat is sleeping'

    # next function transform cat age to human age:
    # - first cat year = 15 human years
    # - second cat year = +10 human years (2 cat years == 25 human years)
    # - every next cat year == +4 human years

    @classmethod
    def transform_to_human_age(cls, age=1) -> str:
        human_years = 0
        if age == 1:
            human_years = 15
        elif age == 2:
            human_years = 25
        elif age > 2:
            human_years = 25 + (age-2) * 4
        return f"{age} cat's years = {human_years} human years"

    @staticmethod
    def oriental_cat_photo():  # just cute oriental cat photo
        return r'https://ru.wikipedia.org/wiki/%D0%9E%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1' \
               r'%8F_%D0%BA%D0%BE%D1%88%D0%BA%D0%B0#/media/%D0%A4%D0%B0%D0%B9%D0%BB:%D0%9E%D1%80%D0%B8%D0%B5%D0%BD%D1' \
               r'%82%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%BA%D0%BE%D1%88%D0%BA%D0%B0,_%D1%8D%D0%BA%D1%81%D1%82%D1' \
               r'%80%D0%B5%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D1%82%D0%B8%D0%BF.jpg'

    @property
    def cat_food(self) -> str:  # GETTER
        return self.meal

    @cat_food.setter
    def cat_food(self, value) -> str:  # SETTER
        self.meal = value

    @cat_food.deleter
    def cat_food(self) -> str:  # DELETER
        self.meal = 'no meal'


print(Cat())

efim = Cat()
print(efim(mood='active'))
print(efim.transform_to_human_age(8))
print(Cat.oriental_cat_photo())
print(efim.cat_food)  # GETTER
efim.cat_food = 'meat'  # SETTER
print(efim.cat_food)
del efim.cat_food  # DELETER
print(efim.cat_food)


