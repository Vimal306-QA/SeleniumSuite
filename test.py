import json
from faker import Faker

fake = Faker('en_IN')  # Set Faker to Indian locale
records = []

for i in range(1, 10001):
    records.append({
        "registrationID": i,
        "name": fake.name(),  # Generate realistic Indian name
        "age": 20 + (i % 30),
        "mobileNumber": f"9456069{str(i % 1000).zfill(3)}",
        "gender": "Male" if i % 2 == 0 else "Female",
        "illnesses": "Fever" if i % 2 == 0 else "Cold",
        "ayushmanStatus": "Yes" if i % 3 == 0 else "No",
        "incomeScale": "50000" if i % 5 == 0 else "",
        "pastHistory": "Cold" if i % 2 == 0 else "Cough",
        "villageId": (i % 10) + 1,
        "dateOfRegistration": "2025-01-24 10:02:50"
    })

# Use ensure_ascii=False to display Hindi text correctly
json_data = json.dumps({"data": records}, indent=4, ensure_ascii=False)

# Save JSON with correct Hindi characters
with open("output.json", "w", encoding="utf-8") as f:
    f.write(json_data)

print("JSON data with Indian names saved as output.json")
