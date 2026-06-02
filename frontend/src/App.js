import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const [activeThreats, setActiveThreats] = useState(0);
  const [criticalIncidents, setCriticalIncidents] = useState(0);
  const [attackVolume, setAttackVolume] = useState(0);
  const [securityHealth, setSecurityHealth] = useState(0);

  const [threats, setThreats] = useState([]);
  const [malware, setMalware] = useState([]);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/threats")
      .then((res) => {
        setActiveThreats(res.data.length);
      })
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/api-events")
      .then((res) => {
        setCriticalIncidents(res.data.length);
        setAttackVolume(res.data.length);
      })
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/cloud-events")
      .then((res) => {
        const score =
          100 -
          res.data.filter(
            (item) => item.severity === "Critical"
          ).length * 5;

        setSecurityHealth(score);
      })
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/threat-categories")
      .then((res) => {
        setThreats(res.data);
      })
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/malware")
      .then((res) => {
        setMalware(res.data);
      })
      .catch(console.error);

    axios
      .get("http://127.0.0.1:8000/user-risk")
      .then((res) => {
        setUsers(res.data.slice(0, 10));
      })
      .catch(console.error);

  }, []);

  const chartData = {
    labels: threats.map((item) => item.attack_type),
    datasets: [
      {
        label: "Attack Count",
        data: threats.map((item) => item.attack_count),
        backgroundColor: "#00ffff",
      },
    ],
  };

  return (
    <div className="dashboard">
      <h1 className="title">ShadowNet SOC Command Center</h1>

      <div className="cards">
        <div className="card">
          <h3>Active Threats</h3>
          <p>{activeThreats}</p>
        </div>

        <div className="card">
          <h3>Critical Incidents</h3>
          <p>{criticalIncidents}</p>
        </div>

        <div className="card">
          <h3>Attack Volume</h3>
          <p>{attackVolume}</p>
        </div>

        <div className="card">
          <h3>Security Health Score</h3>
          <p>{securityHealth}</p>
        </div>
      </div>

      <h2>Threat Categories</h2>

      <table>
        <thead>
          <tr>
            <th>Attack Type</th>
            <th>Count</th>
          </tr>
        </thead>

        <tbody>
          {threats.map((item, index) => (
            <tr key={index}>
              <td>{item.attack_type}</td>
              <td>{item.attack_count}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Attack Trends</h2>

      <div
        style={{
          width: "80%",
          margin: "30px auto",
          background: "#16233b",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        <Bar data={chartData} />
      </div>

      <h2>Malware Intelligence</h2>

      <table>
        <thead>
          <tr>
            <th>Malware Type</th>
            <th>Count</th>
            <th>Severity</th>
          </tr>
        </thead>

        <tbody>
          {malware.map((item, index) => (
            <tr key={index}>
              <td>{item.malware_type}</td>
              <td>{item.malware_count}</td>
              <td>{item.severity}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>User Risk Analytics</h2>

      <table>
        <thead>
          <tr>
            <th>User ID</th>
            <th>Login Attempts</th>
            <th>Failed Attempts</th>
          </tr>
        </thead>

        <tbody>
          {users.map((user, index) => (
            <tr key={index}>
              <td>{user.user_id}</td>
              <td>{user.login_attempts}</td>
              <td>{user.failed_attempts}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;