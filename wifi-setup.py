import requests
import json

def connect_to_cozmo_wifi(cozmo_ip):
    # Prompt for details
    target_ssid = input("Enter your Wi-Fi SSID (network name): ").strip()
    target_password = input("Enter your Wi-Fi Password: ").strip()

    # Payload for Wi-Fi setup
    payload = {
        "ssid": target_ssid,
        "security_type": "wpa2-psk",
        "key": target_password
    }

    url = f"http://{cozmo_ip}:80/v1/wifi/connect"

    print(f"Sending Wi-Fi info to Cozmo at {url}...")

    try:
        r = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
        if r.status_code == 200:
            print("✅ Success! Cozmo should now reboot and attempt to join your Wi-Fi.")
        else:
            print(f"⚠️ Failed: {r.status_code} → {r.text}")
    except Exception as e:
        print(f"❌ Error communicating with Cozmo: {e}")

if __name__ == "__main__":
    print("Make sure you are connected to Cozmo's Wi-Fi before running this.")
    cozmo_ip = "172.31.1.188"  # Default IP for Cozmo's hotspot
    connect_to_cozmo_wifi(cozmo_ip)
