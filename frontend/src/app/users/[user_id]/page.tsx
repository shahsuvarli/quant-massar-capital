import Breadcrumb from "@/components/Breadcrumbs/Breadcrumb";
import Image from "next/image";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"


export const metadata: Metadata = {
    title: "Next.js Profile | TailAdmin - Next.js Dashboard Template",
    description:
        "This is Next.js Profile page for TailAdmin - Next.js Tailwind CSS Admin Dashboard Template",
};

const Profile = ({ params: { user_id } }: { params: { user_id: number } }) => {

    return (
        <DefaultLayout>
            <div className="mx-auto">
                <Breadcrumb pageName="Profile" />

                <div className="overflow-hidden rounded-lg border border-stroke bg-[#2F2F41] shadow-default dark:border-strokedark dark:bg-boxdark p-8 flex flex-row items-start gap-5 relative z-1">
                    <span className="flex flex-col items-start gap-5">
                        <p className="text-white text-2xl font-semibold">Welcome, Elvin</p>
                        <p className="text-gray-400 text-md">Check all the information about your account and manage your profile</p>
                    </span>

                </div>


                <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mt-5">
                    <div>
                        <p className="text-gray-500 text-md font-semibold">
                            User information
                        </p>
                        <div className="rounded-lg border border-stroke bg-[#2F2F41] shadow-default dark:border-strokedark dark:bg-boxdark p-2 flex flex-col items-start justify-center gap-5">
                            <div className="flex items-center gap-5">
                                <Image src="/images/user/character.png" width={150} height={200} alt="Profile" />
                                <div>
                                    <p className="text-gray-400 text-md">Name</p>
                                    <p className="text-gray-400 text-md">Username</p>
                                    <p className="text-gray-400 text-md">Email</p>
                                </div>
                                <div>
                                    <p className="text-white text-md">Elvin</p>
                                    <p className="text-white text-md"> 12.12.1990</p>
                                    <p className="text-white text-md">shahsuvarli.elvin@gmail.com</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <p className="text-gray-500 text-md font-semibold">
                            Financial status
                        </p>
                        <div className="rounded-lg border border-stroke bg-[#2F2F41] shadow-default dark:border-strokedark dark:bg-boxdark p-2 flex flex-col items-start justify-center gap-5">
                            <div className="flex items-center gap-5">
                                <Image src="/images/user/finance.png" width={150} height={200} alt="Profile" />
                                <div>
                                    <p className="text-gray-400 text-md">Country</p>
                                    <p className="text-gray-400 text-md">Account balance</p>
                                    <p className="text-gray-400 text-md">Risk tolerance</p>
                                </div>
                                <div>
                                    <p className="text-white text-md">Austria</p>
                                    <p className="text-white text-md">$ 100.000</p>
                                    <p className="text-white text-md">High</p>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mt-5">
                    <div className="rounded-lg border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark p-2 flex flex-col items-start justify-center gap-5">
                        <p className="text-gray-700 text-md font-semibold">Your Portfolios</p>
                        <Table className="w-full">
                            <TableHeader>
                                <TableRow>
                                    <TableHead className="w-[100px]">ID</TableHead>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Created at</TableHead>
                                    {/* <TableHead>Method</TableHead> */}
                                    <TableHead className="text-right">Fund</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableRow>
                                    <TableCell className="font-medium">INV001</TableCell>
                                    <TableCell>Paid</TableCell>
                                    <TableCell>Paid</TableCell>
                                    {/* <TableCell>Credit Card</TableCell> */}
                                    <TableCell className="text-right">$250.00</TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </div>
                    <div className="rounded-lg border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark p-2 flex flex-col items-start justify-center gap-5">
                        <p className="text-gray-700 text-md font-semibold">Your Transactions</p>
                        <Table className="w-full">
                            <TableHeader>
                                <TableRow>
                                    <TableHead className="w-[100px]">ID</TableHead>
                                    <TableHead>Name</TableHead>
                                    <TableHead>Created at</TableHead>
                                    {/* <TableHead>Method</TableHead> */}
                                    <TableHead className="text-right">Fund</TableHead>
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                <TableRow>
                                    <TableCell className="font-medium">INV001</TableCell>
                                    <TableCell>Paid</TableCell>
                                    <TableCell>Paid</TableCell>
                                    {/* <TableCell>Credit Card</TableCell> */}
                                    <TableCell className="text-right">$250.00</TableCell>
                                </TableRow>
                            </TableBody>
                        </Table>
                    </div>
                </div>
            </div>
        </DefaultLayout >
    );
};

export default Profile;
