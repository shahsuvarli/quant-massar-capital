import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { Fund, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"

export const metadata: Metadata = {
    title: "Hedge funds | Quantm",
    description: "Hedge funds page",
}


export default async function DemoPage() {
    const data: Fund[] = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/hedgefunds/`, {
        method: 'GET',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName="Hedge funds" />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
