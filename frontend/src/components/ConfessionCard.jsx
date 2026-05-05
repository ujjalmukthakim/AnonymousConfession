import { useState } from "react";
import API from "../api";

export default function ConfessionCard({ conf, refresh }) {
  const [showComments, setShowComments] = useState(false);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState("");

  const handleReact = async () => {
    try {
      await API.post(`confessions/${conf.id}/react/`);
      refresh();
    } catch (err) {
      alert(err.response.data.error);
    }
  };

  const toggleComments = async () => {
    if (!showComments) {
      const res = await API.get(`confessions/${conf.id}/comments/`);
      setComments(res.data);
    }
    setShowComments(!showComments);
  };

  const handleAddComment = async () => {
    if (!newComment) return;

    await API.post(`confessions/${conf.id}/comment/`, {
      content: newComment,
    });

    setNewComment("");
    toggleComments(); // refresh comments
  };

  return (
    <div   style={{
    border: "1px solid #ddd",
    borderRadius: "12px",
    padding: "15px",
    marginBottom: "15px",
    boxShadow: "0 2px 5px rgba(0,0,0,0.05)",
  }}>
      <p>{conf.content}</p>

<button onClick={handleReact} style={{ marginRight: "10px" }}>
  ❤️ {conf.reaction_count}
</button>

<button onClick={toggleComments}>
  💬 {conf.comment_count}
</button>

{showComments && (
  <div style={{ marginTop: "10px", paddingLeft: "10px" }}>
    <h4>Comments</h4>

    {comments.map((c) => (
      <div
        key={c.id}
        style={{
          background: "#f5f5f5",
          padding: "8px",
          marginBottom: "5px",
          borderRadius: "6px",
        }}
      >
        {c.content}
      </div>
    ))}

    <input
      value={newComment}
      onChange={(e) => setNewComment(e.target.value)}
      placeholder="Write comment..."
      style={{
        width: "100%",
        padding: "8px",
        marginTop: "10px",
      }}
    />

    <button onClick={handleAddComment} style={{ marginTop: "5px" }}>
      Send
    </button>
  </div>
)}
    </div>
  );
}