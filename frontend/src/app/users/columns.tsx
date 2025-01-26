"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type UserProfile = {
    id: number
    user: {
        id: number
        username: string
        email: string
        phone_number: string
        is_trader: boolean
        is_investor: boolean
    }
    bio: string
    country: string
    date_of_birth: string
    account_balance: string
    risk_tolerance: "High" | "Medium" | "Low"

}

export const columns: ColumnDef<UserProfile>[] = [
    {
        accessorKey: "user.username",
        header: "Username",
    },
    {
        accessorKey: "user.email",
        header: "Email",
        // accessor: (row) => row.user.email,
    },
    {
        accessorKey: "user.phone_number",
        header: "Phone Number",
        // accessor: (row) => row.user.phone_number,
    },
    {
        accessorKey: "user.is_trader",
        header: "Trader",
        // accessor: (row) => row.user.is_trader.toString(),
    },
    {
        accessorKey: "user.is_investor",
        header: "Investor",
        // accessor: (row) => row.user.is_investor.toString(),
    },
    // {
    //     accessorKey: "bio",
    //     header: "Bio",
    //     // accessor: (row) => row.bio,
    // },
    {
        accessorKey: "country",
        header: "Country",
        // accessor: (row) => row.country,
    },
    {
        accessorKey: "date_of_birth",
        header: "Date of Birth",
        // accessor: (row) => row.date_of_birth,
    },
    {
        accessorKey: "account_balance",
        header: "Account Balance",
        // accessor: (row) => row.account_balance,
    },
    {
        accessorKey: "risk_tolerance",
        header: "Risk Tolerance",
        // accessor: (row) => row.risk_tolerance,
    },
]
