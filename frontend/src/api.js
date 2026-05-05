import axios from "axios";

const API = axios.create({
  baseURL: "https://anonymousconfession-fil2.onrender.com/api/"
});

export default API;