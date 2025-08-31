world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'

for year, country in world_champions.items():
    print(f"{year} - {country}")

country_it = 'Италия'
if country_it in world_champions.values():
    print(f"{country_it} становилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country_it} не выигрывала чемпионат мира по футболу в 21 веке.")