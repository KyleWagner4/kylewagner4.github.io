/*
  Number formatting with financial-statement conventions:
  negatives in parentheses for statements, a true minus (U+2212) for
  signed changes, and fixed decimals so columns align.
*/

export type FigureStyle = 'number' | 'currency' | 'percent';

export interface FigureOptions {
  style?: FigureStyle;
  decimals?: number;
  /** Value is already in percent units (5.2 means 5.2%). */
  percentUnits?: boolean;
}

const MINUS = '−';

function formatter({ style = 'number', decimals = 0 }: FigureOptions): Intl.NumberFormat {
  return new Intl.NumberFormat('en-US', {
    style: style === 'currency' ? 'currency' : style === 'percent' ? 'percent' : 'decimal',
    currency: 'USD',
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

function magnitude(value: number, options: FigureOptions): string {
  const scaled = options.style === 'percent' && options.percentUnits ? value / 100 : value;
  return formatter(options).format(Math.abs(scaled));
}

/** "1,234" or "(1,234)". */
export function formatStatement(value: number, options: FigureOptions = {}) {
  const text = magnitude(value, options);
  const negative = value < 0;
  return { text: negative ? `(${text})` : text, negative, plain: negative ? `${MINUS}${text}` : text };
}

/** "+1.2%" or "−1.2%"; zero has no sign. */
export function formatDelta(value: number, options: FigureOptions = {}): string {
  const text = magnitude(value, options);
  if (value > 0) return `+${text}`;
  if (value < 0) return `${MINUS}${text}`;
  return text;
}

/** Plain figure, true minus for negatives. */
export function formatFigure(value: number, options: FigureOptions = {}): string {
  const text = magnitude(value, options);
  return value < 0 ? `${MINUS}${text}` : text;
}
