function formatError(message) {
  if (!message) return "Something went wrong.";
  if (typeof message === "string") return message;
  if (Array.isArray(message)) {
    return message.map((m) => m.msg || "Invalid input").join(", ");
  }
  return "Something went wrong.";
}

export async function sendPrompt(prompt) {
  let res;
  try {
    res = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });
  } catch {
    throw new Error("Cannot reach the server. Is the backend running?");
  }

  const data = await res.json().catch(() => ({}));

  if (!res.ok) {
    throw new Error(formatError(data.message));
  }
  return data.response;
}