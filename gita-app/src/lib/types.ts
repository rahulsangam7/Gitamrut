export type Language = "english" | "sanskrit";

export type Verse = {
  chapterNumber: number;
  verseNumber: number;
  chapterTitleSanskrit: string;
  chapterTitleEnglish: string;
  sanskrit: string;
  english: string;
  /** Linear index across all 701 verses — used for prev/next navigation. */
  linearIndex: number;
};
