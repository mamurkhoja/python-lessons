davlatlar={
    'afg‘oniston':'kobul',
    'banladesh':'dakka',
    'germaniya':'berlin',
    'ukraina':'kiyev',
    'rossiya':'moskva',
    'meksika':'mexiko',
    'braziliya':'brazilia',
    'ekvador':'kito',
    'urugvay':'montevideo'
    }
print("Dunyo davlatlari:")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())
print("\nDavlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())
dav=input('Istalgan davlat nomini kiriting?\n> ')
poyt=davlatlar.get(dav)
if poyt:
    print(f"{dav.title()}ning poytaxti {poyt.title()} shahri.")
else:
    print("Bizda bunday ma'lumot yo‘q")