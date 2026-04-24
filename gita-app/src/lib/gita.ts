import rawData from "@/data/english.json";
import type { Verse } from "./types";

type RawChapter = {
  chapter_number: number;
  chapter_title_sanskrit: string;
  chapter_title_english: string;
  verses: Array<{
    verse_number: number;
    sanskrit: string;
    translation: string | null;
  }>;
};

type RawData = { chapters: RawChapter[] };

/**
 * Flatten all 701 verses into a single linear array so prev/next can simply
 * increment or decrement an index. Each verse carries its chapter context
 * so callers don't need to look anything up.
 */
function buildVerses(): Verse[] {
  const data = rawData as RawData;
  const verses: Verse[] = [];
  let idx = 0;
  for (const ch of data.chapters) {
    for (const v of ch.verses) {
      verses.push({
        chapterNumber: ch.chapter_number,
        verseNumber: v.verse_number,
        chapterTitleSanskrit: ch.chapter_title_sanskrit,
        chapterTitleEnglish: ch.chapter_title_english,
        sanskrit: v.sanskrit,
        english: v.translation ?? "",
        linearIndex: idx++,
      });
    }
  }
  return verses;
}

export const VERSES: Verse[] = buildVerses();
export const TOTAL_VERSES = VERSES.length;
