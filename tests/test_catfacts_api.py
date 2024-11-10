import requests
import random

BASE_URL = "https://catfact.ninja"

# Test the /fact endpoint without parameters
def test_get_single_fact():
    response = requests.get(f"{BASE_URL}/fact")
    assert response.status_code == 200
    data = response.json()
    print("Single fact response:", data)
    assert "fact" in data
    assert "length" in data
    assert isinstance(data["fact"], str) and data["fact"]
    assert isinstance(data["length"], int) and data["length"] > 0

# Test the /fact endpoint with a random max_length parameter
def test_get_fact_with_random_max_length():
    max_length = random.randint(10, 100)
    response = requests.get(f"{BASE_URL}/fact", params={"max_length": max_length})
    assert response.status_code == 200
    data = response.json()
    assert "fact" in data
    assert "length" in data
    assert data["length"] <= max_length
    assert len(data["fact"]) <= max_length
    print(f"Fact with max_length={max_length}: length={data['length']}")

# Test the /facts endpoint for multiple facts with default settings
def test_get_multiple_facts():
    response = requests.get(f"{BASE_URL}/facts")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    facts = data["data"]
    assert isinstance(facts, list)
    for fact in facts:
        assert "fact" in fact
        assert "length" in fact
        assert isinstance(fact["fact"], str) and fact["fact"]
        assert isinstance(fact["length"], int) and fact["length"] > 0
    print("Multiple facts response:", data)

# Test the /facts endpoint with limit and max_length parameters
def test_get_multiple_facts_with_limit_and_max_length():
    limit = random.randint(1, 10)
    max_length = random.randint(10, 100)
    response = requests.get(f"{BASE_URL}/facts", params={"limit": limit, "max_length": max_length})

    assert response.status_code == 200
    data = response.json()

    print(f"Response data: {data}")

    facts = data.get("data", [])
    print(f"Received {len(facts)} facts.")

    # Check if the facts were returned and if they meet the limit
    assert len(facts) == limit, f"Expected {limit} facts, but got {len(facts)}"
    for fact in facts:
        assert "fact" in fact
        assert "length" in fact
        assert fact["length"] <= max_length, f"Expected fact length <= {max_length}, but got {fact['length']}"
        assert len(
            fact["fact"]) <= max_length, f"Expected fact text length <= {max_length}, but got {len(fact['fact'])}"

    print(f"Tested with limit={limit}, max_length={max_length}, received {len(facts)} facts.")


