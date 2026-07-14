
# 🌱 Smart Drop

> **Solar-Powered Irrigation Monitoring System**

Smart Drop is an IoT-powered irrigation monitoring system designed to help farmers make smarter irrigation decisions through real-time monitoring, automation, and data visualization. The platform combines ESP32 hardware with a Flask web application to provide live insights into water levels, pump status, battery health, and solar performance.

---

## 📖 Overview

Agriculture relies heavily on efficient water management. Smart Drop addresses this challenge by providing farmers with a simple, affordable, and intelligent solution for monitoring irrigation systems from anywhere.

The system integrates sensors, IoT hardware, and a responsive web dashboard to improve water efficiency, reduce manual monitoring, and support sustainable farming.

---

## ✨ Features

* 🌊 Real-time water tank level monitoring
* 🚰 Pump status monitoring and control
* ☀️ Solar panel performance tracking
* 🔋 Battery health monitoring
* 📊 Interactive analytics dashboard
* 🔔 Smart alerts and notifications
* 📱 Responsive web interface
* 🌍 Built for smart agriculture

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js

### Database

* SQLite

### Hardware

* ESP32
* HC-SR04 Ultrasonic Sensor
* Relay Module
* Solar Panel
* Rechargeable Battery

---

## 🏗️ System Architecture

```text
HC-SR04 Sensor
        │
        ▼
     ESP32
        │
        ▼
 Flask Backend API
        │
        ▼
     SQLite
        │
        ▼
 Web Dashboard
```

---

## 📸 Screenshots

### Login Page

*Add screenshot here*

### Dashboard

*Add screenshot here*

### Analytics

*Add screenshot here*

### Hardware Prototype

*Add photo here*

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/kobilo-1212cloud/Smart-Drop.git
```

### Navigate to the project

```bash
cd Smart-Drop
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```text
Smart-Drop/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── analytics.html
│   ├── water.html
│   ├── solar.html
│   ├── alerts.html
│   └── profile.html
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🎯 Future Improvements

* Soil moisture sensor integration
* Weather API integration
* Mobile application
* AI-powered irrigation recommendations
* Multi-farm management
* SMS and email alerts
* Cloud database support
* Historical analytics and reporting

---

## 🌍 Impact

Smart Drop aims to improve agricultural productivity by combining renewable energy, IoT, and data-driven decision-making. The project supports sustainable farming by helping reduce water waste, optimize irrigation, and simplify farm monitoring.

---

## 👩‍💻 Developer

**Ivy Chebet**

IT Student | Software Developer | IoT Enthusiast

* GitHub: https://github.com/kobilo-1212cloud
* Email: [ivychebet1212@gmail.com](mailto:ivychebet1212@gmail.com)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project interesting, consider giving it a star and following my work as I continue building solutions at the intersection of software, IoT, and smart agriculture.
