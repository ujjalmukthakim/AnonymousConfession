import { useState } from "react";
import API from "../api";
export default function CreateConfession({ refresh }) {
  const [content, setContent] = useState("");

  const handleSubmit = async () => {
    if (!content) return;

    await API.post("confessions/", { content });
    setContent("");
    refresh();
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Write your confession..."
        style={{
          width: "100%",
          height: "80px",
          padding: "10px",
          borderRadius: "8px",
          border: "1px solid #ccc",
        }}
      />

      <button
        onClick={handleSubmit}
        style={{
          marginTop: "10px",
          padding: "10px 20px",
          borderRadius: "8px",
          border: "none",
          backgroundColor: "black",
          color: "white",
          cursor: "pointer",
        }}
      >
        Post
      </button>
    </div>
  );
}