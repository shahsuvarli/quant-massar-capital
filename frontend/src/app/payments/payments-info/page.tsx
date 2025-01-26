import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { PaymentInfo, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"

const name = "Payments Info"

export const metadata: Metadata = {
    title: `${name} | Quantm`,
    description: `${name} page`,
}


export default async function DemoPage() {
    const data: PaymentInfo[] = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/payments/payments-info`, {
        method: 'GET',
        cache: 'no-store',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName={`Payments / ${name}`} />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
