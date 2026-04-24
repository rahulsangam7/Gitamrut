import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        parchment: {
          50: "#fbf5e6",
          100: "#f5ead7",
          200: "#ede0c8",
          300: "#e0cfa8",
          400: "#c9b284",
        },
        ink: {
          DEFAULT: "#2a1f18",
          soft: "#3a2817",
          muted: "#6b4f39",
        },
        gold: {
          DEFAULT: "#b8860b",
          light: "#d4a548",
          dark: "#8b6508",
        },
        saffron: "#d97706",
        terracotta: "#9c3d1e",
      },
      fontFamily: {
        display: ["var(--font-cinzel)", "serif"],
        serif: ["var(--font-cormorant)", "Georgia", "serif"],
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
        deva: ["var(--font-deva)", "serif"],
      },
      boxShadow: {
        scroll: "0 20px 60px -20px rgba(58, 40, 23, 0.35), 0 0 0 1px rgba(184, 134, 11, 0.15)",
      },
    },
  },
  plugins: [],
};

export default config;
