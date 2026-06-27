// =========================================
// overview.js
// Repository Overview
// -----------------------------------------
// DOM Elements
// -----------------------------------------
const repoAvatar = document.getElementById("repoAvatar");
const repoName = document.getElementById("repoName");
const repoDescription = document.getElementById("repoDesc");
const statStars = document.getElementById("statStars");
const statForks = document.getElementById("statForks");
const statLanguage = document.getElementById("statLang");
// =========================================
// Update Repository Card
// =========================================
function updateRepositoryOverview(data){
    if(!data){
        return;
    }
    repoName.textContent = data.repo || "Unknown Repository";
    repoDescription.textContent = data.description || "Repository indexed successfully.";
    statStars.textContent = data.stars ?? "-";
    statForks.textContent = data.forks ?? "-";
    statLanguage.textContent = data.language ?? "-";
    updateAvatar(data.repo);
}
// =========================================
// Avatar
// =========================================
function updateAvatar(repo){
    if(!repo){
        repoAvatar.textContent = "📦";
        return;
    }
    const parts = repo.split("/");
    if(parts.length !== 2){
        repoAvatar.textContent = "📦";
        return;
    }
    repoAvatar.textContent = parts[1].charAt(0).toUpperCase();
}
// =========================================
// Reset Repository
// =========================================
function clearRepositoryOverview(){
    repoAvatar.textContent = "📦";
    repoName.textContent = "owner/repository";
    repoDescription.textContent = "Repository Description";
    statStars.textContent = "-";
    statForks.textContent = "-";
    statLanguage.textContent = "-";
}
// =========================================
// Loading
// =========================================
function repositoryLoading(){
    repoName.textContent = "Loading...";
    repoDescription.textContent = "Fetching repository information...";
    statStars.textContent = "...";
    statForks.textContent = "...";
    statLanguage.textContent = "...";
}



// =========================================
// Error
// =========================================

function repositoryError(){
    repoName.textContent = "Unable to load repository";
    repoDescription.textContent = "Please try again.";
    statStars.textContent = "-";
    statForks.textContent = "-";
    statLanguage.textContent = "-";
}
// =========================================
// Repository Indexed
// =========================================
function repositoryIndexedSuccessfully(data){
    updateRepositoryOverview(data);
}
// =========================================
// Repository Statistics
// =========================================

function updateStatistics(stats){
    if(!stats){
        return;
    }
    statStars.textContent = stats.stars ?? "-";
    statForks.textContent = stats.forks ?? "-";
    statLanguage.textContent = stats.language ?? "-";
}
// =========================================
// Repository Ready
// =========================================
function showRepositoryCard(){
    document.getElementById("repoResult").classList.add("visible");
}
// =========================================
// Hide Repository Card
// =========================================
function hideRepositoryCard(){
    document.getElementById("repoResult").classList.remove("visible");
}
// =========================================
// Initialize
// =========================================
document.addEventListener(
    "DOMContentLoaded",
    ()=>{
        clearRepositoryOverview();
    }
);