"use client";

type Props = {
  chapter: number;
  verse: number;
};

/**
 * Square illustration above each verse. Currently uses picsum.photos with a
 * deterministic seed per (chapter, verse) — same verse always gets the same
 * placeholder. Will be swapped for nano-banana generated art later.
 */
export function VerseImage({ chapter, verse }: Props) {
  const seed = `gita-${chapter}-${verse}`;
  const src = `https://picsum.photos/seed/${seed}/720/720`;

  return (
    <div className="relative mx-auto aspect-square w-full max-w-sm overflow-hidden rounded-lg border border-gold/30 shadow-scroll">
      {/* Subtle gold inner frame, evoking illuminated-manuscript borders. */}
      <div className="pointer-events-none absolute inset-0 rounded-lg ring-1 ring-inset ring-gold/20" />
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        key={seed}
        src={src}
        alt={`Illustration for Chapter ${chapter}, Verse ${verse}`}
        className="h-full w-full object-cover"
        loading="eager"
      />
      {/* Warm sepia wash to blend placeholder imagery into the parchment palette. */}
      <div className="pointer-events-none absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-parchment-100/30 mix-blend-multiply" />
    </div>
  );
}
