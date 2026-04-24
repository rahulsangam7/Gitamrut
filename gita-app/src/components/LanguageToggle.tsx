"use client";

import type { Language } from "@/lib/types";

type Props = {
  language: Language;
  onChange: (lang: Language) => void;
};

export function LanguageToggle({ language, onChange }: Props) {
  return (
    <div
      role="radiogroup"
      aria-label="Language"
      className="inline-flex items-center rounded-full border border-gold/40 bg-parchment-50/60 p-1 shadow-sm backdrop-blur"
    >
      <Option
        label="English"
        active={language === "english"}
        onClick={() => onChange("english")}
      />
      <Option
        label="संस्कृत"
        active={language === "sanskrit"}
        onClick={() => onChange("sanskrit")}
      />
    </div>
  );
}

function Option({
  label,
  active,
  onClick,
}: {
  label: string;
  active: boolean;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      role="radio"
      aria-checked={active}
      onClick={onClick}
      className={
        "rounded-full px-4 py-1.5 text-sm font-medium tracking-wide transition-all " +
        (active
          ? "bg-gold text-parchment-50 shadow-sm"
          : "text-ink-muted hover:text-ink")
      }
    >
      {label}
    </button>
  );
}
