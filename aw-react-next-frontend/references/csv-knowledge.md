# Offline technical knowledge

Run these commands from the directory containing this skill's SKILL.md, or use
absolute script paths. Run the task mapper first; it routes recognized technical intent to bundled CSV records:

```bash
python3 scripts/map-task.py --root /path/to/project --task 'tối ưu tải dữ liệu React Next.js'
python3 scripts/map-task.py --root /path/to/project --task 'Làm luồng đặt lịch' --query 'form validation accessibility'
```

Run a focused lookup when repository mapping is already available:

```bash
python3 scripts/search-csv.py 'data fetching' --domain nextjs
python3 scripts/search-csv.py 'keyboard focus' --domain web
```

| Domain | Local dataset | Routing evidence |
| --- | --- | --- |
| `react` | `data/react-performance.csv` | React/Next task mention or declared dependency |
| `react-stack` | `data/stacks/react.csv` | Same framework evidence; inspect `Applies To` |
| `nextjs` | `data/stacks/nextjs.csv` | Next task mention or declared dependency |
| `web` | `data/ux-guidelines.csv` | Form, accessibility, layout intent; generic fallback |

Interpret `knowledge.searches` as ranked evidence, not implementation instructions:

- Follow `source` relative to this skill and `record` as the one-based data row, excluding the header. CSV records may span physical lines.
- Check `values`, matched terms, platform, version applicability, and linked official documentation before applying a suggestion.
- Prefer Vercel/React/Next.js primary guidance when records disagree. Some stack rows target newer versions than the repository; preserve existing versions and router.
- Keep business/domain vocabulary out of technical lookup unless explicitly relevant. The mapper extracts fetching, caching, rendering, bundles, forms, accessibility, routing, composition, images, or layout intent.
- Treat `no_match` honestly; use an explicit English `--query` when the finite Vietnamese aliases or intent patterns miss the request. Unknown tasks do not trigger generic React matches merely from the framework name.
- Treat `error` as a missing/invalid data warning; repository mapping remains available.
- Inspect manifest paths in routing reasons before applying results to one app of a monorepo.

The search reads local CSVs only. No packages, credentials, environment variables, or network calls are needed. See `requirements.txt`. Review bundled provenance and license before redistributing the datasets.
