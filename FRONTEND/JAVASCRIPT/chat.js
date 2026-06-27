// ==========================================
// chat.js
// Handles Chat Interface
// ==========================================
// ------------------------------------------
// DOM Elements
// ------------------------------------------
const chatMessages = document.getElementById("chatMessages");
const chatInputBox = document.getElementById("chatInput");
const sendButton = document.getElementById("sendBtn");


// ==========================================
// Append User Message
// ==========================================

function appendUserMessage(message){
    const wrapper = document.createElement("div");
    wrapper.className = "msg user";
    wrapper.innerHTML =
    `    <div class="msg-avatar">
        You
    </div>
    <div class="msg-bubble">
        ${escapeHTML(message)}

    </div>`;
    chatMessages.appendChild(wrapper);
    scrollChat();
}

// ==========================================
// Append Bot Message
// ==========================================
function appendBotMessage(message){
    const wrapper = document.createElement("div");
    wrapper.className = "msg bot";
    wrapper.innerHTML =
    `
    <div class="msg-avatar">
        AI
    </div>
    <div class="msg-bubble">
        ${formatMessage(message)}
    </div>`;
    chatMessages.appendChild(wrapper);
    scrollChat();
}
// ==========================================
// Typing Animation
// ==========================================
let typingElement = null;
function showTyping(){
    typingElement = document.createElement("div");
    typingElement.className ="msg bot";
    typingElement.innerHTML =
    `
    <div class="msg-avatar">
        AI
    </div>
    <div class="msg-bubble">
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
    </div>
    `;
    chatMessages.appendChild(typingElement);
    scrollChat();
}
function hideTyping(){
    if(typingElement){
        typingElement.remove();
        typingElement = null;
    }
}
// ==========================================
// Scroll Chat
// =========================================
function scrollChat(){
    chatMessages.scrollTop =
        chatMessages.scrollHeight;
}
// =========================================
// Escape HTML
// ==========================================
function escapeHTML(text){
    return text
        .replace(/&/g,"&amp;")
        .replace(/</g,"&lt;")
        .replace(/>/g,"&gt;");
}
// ==========================================
// Format Response
// ==========================================
function formatMessage(message){
    if(!message){
        return "";
    }
    return escapeHTML(message)
        .replace(/\n/g,"<br>")
        .replace(
            /`([^`]+)`/g,
            "<code>$1</code>"
        );
}
// ==========================================
// Clear Chat
// ==========================================
function clearChat(){
    chatMessages.innerHTML = "";
}
// ==========================================
// Disable Input
// ==========================================
function disableChat(){
    chatInputBox.disabled = true;
    sendButton.disabled = true;
}
// ==========================================
// Enable Input
// ==========================================
function enableChat(){
    chatInputBox.disabled = false;
    sendButton.disabled = false;
}
// ==========================================
// Welcome Message
// ==========================================
function loadWelcomeMessage(){
    appendBotMessage(
`Hello 👋
I'm your GitHub Repository Assistant.
You can ask questions like:
• Explain the project architecture.
• What is the execution flow?
• Explain this function.
• Which file handles authentication?
• Where is the API defined?
• How does the RAG pipeline work?`
    );
}
// ==========================================
// Reset Chat
// ==========================================
function resetChat(){
    clearChat();
    loadWelcomeMessage();
}
// ==========================================
// Initialize
// ==========================================

document.addEventListener(
    "DOMContentLoaded",
    ()=>{
        loadWelcomeMessage();
    }
);