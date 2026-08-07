async function sendMessage() {

    const input = document.getElementById("user-input");
    const restaurant = document.getElementById("restaurant");
    const chatBox = document.getElementById("chat-box");

    const text = input.value.trim();

    if (!text) return;

    const userDiv = document.createElement("div");

    userDiv.className = "message user-message";

    userDiv.innerHTML = `
        <strong>${restaurant.value}</strong><br>
        ${escapeHtml(text)}
    `;

    chatBox.appendChild(userDiv);

    input.value = "";

    const loadingDiv = document.createElement("div");

    loadingDiv.className = "message bot-message";

    loadingDiv.innerHTML = `
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chatBox.appendChild(loadingDiv);

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                restaurant: restaurant.value,
                message: text
            })

        });

        const data = await response.json();

        loadingDiv.remove();

        if (!response.ok || data.error) {
            throw new Error(data.error || "Analysis could not be completed.");
        }

        const botDiv = document.createElement("div");

        botDiv.className = "message bot-message";

        botDiv.innerHTML = `
    <div class="ai-card">

        <div class="ai-header">
            🤖 FOOD SAFETY AI REPORT
        </div>

        <div class="score-card"
     style="--score:${data.score}">

            <div class="score-title">
                Food Safety Score
            </div>

            <div class="score-value">
                ${escapeHtml(String(data.score))}%
            </div>

        </div>
<div class="metrics-grid">

    <div class="metric-card">
        <div class="metric-icon">⭐</div>
        <div class="metric-value">${escapeHtml(String(data.metrics.rating))}</div>
        <div class="metric-label">Rating</div>
    </div>

    <div class="metric-card">
        <div class="metric-icon">📦</div>
        <div class="metric-value">${escapeHtml(String(data.metrics.orders))}</div>
        <div class="metric-label">Orders</div>
    </div>

    <div class="metric-card">
        <div class="metric-icon">⚠️</div>
        <div class="metric-value">${escapeHtml(String(data.metrics.complaints))}</div>
        <div class="metric-label">Complaints</div>
    </div>

    <div class="metric-card">
        <div class="metric-icon">💸</div>
        <div class="metric-value">${escapeHtml(String(data.metrics.refunds))}</div>
        <div class="metric-label">Refunds</div>
    </div>

</div>
        <div class="report-section">

            <h3>⚠️ Risk Level</h3>

            <div class="risk-badge ${getRiskClass(data.risk)}">
    ${escapeHtml(data.risk)}
</div>

        </div>

        <div class="report-section">

            <h3>🚨 Detected Issues</h3>

            <p>${data.issues && data.issues.length ? escapeHtml(data.issues.join(", ")) : "None"}</p>

        </div>

        <div class="report-section">

            <h3>🤖 AI Assessment</h3>

            <p>${escapeHtml(data.analysis).replace(/\n/g, "<br>")}</p>

        </div>

    </div>
`;

        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        loadingDiv.remove();

        const errorDiv = document.createElement("div");

        errorDiv.className = "message bot-message";

        errorDiv.innerHTML = `
            ❌ ${error.message || "Failed to contact the analysis service."}
        `;

        chatBox.appendChild(errorDiv);
    }
}

function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, character => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;"
    }[character]));
}

document
    .getElementById("user-input")
    .addEventListener("keydown", function(event) {

        if (event.key === "Enter") {

            event.preventDefault();

            sendMessage();
        }

    });
    function getRiskClass(risk) {

    if (risk.includes("High Confidence"))
        return "risk-green";

    if (risk.includes("Minor Concerns"))
        return "risk-yellow";

    if (risk.includes("Consume With Caution"))
        return "risk-orange";

    if (risk.includes("High Risk"))
        return "risk-red";

    return "risk-darkred";
}
