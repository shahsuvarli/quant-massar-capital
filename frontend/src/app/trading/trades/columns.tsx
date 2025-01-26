"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Trade = {
    id: number
    portfolio: {
        id: number,
        name: string,
        created_at: string,
        fund: string,
        manager: number
    },
    instrument: {
        id: number,
        name: string,
        symbol: string,
        instrument_type: string,
        currency: string
    },
    trade_type: string,
    quantity: string,
    price: string,
    trade_date: string,
    executed_at: string
}


export const columns: ColumnDef<Trade>[] = [
    {
        accessorKey: "trade_type",
        header: "Trade Type",
    },
    {
        accessorKey: "quantity",
        header: "Quantity",
    },
    {
        accessorKey: "price",
        header: "Price",
    },
    {
        accessorKey: "trade_date",
        header: "Trade Date",
    },
    // {
    //     accessorKey: "executed_at",
    //     header: "Executed At",
    // },
    {
        accessorKey: "trade_type",
        header: "Trade Type",
    },
    {
        accessorKey: "portfolio.name",
        header: "Portfolio",
    },
    {
        accessorKey: "instrument.name",
        header: "Instrument",
    },
]
