import requests
import time

# Setting the logs up
def log(msg):
    timestamp = time.strftime("[%H:%M:%S]")
    print(f"{timestamp} {msg}")

# Get site URL from user
while True:
    site = input("Which site do you want to track?: ").strip()
    if site:
        break
    print("Input cannot be empty.")

# Time between checks
timing = float(input("How much time between each check?: "))
timing_mode = input("Seconds/minutes/hours/days? (s/m/h/d): ").strip().lower()

# Number of cycles
cycles = int(input("How many cycles?: "))

# Time multiplier map
multipliers = {
    "s": 1,
    "m": 60,
    "h": 3600,
    "d": 86400
}
wait = timing * multipliers.get(timing_mode, 1)

# Main check loop
while cycles > 0:
    try:
        response = requests.get(site)
        log(f"Status: {response.status_code}")
    except Exception as e:
        log(f"Error: {e}")

    time.sleep(wait)
    cycles -= 1
