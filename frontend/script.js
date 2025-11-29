const taskInput = document.getElementById("taskInput");
const resultsDiv = document.getElementById("results");
const suggestionsDiv = document.getElementById("suggestions");
const strategyEl = document.getElementById("strategy");

document.getElementById("analyzeBtn").addEventListener("click", analyzeTasks);
document.getElementById("suggestBtn").addEventListener("click", suggestTasks);

// Convert textbox JSON into array
function parseTasks() {
  try {
    return JSON.parse(taskInput.value);
  } catch {
    alert("Invalid JSON format!");
    return null;
  }
}

async function analyzeTasks() {
  const tasks = parseTasks();
  if (!tasks) return;

  const res = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(tasks),
  });

  const sorted = await res.json();
  displayResults(sorted);
}

function displayResults(tasks) {
  resultsDiv.innerHTML = "";

  tasks.forEach((t) => {
    const div = document.createElement("div");
    const priority =
      t.score >= 100 ? "priority-high" :
      t.score >= 60 ? "priority-medium" :
      "priority-low";

    div.className = `task-card ${priority}`;
    div.innerHTML = `
      <div class="task-title"><strong>${t.title}</strong> — Score: ${t.score}</div>
      <div class="task-meta">
        Due: ${t.due_date} | Importance: ${t.importance} | Hours: ${t.estimated_hours} | Dependencies: ${t.dependencies}
      </div>
    `;
    resultsDiv.appendChild(div);
  });
}

async function suggestTasks() {
  const tasks = parseTasks();
  if (!tasks) return;

  const res = await fetch("http://127.0.0.1:8000/api/tasks/suggest/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(tasks),
  });

  const data = await res.json();
  suggestionsDiv.innerHTML = "";
  data.explanations.forEach((s) => {
    const div = document.createElement("div");
    div.className = "task-card priority-medium";
    div.textContent = s;
    suggestionsDiv.appendChild(div);
  });
}
