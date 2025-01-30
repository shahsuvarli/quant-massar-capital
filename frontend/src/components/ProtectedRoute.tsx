'use client'

import { AuthContext, AuthContextType } from "@/context/AuthContext"
import { redirect } from "next/navigation"
import { ReactNode, useContext } from "react"


const ProtectedRoute = ({ children }: { children: ReactNode }) => {
    const { user, loading } = useContext(AuthContext) as AuthContextType
    if (loading) return <div>Loading...</div>
    if (!user) redirect('/login')
    return children
}

export default ProtectedRoute