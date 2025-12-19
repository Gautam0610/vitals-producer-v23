# vitals-producer-v23

A Python application that generates and sends random vitals data to a Kafka topic.

## Usage

1.  Clone the repository:
   ```bash
   git clone https://github.com/Gautam0610/vitals-producer-v23.git
   cd vitals-producer-v23
   ```
2.  Set the environment variables in a `.env` file:
   ```
   OUTPUT_TOPIC=<your_kafka_topic>
   BOOTSTRAP_SERVERS=<your_bootstrap_servers>
   SECURITY_PROTOCOL=<your_security_protocol>
   SASL_MECHANISM=<your_sasl_mechanism>
   SASL_USERNAME=<your_sasl_username>
   SASL_PASSWORD=<your_sasl_password>
   INTERVAL_MS=<milliseconds_between_messages>
   ```
3.  Build the Docker image:
   ```bash
   docker build -t vitals-producer .
   ```
4.  Run the Docker container:
   ```bash
   docker run --env-file .env vitals-producer
   ```
