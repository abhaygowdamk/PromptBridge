import ReactMarkdown from "react-markdown";

export default function Message({ role, content, error }) {
  const isUser = role === "user";

  return (
    <div className={`row ${isUser ? "row-user" : "row-bot"}`}>
      {!isUser && <div className="avatar">{"\u2728"}</div>}
      <div className={`bubble ${isUser ? "bubble-user" : "bubble-bot"} ${error ? "bubble-error" : ""}`}>
        {isUser ? (
          <p className="plain">{content}</p>
        ) : (
          <div className="markdown">
            <ReactMarkdown>{content}</ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}