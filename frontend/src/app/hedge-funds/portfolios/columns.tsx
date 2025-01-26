"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Portfolio = {
    id: number
    fund: {
        id: number,
        name: string,
        inception_date: string,
        total_aum: string,
        hedge_fund_company: number
    },
    manager: {
        id: number,
        username: string,
        email: string,
        phone_number: string,
        is_trader: boolean,
        is_investor: boolean
    },
    name: string,
    created_at: string,
}

// This is the actual column definition.
export const columns: ColumnDef<Portfolio>[] = [
    {
        accessorKey: "fund.name",
        header: "Name",
    }, {
        accessorKey: "manager.username",
        header: "Manager",
    }, {
        accessorKey: "name",
        header: "Portfolio Name",
    }, {
        accessorKey: "created_at",
        header: "Created At",
    }
]
