class Customer:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    

    # first_name property
    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, first_name):
        if isinstance(first_name, str) and 1 <= len(first_name) <= 25:
            self._first_name = first_name    
    first_name = property(get_first_name, set_first_name)



    # last_name property
    def get_last_name(self):
        return self._last_name
    def set_last_name(self, last_name):
        if isinstance(last_name, str) and 1 <= len(last_name) <= 25:
            self._last_name = last_name    

    last_name = property(get_last_name, set_last_name)


    def reviews(self):
        return [review for review in Review.all if review.customer == self]
    

    def restaurants(self):
        return list(set([review.restaurant for review in self.reviews()]))

    def num_negative_reviews(self):
        return sum(1 for review in self.reviews() if review.rating <= 2)
    

    def has_reviewed_restaurant(self, restaurant):
        for review in self.reviews():
            if review.restaurant == restaurant:
                return True
        return False
    







class Restaurant:
    def __init__(self, name):
        self.name = name
    
    # Restaurant name property
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name    
        
    name = property(get_name, set_name)


    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if ratings:
            return round( sum(ratings) / len(ratings), 1)
        else:
            return 0.0

    @classmethod
    def top_two_restaurants(cls):
        # Find all restaurants with reviews
        # sort them using average_star rating
        # return the first two
        # Returns none if there are no reviews for that restaurant
        def top_two_restaurants(cls):
            sorted_restaurants = sorted(cls.all, key=lambda x: x.average_star_rating(), reverse=True)
            return sorted_restaurants[:2] if sorted_restaurants else []
    
    

class Review:
    all = []
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all.append(self)
    
    # Review property rating
    def get_rating(self):
        return self._rating

    def set_rating(self, val):
        if isinstance(val, int) and 1 <= val <= 5 and not hasattr(self, '_rating'):
            self._rating = val      
    
    rating = property(get_rating, set_rating)

    
    def get_customer(self):
         return self._customer
    
    def set_customer(self, value):
         if isinstance(value, Customer):
             self._customer = value

    customer = property(get_customer, set_customer)




    def get_restaurant(self):
         return self._restaurant
    
    def set_restaurant(self, value):
         if isinstance(value, Restaurant):
             self._restaurant = value
         
    restaurant = property(get_restaurant, set_restaurant)

   