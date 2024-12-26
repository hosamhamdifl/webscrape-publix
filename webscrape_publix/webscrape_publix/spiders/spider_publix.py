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
     
{"city": "Apex", "lat": 35.7326, "lng": -78.8503},
    {"city": "Asheville", "lat": 35.5951, "lng": -82.5515},
    {"city": "Banner Elk", "lat": 36.1637, "lng": -81.8715},
    {"city": "Black Mountain", "lat": 35.6179, "lng": -82.3215},
    {"city": "Blowing Rock", "lat": 36.1359, "lng": -81.6770},
    {"city": "Boone", "lat": 36.2168, "lng": -81.6746},
    {"city": "Brevard", "lat": 35.2346, "lng": -82.7336},
    {"city": "Bryson City", "lat": 35.4304, "lng": -83.4474},
    {"city": "Carolina Beach", "lat": 34.0263, "lng": -77.8893},
    {"city": "Cary", "lat": 35.7915, "lng": -78.7812},
    {"city": "Charlotte", "lat": 35.2271, "lng": -80.8431},
    {"city": "Chapel Hill", "lat": 35.9132, "lng": -79.0558},
    {"city": "Concord", "lat": 35.4083, "lng": -80.5795},
    {"city": "Durham", "lat": 35.9940, "lng": -78.8986},
    {"city": "Elkin", "lat": 36.2449, "lng": -80.8487},
    {"city": "Forest City", "lat": 35.3387, "lng": -81.8570},
    {"city": "Franklin", "lat": 35.1826, "lng": -83.3812},
    {"city": "Gastonia", "lat": 35.2623, "lng": -81.1873},
    {"city": "Goldboro", "lat": 35.3855, "lng": -77.9933},
    {"city": "Greensboro", "lat": 36.0726, "lng": -79.7910},
    {"city": "Greenville", "lat": 35.6127, "lng": -77.3664},
    {"city": "Hendersonville", "lat": 35.3187, "lng": -82.4609},
    {"city": "High Point", "lat": 35.9557, "lng": -80.0053},
    {"city": "Huntersville", "lat": 35.4105, "lng": -80.8420},
    {"city": "Indian Trail", "lat": 35.0915, "lng": -80.6207},
    {"city": "Jacksonville", "lat": 34.7546, "lng": -77.4309},
    {"city": "Jefferson", "lat": 36.4079, "lng": -81.4704},
    {"city": "Knightdale", "lat": 35.7980, "lng": -78.4912},
    {"city": "Lincolnton", "lat": 35.4732, "lng": -81.2543},
    {"city": "Lillington", "lat": 35.3993, "lng": -78.8153},
    {"city": "Lumberton", "lat": 34.6182, "lng": -79.0086},
    {"city": "Macon", "lat": 35.1867, "lng": -83.3854},
    {"city": "Marion", "lat": 35.6848, "lng": -82.0093},
    {"city": "Matthews", "lat": 35.1168, "lng": -80.7237},
    {"city": "Monroe", "lat": 34.9854, "lng": -80.5495},
    {"city": "Mooresville", "lat": 35.5795, "lng": -80.8857},
    {"city": "Morganton", "lat": 35.7454, "lng": -81.6848},
    {"city": "Morrisville", "lat": 35.8495, "lng": -78.8358},
    {"city": "Mount Airy", "lat": 36.4993, "lng": -80.6073},
    {"city": "Mount Holly", "lat": 35.2987, "lng": -81.0151},
    {"city": "Murraysville", "lat": 34.2991, "lng": -77.8283},
    {"city": "Nashville", "lat": 35.9743, "lng": -77.9653},
    {"city": "Oak Island", "lat": 33.9200, "lng": -78.1500},
    {"city": "Oxford", "lat": 36.3102, "lng": -78.5906},
    {"city": "Pineville", "lat": 35.0847, "lng": -80.8837},
    {"city": "Reidsville", "lat": 36.3543, "lng": -79.6645},
    {"city": "Rocky Mount", "lat": 35.9381, "lng": -77.7904},
    {"city": "Roanoke Rapids", "lat": 36.4615, "lng": -77.6544},
    {"city": "Salisbury", "lat": 35.6709, "lng": -80.4742},
    {"city": "Sanford", "lat": 35.4799, "lng": -79.1803},
    {"city": "Selma", "lat": 35.5360, "lng": -78.2831},
    {"city": "Smithfield", "lat": 35.5085, "lng": -78.3397},
    {"city": "Southern Pines", "lat": 35.1740, "lng": -79.3928},
    {"city": "Spring Lake", "lat": 35.1679, "lng": -78.9783},
    {"city": "Sylva", "lat": 35.3734, "lng": -83.2250},
    {"city": "Taylorsville", "lat": 35.9190, "lng": -81.1833},
    {"city": "Tarboro", "lat": 35.8963, "lng": -77.5356},
    {"city": "Thomasville", "lat": 35.8826, "lng": -80.0816},
    {"city": "Wake Forest", "lat": 35.9799, "lng": -78.5097},
    {"city": "Washington", "lat": 35.5463, "lng": -77.0528},
    {"city": "Waynesville", "lat": 35.4887, "lng": -82.9887},
    {"city": "Whiteville", "lat": 34.3302, "lng": -78.7036},
    {"city": "Winston-Salem", "lat": 36.0999, "lng": -80.2442},
    {"city": "Zebulon", "lat": 35.8249, "lng": -78.3142},
    {"city": "Albemarle", "lat": 35.3500, "lng": -80.2045},
    {"city": "Angier", "lat": 35.5085, "lng": -78.7340},
    {"city": "Archdale", "lat": 35.8950, "lng": -79.9772},
    {"city": "Ayden", "lat": 35.4644, "lng": -77.3667},
    {"city": "Bessemer City", "lat": 35.2851, "lng": -81.2549},
    {"city": "Bethel", "lat": 35.8963, "lng": -77.3545},
    {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
    {"city": "Clyde", "lat": 35.5177, "lng": -82.9465},
    {"city": "Columbus", "lat": 35.2435, "lng": -82.0917},
    {"city": "Creston", "lat": 36.4494, "lng": -81.6237},
    {"city": "East Spencer", "lat": 35.6827, "lng": -80.4333},
    {"city": "Elizabethtown", "lat": 34.6225, "lng": -78.6022},
    {"city": "Elon", "lat": 36.1023, "lng": -79.2082},
    {"city": "Enfield", "lat": 36.2208, "lng": -77.7034},
    {"city": "Fairmont", "lat": 34.4872, "lng": -79.1106},
    {"city": "Fayetteville", "lat": 35.0527, "lng": -78.8784},
    {"city": "Forest City", "lat": 35.3387, "lng": -81.8570},
    {"city": "Franklinton", "lat": 36.0840, "lng": -78.3781},
    {"city": "Gastonia", "lat": 35.2623, "lng": -81.1873},
     {"city": "Aberdeen", "lat": 35.1304, "lng": -79.4143},
    {"city": "Alexis", "lat": 35.4074, "lng": -81.1173},
    {"city": "Ansonville", "lat": 34.9901, "lng": -80.0705},
    {"city": "Appalachian State University", "lat": 36.2137, "lng": -81.6824},
    {"city": "Aulander", "lat": 36.0611, "lng": -77.1462},
    {"city": "Barkers Creek", "lat": 35.6842, "lng": -81.5042},
    {"city": "Bear Creek", "lat": 35.6636, "lng": -79.5163},
    {"city": "Beaver Creek", "lat": 35.4553, "lng": -81.6111},
    {"city": "Belmont", "lat": 35.2421, "lng": -81.0352},
    {"city": "Bessemer City", "lat": 35.2851, "lng": -81.2549},
    {"city": "Bladenboro", "lat": 34.6181, "lng": -78.7884},
    {"city": "Bogue", "lat": 34.6845, "lng": -77.0843},
    {"city": "Bolivia", "lat": 33.9459, "lng": -78.1947},
    {"city": "Brevard", "lat": 35.2346, "lng": -82.7336},
    {"city": "Broadway", "lat": 35.4281, "lng": -79.0187},
    {"city": "Burlington", "lat": 36.0957, "lng": -79.4378},
    {"city": "Burnsville", "lat": 35.9172, "lng": -82.3089},
    {"city": "Caldwell", "lat": 35.8311, "lng": -82.3737},
    {"city": "Camden", "lat": 36.2779, "lng": -76.2897},
    {"city": "Candler", "lat": 35.5525, "lng": -82.6074},
    {"city": "Candor", "lat": 35.2939, "lng": -79.5361},
    {"city": "Carolina Shores", "lat": 33.8836, "lng": -78.5831},
    {"city": "Carrboro", "lat": 35.9111, "lng": -79.0796},
    {"city": "Casar", "lat": 35.4872, "lng": -81.4772},
    {"city": "Castalia", "lat": 36.0483, "lng": -77.9574},
    {"city": "Cat Square", "lat": 35.4384, "lng": -81.1474},
    {"city": "Cedar Point", "lat": 34.7105, "lng": -77.0577},
    {"city": "Chapel Hill", "lat": 35.9132, "lng": -79.0558},
    {"city": "Chinquapin", "lat": 34.9620, "lng": -77.7461},
    {"city": "Claremont", "lat": 35.6907, "lng": -81.1344},
    {"city": "Clayton", "lat": 35.6501, "lng": -78.4565},
    {"city": "Clifton", "lat": 35.9122, "lng": -80.3987},
    {"city": "Columbus", "lat": 35.2435, "lng": -82.0917},
    {"city": "Connelly Springs", "lat": 35.6245, "lng": -81.5420},
    {"city": "Cramerton", "lat": 35.2564, "lng": -81.0397},
    {"city": "Creedmoor", "lat": 36.1379, "lng": -78.7056},
    {"city": "Creswell", "lat": 35.8667, "lng": -76.3778},
    {"city": "Cullowhee", "lat": 35.3086, "lng": -83.1834},
    {"city": "Dallas", "lat": 35.3486, "lng": -81.2094},
    {"city": "Davidson", "lat": 35.4989, "lng": -80.8432},
    {"city": "Denton", "lat": 35.6379, "lng": -80.2179},
    {"city": "Dillsboro", "lat": 35.3586, "lng": -83.2172},
    {"city": "Durham", "lat": 35.9940, "lng": -78.8986},
    {"city": "East Bend", "lat": 36.2014, "lng": -80.4315},
    {"city": "Eastover", "lat": 35.0800, "lng": -78.7323},
    {"city": "Eden", "lat": 36.5084, "lng": -79.7744},
    {"city": "Edenton", "lat": 36.0643, "lng": -76.6010},
    {"city": "Elizabethtown", "lat": 34.6225, "lng": -78.6022},
    {"city": "Enfield", "lat": 36.2208, "lng": -77.7034},
    {"city": "Fairfield", "lat": 35.1695, "lng": -78.9783},
    {"city": "Farmville", "lat": 35.5943, "lng": -77.5523},
    {"city": "Fayetteville", "lat": 35.0527, "lng": -78.8784},
    {"city": "Fletcher", "lat": 35.4317, "lng": -82.4759},
    {"city": "Forest City", "lat": 35.3387, "lng": -81.8570},
    {"city": "Fort Bragg", "lat": 35.1447, "lng": -79.0043},
    {"city": "Franklin", "lat": 35.1826, "lng": -83.3812},
    {"city": "Gastonia", "lat": 35.2623, "lng": -81.1873}
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
        # Read the existing store data to check for duplicates
        existing_stores = set()
        try:
            with open('publix_stores.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Add unique identifier to set (storeNumber in this case)
                    existing_stores.add(row['storeNumber'])
        except FileNotFoundError:
            pass  # If the file doesn't exist, that's fine

        # Only save the store data if it's not already in the existing stores set
        if store_data['storeNumber'] not in existing_stores:
            with open('publix_stores.csv', mode='a', newline='', encoding='utf-8') as file:
                fieldnames = store_data.keys()  # Use the store_data keys as fieldnames
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(store_data)
            print(f"Store data saved to publix_stores.csv")
        else:
            print(f"Duplicate store found: {store_data['storeNumber']}")

    def parse(self, response):
        # No need to implement parsing here as the data is fetched and written directly in start_requests
        pass
