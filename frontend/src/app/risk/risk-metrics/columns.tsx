"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type RiskMetric = {
    id: number
    user: {
        username: string,
    },
    metric_name: string,
    value: string,
    as_of_date: string

}


export const columns: ColumnDef<RiskMetric>[] = [
    {
        accessorKey: "portfolio.name",
        header: "Portfolio",
    },
    {
        accessorKey: "metric_name",
        header: "Metric Name",
    },
    {
        accessorKey: "value",
        header: "Value",
    },
    {
        accessorKey: "as_of_date",
        header: "As Of Date",
    },
]
