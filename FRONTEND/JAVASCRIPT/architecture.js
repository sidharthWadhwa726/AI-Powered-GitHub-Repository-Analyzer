// ==========================================
// architecture.js
// Handles Architecture Tab
// ==========================================
// ------------------------------
// DOM Elements
// ------------------------------
const repoSummary = document.getElementById("repoSummary");
const dirTree = document.getElementById("dirTree");
const functionGraph = document.getElementById("functionGraph");
const importGraph = document.getElementById("importGraph");
const executionFlow = document.getElementById("executionFlow");
// ==========================================
// Display Architecture
// ==========================================
function displayArchitecture(data){
    if(!data){
        return;
    }
    repoSummary.textContent = data.summary || "No summary available.";
    dirTree.textContent = data.folder_tree || "No folder tree.";
    functionGraph.textContent = formatFunctionGraph(data.function_graph);
    importGraph.textContent = formatImportGraph(data.import_graph);
    executionFlow.textContent = formatExecutionFlow(data.execution_flow);
}
// ==========================================
// Folder Tree
// ==========================================
function displayFolderTree(tree){
    dirTree.textContent = tree;
}
// =========================================
// Function Graph
// ==========================================

function formatFunctionGraph(graph){
    if(!graph){
        return "No function graph.";
    }
    if(typeof graph==="string"){
        return graph;
    }
    let output="";
    Object.entries(graph).forEach(
        ([file,functions])=>{
            output += file + "\n";
            functions.forEach(fn=>{
                output +=
                    "   └── "
                    + fn +
                    "\n";
            });
            output += "\n";
        }
    );
    return output;
}
// ==========================================
// Import Graph
// ==========================================

function formatImportGraph(graph){
    if(!graph){
       return "No import graph.";
    }
    if(typeof graph==="string"){
        return graph;
    }
    let output="";
    Object.entries(graph).forEach(
        ([file,imports])=>{
            output += file + "\n";
            imports.forEach(im=>{
                output +=
                    "   → "
                    + im +
                    "\n";
            });
            output += "\n";
        }
    );
    return output;
}



// ==========================================
// Execution Flow
// ==========================================

function formatExecutionFlow(flow){
    if(!flow){
        return "No execution flow.";
    }
    if(typeof flow==="string"){
        return flow;
    }
    let output="";
    flow.forEach(step=>{
        output +=
            "→ "
            + step
            + "\n";
    });
    return output;
}



// ==========================================
// Clear Architecture
// ==========================================

function clearArchitecture(){
    repoSummary.textContent="";
    dirTree.textContent="";
    functionGraph.textContent="";
    importGraph.textContent="";
    executionFlow.textContent="";
}
// ==========================================
// Loading State
// ==========================================
function showArchitectureLoading(){
    repoSummary.textContent = "Loading...";
    dirTree.textContent = "Loading...";
    functionGraph.textContent = "Loading...";
    importGraph.textContent = "Loading...";
    executionFlow.textContent = "Loading...";
}
// ==========================================
// Error State
// ==========================================
function architectureError(){
    repoSummary.textContent = "Unable to load architecture.";
    dirTree.textContent="";
    functionGraph.textContent="";
    importGraph.textContent="";
    executionFlow.textContent="";
}