"use client";

import type { Language, Verse } from "@/lib/types";
import { VerseImage } from "./VerseImage";

type Props = {
  verse: Verse;
  language: Language;
};

export function VerseCard({ verse, language }: Props) {
  const isSanskrit = language === "sanskrit";
  const text = isSanskrit ? verse.sanskrit : verse.english;
  const chapterTitle = isSanskrit
    ? verse.chapterTitleSanskrit
    : verse.chapterTitleEnglish;

  return (
    <article
      key={`${verse.chapterNumber}-${verse.verseNumber}-${language}`}
      className="verse-fade mx-auto flex w-full max-w-3xl flex-col items-center gap-6 sm:gap-8"
    >
      {/* Chapter header — intentionally quiet, sits above the image. */}
      <header className="w-full text-center">
        <p className="font-display text-xs sm:text-sm tracking-[0.35em] uppercase text-gold-dark">
          Chapter {verse.chapterNumber} · Verse {verse.verseNumber}
        </p>
        <h2
          className={
            "mt-2 font-display text-lg sm:text-xl md:text-2xl tracking-wide text-ink " +
            (isSanskrit ? "sanskrit-text font-deva" : "")
          }
        >
          {chapterTitle}
        </h2>
      </header>

      <VerseImage chapter={verse.chapterNumber} verse={verse.verseNumber} />

      <div className="ornamental-divider w-full max-w-lg">
        <span className="ornament" aria-hidden="true" />
      </div>

      <div className="w-full">
        <p
          className={
            "whitespace-pre-line text-center text-ink " +
            (isSanskrit
              ? "sanskrit-text font-deva text-lg sm:text-xl md:text-2xl"
              : "font-serif text-lg sm:text-xl md:text-2xl leading-relaxed")
          }
        >
          {text || (
            <span className="italic text-ink-muted">
              (translation unavailable)
            </span>
          )}
        </p>
      </div>
    </article>
  );
}
