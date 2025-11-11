# 🌦️ Weather API Project  
### ✨ *This README is provided in both English and Persian (دو زبانه: انگلیسی و فارسی)*  

---
## 📘 Description  
A simple Python project that fetches and displays **current weather data** for any city entered by the user.  
It uses the **OpenWeatherMap API** to get city coordinates (latitude and longitude) and then retrieves real-time weather details such as **temperature, city name, and weather conditions**.  

The user only needs to type the name of a city — the program does the rest automatically! ⚡  
---
## ⚙️ Features
- 🌍 Get live weather information by city name  
- 🧭 Uses OpenWeatherMap’s **Geo API** for latitude & longitude  
- 🌡️ Displays temperature and weather description  
- 💻 Error handling for invalid city names or failed connections  
---
## 🧠 Skills Used
- 🐍 **Python basics**  
- 🌐 **Requests library** (for API communication)  
- 🧩 **JSON parsing**  
- 🔗 **API integration**  
- 🧭 **User input handling**  
---
## 🔗 APIs Used
- [🌍 OpenWeatherMap Geocoding API](https://openweathermap.org/api/geocoding-api)  
- [☁️ OpenWeatherMap Current Weather Data API](https://openweathermap.org/current)
---
## 🏁 How to Use
1. Get your own API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).  
2. Replace the variable `API_KEY` in the code with your key.  
3. Run the script and enter a city name when prompted.  
4. The program will print:
   - 🏙️ City name  
   - 🌡️ Temperature (°C)  
   - ☁️ Weather condition  
---
## 🧩 Example Output
* bash
* city : Tehran
* vazeiat : lat=35.6944, lon=51.4215
* Weather : Tehran:
* The temperature now : 12°C
* Weather condition : clear sky
---
```🇮🇷 پروژه‌ی API وضعیت هوا
📘 توضیحات
این پروژه‌ی ساده‌ی پایتونی، با گرفتن نام یک شهر از کاربر، وضعیت فعلی هوا را از سایت OpenWeatherMap دریافت و نمایش می‌دهد.
برنامه ابتدا با استفاده از API مختصات شهر (Geo API)، طول و عرض جغرافیایی شهر را پیدا می‌کند
و سپس با API وضعیت هوا (Weather API)، دمای فعلی، نام شهر و توضیح وضعیت آب‌وهوا را نشان می‌دهد.
کاربر فقط کافی است نام شهر را وارد کند؛ باقی کارها به‌صورت خودکار انجام می‌شود ✅

🧰 مهارت‌های به‌کاررفته
🐍 مبانی پایتون
🌐 کار با کتابخانه requests
🧩 پردازش داده‌های JSON
🔗 استفاده از API و ارسال درخواست HTTP
⚙️ مدیریت خطا و ورودی کاربر

🪄 نمونه خروجی
```
```bash
Copy code
city : Shiraz
vazeiat : lat=29.6103, lon=52.5311
Weather : Shiraz:
The temperature now : 18°C
Weather condition : scattered clouds
