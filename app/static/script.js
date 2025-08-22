// DOM Elements
const chatBox = document.getElementById("chat-box");
const referenceInput = document.getElementById("reference-input");
const targetInput = document.getElementById("target-input");
const sendBtn = document.getElementById("send-btn");
const newChatBtn = document.getElementById("new-chat-btn");
const loadingIndicator = document.getElementById("loading-indicator");

// Dynamic Text Input Resizing
referenceInput.addEventListener("input", () => {
    referenceInput.style.height = "auto";
    referenceInput.style.height = `${referenceInput.scrollHeight}px`;
});

targetInput.addEventListener("input", () => {
    targetInput.style.height = "auto";
    targetInput.style.height = `${targetInput.scrollHeight}px`;
});

// Send Message
sendBtn.addEventListener("click", sendMessage);
referenceInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault(); // Prevent default behavior (new line)
        sendMessage();
    }
});

targetInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault(); // Prevent default behavior (new line)
        sendMessage();
    }
});

// New Chat
newChatBtn.addEventListener("click", () => {
    chatBox.innerHTML = "";
});

// Function to Send Message
function sendMessage() {
    const referenceText = referenceInput.value.trim();
    const targetText = targetInput.value.trim();

    if (referenceText === "" || targetText === "") return;

    // Add User Message to Chat Box
    appendMessage("user", `متن مرجع: ${referenceText}<br>متن هدف: ${targetText}`);
    referenceInput.value = "";
    targetInput.value = "";
    referenceInput.style.height = "auto"; // Reset input height
    targetInput.style.height = "auto"; // Reset input height

    // Show Loading Indicator
    loadingIndicator.style.display = "flex";

    // Send Message to the Server
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ reference: referenceText, target: targetText }),
    })
        .then((response) => response.json())
        .then((data) => {
            // Add Bot Response to Chat Box
            appendMessage("bot", data.response);
            loadingIndicator.style.display = "none";
        })
        .catch((error) => {
            console.error("Error:", error);
            loadingIndicator.style.display = "none";
        });
}

// Function to Append Message
function appendMessage(sender, message) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender);

    const messageText = document.createElement("p");
    messageText.innerHTML = formatMessage(message);

    const timestamp = document.createElement("div");
    timestamp.classList.add("timestamp");
    timestamp.textContent = new Date().toLocaleTimeString();

    messageElement.appendChild(messageText);
    messageElement.appendChild(timestamp);
    chatBox.appendChild(messageElement);

    // Scroll to Bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Function to Format Message (Bold Farsi Text)
function formatMessage(message) {
    return message.replace(/([\u0600-\u06FF]+)/g, "<strong>$1</strong>");
}