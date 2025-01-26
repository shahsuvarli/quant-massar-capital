"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Fund = {
    id: number
    hedge_fund_company: {
        id: number,
        name: string,
        inception_date: string,
        total_aum: string,
        manager: number
    },
    name: string,
    total_aum: string,
    inception_date: string,
}

export const columns: ColumnDef<Fund>[] = [
    {
        accessorKey: "name",
        header: "Name",
    },
    {
        accessorKey: "hedge_fund_company.name",
        header: "Company",
    },
    {
        accessorKey: "total_aum",
        header: "AUM",
    },
    {
        accessorKey: "inception_date",
        header: "Inception Date",
    },
]
