import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { Trade, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"

const name = "Trades"

export const metadata: Metadata = {
    title: `${name} | Quantm`,
    description: `${name} page`,
}


export default async function DemoPage() {
    const data: Trade[] = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/trading/trades`, {
        method: 'GET',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName={`Trading / ${name}`} />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
