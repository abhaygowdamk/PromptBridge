import { useState } from "react";
import Header from "./components/Header";
import MessageList from "./components/MessageList";
import ChatInput from "./components/ChatInput";
import { sendPrompt } from "./api";

export default function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend(text) {
    const userMessage = { id: crypto.randomUUID(), role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const answer = await sendPrompt(text);
      setMessages((prev) => [
        ...prev,
        { id: crypto.randomUUID(), role: "assistant", content: answer },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          id: crypto.randomUUID(),
          role: "assistant",
          content: err.message,
          error: true,
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app">
      <Header
        onClear={() => setMessages([])}
        canClear={messages.length > 0 && !loading}
      />
      <MessageList messages={messages} loading={loading} onPick={handleSend} />
      <ChatInput onSend={handleSend} disabled={loading} />
    </div>
  );
}