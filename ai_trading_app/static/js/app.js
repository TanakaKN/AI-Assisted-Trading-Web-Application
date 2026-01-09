document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("trade-form");
    const resultDiv = document.getElementById("result");
    const loadingDiv = document.getElementById("loading");
    const button = document.getElementById("analyze-btn");

    // Ensure spinner is hidden on load
    loadingDiv.classList.add("hidden");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const ticker = document.getElementById("ticker").value;

        resultDiv.innerHTML = "";
        loadingDiv.classList.remove("hidden");
        button.disabled = true;

        const formData = new FormData();
        formData.append("ticker", ticker);

        fetch("/analyze/", {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Server error");
            }
            return response.json();
        })
        .then(data => {
            loadingDiv.classList.add("hidden");
            button.disabled = false;

            if (data.error) {
                resultDiv.innerHTML = "Error: " + data.error;
                return;
            }

            const decision = data.decision;

            resultDiv.innerHTML = `
                <h3>Result for ${data.ticker}</h3>
                <strong>Action:</strong> ${decision.action}<br>
                <strong>Confidence:</strong> ${decision.confidence}<br><br>

                <strong>Explanation:</strong>
                <ul>
                    ${decision.explanation.map(e => `<li>${e}</li>`).join("")}
                </ul>

                <em>Model cached: ${data.cached ? "Yes (fast)" : "No (trained now)"}</em>
            `;
        })
        .catch(err => {
            loadingDiv.classList.add("hidden");
            button.disabled = false;
            resultDiv.innerHTML = "Backend error. Check Django terminal.";
            console.error(err);
        });
    });
});
