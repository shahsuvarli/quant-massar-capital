"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type UserProfile = {
    id: number
    username: string
    email: string
    phone_number: string
    is_trader: boolean
    is_investor: boolean
    account_balance: string
    risk_tolerance: "High" | "Medium" | "Low"

}

export const columns: ColumnDef<UserProfile>[] = [
    {
        accessorKey: "username",
        header: "Username",
    },
    {
        accessorKey: "email",
        header: "Email",
    },
    {
        accessorKey: "phone_number",
        header: "Phone Number",
    },
    {
        accessorKey: "is_trader",
        header: "Trader",
    },
    {
        accessorKey: "is_investor",
        header: "Investor",
    },
    {
        accessorKey: "account_balance",
        header: "Account Balance",
    },
    {
        accessorKey: "risk_tolerance",
        header: "Risk Tolerance",
    },
]
