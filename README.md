🦌 Hunt AI Assistant 🌦️
This is a Django-based REST API that provides real-time weather and hunting risk information for a given area. It combines data from OpenWeatherMap API and AI-powered suggestions from Groq's LLaMA model to inform users about animals, weather risks, and hunting advice.

📌 Features
🔍 Location-Based Input – Enter any area or city name.

🌤️ Live Weather Data – Retrieves temperature, humidity, and conditions using OpenWeatherMap.

🧠 AI-Powered Hunting Insights – Uses Groq's LLaMA model to generate information on:

Local animal types

Weather-related risks

Hunting strategies

🛠️ Tech Stack
Python 3.10+

Django

Django REST Framework

OpenWeatherMap API

Groq LLaMA3 model (via https://api.groq.com)

🚀 Getting Started
1. Clone the repository

git clone https://github.com/your-username/hunt-ai-assistant.git
cd hunt-ai-assistant
2. Install dependencies

pip install -r requirements.txt
3. Add your API keys
Update the following placeholders in views.py:

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
"Authorization": f"Bearer YOUR_GROQ_API_KEY"
You can also use environment variables for better security.

4. Run the server
5. 
python manage.py runserver
🧪 Example API Usage
Endpoint
POST /hunt-info/
Request Body
{
  "area": "Sylhet,BD"
}
Response Example
{
  "area": "Sylhet,BD",
  "weather": {
    "temperature": 29.5,
    "humidity": 70,
    "weather": "light rain"
  },
  "animal_risk_info": "In Sylhet, common animals include deer, wild boar..."
}
📂 URL Configuration
In your urls.py:

python
Copy
Edit
from django.urls import path
from .views import HuntInfoView

urlpatterns = [
    path("hunt-info/", HuntInfoView.as_view(), name="hunt-info"),
]
❗ Notes
Use full area format like City,CountryCode (e.g., "Khulna,BD") for better accuracy with OpenWeatherMap.

Make sure your Groq API key is valid and authorized to use the llama3-8b-8192 model.
