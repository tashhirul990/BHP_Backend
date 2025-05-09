# BHP_Backend

This is the backend service for the **Bangalore Home Price Prediction** project, built with **Flask**. It exposes APIs to fetch available locations and predict home prices based on square footage, number of bedrooms (BHK), bathrooms, and location.

---

## 🚀 Deployed on Render

- **Base URL:**  
  [https://bhp-backend-1.onrender.com](https://bhp-backend-1.onrender.com)

---

## 📍 Get Locations (GET)

**Endpoint:**  
[https://bhp-backend-1.onrender.com/get_locations](https://bhp-backend-1.onrender.com/get_locations)

**Description:**  
Returns a list of all available locations used for price prediction.

---

## 🏠 Predict Home Price (POST)

**Endpoint:**  
[https://bhp-backend-1.onrender.com/predict_home_price](https://bhp-backend-1.onrender.com/predict_home_price)

**Method:** `POST`  
**Content-Type:** `form-data`

**Body Parameters:**
| Key      | Type   | Description                        |
|----------|--------|------------------------------------|
| `sqft`   | float  | Total square footage               |
| `bath`   | int    | Number of bathrooms                |
| `bhk`    | int    | Number of bedrooms                 |
| `location` | string | Location (choose from dropdown returned by `/get_locations`) |

**Example Request:**

