import json
from random import uniform

from utils import db

europe_codes = [
    "AT", "BE", "BG", "HU", "DE", "GI", "GR", "GE", "DK", "JE", "IS", "ES", "IE", "IT", "CY", "LV", "LT", "LI", "LU",
    "MT", "NL", "NO", "PT", "RU", "RO", "RS", "SI", "GB", "TR", "UA", "FI", "FR", "HR", "ME", "CZ", "SE", "CH", "EE"
]

asia_codes = ["AU", "VN", "ID", "KH", "CN", "LA", "MO", "MY", "SG", "TW", "TH", "KR", "JP"]

latin_codes = ["AR", "BO", "BR", "VE", "HN", "GT", "CO", "CR", "MX", "NI", "PA", "PY", "PE", "SV", "UY", "CL", "EC"]

middle_east_codes = ["BH", "CY", "EG", "IQ", "IL", "JO", "KW", "LB", "OM", "PS", "QA", "SA", "TR", "AE", "YE"]

supported_countries = list(set(europe_codes + asia_codes + latin_codes + middle_east_codes))

all_countries = json.load(open('app/assets/country-list.json'))

def generate_plan_default(name, regions, gb_limit, days, price):
	return {
	    "technical_name": name,
	    "regions": regions,
	    "duration": 60 * 60 * 24 * days,
	    "bytes": 1024**3 * gb_limit,
	    "price_x100": int(price * 100),
	    "is_active": True
	}

def generate_single_country_plans():
	plans = []
	for country in all_countries:
		if country['code'] not in supported_countries:
			continue

		def prices():
			return [round(uniform(x / 1.5, x * 1.2), ndigits=2) for x in [5, 15, 35]]

		name = country['name'].lower().replace(' ', '_')
		plans.append(generate_plan_default(f"{name}_1gb_7d", [country['code']], 1, 7, prices()[0]))
		plans.append(generate_plan_default(f"{name}_3gb_14d", [country['code']], 3, 14, prices()[1]))
		plans.append(generate_plan_default(f"{name}_6gb_30d", [country['code']], 6, 30, prices()[2]))

	return plans

all_plans = ([
    generate_plan_default("all_europe_1gb_7d", europe_codes, 1, 7, 4.66),
    generate_plan_default("all_europe_3gb_10d", europe_codes, 3, 10, 10.81),
    generate_plan_default("all_europe_5gb_15d", europe_codes, 5, 15, 16.98),
    generate_plan_default("all_asia_1gb_7d", asia_codes, 1, 7, 9.09),
    generate_plan_default("all_asia_3gb_30d", asia_codes, 3, 30, 22.50),
    generate_plan_default("all_asia_5gb_30d", asia_codes, 5, 30, 32.76),
    generate_plan_default("all_latin1_1gb_7d", latin_codes, 1, 7, 15.58),
    generate_plan_default("all_latin1_3gb_10d", latin_codes, 3, 10, 43.66), *generate_single_country_plans()
])  #pyright: ignore

db.plan.create_many(all_plans)
