class Car:
    
    def __init__(self, id, model):
        self.id = id
        self.model = model
        self.tyres = 4
        self.followers = 0
        self.following = 0
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

gadi = Car(1, 'Lamborgini')
gadi2 = Car(1, 'Lamborgini')
print(gadi.id, gadi.model, gadi.tyres) 

gadi.follow(gadi2)
print(gadi.followers)
print(gadi.following)
print(gadi2.followers)
print(gadi2.following)