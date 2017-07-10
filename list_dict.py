

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
languages = ["HTML","CSS","JavaScript","Python","Ruby"]
drink = ["kool-aid"]
foods = ["steak","potato","cheese"]

def make_dict(arr1, arr2):

    dictionary = dict(zip(arr1, arr2))
    new_dice = dict(zip(arr2, arr1))
    i = len(arr1)
    x = len(arr2)

    if i >= x:
        print dictionary

    else:
        print new_dice

make_dict(languages,favorite_animal)  #should output favorite_animal then languages

make_dict(favorite_animal,languages)  #should output the same as above

make_dict(name,favorite_animal)  #should output name then favorite_animal

make_dict(favorite_animal,name)  #should output favorite_animal then name

make_dict(drink,foods)  #should output foods then drink

make_dict(foods,drink)  #should output same as above
