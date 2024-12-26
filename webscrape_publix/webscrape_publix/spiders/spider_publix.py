import scrapy
import requests
import csv
import json
import time


class SpiderPublixSpider(scrapy.Spider):
    name = "spider_publix"
    allowed_domains = ["www.publix.com"]
    start_urls = ["https://www.publix.com/locations"]
    
   # List of cities in North Carolina with their latitude and longitude
    cities = [
                {"city": "Charlotte", "lat": 35.2271, "lng": -80.8431},
        {"city": "Raleigh", "lat": 35.7796, "lng": -78.6382},
        {"city": "Greensboro", "lat": 36.0726, "lng": -79.7910},
        {"city": "Durham", "lat": 35.9940, "lng": -78.8986},
        {"city": "Winston-Salem", "lat": 36.0999, "lng": -80.2442},
        {"city": "Fayetteville", "lat": 35.0527, "lng": -78.8784},
        {"city": "Cary", "lat": 35.7915, "lng": -78.7812},
        {"city": "High Point", "lat": 35.9557, "lng": -80.0048},
        {"city": "Greenville", "lat": 35.6120, "lng": -77.3664},
        {"city": "Gastonia", "lat": 35.2620, "lng": -81.1873},
        {"city": "Chapel Hill", "lat": 35.9049, "lng": -79.0450},
        {"city": "Rocky Mount", "lat": 35.9383, "lng": -77.7900},
        {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
        {"city": "Huntersville", "lat": 35.4106, "lng": -80.8423},
        {"city": "Indian Trail", "lat": 35.0982, "lng": -80.6207},
        {"city": "Mooresville", "lat": 35.5849, "lng": -80.8100},
        {"city": "Jacksonville", "lat": 34.7455, "lng": -77.4305},
        {"city": "Apex", "lat": 35.7312, "lng": -78.8503},
        {"city": "Goldsboro", "lat": 35.3855, "lng": -77.9980},
        {"city": "Asheville", "lat": 35.5951, "lng": -82.5515},
        {"city": "Concord", "lat": 35.4087, "lng": -80.5795},
        {"city": "Shelby", "lat": 35.2904, "lng": -81.5347},
        {"city": "Statesville", "lat": 35.7823, "lng": -80.8893},
        {"city": "Wilson", "lat": 35.7213, "lng": -77.9154},
        {"city": "Lumberton", "lat": 34.6251, "lng": -78.9993},
        {"city": "Hickory", "lat": 35.7345, "lng": -81.3412},
        {"city": "New Bern", "lat": 35.1085, "lng": -77.0441},
        {"city": "Pinehurst", "lat": 35.1940, "lng": -79.3920},
        {"city": "Wilmington", "lat": 34.2257, "lng": -77.9447},
        {"city": "Brevard", "lat": 35.2345, "lng": -82.7332},
        {"city": "Lexington", "lat": 35.8259, "lng": -80.2538},
        {"city": "Kinston", "lat": 35.2621, "lng": -77.5861},
        {"city": "Albemarle", "lat": 35.3503, "lng": -80.2006},
        {"city": "Asheboro", "lat": 35.7079, "lng": -79.8136},
        {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
        {"city": "Carrboro", "lat": 35.9101, "lng": -79.0753},
        {"city": "Clayton", "lat": 35.6507, "lng": -78.4564},
        {"city": "Elizabeth City", "lat": 36.2946, "lng": -76.2510},
        {"city": "Garner", "lat": 35.7113, "lng": -78.6142},
        {"city": "Havelock", "lat": 34.8791, "lng": -76.9013},
        {"city": "Henderson", "lat": 36.3296, "lng": -78.3992},
        {"city": "Holly Springs", "lat": 35.6513, "lng": -78.8336},
        {"city": "Hope Mills", "lat": 34.9704, "lng": -78.9453},
        {"city": "Kannapolis", "lat": 35.4874, "lng": -80.6217},
        {"city": "Kernersville", "lat": 36.1199, "lng": -80.0737},
        {"city": "Laurinburg", "lat": 34.7740, "lng": -79.4628},
        {"city": "Lenoir", "lat": 35.9140, "lng": -81.5380},
        {"city": "Lillington", "lat": 35.3993, "lng": -78.8153},
        {"city": "Lincolnton", "lat": 35.4732, "lng": -81.2543},
        {"city": "Lumberton", "lat": 34.6182, "lng": -79.0086},
        {"city": "Matthews", "lat": 35.1168, "lng": -80.7237},
        {"city": "Monroe", "lat": 34.9854, "lng": -80.5495},
        {"city": "Morganton", "lat": 35.7454, "lng": -81.6848},
        {"city": "Mount Airy", "lat": 36.4993, "lng": -80.6073},
        {"city": "Mount Holly", "lat": 35.2987, "lng": -81.0151},
        {"city": "Murraysville", "lat": 34.2991, "lng": -77.8283},
        {"city": "Nashville", "lat": 35.9743, "lng": -77.9653},
        {"city": "Oak Island", "lat": 33.9200, "lng": -78.1500},
        {"city": "Oxford", "lat": 36.3102, "lng": -78.5906},
        {"city": "Reidsville", "lat": 36.3543, "lng": -79.6645},
        {"city": "Roanoke Rapids", "lat": 36.4615, "lng": -77.6544},
        {"city": "Salisbury", "lat": 35.6709, "lng": -80.4742},
        {"city": "Sanford", "lat": 35.4799, "lng": -79.1803},
        {"city": "Selma", "lat": 35.5360, "lng": -78.2831},
        {"city": "Smithfield", "lat": 35.5085, "lng": -78.3397},
        {"city": "Southern Pines", "lat": 35.1740, "lng": -79.3928},
        {"city": "Spring Lake", "lat": 35.1679, "lng": -78.9783},
        {"city": "Tarboro", "lat": 35.8963, "lng": -77.5356},
        {"city": "Thomasville", "lat": 35.8826, "lng": -80.0816},
        {"city": "Wake Forest", "lat": 35.9799, "lng": -78.5097},
        {"city": "Washington", "lat": 35.5463, "lng": -77.0528},
        {"city": "Waynesville", "lat": 35.4887, "lng": -82.9887},
        {"city": "Whiteville", "lat": 34.3302, "lng": -78.7036},
        {"city": "Zebulon", "lat": 35.8249, "lng": -78.3142},
        {"city": "Kings Mountain", "lat": 35.2440, "lng": -81.3412},
        {"city": "Boone", "lat": 36.2168, "lng": -81.6746},
        {"city": "Franklin", "lat": 35.1826, "lng": -83.3812},
        {"city": "Sylva", "lat": 35.3734, "lng": -83.2250},
        {"city": "Bryson City", "lat": 35.4304, "lng": -83.4474},
        {"city": "Marion", "lat": 35.6848, "lng": -82.0093},
        {"city": "Black Mountain", "lat": 35.6179, "lng": -82.3215},
        {"city": "Hendersonville", "lat": 35.3187, "lng": -82.4609},
        {"city": "Blowing Rock", "lat": 36.1359, "lng": -81.6770},
        {"city": "Banner Elk", "lat": 36.1637, "lng": -81.8715},
        {"city": "Elkin", "lat": 36.2449, "lng": -80.8487},
        {"city": "Wilkesboro", "lat": 36.1468, "lng": -81.1598}
            ]

    
    # ScraperAPI payload template
    payload_template = {
        'api_key': '621b20ec8d6e7d27219a388c47b42a70',
        'autoparse': 'true',
        'output_format': 'csv',
        'country_code': 'us',
        'device_type': 'desktop',
        'follow_redirect': 'false'
    }

    def start_requests(self):
        # Open the CSV file once to write all data
        with open('publix_stores.csv', mode='w', newline='', encoding='utf-8') as file:
            # Write the header first
            fieldnames = ["storeNumber", "name", "streetAddress", "city", "state", "zip", "phoneNumber", "hours"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        
        # Loop through each city and make a request for its latitude and longitude
        for city in self.cities:
            latitude = city['lat']
            longitude = city['lng']
            
            # Prepare the payload for the current city
            payload = self.payload_template.copy()
            payload['url'] = f"https://services.publix.com/storelocator/api/v1/stores/?latitude={latitude}&longitude={longitude}"
            
            # Send GET request for each city
            self.fetch_store_data(payload, city)

    def fetch_store_data(self, payload, city):
        try:
            r = requests.get('https://api.scraperapi.com/', params=payload)
            if r.status_code == 200:
                # Check if response is empty
                if r.text.strip():
                    try:
                        data = r.json()  # Get the response as JSON
                        # Loop through the stores and extract details
                        for store in data.get('stores', []):
                            store_data = {
                                "storeNumber": store.get('storeNumber'),
                                "name": store.get('name'),
                                "streetAddress": store.get('address', {}).get('streetAddress'),
                                "city": store.get('address', {}).get('city'),
                                "state": store.get('address', {}).get('state'),
                                "zip": store.get('address', {}).get('zip'),
                                "phoneNumber": store.get('phoneNumbers', {}).get('Store', ''),
                               
                            }
                            # Save to CSV
                            self.save_to_csv(store_data)
                    except json.JSONDecodeError:
                        print(f"Failed to decode JSON for {city['city']}")
                else:
                    print(f"Empty response for {city['city']}")
            else:
                print(f"Failed to fetch data for {city['city']}, status code: {r.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request error for {city['city']}: {e}")
            time.sleep(2)  # Wait a little before retrying

    def save_to_csv(self, store_data):
        # Open the CSV file and append the store data
        with open('publix_stores.csv', mode='a', newline='', encoding='utf-8') as file:
            fieldnames = store_data.keys()  # Use the store_data keys as fieldnames
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(store_data)
        
        print(f"Store data saved to publix_stores.csv")

    def parse(self, response):
        # No need to implement parsing here as the data is fetched and written directly in start_requests
        pass
