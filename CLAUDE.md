# Kyle's Portfolio Site

## Purpose
Personal portfolio for FP&A and finance roles in Los Angeles.
Positioning: "I build financial models and the tools that automate them."
Primary audience: finance hiring managers and recruiters, who skim fast.

## Content plan
- Case studies (3): problem → what I built → how it works → measurable result
  1. SEC 10-K/10-Q Analyzer (XBRL normalization)
  2. Macro Monitor (Sahm rule and recession signals from FRED)
  3. Automated morning report on dividend stocks and covered call rates
- Project cards: Portfolio Analytics Dashboard (link to Streamlit),
  401(k) revenue-sharing research

## Design philosophy
Simple at first glance, intricate on inspection. The layout is calm and
restrained; the sophistication lives in the details. Think editorial
financial publication meets precision instrument. Every detail should
reward a trained eye without adding visual noise for everyone else.

## Typography
- Use a variable font with optical sizing; tune weight and optical size
  per context (display vs. body vs. captions)
- Fluid type scale using clamp(), based on a modular ratio
- Tabular, lining figures (font-variant-numeric: tabular-nums) for all
  numbers, so figures align like a financial statement
- text-wrap: balance on headings, text-wrap: pretty on body text
- Hanging punctuation, proper typographic quotes and dashes, small caps
  for labels and abbreviations
- Tight, deliberate letter-spacing on display sizes; looser on small caps

## Layout and grid
- Strict 12-column grid with a consistent spacing scale (one base unit,
  all spacing derived from it)
- Use CSS subgrid so nested content aligns to the parent grid
- Hairline rules (0.5px–1px) and precise alignment as structural elements,
  inspired by financial statements and annual reports
- Generous, intentional whitespace; asymmetric compositions where it helps

## Color
- Define the palette in OKLCH for perceptually even tones
- Mostly neutral, with one restrained accent color used sparingly
- Full light and dark modes, both designed deliberately (not just inverted)

## Motion and interaction
- Motion is subtle, purposeful, and fast; it should feel physical, never decorative
- Use the View Transitions API for page-to-page transitions
- Use CSS scroll-driven animations for gentle reveals, not JavaScript scroll listeners
- Refined micro-interactions on links, buttons, and focus states
- Custom easing curves; no default linear or ease timing
- Always respect prefers-reduced-motion

## Data and finance details
- Charts and tables styled like a high-end annual report: minimal ink,
  precise labels, no chart junk
- The covered call calculator should feel like a precision tool:
  instant updates, tabular numbers, clear inputs, smooth value transitions

## Quality bar
- Lighthouse 95+ across performance, accessibility, best practices, SEO
- Semantic HTML, keyboard accessible, visible focus states, WCAG AA contrast
- Fast: minimal JavaScript, optimized fonts (subset, preload), optimized images
- Pixel-level polish: check alignment, spacing, and rhythm at every breakpoint

## Stack
Astro, zero JS by default, no UI framework. Native CSS View Transitions
(no ClientRouter). Content collections for case studies and writing.
Deploys via GitHub Actions to GitHub Pages (kylewagner4.github.io).

## Hard rules
 - Never name my current wealth management employer, and never include
  client data or real positions. Use sample tickers and illustrative
  numbers only. UC San Diego Economics may be named.
- Drop the lifeguard role from the site.
- Work on the `redesign` branch; never commit directly to main.
- Make small, focused commits with clear messages.
- Ask before deleting existing files or content.