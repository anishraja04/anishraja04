"""Generate the animated header SVGs for the profile README.

Self-hosted rather than fetched from a typing-SVG service: a third-party
outage would leave a broken image at the top of the profile. Two files
because GitHub picks between them with <picture media=...>, which is its
documented way of doing light/dark and is more reliable than a
prefers-color-scheme query inside a proxied image.

The reveal is a clipPath whose width animates in monospace character steps,
so the text appears a character at a time instead of sliding into view.
"""

from __future__ import annotations

from pathlib import Path

LINE = "I make agents prove it."
CHAR_W = 20.4          # advance width of the monospace face at 34px
FONT_PX = 34
START_X = 58
BASE_Y = 60
TYPE_SECONDS = 2.6
HOLD_SECONDS = 3.2

THEMES = {
    "light": {"bg": "none", "prompt": "#0b6477", "text": "#0f1012", "cursor": "#18a05f"},
    "dark": {"bg": "none", "prompt": "#3fb8af", "text": "#e6edf3", "cursor": "#3fb897"},
}


def build(theme: dict[str, str]) -> str:
    steps = len(LINE)
    text_w = steps * CHAR_W
    width = START_X + int(text_w) + 40
    total = TYPE_SECONDS + HOLD_SECONDS
    # One timeline, not two. With calcMode="discrete" each value holds until the
    # next keyTime, so ending the keyTimes at the typing fraction leaves the
    # final (full-width) value on screen for the rest of the cycle - that is the
    # hold, without a second <animate> competing for the same attribute.
    type_frac = TYPE_SECONDS / total
    values = ";".join(str(round(i * CHAR_W, 2)) for i in range(steps + 1))
    key_times = ";".join(
        str(round(i / steps * type_frac, 4)) for i in range(steps + 1))
    cursor_x = START_X + text_w + 4

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 96"
     width="{width}" height="96" role="img"
     aria-label="{LINE}">
  <title>{LINE}</title>
  <defs>
    <clipPath id="reveal">
      <rect x="{START_X}" y="20" height="56" width="0">
        <animate attributeName="width" values="{values}" keyTimes="{key_times}"
                 dur="{total}s" repeatCount="indefinite" calcMode="discrete" />
      </rect>
    </clipPath>
    <style>
      .mono {{
        font-family: ui-monospace, 'JetBrains Mono', 'SF Mono', Menlo, Consolas, monospace;
        font-size: {FONT_PX}px;
        font-weight: 700;
      }}
    </style>
  </defs>

  <text x="18" y="{BASE_Y}" class="mono" fill="{theme['prompt']}">&gt;</text>
  <g clip-path="url(#reveal)">
    <text x="{START_X}" y="{BASE_Y}" class="mono" fill="{theme['text']}"
          textLength="{round(text_w, 2)}" lengthAdjust="spacing">{LINE}</text>
  </g>
  <rect x="{cursor_x}" y="30" width="13" height="40" fill="{theme['cursor']}">
    <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1"
             dur="1.06s" repeatCount="indefinite" />
  </rect>
</svg>
"""


def main() -> int:
    out = Path(__file__).parent / "assets"
    out.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        path = out / f"typewriter-{name}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print(f"wrote {path} ({path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
