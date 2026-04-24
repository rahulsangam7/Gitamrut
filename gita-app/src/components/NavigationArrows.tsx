"use client";

type Props = {
  onPrev: () => void;
  onNext: () => void;
  canPrev: boolean;
  canNext: boolean;
  position: { current: number; total: number };
};

export function NavigationArrows({ onPrev, onNext, canPrev, canNext, position }: Props) {
  return (
    <div className="flex items-center justify-between gap-4 w-full max-w-2xl mx-auto">
      <ArrowButton direction="prev" disabled={!canPrev} onClick={onPrev} />
      <span className="font-sans text-xs tracking-[0.2em] uppercase text-ink-muted">
        {position.current} / {position.total}
      </span>
      <ArrowButton direction="next" disabled={!canNext} onClick={onNext} />
    </div>
  );
}

function ArrowButton({
  direction,
  disabled,
  onClick,
}: {
  direction: "prev" | "next";
  disabled: boolean;
  onClick: () => void;
}) {
  const label = direction === "prev" ? "Previous verse" : "Next verse";
  return (
    <button
      type="button"
      aria-label={label}
      onClick={onClick}
      disabled={disabled}
      className={
        "group flex items-center justify-center h-12 w-12 sm:h-14 sm:w-14 rounded-full " +
        "border border-gold/40 bg-parchment-50/70 text-gold-dark " +
        "transition-all duration-200 shadow-sm " +
        "hover:enabled:border-gold hover:enabled:bg-gold hover:enabled:text-parchment-50 " +
        "hover:enabled:shadow-md hover:enabled:-translate-y-0.5 " +
        "active:enabled:translate-y-0 " +
        "disabled:opacity-30 disabled:cursor-not-allowed"
      }
    >
      <svg
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth={1.75}
        strokeLinecap="round"
        strokeLinejoin="round"
        className={
          "h-5 w-5 transition-transform duration-200 " +
          (direction === "prev"
            ? "group-hover:enabled:-translate-x-0.5"
            : "group-hover:enabled:translate-x-0.5")
        }
      >
        {direction === "prev" ? (
          <polyline points="15 18 9 12 15 6" />
        ) : (
          <polyline points="9 18 15 12 9 6" />
        )}
      </svg>
    </button>
  );
}
