import { useEffect, useRef } from "react";
import Message from "./Message";

const SUGGESTIONS = [
  "Explain tokens in one sentence",
  "What is an embedding?",
  "Give me 3 project ideas using FastAPI",
  "Explain attention like I'm 15",
];

export default function MessageList({ messages, loading, onPick }) {
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  if (messages.length === 0 && !loading) {
    return (
      <main className="messages empty">
        <div className="hero">
          <div className="hero-icon">{"\u{1F309}"}</div>
          <h2>What can I help you with?</h2>
          <p>Ask anything, or try one of these.</p>
          <div className="chips">
            {SUGGESTIONS.map((s) => (
              <button key={s} className="chip" onClick={() => onPick(s)}>
                {s}
              </button>
            ))}
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="messages">
      {messages.map((m) => (
        <Message key={m.id} {...m} />
      ))}

      {loading && (
        <div className="row row-bot">
          <div className="avatar">{"\u2728"}</div>
          <div className="bubble bubble-bot typing">
            <span />
            <span />
            <span />
          </div>
        </div>
      )}
      <div ref={bottomRef} />
    </main>
  );
}