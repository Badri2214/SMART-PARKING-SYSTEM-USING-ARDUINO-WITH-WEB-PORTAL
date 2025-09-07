# 🚗 Smart Parking System using Arduino with Web Portal  

## 📌 Project Overview  
The **Smart Parking System** is designed to monitor and display real-time parking slot availability using **Arduino** and **IR sensors**. The system integrates with a **web portal**, allowing users to check available slots online. This project aims to reduce the hassle of searching for parking spaces and provide a smarter, automated parking management solution.  

---

## ✨ Features  
- 🔹 Real-time parking slot availability detection  
- 🔹 Arduino UNO with IR sensors for vehicle detection  
- 🔹 Servo motor for barrier control  
- 🔹 User-friendly Web Portal for checking slot status  
- 🔹 Authentication system (Signin / Signup)  
- 🔹 Visual display of available slots on the portal  

---

## 🛠️ Technologies Used  

### 🔧 Hardware  
- Arduino UNO  
- IR Sensors  
- Servo Motor  
- USB Module  

### 💻 Software / Web Portal  
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **Database**: SQLite  
- **Communication**: Arduino Serial Communication  

---

## 📂 Project Structure  
├── Arduino_Code/        # Arduino sketches for sensors & servo  
├── Web_Portal/          # Flask web portal files  
│   ├── static/          # CSS, JS, images  
│   ├── templates/       # HTML pages (Home, Signin, Signup, Dashboard)  
│   └── app.py           # Flask backend  
├── assets/              # Screenshots & circuit images  
├── README.md            # Documentation  

## ⚙️ How It Works  

1. 🚘 A car approaches the parking slot.  
2. 📡 IR sensors detect the presence/absence of a car.  
3. 🔄 Arduino processes the data and sends slot status to the web portal.  
4. 🌐 The web portal updates availability in real-time.  
5. 🚧 The servo motor acts as a barrier (optional) for automated entry control.  

---

## 🔑 Authentication  

- **Signin Page** → Existing users can log in.  
- **Signup Page** → New users can register.  
- ✅ After login, users can view available parking slots in the dashboard.  

Signin Page → Existing users can log in.

Signup Page → New users can register.

Users can then view available parking slots.

## 📸 Screenshots  

🔹 **Home Page**  

<img width="1767" height="825" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/c285250f-16fc-48d4-9cff-ee6f8b55087f" />


🔹 **Signin Page**  

<img width="1896" height="733" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/c7135a5a-8d74-4170-a531-b2cba0a6c8cc" />


🔹 **Parking Slot Availability**  

<img width="1811" height="810" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/d2602aa6-babd-48b6-9f23-7726687aaa1d" />


🔹 **Arduino Circuit Design**  

<img width="1046" height="741" alt="Screenshot (26)" src="https://github.com/user-attachments/assets/bec62cb8-95c2-4007-9fb7-3160c2ddea20" />


🔹 **Hardware Implementation**  

<img width="733" height="784" alt="Screenshot (27)" src="https://github.com/user-attachments/assets/ec34f9ae-d44d-4cfa-99a4-b50257eeb2c2" />


