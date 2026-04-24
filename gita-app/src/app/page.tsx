"use client";

import { useCallback, useEffect, useState } from "react";
import { LanguageToggle } from "@/components/LanguageToggle";
import { NavigationArrows } from "@/components/NavigationArrows";
import { VerseCard } from "@/components/VerseCard";
import { VERSES, TOTAL_VERSES } from "@/lib/gita";
import type { Language } from "@/lib/types";

export default function Page() {
  const [index, setIndex] = useState(0);
  const [language, setLanguage] = useState<Language>("english");

  const verse = VERSES[index];
  const canPrev = index > 0;
  const canNext = index < TOTAL_VERSES - 1;

  const goPrev = useCallback(() => {
    setIndex((i) => (i > 0 ? i - 1 : i));
  }, []);
  const goNext = useCallback(() => {
    setIndex((i) => (i < TOTAL_VERSES - 1 ? i + 1 : i));
  }, []);

  // Keyboard navigation — arrow keys step through verses.
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "ArrowLeft") goPrev();
      else if (e.key === "ArrowRight") goNext();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [goPrev, goNext]);

  // Scroll to top on verse change so long verses don't leave the next one
  // half-scrolled.
  useEffect(() => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, [index]);

  return (
    <div className="flex min-h-screen flex-col">
      {/* Header — language toggle, anchored top. */}
      <header className="sticky top-0 z-10 w-full border-b border-gold/20 bg-parchment-100/80 backdrop-blur">
        <div className="mx-auto flex w-full max-w-5xl items-center justify-between gap-4 px-4 py-3 sm:px-6 sm:py-4">
          <div className="flex items-baseline gap-3">
            <h1 className="font-display text-base sm:text-lg tracking-[0.25em] text-ink">
              BHAGAVAD GĪTĀ
            </h1>
            <span className="hidden font-serif text-sm italic text-ink-muted sm:inline">
              verse by verse
            </span>
          </div>
          <LanguageToggle language={language} onChange={setLanguage} />
        </div>
      </header>

      {/* Main content — verse card. */}
      <main className="flex-1 w-full">
        <div className="mx-auto w-full max-w-5xl px-4 py-8 sm:px-6 sm:py-12">
          <VerseCard verse={verse} language={language} />
        </div>
      </main>

      {/* Bottom nav — prev/next arrows, always reachable. */}
      <footer className="sticky bottom-0 w-full border-t border-gold/20 bg-parchment-100/80 backdrop-blur">
        <div className="mx-auto w-full max-w-5xl px-4 py-3 sm:px-6 sm:py-4">
          <NavigationArrows
            onPrev={goPrev}
            onNext={goNext}
            canPrev={canPrev}
            canNext={canNext}
            position={{ current: index + 1, total: TOTAL_VERSES }}
          />
        </div>
      </footer>
    </div>
  );
}
