import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { RiskMetric, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"

const name = "Risk Metrics"

export const metadata: Metadata = {
    title: `${name} | Quantm`,
    description: `${name} page`,
}


export default async function DemoPage() {
    const data: RiskMetric[] = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/risk/risk-metrics`, {
        method: 'GET',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName={`Risk / ${name}`} />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
