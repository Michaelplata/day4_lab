def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, snack):
    likes_snack = True
    for i in person["favourites"]["snacks"]: 
        if i == snack:
            likes_snack = True
        else: 
            likes_snack = False
    return likes_snack
    
def add_friend(person, new_friend):
    return person["friends"].append("Scrappy-Doo")

    




