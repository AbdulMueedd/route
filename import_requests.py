import requests
import json

API_KEY = "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"  # must start with nvapi-

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

payload = {
    "cost_matrix_data": {
        "data": {
            "1": [
                [0, 5, 4, 3, 5],
                [5, 0, 6, 4, 3],
                [4, 8, 0, 4, 2],
                [1, 4, 3, 0, 4],
                [3, 3, 5, 6, 0],
            ]
        }
    },
    "travel_time_matrix_data": {
        "data": {
            "1": [
                [ 0, 10,  8,  6, 10],
                [10,  0, 12,  8,  6],
                [ 8, 16,  0,  8,  4],
                [ 2,  8,  6,  0,  8],
                [ 6,  6, 10, 12,  0],
            ]
        }
    },
    "fleet_data": {
        "vehicle_locations": [[0,0],[0,0],[0,0]],
        "vehicle_ids": ["Truck-A","Truck-B","Truck-C"],
        "vehicle_types": [1, 1, 1],
        "capacities": [[75, 75, 75]],
        "vehicle_time_windows": [[0,100],[0,100],[0,100]]
    },
    "task_data": {
        "task_locations": [1, 2, 3, 4],
        "demand": [[30, 40, 40, 30]],
        "task_time_windows": [
            [3, 20], [5, 30], [1, 20], [4, 40]
        ],
        "service_times": [3, 1, 8, 4]
    },
    "solver_config": {
        "objectives": {"cost": 1, "travel_time": 1},
        "time_limit": 5
    }
}

# Try the API catalog URL
url = "https://integrate.api.nvidia.com/v1/cuopt/cuopt"

response = requests.post(url, headers=headers, json=payload)
print(f"Status: {response.status_code}")
print(response.text[:2000])