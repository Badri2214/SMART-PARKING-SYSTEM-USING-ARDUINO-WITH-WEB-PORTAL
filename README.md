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
![Home Page](<img width="1767" height="825" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/11f61ef3-afab-4434-8f21-44fcec211bf2" />)  

🔹 **Signin Page**  
![Signin Page](<img width="1896" height="733" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/28518a57-168c-43c1-942b-8c4c9c25ccc7" />)  

🔹 **Parking Slot Availability**  
![Slot Availability](<img width="1811" height="810" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/682d2b65-4200-4c74-a104-de52fa656a8c" />)  

🔹 **Arduino Circuit Design**  
![Circuit Design](<img width="1046" height="741" alt="Screenshot (26)" src="https://github.com/user-attachments/assets/25305b14-e20b-4f82-8994-af73ff497ec4" />)  

🔹 **Implementation**  
![Hardware Implementation](<img width="733" height="784" alt="Screenshot (27)" src="https://github.com/user-attachments/assets/60d585be-3915-4255-a2fe-10210b030a61" />)  

