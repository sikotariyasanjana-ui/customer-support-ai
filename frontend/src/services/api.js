import axios from "axios";

// Backend API URL
let API_BASE_URL =
    import.meta.env.VITE_API_URL || "https://customer-support-ai-7qzp.onrender.com";

// Normalize URL: remove trailing /api or / if they were included
if (API_BASE_URL.endsWith("/api")) {
    API_BASE_URL = API_BASE_URL.slice(0, -4);
}
if (API_BASE_URL.endsWith("/")) {
    API_BASE_URL = API_BASE_URL.slice(0, -1);
}

// Create Axios instance
const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        "Content-Type": "application/json",
    },
    timeout: 90000, // 90 seconds (allows Render free tier to wake up)
});

// Request interceptor
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("access_token");

        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }

        return config;
    },
    (error) => Promise.reject(error)
);

// Response interceptor
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response) {
            console.error("API Error:", error.response.data);
        } else {
            console.error("Network Error:", error.message);
        }

        return Promise.reject(error);
    }
);

export default api;