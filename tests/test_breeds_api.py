import requests
import random

BASE_URL = "https://catfact.ninja"

# Test the /breeds endpoint without parameters
def test_get_all_breeds():
    response = requests.get(f"{BASE_URL}/breeds")
    assert response.status_code == 200
    data = response.json()
    breeds = data["data"]
    assert len(breeds) > 0
    print("All breeds response:", data)

# Test the /breeds endpoint with a limit parameter
def test_get_breeds_with_limit():
    limit = random.randint(1, 10)
    response = requests.get(f"{BASE_URL}/breeds", params={"limit": limit})
    assert response.status_code == 200
    data = response.json()
    breeds = data["data"]
    assert len(breeds) == limit
    print(f"Breeds with limit={limit}: received {len(breeds)} breeds.")
