import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

class HuntInfoView(APIView):
    def post(self, request):
        area = request.data.get('area')

        if not area:
            return Response({'error': 'Area name is required'}, status=400)

        # 1. Get weather
        weather_info = self.get_weather_info(area)

        # 2. Get animal/risk info using AI (Groq / HuggingFace)
        animal_info = self.get_animal_info_with_ai(area)

        if "error" in animal_info:
            return Response({"error": "AI response failed", "details": animal_info["error"]}, status=500)

        # Merge and send
        return Response({
            "area": area,
            "weather": weather_info,
            "animal_risk_info": animal_info
        })

    def get_weather_info(self, area):
        API_KEY = "YOUR_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={area}&appid={API_KEY}&units=metric"
        try:
            res = requests.get(url)
            data = res.json()

            # Check if city is not found or other API error
            if res.status_code != 200 or "main" not in data or "weather" not in data:
                return {"error": data.get("message", "Invalid response from weather API.")}

            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"]
            }

        except Exception as e:
            return {"error": str(e)}

    def get_animal_info_with_ai(self, area):
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            
            "Authorization": f"Bearer API_KEY",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a hunting expert."},
                {"role": "user", "content": f"Tell me what animals are found in {area}, weather-related risks, and hunting advice."}
            ],
            "temperature": 0.7
        }

        try:
            res = requests.post(url, headers=headers, json=data)
            if res.status_code != 200:
                return {"error": f"Groq API Error: {res.status_code} - {res.text}"}
            result = res.json()
            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return {"error": str(e)}
        

        # Test data
        # {
        #     "area": "Dhaka,BD"
        # }
