import { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const reader = res.body.getReader();
    let response = "";
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      response += new TextDecoder().decode(value);
      setMessages((msgs) => [...msgs, { role: "bot", text: response }]);
    }
    setInput("");
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((m, i) => (
          <div key={i} className={m.role}>
            {m.text}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your question..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;
