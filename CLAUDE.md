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

### File Structure
```
Vetrina26/
├── index.html    # Full HoDiritto website (HTML + CSS + JS, self-contained)
└── CLAUDE.md     # This file
```

### Tech Stack
- **Type**: Static single-page site, single `index.html`
- **Language**: Vanilla HTML, CSS, JavaScript — no frameworks, no build tools
- **Fonts**: Google Fonts — Inter (300–900) + Outfit (400–900)
- **Icons**: Inline SVGs
- **Styling**: All CSS embedded in `<style>` within `<head>`
- **JavaScript**: All JS in `<script>` at end of `<body>`
- **No dependencies**: No `package.json`, no `node_modules`

### Design System
- **Theme**: Light/clean with indigo/cyan accents
- **Background**: `#FAFBFF` (soft blue-white)
- **Primary**: `#4F46E5` (indigo) with gradient to `#7C3AED` and `#06B6D4` (cyan)
- **Typography**: Outfit (headings) + Inter (body)
- **Cards**: Glassmorphism, soft shadows, gradient top-borders on hover
- **Animations**: Scroll reveal, counter animation, process line, parallax shapes, dot pulse, gradient shift, button shine

### Sections
1. **Nav** — Fixed, glassmorphism on scroll, logo "H" icon + "HoDiritto", links + auth buttons, hamburger mobile
2. **Hero** — Full-viewport, floating gradient shapes, dot grid, badge, headline with gradient text, stats row
3. **Features** (`#features`) — 3 cards: Proattivo, Personalizzato, Dalla tua parte
4. **Stats** (`#stats`) — 3 animated counter cards: 16M, 32Mrd€, 1 su 2
5. **Process** (`#process`) — 3-step timeline with animated connecting line
6. **Case Study** (`#case-study`) — Carlo's story with loss/win comparison boxes + notification
7. **Dual CTA** (`#cta`) — Worker form (waiting list) + Company form (contact)
8. **Footer** — Logo, legal links, copyright

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
- **All code is in `index.html`** — edit and refresh, no build step
- Forms have no backend connected (textarea + button only)
- Auth links (Registrati/Accedi) are placeholder `href="#"`

### Responsive Breakpoints
- `900px` — Mobile nav (hamburger menu)
- `768px` — Feature cards, stats, process steps, CTA cards stack
- `600px` — Footer stacks
