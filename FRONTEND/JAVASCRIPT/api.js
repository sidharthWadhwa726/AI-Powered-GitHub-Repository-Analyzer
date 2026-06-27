const API_BASE = "http://127.0.0.1:8000";
// Repository Indexing
// POST /repo/index
async function indexRepository(repoUrl) {
    try {
        const response = await fetch(`${API_BASE}/repo/index`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                repo_url: repoUrl
            })
        });
        if (!response.ok) {
           throw new Error("Repository indexing failed.");
        }
        const data = await response.json();
        return data;
    }
    catch (error) {
        console.error(error);
        alert(error.message);
        return null;
    }
}

// Get Architecture
// GET /repo/architecture/{owner}/{repo}

async function fetchArchitecture(owner, repo) {
    try {
        const response = await fetch(
            `${API_BASE}/repo/architecture/${owner}/${repo}`
        );
        if (!response.ok) {
            throw new Error("Unable to load architecture.");
        }
        return await response.json();
    }
    catch (error) {
        console.error(error);
        alert(error.message);
        return null;
    }
}
// Chat API
// POST /chat
async function askQuestion(question, repoId) {
    try {
        const response = await fetch(
            `${API_BASE}/chat`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    question: question,
                    repo_id: repoId
                })
            }
        );
        if (!response.ok) {
            throw new Error("Chat request failed.");
        }
        return await response.json();
    }
    catch (error) {
        console.error(error);
        alert(error.message);
        return null;
    }
}
// Extract owner/repo
function parseRepository(url) {
    const parts = url.split("/");
    return {
        owner: parts[3],
        repo: parts[4]
    };
}
// Global Repository
let CURRENT_REPOSITORY = "";
// Index Complete Flow

async function analyseRepository() {
    const repoUrl = document.getElementById("repoUrl").value.trim();
    if (repoUrl === "") {
        alert("Enter GitHub Repository URL");
        return;
    }
    document.getElementById("repoLoading").classList.add("visible");
    document.getElementById("repoResult").classList.remove("visible");
    const result = await indexRepository(repoUrl);
    document.getElementById("repoLoading").classList.remove("visible");
    if (!result) {
        return;
    }
    CURRENT_REPOSITORY = result.repo;
    document.getElementById("repoResult").classList.add("visible");
    document.getElementById("repoName").textContent = result.repo;
    document.getElementById("repoDesc").textContent =
        "Repository indexed successfully.";
    document.getElementById("statStars").textContent = "-";
    document.getElementById("statForks").textContent = "-";
    document.getElementById("statLang").textContent = "-";
    const parsed = parseRepository(repoUrl);
    const architecture = await fetchArchitecture(
        parsed.owner,
        parsed.repo
    );
    if (architecture) {
        displayArchitecture(architecture);
    }
}


// Chat Wrapper
async function sendQuestion(question) {
    if (CURRENT_REPOSITORY === "") {
        alert("Index repository first.");
        return;
    }
    return await askQuestion(question,CURRENT_REPOSITORY);

}