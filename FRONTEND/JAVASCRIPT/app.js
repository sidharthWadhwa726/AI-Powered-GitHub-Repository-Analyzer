// =========================================
// app.js
// Main controller for the frontend
// =========================================

// Global State
let CURRENT_REPO = "";
let CURRENT_OWNER = "";
let CURRENT_NAME = "";
// ===============================
// DOM Elements
// ===============================
const repoTab = document.getElementById("nav-repo");
const archTab = document.getElementById("nav-arch");
const chatTab = document.getElementById("nav-chat");
const repoPane = document.getElementById("pane-repo");
const archPane = document.getElementById("pane-arch");
const chatPane = document.getElementById("pane-chat");
const analyseBtn = document.getElementById("analyseBtn");
const loadingDiv = document.getElementById("repoLoading");
const repoResult = document.getElementById("repoResult");
// =========================================
// Navigation
// =========================================

function switchTab(tab) {
    document
        .querySelectorAll(".tab-nav-btn")
        .forEach(btn => btn.classList.remove("active"));
    document
        .querySelectorAll(".tab-pane")
        .forEach(pane => pane.classList.remove("active"));
    if(tab === "repo"){
        repoTab.classList.add("active");
        repoPane.classList.add("active");
    }
    else if(tab === "arch"){
        archTab.classList.add("active");
        archPane.classList.add("active");
    }
    else{
        chatTab.classList.add("active");
        chatPane.classList.add("active");
    }
}
// =========================================
// Loading
// =========================================

function showLoading(){
    loadingDiv.classList.add("visible");
    repoResult.classList.remove("visible");
}
function hideLoading(){
    loadingDiv.classList.remove("visible");
}
// =========================================
// Repository Indexed Successfully
// =========================================

function repositoryIndexed(data){
    CURRENT_REPO = data.repo;
    repoResult.classList.add("visible");
    document.getElementById("repoName").textContent =
        data.repo;
    document.getElementById("repoDesc").textContent =
        "Repository indexed successfully.";
    document.getElementById("statStars").textContent="-";
    document.getElementById("statForks").textContent="-";
    document.getElementById("statLang").textContent="-";
}
// =========================================
// Analyse Button
// =========================================
analyseBtn.addEventListener("click", async ()=>{
    const url = document.getElementById("repoUrl").value.trim();
    if(url===""){
        alert("Enter a GitHub Repository");
        return;
    }
    const parsed = parseRepository(url);
    CURRENT_OWNER = parsed.owner;
    CURRENT_NAME = parsed.repo;
    showLoading();
    const response = await indexRepository(url);
    hideLoading();
    if(!response){
        return;
    }
    repositoryIndexed(response);
    loadArchitecture();
});



// =========================================
// Tab Clicks
// =========================================

repoTab.addEventListener("click",()=>{
    switchTab("repo");
});

archTab.addEventListener("click",()=>{
    if(CURRENT_REPO===""){
        alert("Index a repository first.");
        return;
    }
    switchTab("arch");
});
chatTab.addEventListener("click",()=>{
    if(CURRENT_REPO===""){
        alert("Index a repository first.");
        return;
    }
    switchTab("chat");
});
// =========================================
// Load Architecture
// =========================================
async function loadArchitecture(){
    const architecture =
        await fetchArchitecture(
            CURRENT_OWNER,
            CURRENT_NAME
        );
    if(!architecture){
        return;
    }
    displayArchitecture(architecture);

}


// =========================================
// Send Button
// =========================================

const sendBtn = document.getElementById("sendBtn");
const chatInput = document.getElementById("chatInput");
sendBtn.addEventListener("click", sendMessage);
chatInput.addEventListener("keydown", function(e){
    if(e.key==="Enter" && !e.shiftKey){
        e.preventDefault();
        sendMessage();
    }
});
// =========================================
// Send Message
// =========================================
async function sendMessage(){
    const question = chatInput.value.trim();
    if(question===""){
        return;
    }
    appendUserMessage(question);
    chatInput.value="";
    showTyping();
    const response = await sendQuestion(question);
    hideTyping();
    if(!response){
        appendBotMessage(
            "Unable to generate response."
        );
        return;
    }
    appendBotMessage(response.answer);
}
// =========================================
// Auto Resize Textarea
// =========================================
chatInput.addEventListener("input",()=>{
    chatInput.style.height="auto";
    chatInput.style.height= chatInput.scrollHeight+"px";
});
// =========================================
// Suggested Questions
// =========================================
const suggestions=[
    "Explain the repository architecture.",
    "What is the execution flow?",
    "Where is the entry point?",
    "Explain the folder structure.",
    "Which files handle API requests?",
    "How does the RAG pipeline work?"
];



function loadSuggestions(){
    const container= document.getElementById("suggestedQs");
    container.innerHTML="";
    suggestions.forEach(question=>{
        const btn=document.createElement("button");
        btn.className="sq-btn";
        btn.textContent=question;
        btn.onclick=()=>{
            chatInput.value=question;
            sendMessage();
        };
        container.appendChild(btn);
    });
}



// =========================================
// Empty State
// =========================================

function enableApplication(){
    document.getElementById("arch-empty").style.display="none";
    document.getElementById("chat-empty").style.display="none";
    document.getElementById("arch-content").style.display="block";
    document.getElementById("chat-content").style.display="flex";
}



// =========================================
// After Repository Indexed
// =========================================

function applicationReady(){
    enableApplication();
    loadSuggestions();
}
// =========================================
// Override repositoryIndexed()
// =========================================
const oldRepositoryIndexed = repositoryIndexed;
repositoryIndexed=function(data){
    oldRepositoryIndexed(data);
    applicationReady();
};



// =========================================
// Initial Page State
// =========================================
window.onload=()=>{
    switchTab("repo");
    document.getElementById("arch-content").style.display="none";
    document.getElementById("chat-content").style.display="none";
};