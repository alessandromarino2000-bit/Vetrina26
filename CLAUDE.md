# Vetrina26 — HoDiritto Website

## Target Website
URL: `https://davidechirichella.com/`
The target site to study/replicate is **HoDiritto** — an Italian healthcare rights assistant platform.

---

## Target Site Analysis (davidechirichella.com)

### What Is HoDiritto?
HoDiritto is a personal healthcare assistant for Italian workers. It helps users discover and claim healthcare benefits they're entitled to from their employer-provided health funds (fondi sanitari) and the Italian National Health Service (SSN). The tagline: **"La tua salute ha dei diritti. Noi ti aiutiamo a usarli."** (Your health has rights. We help you use them.)

### Target Audience
1. **Workers (Lavoratori)** — Employees who have employer-provided health fund coverage but don't know what they're entitled to
2. **Companies (Aziende)** — Employers already investing in employee welfare who want to increase ROI on those benefits

### Key Value Propositions
- **Proactive**: Alerts users before deadlines expire or reimbursements are lost
- **Personalized**: Analyzes individual profiles (age, region, fund, contracts) to show only relevant benefits
- **User-first**: Works for the user, not for funds or insurance companies

### Site Sections
1. **Nav** — Logo "HoDiritto", links: Chi siamo, Come funziona, Unisciti a noi, Registrati, Accedi
2. **Hero** — Headline + subtitle, dual CTAs: "Entra nel portale" / "Entra nella waiting list"
3. **What is HoDiritto? (Cos'è HoDiritto?)** — 3 feature cards: Proattivo, Personalizzato, Dalla tua parte
4. **Stats (I numeri della sanità integrativa)** — 3 key metrics:
   - 16 Milioni — Italiani con fondo sanitario
   - 32 Miliardi € — Pagati di tasca propria ogni anno
   - 1 su 2 — Lavoratori disinformati
5. **How It Works (Tre passi. Zero burocrazia.)** — 3 steps:
   1. Raccontaci chi sei (Tell us who you are)
   2. Analizziamo i tuoi diritti (We analyze your rights)
   3. Ti diciamo come ottenerli (We tell you how to get them)
6. **Testimonial/Case Study** — Story of Carlo, 45yo metalworker, who didn't know Metasalute covered his surgery
7. **Dual CTA Section (Da dove vuoi iniziare?)** — Two paths:
   - **Sei un lavoratore?** — Worker signup with waiting list form (textarea + "Tienimi aggiornato")
   - **Sei un'azienda?** — Company contact form (textarea + "Contattatemi")
8. **Footer** — Logo, Termini di Servizio, Cookie Policy, Contatti, copyright 2026, build date

### Content Language
- **Italian** — The entire site is in Italian

---

## Current Repo State

### What's In The Repo Now
The repo currently contains a **Klyren** landing page (B2B lead gen agency) — this is a different site/template, NOT the HoDiritto target.

### Current File Structure
```
Vetrina26/
├── index.html    # Klyren landing page (~1040 lines, self-contained HTML+CSS+JS)
└── CLAUDE.md     # This file
```

### Current Tech Stack (Klyren template in repo)
- **Type**: Static single-page site, single `index.html`
- **Language**: Vanilla HTML, CSS, JavaScript — no frameworks, no build tools
- **Font**: Google Fonts — Inter (weights: 300–900)
- **Icons**: Inline SVGs
- **Styling**: All CSS embedded in `<style>` within `<head>`
- **JavaScript**: All JS in `<script>` at end of `<body>`
- **No dependencies**: No `package.json`, no `node_modules`

### Current Design System (Klyren)
- Dark theme: near-black background (`#0a0a0a`)
- Purple accent palette (`#9333EA`, `#C084FC`, `#A855F7`)
- Font: Inter, system-ui fallback
- Animations: cursor glow, floating particles, scroll reveal, counter animation, card spotlight, parallax orbs

### Current Sections (Klyren)
1. Nav (fixed, with hamburger mobile menu)
2. Hero (full-viewport, animated orbs background)
3. Marquee (auto-scrolling keywords)
4. Services (5 cards in grid)
5. Process (4-step horizontal timeline)
6. Results (3 metrics + 3 testimonials)
7. About (brand story)
8. Contact (CTA block + form)
9. Footer (logo + socials)

---

## Development Environment

### How to Run
```bash
# Option 1: Python
python3 -m http.server 8000

# Option 2: Node (if available)
npx serve .

# Option 3: Just open directly
open index.html
```

### How to Modify
- **All code is in `index.html`** — CSS in `<style>` (lines 11–573), HTML (lines 575–900), JS in `<script>` (lines 902–1038)
- No build step — edit and refresh
- Form uses `onsubmit="return false"` (no backend)
- Social links are placeholder `href="#"`

### Responsive Breakpoints (current)
- `768px` — Mobile nav, process steps stack
- `640px` — Metrics stack
- `500px` — Form single column
- `420px` — Service cards single column

---

## Key Differences: Current Repo vs Target Site

| Aspect | Current (Klyren) | Target (HoDiritto) |
|---|---|---|
| **Language** | English | Italian |
| **Business** | B2B lead gen agency | Healthcare rights assistant |
| **Audience** | SMBs needing outbound | Italian workers & companies |
| **Sections** | Services, Process, Results, About, Contact | Features, Stats, How-It-Works, Case Study, Dual CTA |
| **Forms** | Single contact form | Two forms (worker waiting list + company contact) |
| **Auth** | None | Has Registrati/Accedi (Register/Login) |
| **CTA Style** | "Book a Call" | "Entra nel portale" / "Waiting list" |
| **Testimonials** | 3 generic review cards | 1 detailed case study (Carlo) |
| **Stats** | 500+ Leads, 95% Deliverability, $12K MRR | 16M Italians, €32B out-of-pocket, 1 in 2 uninformed |
