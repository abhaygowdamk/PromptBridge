import { useRef, useState } from "react";

export default function ChatInput({ onSend, disabled }) {
  const [text, setText] = useState("");
  const areaRef = useRef(null);

  function resize() {
    const el = areaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = Math.min(el.scrollHeight, 180) + "px";
  }

  function submit() {
    const value = text.trim();
    if (!value || disabled) return;
    onSend(value);
    setText("");
    requestAnimationFrame(() => {
      if (areaRef.current) areaRef.current.style.height = "auto";
    });
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  }

  return (
    <footer className="input-wrap">
      <div className="input-box">
        <textarea
          ref={areaRef}
          rows={1}
          value={text}
          placeholder="Message PromptBridge..."
          onChange={(e) => {
            setText(e.target.value);
            resize();
          }}
          onKeyDown={handleKeyDown}
        />
        <button
          className="send-btn"
          onClick={submit}
          disabled={disabled || !text.trim()}
          aria-label="Send"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path
              d="M12 19V5M12 5l-6 6M12 5l6 6"
              stroke="currentColor"
              strokeWidth="2.4"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>
      <p className="hint">Enter to send &middot; Shift + Enter for a new line</p>
    </footer>
  );
}