export default function Header({ onClear, canClear }) {
  return (
    <header className="header">
      <div className="brand">
        <div className="logo">{"\u{1F309}"}</div>
        <div>
          <h1>PromptBridge</h1>
          <p>Your bridge to the LLM</p>
        </div>
      </div>
      <button className="ghost-btn" onClick={onClear} disabled={!canClear}>
        Clear chat
      </button>
    </header>
  );
}