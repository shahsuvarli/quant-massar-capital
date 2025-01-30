import { Metadata } from "next";
import { FC } from "react";
import LoginForm from "@/components/Maps/Login";

export const metadata: Metadata = {
  title: "Login Page | Quantm",
  description: "This is Quantm Login Page",
};

const SignIn: FC = () => {
  return (
    <LoginForm />
  );
};

export default SignIn;
