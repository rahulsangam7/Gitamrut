import type { Metadata } from "next";
import { Cinzel, Cormorant_Garamond, Inter, Noto_Serif_Devanagari } from "next/font/google";
import "./globals.css";

const cinzel = Cinzel({
  subsets: ["latin"],
  variable: "--font-cinzel",
  display: "swap",
  weight: ["400", "500", "600"],
});

const cormorant = Cormorant_Garamond({
  subsets: ["latin"],
  variable: "--font-cormorant",
  display: "swap",
  weight: ["400", "500", "600"],
});

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const deva = Noto_Serif_Devanagari({
  subsets: ["devanagari"],
  variable: "--font-deva",
  display: "swap",
  weight: ["400", "500", "600"],
});

export const metadata: Metadata = {
  title: "Bhagavad Gita — Verse by Verse",
  description:
    "Read the Bhagavad Gita in Sanskrit and plain English, one verse at a time.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${cinzel.variable} ${cormorant.variable} ${inter.variable} ${deva.variable}`}>
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
