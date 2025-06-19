<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GreenEdge Zero-Carbon Edge Datacenter</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            overflow-x: hidden;
        }

        .header {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header h1 {
            font-size: 2rem;
            font-weight: 700;
            background: linear-gradient(45deg, #00ff88, #00ccff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            color: #b0b0b0;
            margin-top: 0.5rem;
        }

        .dashboard {
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            max-width: 1400px;
            margin: 0 auto;
        }

        .card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 2rem;
            position: relative;
            overflow: hidden;
            transition: all 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 255, 136, 0.2);
            border-color: rgba(0, 255, 136, 0.3);
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #00ff88, #00ccff);
            opacity: 0.8;
        }

        .card h3 {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            color: #00ff88;
        }

        .metric {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        .metric:last-child {
            border-bottom: none;
        }

        .metric-value {
            font-weight: 600;
            font-size: 1.1rem;
        }

        .status-good { color: #00ff88; }
        .status-warning { color: #ffaa00; }
        .status-critical { color: #ff4444; }

        .progress-bar {
            width: 100%;
            height: 8px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            overflow: hidden;
            margin: 0.5rem 0;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #00ff88, #00ccff);
            border-radius: 4px;
            transition: width 0.5s ease;
        }

        .node-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .node {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .node:hover {
            background: rgba(0, 255, 136, 0.1);
        }

        .node-status {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin: 0 auto 0.5rem;
        }

        .energy-visualization {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 1rem 0;
        }

        .solar-panel, .battery, .datacenter {
            text-align: center;
            position: relative;
        }

        .energy-flow {
            width: 50px;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00ff88, transparent);
            animation: flow 2s infinite;
        }

        @keyframes flow {
            0% { opacity: 0.3; }
            50% { opacity: 1; }
            100% { opacity: 0.3; }
        }

        .chart-container {
            height: 200px;
            margin: 1rem 0;
            position: relative;
        }

        .chart {
            width: 100%;
            height: 100%;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.05);
        }

        .alerts {
            max-height: 300px;
            overflow-y: auto;
        }

        .alert {
            background: rgba(255, 170, 0, 0.1);
            border-left: 3px solid #ffaa00;
            padding: 1rem;
            margin: 0.5rem 0;
            border-radius: 5px;
        }

        .timestamp {
            color: #888;
            font-size: 0.8rem;
        }

        .live-indicator {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: #00ff88;
        }

        .pulse {
            width: 8px;
            height: 8px;
            background: #00ff88;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }

        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
            100% { opacity: 1; transform: scale(1); }
        }

        .controls {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }

        .btn {
            background: linear-gradient(45deg, #00ff88, #00ccff);
            border: none;
            color: #000;
            padding: 0.75rem 1.5rem;
            border-radius: 25px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(0, 255, 136, 0.3);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌱 GreenEdge Zero-Carbon Edge Datacenter</h1>
        <p>Solar-Powered Kubernetes Cluster • Raspberry Pi 4 Nodes • 167+ Days Uptime</p>
        <div class="live-indicator">
            <div class="pulse"></div>
            <span>Live Monitoring</span>
        </div>
    </div>

    <div class="dashboard">
        <!-- System Overview -->
        <div class="card">
            <h3>📊 System Overview</h3>
            <div class="metric">
                <span>Cluster Uptime</span>
                <span class="metric-value status-good" id="uptime">167d 14h 32m</span>
            </div>
            <div class="metric">
                <span>Active Nodes</span>
                <span class="metric-value status-good">8/8</span>
            </div>
            <div class="metric">
                <span>Running Pods</span>
                <span class="metric-value status-good" id="pods">142</span>
            </div>
            <div class="metric">
                <span>CPU Utilization</span>
                <span class="metric-value status-good" id="cpu">23%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 23%"></div>
            </div>
            <div class="metric">
                <span>Memory Usage</span>
                <span class="metric-value status-good" id="memory">45%</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 45%"></div>
            </div>
        </div>

        <!-- Energy Management -->
        <div class="card">
            <h3>⚡ Energy Management</h3>
            <div class="energy-visualization">
                <div class="solar-panel">
                    <div style="font-size: 2rem;">☀️</div>
                    <div>Solar Panels</div>
                    <div class="metric-value status-good">2.8kW</div>
                </div>
                <div class="energy-flow"></div>
                <div class="battery">
                    <div style="font-size: 2rem;">🔋</div>
                    <div>Battery Bank</div>
                    <div class="metric-value status-good" id="battery">87%</div>
                </div>
                <div class="energy-flow"></div>
                <div class="datacenter">
                    <div style="font-size: 2rem;">🖥️</div>
                    <div>Edge Cluster</div>
                    <div class="metric-value status-good">1.2kW</div>
                </div>
            </div>
            <div class="metric">
                <span>Carbon Footprint</span>
                <span class="metric-value status-good">0 kg CO₂/day</span>
            </div>
            <div class="metric">
                <span>Energy Efficiency</span>
                <span class="metric-value status-good">98.5%</span>
            </div>
            <div class="metric">
                <span>Grid Independence</span>
                <span class="metric-value status-good">100%</span>
            </div>
        </div>

        <!-- Node Status -->
        <div class="card">
            <h3>🖲️ Kubernetes Nodes</h3>
            <div class="node-grid">
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>master-01</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-01</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-02</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-03</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-04</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-05</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>worker-06</div>
                    <div class="timestamp">Ready</div>
                </div>
                <div class="node">
                    <div class="node-status status-good" style="background: #00ff88;"></div>
                    <div>edge-01</div>
                    <div class="timestamp">Ready</div>
                </div>
            </div>
            <div class="controls">
                <button class="btn" onclick="scaleCluster()">Scale Cluster</button>
                <button class="btn btn-secondary" onclick="drainNode()">Drain Node</button>
            </div>
        </div>

        <!-- Real-time Metrics -->
        <div class="card">
            <h3>📈 Performance Metrics</h3>
            <div class="chart-container">
                <canvas class="chart" id="metricsChart"></canvas>
            </div>
            <div class="metric">
                <span>Network I/O</span>
                <span class="metric-value status-good" id="network">1.2 GB/s</span>
            </div>
            <div class="metric">
                <span>Disk I/O</span>
                <span class="metric-value status-good" id="disk">450 MB/s</span>
            </div>
            <div class="metric">
                <span>Temperature</span>
                <span class="metric-value status-good" id="temp">42°C</span>
            </div>
        </div>

        <!-- Applications -->
        <div class="card">
            <h3>🚀 Running Applications</h3>
            <div class="metric">
                <span>Prometheus (Monitoring)</span>
                <span class="metric-value status-good">Running</span>
            </div>
            <div class="metric">
                <span>Grafana (Visualization)</span>
                <span class="metric-value status-good">Running</span>
            </div>
            <div class="metric">
                <span>Edge ML Inference</span>
                <span class="metric-value status-good">4 replicas</span>
            </div>
            <div class="metric">
                <span>IoT Data Pipeline</span>
                <span class="metric-value status-good">Running</span>
            </div>
            <div class="metric">
                <span>Load Balancer</span>
                <span class="metric-value status-good">NGINX</span>
            </div>
            <div class="controls">
                <button class="btn" onclick="deployApp()">Deploy App</button>
                <button class="btn btn-secondary" onclick="rollback()">Rollback</button>
            </div>
        </div>

        <!-- Alerts & Logs -->
        <div class="card">
            <h3>🔔 System Alerts</h3>
            <div class="alerts">
                <div class="alert">
                    <div>Battery level optimal - switching to grid backup disabled</div>
                    <div class="timestamp">2 hours ago</div>
                </div>
                <div class="alert">
                    <div>Scheduled maintenance window completed successfully</div>
                    <div class="timestamp">1 day ago</div>
                </div>
                <div class="alert">
                    <div>New ML model deployed to edge inference service</div>
                    <div class="timestamp">3 days ago</div>
                </div>
            </div>
            <div class="controls">
                <button class="btn btn-secondary" onclick="viewLogs()">View Logs</button>
                <button class="btn btn-secondary" onclick="exportMetrics()">Export Metrics</button>
            </div>
        </div>
    </div>

    <script>
        // Simulate real-time data updates
        function updateMetrics() {
            // Update CPU
            const cpu = Math.floor(Math.random() * 30 + 15);
            document.getElementById('cpu').textContent = cpu + '%';
            document.querySelector('.progress-fill').style.width = cpu + '%';

            // Update Memory
            const memory = Math.floor(Math.random() * 20 + 40);
            document.getElementById('memory').textContent = memory + '%';
            document.querySelectorAll('.progress-fill')[1].style.width = memory + '%';

            // Update Battery
            const battery = Math.floor(Math.random() * 10 + 85);
            document.getElementById('battery').textContent = battery + '%';

            // Update Pods
            const pods = Math.floor(Math.random() * 20 + 130);
            document.getElementById('pods').textContent = pods;

            // Update Temperature
            const temp = Math.floor(Math.random() * 8 + 38);
            document.getElementById('temp').textContent = temp + '°C';

            // Update Network
            const network = (Math.random() * 0.5 + 1).toFixed(1);
            document.getElementById('network').textContent = network + ' GB/s';

            // Update Disk
            const disk = Math.floor(Math.random() * 100 + 400);
            document.getElementById('disk').textContent = disk + ' MB/s';
        }

        // Update uptime
        function updateUptime() {
            const uptimeEl = document.getElementById('uptime');
            const current = uptimeEl.textContent;
            const parts = current.match(/(\d+)d (\d+)h (\d+)m/);
            if (parts) {
                let minutes = parseInt(parts[3]) + 1;
                let hours = parseInt(parts[2]);
                let days = parseInt(parts[1]);
                
                if (minutes >= 60) {
                    minutes = 0;
                    hours++;
                }
                if (hours >= 24) {
                    hours = 0;
                    days++;
                }
                
                uptimeEl.textContent = `${days}d ${hours}h ${minutes}m`;
            }
        }

        // Button handlers
        function scaleCluster() {
            alert('Scaling cluster... Adding 2 new worker nodes');
        }

        function drainNode() {
            alert('Draining worker-06 for maintenance...');
        }

        function deployApp() {
            alert('Deploying new application to the cluster...');
        }

        function rollback() {
            alert('Rolling back to previous stable version...');
        }

        function viewLogs() {
            alert('Opening Kubernetes logs dashboard...');
        }

        function exportMetrics() {
            alert('Exporting Prometheus metrics to CSV...');
        }

        // Initialize
        setInterval(updateMetrics, 3000);
        setInterval(updateUptime, 60000);
        updateMetrics();

        // Add some visual effects
        document.addEventListener('mousemove', (e) => {
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                if (x >= 0 && x <= rect.width && y >= 0 && y <= rect.height) {
                    const centerX = rect.width / 2;
                    const centerY = rect.height / 2;
                    const rotateX = (y - centerY) / 10;
                    const rotateY = (centerX - x) / 10;
                    
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
                } else {
                    card.style.transform = '';
                }
            });
        });
    </script>
</body>
</html>
