"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Portfolio = {
    id: number
    manager: {
        id: number,
        username: string,
        email: string,
        phone_number: string,
        is_trader: boolean,
        is_investor: boolean
    },
    name: string,
    inception_date: string,
    total_aum: string
}

// This is the actual column definition.
export const columns: ColumnDef<Portfolio>[] = [
    {
        accessorKey: "manager.username",
        header: "Manager",
    },
    {
        accessorKey: "name",
        header: "Company",
    },
    {
        accessorKey: "inception_date",
        header: "Inception Date",
    }, {
        accessorKey: "total_aum",
        header: "Total AUM",
    }
]
