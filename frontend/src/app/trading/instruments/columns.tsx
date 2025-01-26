"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type Instrument = {
    id: number
    name: string,
    symbol: string,
    instrument_type: string,
    currency: string,
}

export const columns: ColumnDef<Instrument>[] = [
    {
        accessorKey: "name",
        header: "Name",
    },
    {
        accessorKey: "symbol",
        header: "Symbol",
    },
    {
        accessorKey: "instrument_type",
        header: "Instrument Type",
    },
    {
        accessorKey: "currency",
        header: "Currency",
    },
]
