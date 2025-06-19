# GreenEdge Zero-Carbon Edge Datacenter
# Complete Infrastructure as Code Implementation

#==============================================================================
# 1. KUBERNETES CLUSTER CONFIGURATION
#==============================================================================

# cluster-config/kubeadm-config.yaml
apiVersion: kubeadm.k8s.io/v1beta3
kind: ClusterConfiguration
metadata:
  name: greenedge-cluster
kubernetesVersion: v1.28.0
clusterName: greenedge
networking:
  serviceSubnet: 10.96.0.0/12
  podSubnet: 10.244.0.0/16
apiServer:
  advertiseAddress: 192.168.1.100
  bindPort: 6443
controllerManager:
  extraArgs:
    bind-address: 0.0.0.0
scheduler:
  extraArgs:
    bind-address: 0.0.0.0
etcd:
  local:
    dataDir: /var/lib/etcd
---
# cluster-config/flannel-cni.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: kube-flannel
  labels:
    k8s-app: flannel
    pod-security.kubernetes.io/enforce: privileged
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: kube-flannel-ds
  namespace: kube-flannel
  labels:
    tier: node
    app: flannel
    k8s-app: flannel
spec:
  selector:
    matchLabels:
      app: flannel
  template:
    metadata:
      labels:
        tier: node
        app: flannel
    spec:
      hostNetwork: true
      priorityClassName: system-node-critical
      tolerations:
      - operator: Exists
        effect: NoSchedule
      serviceAccountName: flannel
      containers:
      - name: kube-flannel
        image: docker.io/flannel/flannel:v0.22.0-arm64
        command:
        - /opt/bin/flanneld
        args:
        - --ip-masq
        - --kube-subnet-mgr
        resources:
          requests:
            cpu: "100m"
            memory: "50Mi"
        securityContext:
          privileged: false
          capabilities:
            add: ["NET_ADMIN", "NET_RAW"]
        env:
        - name: POD_NAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: EVENT_QUEUE_DEPTH
          value: "5000"
        volumeMounts:
        - name: run
          mountPath: /run/flannel
        - name: flannel-cfg
          mountPath: /etc/kube-flannel/
        - name: xtables-lock
          mountPath: /run/xtables.lock
      volumes:
      - name: run
        hostPath:
          path: /run/flannel
      - name: flannel-cfg
        configMap:
          name: kube-flannel-cfg
      - name: xtables-lock
        hostPath:
          path: /run/xtables.lock
          type: FileOrCreate

#==============================================================================
# 2. ENERGY MONITORING SYSTEM
#==============================================================================

# energy-monitoring/solar-monitor.py
#!/usr/bin/env python3
"""
Solar Panel and Battery Monitoring System
Collects real-time energy data from solar panels and battery bank
"""

import time
import json
import requests
import RPi.GPIO as GPIO
from datetime import datetime
import logging
from prometheus_client import start_http_server, Gauge, Counter

# Prometheus metrics
SOLAR_POWER = Gauge('solar_power_watts', 'Current solar panel power output')
BATTERY_LEVEL = Gauge('battery_level_percent', 'Battery charge level')
POWER_CONSUMPTION = Gauge('power_consumption_watts', 'Current power consumption')
ENERGY_EFFICIENCY = Gauge('energy_efficiency_percent', 'System energy efficiency')
CARBON_SAVED = Counter('carbon_saved_kg', 'Total CO2 saved in kg')

class EnergyMonitor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_gpio()
        
    def setup_gpio(self):
        """Setup GPIO pins for sensor readings"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN)  # Solar panel sensor
        GPIO.setup(19, GPIO.IN)  # Battery sensor
        GPIO.setup(20, GPIO.IN)  # Power consumption sensor
        
    def read_solar_power(self):
        """Read solar panel power output"""
        # Simulate ADC reading from solar panel current/voltage sensors
        voltage = self.read_adc(0) * 3.3 / 1024  # Convert ADC to voltage
        current = self.read_adc(1) * 3.3 / 1024  # Convert ADC to current
        power = voltage * current * 100  # Scale to realistic wattage
        return max(0, min(power, 3000))  # Cap at 3kW
    
    def read_battery_level(self):
        """Read battery bank charge level"""
        battery_voltage = self.read_adc(2) * 3.3 / 1024
        # Convert voltage to percentage (12V system)
        percentage = ((battery_voltage - 10.5) / (14.4 - 10.5)) * 100
        return max(0, min(percentage, 100))
    
    def read_power_consumption(self):
        """Read current power consumption"""
        consumption_voltage = self.read_adc(3) * 3.3 / 1024
        power = consumption_voltage * 500  # Scale to realistic consumption
        return max(0, min(power, 2000))  # Cap at 2kW
    
    def read_adc(self, channel):
        """Simulate ADC reading (replace with actual ADC code)"""
        import random
        return random.randint(200, 900)
    
    def calculate_efficiency(self, solar_power, consumption):
        """Calculate energy efficiency"""
        if solar_power > 0:
            return min((consumption / solar_power) * 100, 100)
        return 0
    
    def update_metrics(self):
        """Update Prometheus metrics"""
        solar_power = self.read_solar_power()
        battery_level = self.read_battery_level()
        consumption = self.read_power_consumption()
        efficiency = self.calculate_efficiency(solar_power, consumption)
        
        SOLAR_POWER.set(solar_power)
        BATTERY_LEVEL.set(battery_level)
        POWER_CONSUMPTION.set(consumption)
        ENERGY_EFFICIENCY.set(efficiency)
        
        # Calculate carbon savings (0.4kg CO2 per kWh saved)
        carbon_saved = (solar_power / 1000) * 0.4
        CARBON_SAVED.inc(carbon_saved)
        
        self.logger.info(f"Solar: {solar_power}W, Battery: {battery_level}%, "
                        f"Consumption: {consumption}W, Efficiency: {efficiency}%")

def main():
    logging.basicConfig(level=logging.INFO)
    monitor = EnergyMonitor()
    
    # Start Prometheus metrics server
    start_http_server(8000)
    
    try:
        while True:
            monitor.update_metrics()
            time.sleep(30)  # Update every 30 seconds
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    main()

#==============================================================================
# 3. KUBERNETES MONITORING STACK
#==============================================================================

# monitoring/prometheus-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: monitoring
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
      evaluation_interval: 15s
    
    rule_files:
      - "/etc/prometheus/rules/*.yml"
    
    alerting:
      alertmanagers:
        - static_configs:
            - targets:
              - alertmanager:9093
    
    scrape_configs:
      - job_name: 'prometheus'
        static_configs:
          - targets: ['localhost:9090']
      
      - job_name: 'kubernetes-apiservers'
        kubernetes_sd_configs:
          - role: endpoints
        scheme: https
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
        relabel_configs:
          - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
            action: keep
            regex: default;kubernetes;https
      
      - job_name: 'kubernetes-nodes'
        kubernetes_sd_configs:
          - role: node
        scheme: https
        tls_config:
          ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
        relabel_configs:
          - action: labelmap
            regex: __meta_kubernetes_node_label_(.+)
          - target_label: __address__
            replacement: kubernetes.default.svc:443
          - source_labels: [__meta_kubernetes_node_name]
            regex: (.+)
            target_label: __metrics_path__
            replacement: /api/v1/nodes/${1}/proxy/metrics
      
      - job_name: 'kubernetes-pods'
        kubernetes_sd_configs:
          - role: pod
        relabel_configs:
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
            action: keep
            regex: true
          - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
            action: replace
            target_label: __metrics_path__
            regex: (.+)
      
      - job_name: 'energy-monitor'
        static_configs:
          - targets: ['energy-monitor:8000']
        scrape_interval: 30s
      
      - job_name: 'node-exporter'
        kubernetes_sd_configs:
          - role: endpoints
        relabel_configs:
          - source_labels: [__meta_kubernetes_endpoints_name]
            regex: 'node-exporter'
            action: keep

---
# monitoring/prometheus-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      serviceAccountName: prometheus
      containers:
      - name: prometheus
        image: prom/prometheus:v2.47.0
        args:
          - '--config.file=/etc/prometheus/prometheus.yml'
          - '--storage.tsdb.path=/prometheus/'
          - '--web.console.libraries=/etc/prometheus/console_libraries'
          - '--web.console.templates=/etc/prometheus/consoles'
          - '--storage.tsdb.retention.time=200h'
          - '--web.enable-lifecycle'
        ports:
        - containerPort: 9090
        resources:
          requests:
            cpu: 500m
            memory: 500M
          limits:
            cpu: 1
            memory: 1Gi
        volumeMounts:
        - name: prometheus-config-volume
          mountPath: /etc/prometheus/
        - name: prometheus-storage-volume
          mountPath: /prometheus/
      volumes:
      - name: prometheus-config-volume
        configMap:
          defaultMode: 420
          name: prometheus-config
      - name: prometheus-storage-volume
        emptyDir: {}

#==============================================================================
# 4. EDGE APPLICATIONS
#==============================================================================

# edge-apps/ml-inference-service.py
#!/usr/bin/env python3
"""
Edge ML Inference Service
Processes IoT sensor data with TensorFlow Lite models
"""

from flask import Flask, request, jsonify
import numpy as np
import tflite_runtime.interpreter as tflite
import json
import logging
from datetime import datetime
import threading
import queue

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

class MLInferenceService:
    def __init__(self):
        self.model_path = "/models/sensor_anomaly_detection.tflite"
        self.interpreter = None
        self.input_details = None
        self.output_details = None
        self.load_model()
        
    def load_model(self):
        """Load TensorFlow Lite model"""
        try:
            self.interpreter = tflite.Interpreter(model_path=self.model_path)
            self.interpreter.allocate_tensors()
            self.input_details = self.interpreter.get_input_details()
            self.output_details = self.interpreter.get_output_details()
            logging.info("ML model loaded successfully")
        except Exception as e:
            logging.error(f"Failed to load ML model: {e}")
    
    def preprocess_data(self, sensor_data):
        """Preprocess sensor data for inference"""
        # Normalize sensor readings
        normalized_data = np.array(sensor_data, dtype=np.float32)
        normalized_data = (normalized_data - np.mean(normalized_data)) / np.std(normalized_data)
        return normalized_data.reshape(1, -1)
    
    def predict(self, sensor_data):
        """Run inference on sensor data"""
        if self.interpreter is None:
            return {"error": "Model not loaded"}
        
        try:
            # Preprocess input data
            input_data = self.preprocess_data(sensor_data)
            
            # Set input tensor
            self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
            
            # Run inference
            self.interpreter.invoke()
            
            # Get output
            output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
            
            # Process results
            anomaly_score = float(output_data[0][0])
            is_anomaly = anomaly_score > 0.5
            
            return {
                "anomaly_score": anomaly_score,
                "is_anomaly": is_anomaly,
                "timestamp": datetime.now().isoformat(),
                "confidence": float(abs(anomaly_score - 0.5) * 2)
            }
        except Exception as e:
            logging.error(f"Inference error: {e}")
            return {"error": str(e)}

# Initialize service
ml_service = MLInferenceService()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "ml-inference"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        sensor_data = data.get('sensor_data', [])
        
        if not sensor_data:
            return jsonify({"error": "No sensor data provided"}), 400
        
        result = ml_service.predict(sensor_data)
        return jsonify(result)
    
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/metrics', methods=['GET'])
def metrics():
    # Prometheus metrics endpoint
    return "# ML Inference Service Metrics\n", 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

#==============================================================================
# 5. IOT DATA PIPELINE
#==============================================================================

# iot-pipeline/data-collector.py
#!/usr/bin/env python3
"""
IoT Data Collection Pipeline
Collects data from various sensors and forwards to processing services
"""

import asyncio
import aiohttp
import json
import logging
from datetime import datetime
import paho.mqtt.client as mqtt
import redis
import os

class IoTDataCollector:
    def __init__(self):
        self.mqtt_client = mqtt.Client()
        self.redis_client = redis.Redis(host='redis', port=6379, db=0)
        self.ml_service_url = "http://ml-inference:8080/predict"
        self.setup_mqtt()
        
    def setup_mqtt(self):
        """Setup MQTT client for sensor data"""
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect("mqtt-broker", 1883, 60)
        
    def on_connect(self, client, userdata, flags, rc):
        logging.info(f"MQTT connected with result code {rc}")
        # Subscribe to sensor topics
        topics = [
            "sensors/temperature/+",
            "sensors/humidity/+", 
            "sensors/pressure/+",
            "sensors/vibration/+",
            "energy/solar/+",
            "energy/battery/+"
        ]
        for topic in topics:
            client.subscribe(topic)
    
    def on_message(self, client, userdata, msg):
        """Process incoming MQTT messages"""
        try:
            topic = msg.topic
            payload = json.loads(msg.payload.decode())
            
            # Add timestamp and topic to payload
            payload['timestamp'] = datetime.now().isoformat()
            payload['topic'] = topic
            
            # Store in Redis for real-time access
            self.redis_client.setex(
                f"sensor_data:{topic}", 
                300,  # 5 minute TTL
                json.dumps(payload)
            )
            
            # Send to ML inference if it's sensor data
            if topic.startswith('sensors/'):
                asyncio.create_task(self.send_to_ml_service(payload))
                
            logging.info(f"Processed message from {topic}")
            
        except Exception as e:
            logging.error(f"Error processing message: {e}")
    
    async def send_to_ml_service(self, sensor_data):
        """Send sensor data to ML inference service"""
        try:
            # Extract numeric values for ML processing
            sensor_values = []
            if 'temperature' in sensor_data:
                sensor_values.append(sensor_data['temperature'])
            if 'humidity' in sensor_data:
                sensor_values.append(sensor_data['humidity'])
            if 'pressure' in sensor_data:
                sensor_values.append(sensor_data['pressure'])
            if 'vibration' in sensor_data:
                sensor_values.append(sensor_data['vibration'])
            
            if sensor_values:
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        self.ml_service_url,
                        json={"sensor_data": sensor_values}
                    ) as response:
                        result = await response.json()
                        
                        # Store ML results
                        self.redis_client.setex(
                            f"ml_results:{sensor_data['topic']}", 
                            300,
                            json.dumps(result)
                        )
                        
                        # Alert if anomaly detected
                        if result.get('is_anomaly'):
                            await self.send_alert(sensor_data, result)
                            
        except Exception as e:
            logging.error(f"Error sending to ML service: {e}")
    
    async def send_alert(self, sensor_data, ml_result):
        """Send alert for detected anomalies"""
        alert = {
            "type": "anomaly_detected",
            "sensor": sensor_data['topic'],
            "timestamp": sensor_data['timestamp'],
            "anomaly_score": ml_result['anomaly_score'],
            "confidence": ml_result['confidence']
        }
        
        # Store alert in Redis
        self.redis_client.lpush("alerts", json.dumps(alert))
        
        # Send to alerting service (webhook, Slack, etc.)
        logging.warning(f"ANOMALY DETECTED: {alert}")
    
    def run(self):
        """Start the data collection service"""
        logging.info("Starting IoT Data Collector")
        self.mqtt_client.loop_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    collector = IoTDataCollector()
    collector.run()

#==============================================================================
# 6. DEPLOYMENT CONFIGURATIONS
#==============================================================================

# deployment/greenedge-namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: greenedge
  labels:
    name: greenedge
    tier: edge-computing

---
# deployment/ml-inference-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-inference-service
  namespace: greenedge
spec:
  replicas: 4
  selector:
    matchLabels:
      app: ml-inference
  template:
    metadata:
      labels:
        app: ml-inference
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: ml-inference
        image: greenedge/ml-inference:v1.2.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: ml-models
          mountPath: /models
      volumes:
      - name: ml-models
        configMap:
          name: ml-models

---
# deployment/iot-pipeline-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: iot-data-pipeline
  namespace: greenedge
spec:
  replicas: 2
  selector:
    matchLabels:
      app: iot-pipeline
  template:
    metadata:
      labels:
        app: iot-pipeline
    spec:
      containers:
      - name: data-collector
        image: greenedge/iot-pipeline:v1.1.0
        env:
        - name: REDIS_HOST
          value: "redis"
        - name: MQTT_BROKER
          value: "mqtt-broker"
        - name: ML_SERVICE_URL
          value: "http://ml-inference:8080"
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 256Mi

---
# deployment/energy-monitor-deployment.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: energy-monitor
  namespace: greenedge
spec:
  selector:
    matchLabels:
      app: energy-monitor
  template:
    metadata:
      labels:
        app: energy-monitor
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
    spec:
      hostNetwork: true
      containers:
      - name: energy-monitor
        image: greenedge/energy-monitor:v1.0.0
        ports:
        - containerPort: 8000
        resources:
          requests:
            cpu: 50m
            memory: 32Mi
          limits:
            cpu: 100m
            memory: 128Mi
        volumeMounts:
        - name: dev
          mountPath: /dev
        securityContext:
          privileged: true
      volumes:
      - name: dev
        hostPath:
          path: /dev

#==============================================================================
# 7. INFRASTRUCTURE AUTOMATION
#==============================================================================

# scripts/cluster-setup.sh
#!/bin/bash
"""
GreenEdge Cluster Setup Script
Automates the deployment of the entire zero-carbon edge datacenter
"""

set -e

echo "🌱 Setting up GreenEdge Zero-Carbon Edge Datacenter"

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh
sudo usermod -aG docker $USER

# Install Kubernetes components
sudo apt install -y apt-transport-https ca-certificates curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
sudo apt install -y kubelet kubeadm kubectl

# Initialize Kubernetes cluster
sudo kubeadm init --config=cluster-config/kubeadm-config.yaml

# Configure kubectl
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install CNI (Flannel)
kubectl apply -f cluster-config/flannel-cni.yaml

# Create namespaces
kubectl apply -f deployment/greenedge-namespace.yaml
kubectl create namespace monitoring

# Install Prometheus
kubectl apply -f monitoring/prometheus-config.yaml
kubectl apply -f monitoring/prometheus-deployment.yaml

# Deploy applications
kubectl apply -f deployment/ml-inference-deployment.yaml
kubectl apply -f deployment/iot-pipeline-deployment.yaml
kubectl apply -f deployment/energy-monitor-deployment.yaml

# Install Grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm install grafana grafana/grafana --namespace monitoring

echo "✅ GreenEdge cluster setup complete!"
echo "📊 Access Grafana: kubectl port-forward -n monitoring svc/grafana 3000:80"
echo "📈 Access Prometheus: kubectl port-forward -n monitoring svc/prometheus 9090:9090"

# scripts/deploy-app.sh
#!/bin/bash
"""
Application Deployment Script
"""

APP_NAME=$1
VERSION=$2

if [ -z "$APP_NAME" ] || [ -z "$VERSION" ]; then
    echo "Usage: ./deploy-app.sh <app-name> <version>"
    exit 1
fi

echo "🚀 Deploying $APP_NAME version $VERSION"

# Build and push Docker image
docker build -t greenedge/$APP_NAME:$VERSION .
docker push greenedge/$APP_NAME:$VERSION

# Update deployment
kubectl set image deployment/$APP_NAME $APP_NAME=greenedge/$APP_NAME:$VERSION -n greenedge

# Wait for rollout
kubectl rollout status deployment/$APP_NAME -n greenedge

echo "✅ $APP_NAME deployed successfully!"

#==============================================================================
# 8. MONITORING AND ALERTING
#==============================================================================

# monitoring/alerting-rules.yaml
groups:
- name: greenedge.rules
  rules:
  - alert: HighCPUUsage
    expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High CPU usage detected"
      description: "CPU usage is above 80% for more than 5 minutes"

  - alert: LowBatteryLevel
    expr: battery_level_percent < 20
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "Low battery level"
      description: "Battery level is below 20%"

  - alert: SolarPowerDrop
    expr: solar_power_watts < 500
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "Solar power output low"
      description: "Solar power output has been below 500W for 10 minutes"

  - alert: PodCrashLooping
    expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Pod crash looping"
      description: "Pod {{ $labels.pod }} is crash looping"

  - alert: NodeDown
    expr: up{job="kubernetes-nodes"} == 0
    for: 1m
    labels:
      severity: critical
    annotations:
      summary: "Node is down"
      description: "Node {{ $labels.instance }} has been down for more than 1 minute"

#==============================================================================
# 9. DOCKER CONFIGURATIONS
#==============================================================================

# Dockerfile for ML Inference Service
FROM python:3.9-slim-buster

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY edge-apps/ml-inference-service.py .
COPY models/ /models/

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["python", "ml-inference-service.py"]

# docker-compose.yml for local development
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  mqtt-broker:
    image: eclipse-mosquitto:2
    ports:
      - "1883:1883"
      - "9001:9001"
    volumes:
      - ./config/mosquitto.conf:/mosquitto/config/mosquitto.conf

  ml-inference:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8080:8080"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis

  iot-pipeline:
    build:
      context: .
      dockerfile: Dockerfile.iot
    depends_on:
      - redis
      - mqtt-broker
      - ml-inference
    environment:
      - REDIS_HOST=redis
      - MQTT_BROKER=mqtt-broker
      - ML_SERVICE_URL=http://ml-inference:8080

  grafana:
    image: grafana/grafana:10.0.0
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana

  prometheus:
    image: prom/prometheus:v2.47.0
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus

volumes:
  redis_data:
  grafana_data:
  prometheus_
