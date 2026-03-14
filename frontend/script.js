const API = "http://localhost:5000/api";

// ── PAGE NAVIGATION ──────────────────────────────────────────
function showPage(name, el) {
  document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(n => n.classList.remove("active"));
  document.getElementById("page-" + name).classList.add("active");
  if (el) el.classList.add("active");
  if (name === "dashboard") loadDashboard();
  if (name === "history")   loadHistory();
}

// ── DASHBOARD ────────────────────────────────────────────────
async function loadDashboard() {
  try {
    const res      = await fetch(`${API}/sessions`);
    const sessions = await res.json();

    if (!sessions.length) {
      document.getElementById("dashboard-empty").style.display = "flex";
      document.getElementById("dashboard-data").style.display  = "none";
      return;
    }

    const latest = sessions[0];
    document.getElementById("dashboard-empty").style.display = "none";
    document.getElementById("dashboard-data").style.display  = "block";
    document.getElementById("d-stress").textContent  = latest.stress_risk  + "%";
    document.getElementById("d-study").textContent   = latest.study_hours  + " hrs";
    document.getElementById("d-sleep").textContent   = latest.sleep_hours  + " hrs";
    document.getElementById("d-mood").textContent    = latest.mood;
    document.getElementById("d-burnout").textContent = latest.burnout_risk + "%";

    const circle = document.getElementById("gauge-circle");
    const circ   = 2 * Math.PI * 80;
    const offset = circ - (latest.burnout_risk / 100) * circ;
    circle.style.strokeDashoffset = offset;
    const c = latest.burnout_risk > 70 ? "#f43f5e" : latest.burnout_risk > 40 ? "#f59e0b" : "#10b981";
    circle.style.stroke = c;

  } catch (err) { console.error("Dashboard load failed:", err); }
}

// ── STRESS PREDICTOR ─────────────────────────────────────────
document.getElementById("stress-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const btn = document.getElementById("predict-btn");
  btn.disabled    = true;
  btn.textContent = "Analyzing...";

  const body = {
    studyHours:      parseFloat(document.getElementById("study-hours").value),
    sleepHours:      parseFloat(document.getElementById("sleep-hours").value),
    mood:            document.getElementById("mood").value,
    assignmentsDue:  parseInt(document.getElementById("assignments").value)  || 0,
    exerciseMinutes: parseInt(document.getElementById("exercise").value)     || 0
  };

  try {
    const res = await fetch(`${API}/predict-stress`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(body)
    });
    const result = await res.json();
    showResult(result, body);
  } catch (err) {
    alert("Prediction failed. Is the backend running?");
    console.error(err);
  }

  try {
    await fetch(`${API}/sessions`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        studyHours:  body.studyHours,
        sleepHours:  body.sleepHours,
        mood:        body.mood,
        stressRisk:  0,
        burnoutRisk: 0
      })
    });
  } catch (err) {
    console.error("Session save failed:", err);
  }

  btn.disabled    = false;
  btn.textContent = "Run Prediction Model →";
});

function showResult(r, input) {
  document.getElementById("result-empty").style.display = "none";
  const card = document.getElementById("result-card");
  card.style.display = "block";

  const badge = document.getElementById("result-badge");
  badge.textContent = r.level.toUpperCase() + " RISK";
  badge.className   = "badge badge-" + r.level;

  document.getElementById("res-stress").textContent  = r.stressRisk  + "%";
  document.getElementById("res-burnout").textContent = r.burnoutRisk + "%";
  document.getElementById("res-message").textContent = r.message;

  setTimeout(() => {
    document.getElementById("bar-stress").style.width  = r.stressRisk  + "%";
    document.getElementById("bar-burnout").style.width = r.burnoutRisk + "%";
  }, 50);

  const list = document.getElementById("rec-list");
  list.innerHTML = r.recommendations.map(rec => `<li>${rec}</li>`).join("");
}

// ── STUDY PLANNER ────────────────────────────────────────────
document.getElementById("planner-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const btn = document.getElementById("plan-btn");
  btn.disabled    = true;
  btn.textContent = "Generating...";

  const subjects = document.getElementById("subjects").value
    .split(",").map(s => s.trim()).filter(Boolean);

  const body = {
    stressLevel:    parseInt(document.getElementById("stress-range").value),
    availableHours: parseFloat(document.getElementById("plan-hours").value),
    subjects:       subjects
  };

  try {
    const res = await fetch(`${API}/generate-plan`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify(body)
    });

    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.error || "Server error");
    }

    const plan = await res.json();
    showPlan(plan);
  } catch (err) {
    alert("Failed to generate plan. Error: " + err.message);
    console.error(err);
  }

  btn.disabled    = false;
  btn.textContent = "Generate Schedule →";
});

function showPlan(plan) {
  document.getElementById("plan-empty").style.display = "none";
  const result = document.getElementById("plan-result");
  result.style.display = "block";

  document.getElementById("plan-message").textContent = plan.recommendation || "";
  document.getElementById("plan-total").textContent   = "⏱ Total: " + plan.totalStudyTime + " mins";
  document.getElementById("plan-breaks").textContent  = "☕ Break: " + plan.breakDuration  + " mins between sessions";

  const colors = { Focused: "#10b981", Moderate: "#f59e0b", Light: "#f43f5e" };
  const color  = colors[plan.intensity] || "#a855f7";

  document.getElementById("plan-items").innerHTML = plan.schedule.map((item) => `
    <div class="plan-item">
      <div class="plan-item-left">
        <div class="plan-num">${item.slot}</div>
        <div>
          <div class="plan-subject">${item.subject}</div>
          <div class="plan-duration">⏰ ${item.start} – ${item.end} (${item.duration} mins)</div>
        </div>
      </div>
      <span class="badge" style="background:${color}22;color:${color};border:1px solid ${color}44">
        ${item.type}
      </span>
    </div>
  `).join("");
}

// ── VOICE EMOTION ────────────────────────────────────────────
async function detectEmotion() {
  const btn   = document.getElementById("mic-btn");
  const label = document.getElementById("mic-label");
  btn.disabled      = true;
  btn.textContent   = "⏳";
  label.textContent = "Analyzing vocal patterns...";

  try {
    const res = await fetch(`${API}/detect-emotion`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ text: "analyzing" })
    });

    if (!res.ok) throw new Error("Server error " + res.status);
    const result = await res.json();
    showEmotion(result);

  } catch (err) {
    alert("Emotion detection failed. Is backend running?");
    btn.disabled      = false;
    btn.textContent   = "🎙️";
    label.textContent = "Click to initialize analysis";
    console.error(err);
  }
}

function showEmotion(r) {
  document.getElementById("emotion-record").style.display = "none";
  const resultEl = document.getElementById("emotion-result");
  resultEl.style.display = "block";

  const colors = { Calm:"#10b981", Focused:"#10b981", Stressed:"#f43f5e", Anxious:"#f59e0b", Fatigued:"#f59e0b" };
  const badge  = document.getElementById("emotion-badge");
  badge.textContent      = "ANALYSIS COMPLETE";
  badge.style.background = colors[r.emotion] + "22";
  badge.style.color      = colors[r.emotion];
  badge.style.border     = `1px solid ${colors[r.emotion]}44`;

  document.getElementById("emotion-name").textContent       = r.emotion;
  document.getElementById("emotion-confidence").textContent = r.confidence + "% Confidence Match";
  document.getElementById("emotion-rec").textContent        = r.recommendation;
}

function resetEmotion() {
  document.getElementById("emotion-result").style.display = "none";
  document.getElementById("emotion-record").style.display = "flex";
  document.getElementById("mic-btn").disabled             = false;
  document.getElementById("mic-btn").textContent          = "🎙️";
  document.getElementById("mic-label").textContent        = "Click to initialize analysis";
}

// ── HISTORY ──────────────────────────────────────────────────
async function loadHistory() {
  const tbody = document.getElementById("history-body");
  tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:40px;opacity:0.5">Loading...</td></tr>`;

  try {
    const res      = await fetch(`${API}/sessions`);
    const sessions = await res.json();

    if (!sessions.length) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:40px;opacity:0.5">No sessions yet. Run a prediction first.</td></tr>`;
      return;
    }

    const colors = r => r > 70 ? "#f43f5e" : r > 40 ? "#f59e0b" : "#10b981";
    tbody.innerHTML = sessions.map(s => `
      <tr>
        <td>${new Date(s.created_at || s.createdAt).toLocaleString()}</td>
        <td>${s.study_hours  || s.studyHours}  hrs</td>
        <td>${s.sleep_hours  || s.sleepHours}  hrs</td>
        <td style="text-transform:capitalize">${s.mood}</td>
        <td><span style="color:${colors(s.stress_risk  || s.stressRisk)};font-weight:700">${s.stress_risk  || s.stressRisk}%</span></td>
        <td><span style="color:${colors(s.burnout_risk || s.burnoutRisk)};font-weight:700">${s.burnout_risk || s.burnoutRisk}%</span></td>
      </tr>
    `).join("");

  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:40px;color:#f43f5e">Failed to load sessions.</td></tr>`;
    console.error(err);
  }
}

loadDashboard();
