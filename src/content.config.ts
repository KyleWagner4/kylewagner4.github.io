import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Case studies: problem, what I built, how it works, measurable result.
// order sets their position in the home page index.
const work = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/work' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    order: z.number().int().positive(),
    metric: z.object({ value: z.string(), label: z.string() }).optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { work };
