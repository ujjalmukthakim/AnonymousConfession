import { useEffect, useState } from "react";
import API from "../api";
import ConfessionCard from "./ConfessionCard";

export default function ConfessionList() {
  const [confessions, setConfessions] = useState([]);
  
  useEffect(() => {
   fetchConfessions();
    }, []);
  
  const fetchConfessions = async () => {
      const res = await API.get("confessions/");
      setConfessions(res.data);
    };
    
  return (
    <div>
      {confessions.map((conf) => (
        <ConfessionCard key={conf.id} conf={conf} refresh={fetchConfessions} />
      ))}
    </div>
  );
}