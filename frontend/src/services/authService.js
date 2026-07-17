import api from "./api";

export const loginUser = async (email, password) => {
    try {
        const response = await api.post("/api/auth/login", {
            email,
            password,
        });

        const token = response.data.access_token;

        localStorage.setItem("token", token);

        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const registerUser = async (name, email, password) => {
    try {
        const response = await api.post("/api/auth/register", {
            name,
            email,
            password,
        });

        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};

export const logoutUser = () => {
    localStorage.removeItem("token");
};

export const getCurrentUser = async () => {
    try {
        const response = await api.get("/api/auth/me");
        return response.data;
    } catch (error) {
        throw error.response?.data || error.message;
    }
};