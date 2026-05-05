import ConfessionList from "./components/ConfessionList";
import CreateConfession from "./components/CreateConfession";
// import { useState } from "react";

function App() {
  return (
    <div style={{ maxWidth: "600px", margin: "auto", padding: "20px" }}>
      <h1 style={{ textAlign: "center" }}>Anonymous Confessions </h1>

      <CreateConfession refresh={() => window.location.reload()} />
      <ConfessionList />
    </div>
  );
}

export default App;