import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Onboard LED is usually on GPIO2

while True:
    led.value(1)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    led.value(0)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    led.value(1)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    led.value(0)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    led.value(1)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    led.value(0)  # Toggle LED state
    time.sleep(0.1)  # Wait for 500ms
    
    led.value(1)  # Toggle LED state
    time.sleep(0.5)  # Wait for 500ms
    led.value(0)  # Toggle LED state
    time.sleep(0.5)  # Wait for 500ms
    led.value(1)  # Toggle LED state
    time.sleep(0.5)  # Wait for 500ms
    led.value(0)  # Toggle LED state
    time.sleep(0.5)  # Wait for 500ms
    led.value(1)  # Toggle LED state
    time.sleep(0.5)  # Wait for 500ms
    led.value(0)  # Toggle LED state
