"use client"

import { ColumnDef } from "@tanstack/react-table"

// This type is used to define the shape of our data.
// You can use a Zod schema here if you want.
export type PaymentInfo = {
    id: number
    user: {
        username: string,
    },
    payment_method: string,
    account_number: string,
    created_at: string,
}


export const columns: ColumnDef<PaymentInfo>[] = [
    {
        accessorKey: "user.username",
        header: "User",
    },
    {
        accessorKey: "payment_method",
        header: "Payment Method",
    },
    {
        accessorKey: "account_number",
        header: "Account Number",
    },
    {
        accessorKey: "created_at",
        header: "Created At",
    },
]
