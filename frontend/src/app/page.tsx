import ECommerce from "@/components/Dashboard/E-commerce";
import { Metadata } from "next";
import DefaultLayout from "@/components/Layouts/DefaultLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

export const metadata: Metadata = {
  title:
    "Home | Quantm",
  description: "This is the home page of Quantm",
};

export default function Home() {
  return (
    // <>
    <ProtectedRoute>
      <DefaultLayout>
        <ECommerce />
      </DefaultLayout>
    </ProtectedRoute>
    // </>
  );
}
