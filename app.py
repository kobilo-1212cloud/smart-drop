from flask import Flask, render_template, jsonify
import serial
import threading
import time

app = Flask(__name__)

# -----------------------------
# SYSTEM DATA
# -----------------------------
sensor_data = {
    "tank_level": 0,
    "distance": 0,
    "pump_status": "OFF",
    "mode": "AUTO",
    "battery": 95.0,
    "alert": "System operating normally"
}

# -----------------------------
# CONNECT MICRO:BIT
# -----------------------------
try:
    ser = serial.Serial('COM3', 115200, timeout=1)
    print("✅ Micro:bit connected on COM3")
except Exception as e:
    ser = None
    print("❌ Micro:bit not connected:", e)

# -----------------------------
# SENSOR READING THREAD
# -----------------------------
def read_sensor():

    tank_depth = 30

    while True:

        try:

            if ser and ser.in_waiting:

                line = ser.readline().decode(
                    errors="ignore"
                ).strip()

                if line:

                    print("Received:", line)

                    distance = float(line)

                    sensor_data["distance"] = round(
                        distance, 1
                    )

                    level = max(
                        0,
                        min(
                            100,
                            int(
                                ((tank_depth - distance)
                                 / tank_depth) * 100
                            )
                        )
                    )

                    sensor_data["tank_level"] = level

                    # Alerts
                    if level < 10:
                        sensor_data["alert"] = "🚨 Critical water level"

                    elif level < 30:
                        sensor_data["alert"] = "⚠ Low water level"

                    elif sensor_data["pump_status"] == "ON":
                        sensor_data["alert"] = "🚰 Pump currently running"

                    else:
                        sensor_data["alert"] = "✅ System operating normally"

            # Battery simulation
            if sensor_data["pump_status"] == "ON":

                sensor_data["battery"] = max(
                    20,
                    sensor_data["battery"] - 0.02
                )

            else:

                sensor_data["battery"] = min(
                    100,
                    sensor_data["battery"] + 0.01
                )

        except Exception as e:
            print("Sensor Error:", e)

        time.sleep(0.5)

# Start background thread
threading.Thread(
    target=read_sensor,
    daemon=True
).start()

# -----------------------------
# PAGES
# -----------------------------
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/water')
def water():
    return render_template('water.html')

@app.route('/solar')
def solar():
    return render_template('solar.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/alerts')
def alerts():
    return render_template('alerts.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

# -----------------------------
# API
# -----------------------------
@app.route('/api/data')
def api_data():
    return jsonify(sensor_data)

@app.route('/api/status')
def api_status():
    return jsonify(sensor_data)

@app.route('/api/history')
def api_history():
    return jsonify({
        "tank_level": sensor_data["tank_level"],
        "distance": sensor_data["distance"],
        "battery": round(sensor_data["battery"], 1)
    })

# -----------------------------
# PUMP CONTROLS
# -----------------------------
@app.route('/pump/on')
def pump_on():

    sensor_data["pump_status"] = "ON"

    return jsonify({
        "status": "success",
        "pump": "ON"
    })

@app.route('/pump/off')
def pump_off():

    sensor_data["pump_status"] = "OFF"

    return jsonify({
        "status": "success",
        "pump": "OFF"
    })

# -----------------------------
# RUN APP
# -----------------------------
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False
    )