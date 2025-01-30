"use client";

import { createContext, ReactNode, useState, useEffect } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";

type User = {
    username: string;
};

export type AuthContextType = {
    user: User | null;
    login: (username: string, password: string) => Promise<void>;
    register: (username: string, password: string) => Promise<void>;
    logout: () => Promise<void>;
    loading: boolean;
};

export const AuthContext = createContext<AuthContextType | null>(null);

const AuthProvider = ({ children }: { children: ReactNode }) => {
    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);
    const router = useRouter();

    // ✅ Retrieve user from localStorage when component mounts
    useEffect(() => {
        const storedUser = localStorage.getItem("user");
        const access_token = localStorage.getItem("token");

        if (storedUser && access_token) {
            axios.defaults.headers.common["Authorization"] = `Bearer ${access_token}`;
            setUser(JSON.parse(storedUser));
        }
        setLoading(false);
    }, []);

    const login = async (username: string, password: string): Promise<void> => {
        try {
            const { data } = await axios.post(
                `${process.env.NEXT_PUBLIC_API_URL}/accounts/login/`,
                { username, password },
            );

            const userData = { username }; // Store minimal user info
            localStorage.setItem("user", JSON.stringify(userData)); // Store user in localStorage
            localStorage.setItem("token", data.access); // Store token

            axios.defaults.headers.common["Authorization"] = `Bearer ${data.access_token}`;
            setUser(userData);
            router.push("/");
        } catch (error) {
            console.error("Login failed", error);
        }
    };

    const register = async (username: string, password: string): Promise<void> => {
        try {
            await axios.post(`${process.env.NEXT_PUBLIC_API_BASE_URL}/auth/register`, {
                username,
                password,
            });

            // Automatically log in after successful registration
            await login(username, password);
        } catch (error) {
            console.error("Registration failed", error);
        }
    };

    const logout = async () => {
        try {
            localStorage.removeItem("user");
            localStorage.removeItem("token");

            delete axios.defaults.headers.common["Authorization"];
            setUser(null);
            router.push("/login");
        } catch (error) {
            console.error("Logout failed", error);
        }
    };

    return (
        <AuthContext.Provider value={{ user, login, register, logout, loading }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;
