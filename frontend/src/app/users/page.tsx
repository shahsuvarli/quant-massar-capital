import DefaultLayout from "@/components/Layouts/DefaultLayout"
import { UserProfile, columns } from "./columns"
import { DataTable } from "./data-table"
import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb"
import { Metadata } from "next"
import fetchAPI from "@/hooks/fetch"

export const metadata: Metadata = {
    title: "User profiles | Quantm",
    description: "User profiles page",
}


export default async function DemoPage() {
    const data: UserProfile[] = await fetchAPI(`http://localhost:8000/api/accounts/`, {
        // method: 'GET',
        // cache: 'no-store',
        // headers: {
        //     'Content-Type': 'application/json',
        // },
    })
    console.log(data)
    // .then(res => res.json())

    return (
        <DefaultLayout>
            <Breadcrumb pageName="User profiles" />
            <div className="mx-auto">
                <DataTable columns={columns} data={data} />
            </div>
        </DefaultLayout>
    )
}
