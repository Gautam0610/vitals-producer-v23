from kafka import KafkaProducer
import os
import time
import json
import random

# Read environment variables
output_topic = os.environ.get('OUTPUT_TOPIC')
bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
security_protocol = os.environ.get('SECURITY_PROTOCOL', 'PLAINTEXT')
sasl_mechanism = os.environ.get('SASL_MECHANISM', None)
sasl_username = os.environ.get('SASL_USERNAME', None)
sasl_password = os.environ.get('SASL_PASSWORD', None)
interval_ms = int(os.environ.get('INTERVAL_MS', '1000'))

# Configure Kafka producer
producer_config = {
    'bootstrap_servers': bootstrap_servers,
    'value_serializer': lambda v: json.dumps(v).encode('utf-8')
}

if security_protocol and security_protocol.upper() != 'PLAINTEXT':
    producer_config['security_protocol'] = security_protocol.upper()
    if sasl_mechanism:
        producer_config['sasl_mechanism'] = sasl_mechanism.upper()
        producer_config['sasl_plain_username'] = sasl_username
        producer_config['sasl_plain_password'] = sasl_password

producer = KafkaProducer(**producer_config)


# Function to generate random vitals data
def generate_vitals_data():
    body_temp = round(random.uniform(36.5, 37.5), 1)  # Normal body temperature range
    heart_rate = random.randint(60, 100)  # Normal heart rate range
    systolic_pressure = random.randint(90, 140)  # Normal systolic pressure range
    diastolic_pressure = random.randint(60, 90)  # Normal diastolic pressure range
    breaths_per_minute = random.randint(12, 20)  # Normal breaths per minute range
    oxygen_saturation = random.randint(95, 100)  # Normal oxygen saturation range
    blood_glucose = random.randint(70, 140)  # Normal blood glucose range

    vitals_data = {
        'body_temp': body_temp,
        'heart_rate': heart_rate,
        'systolic_pressure': systolic_pressure,
        'diastolic_pressure': diastolic_pressure,
        'breaths_per_minute': breaths_per_minute,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }
    return vitals_data


# Continuously produce vitals data
while True:
    vitals_data = generate_vitals_data()
    producer.send(output_topic, vitals_data)
    print(f"Sent data: {vitals_data}")
    time.sleep(interval_ms / 1000)
