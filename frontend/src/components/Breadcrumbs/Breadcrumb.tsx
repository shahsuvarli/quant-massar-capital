"use client"

import Link from "next/link";
import { Button } from "../ui/button";
import { IoIosAddCircleOutline } from "react-icons/io";
interface BreadcrumbProps {
  pageName: string;
}
const Breadcrumb = ({ pageName }: BreadcrumbProps) => {
  return (
    <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
      <h2 className="text-title-md2 font-semibold text-black dark:text-white">
        {pageName}
      </h2>

      {/* <nav>
        <ol className="flex items-center gap-2">
          <li>
            <Link className="font-medium" href="/">
              Quantm /
            </Link>
          </li>
          <li className="font-medium text-primary">{pageName}</li>
        </ol>
      </nav> */}
      <Button
        size="default"
        onClick={() => console.log("clicked")}
      >
        <IoIosAddCircleOutline /> Add New
      </Button>
    </div>
  );
};

export default Breadcrumb;
