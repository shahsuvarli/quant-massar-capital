import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { Portfolio, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"

const name = "Portfolios"

export const metadata: Metadata = {
    title: `${name} | Quantm`,
    description: `${name} page`,
}


export default async function DemoPage() {
    const data: Portfolio[] = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/hedgefunds/portfolios`, {
        method: 'GET',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName={`Hedge funds / ${name}`} />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
