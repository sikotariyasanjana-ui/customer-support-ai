import api from "./api";

export const sendMessage = async (message, agent) => {
    try {
        const response = await api.post("/api/chat", {
            message,
            agent,
        });

        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const getChatHistory = async () => {
    try {
        const response = await api.get("/api/history");
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const clearHistory = async () => {
    try {
        const response = await api.delete("/api/history");

        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};