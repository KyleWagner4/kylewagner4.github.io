"""Subset the site's variable fonts to WOFF2.

The Fontsource / Google Fonts builds strip small caps, figure-style and
case features, so the fonts are subset from the upstream releases instead:

  Source Serif 4  4.005R  https://github.com/adobe-fonts/source-serif/releases/tag/4.005R
                          (Desktop zip, VAR/SourceSerif4Variable-{Roman,Italic}.ttf)
  Inter           4.1     https://github.com/rsms/inter/releases/tag/v4.1
                          (InterVariable.ttf)

Both are SIL Open Font License 1.1 (see src/assets/fonts/LICENSE-*.txt).
A subset is a Modified Version under the OFL, and "Source" is a Reserved
Font Name, so the serif subsets are renamed internally.
The opsz axis is kept whole; wght is narrowed to the range the design uses,
which tokens.css must stay inside.

Usage (needs fonttools and brotli):
  python scripts/subset-fonts.py <SourceSerif4Variable-Roman.ttf> \
      <SourceSerif4Variable-Italic.ttf> <InterVariable.ttf>
"""

import sys
import tempfile
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

OUT = Path(__file__).resolve().parent.parent / "src" / "assets" / "fonts"

UNICODES = [
    "U+0020-007E",  # Basic Latin
    "U+00A0-00FF",  # Latin-1 Supplement (includes × ÷ ± ° § ² ³)
    "U+0131,U+0152-0153",
    "U+2002-200B",  # en/em/thin/hair spaces
    "U+2010-2027",  # dashes, typographic quotes, bullet, ellipsis
    "U+2030,U+2032-2033,U+2039-203A",  # per mille, primes, angle quotes
    "U+20AC,U+2122",
    "U+2190-2193,U+2197",  # arrows, including the outbound-link arrow
    "U+2212,U+2248,U+2264-2265",  # true minus and comparison signs
]

BASE_FEATURES = [
    "kern", "liga", "ccmp", "locl", "mark", "mkmk",
    "tnum", "pnum", "lnum", "case",
]

# name: (features, wght range, internal family name or None to keep)
FONTS = {
    "serif-roman": (BASE_FEATURES + ["smcp", "c2sc"], (300, 700), "KW Serif"),
    "serif-italic": (BASE_FEATURES, (300, 700), "KW Serif"),
    "inter": (BASE_FEATURES + ["calt"], (400, 650), None),
}


def rename(font: TTFont, family: str) -> None:
    name = font["name"]
    style = name.getDebugName(2) or "Regular"
    for record in list(name.names):
        if record.nameID in (1, 3, 4, 6, 16, 17, 25):
            name.removeNames(nameID=record.nameID)
    name.setName(family, 1, 3, 1, 0x409)
    name.setName(style, 2, 3, 1, 0x409)
    name.setName(f"{family} {style}", 4, 3, 1, 0x409)
    name.setName(f"{family.replace(' ', '')}-{style}", 6, 3, 1, 0x409)
    name.setName(f"{family}; subset of Source Serif 4", 3, 3, 1, 0x409)


def run(src: Path, name: str, features: list[str], wght: tuple[int, int],
        family: str | None) -> None:
    dest = OUT / f"{name}.woff2"
    font = instancer.instantiateVariableFont(TTFont(src), {"wght": wght})
    if family:
        rename(font, family)
    with tempfile.TemporaryDirectory() as tmp:
        narrowed = Path(tmp) / f"{name}.ttf"
        font.save(narrowed)
        subset.main([
            str(narrowed),
            f"--output-file={dest}",
            "--flavor=woff2",
            f"--unicodes={','.join(UNICODES)}",
            f"--layout-features={','.join(features)}",
            "--no-hinting",
            "--name-IDs=0,1,2,3,4,5,6,13,14,16,17,25",
        ])
    print(f"{dest.name}: {dest.stat().st_size / 1024:.1f} KB")


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    OUT.mkdir(parents=True, exist_ok=True)
    for src, (name, (features, wght, family)) in zip(sys.argv[1:], FONTS.items()):
        run(Path(src), name, features, wght, family)


if __name__ == "__main__":
    main()
