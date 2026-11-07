<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0A0A,35:1a1a2e,70:8B0000,100:0A0A0A&height=160&section=header&text=DOSSIER&fontSize=54&fontColor=FCEE0A&stroke=FFFFFF&strokeWidth=0.5&desc=KERBEROS%20KORP%20ARCHIVE%20%E2%80%A2%20TYPE-2026A%20%E2%80%A2%20EST.%202001%20%E2%80%A2%20GULF%20COAST%20FIELD%20UNIT&descAlignY=62&descSize=11&animation=fadeIn" width="100%" />

<div align="center">

**`TRISTEN McDUFF`** — トリステン・マクダフ · UNIT `TM-2026A` · S/N `MGCCC-CYBER-202605` · EST. 2001

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=13&duration=2400&pause=900&color=FCEE0A&center=true&vCenter=true&multiline=true&width=700&height=40&lines=Curated+archive+—+less+clutter%2C+clearer+signal;From+ProjectPortfolio+%26+A32Termux+to+a+single+reference+dossier)](https://git.io/typing-svg)]

<img src="https://img.shields.io/badge/SYSTEM-INDEXED-00F0FF?style=flat-square&labelColor=0A0A0A" /> <img src="https://img.shields.io/badge/STATUS-CURATED-E8E0D0?style=flat-square&labelColor=0A0A0A" /> <a href="https://github.com/Tometri"><img src="https://img.shields.io/badge/Profile-%40Tometri-0A0A0A?style=flat-square&logo=github&logoColor=white" /></a> <a href="https://github.com/Tometri/it_support_bot"><img src="https://img.shields.io/badge/it__support__bot-Live-0078D4?style=flat-square&logo=robotframework&logoColor=white" /></a>

</div>

<div align="left">

```ansi
┌─ kerberos@tm-2026a:/dossier ───────────────────────────  15.734kHz ─┐
│ ◇  ◯  ×  □  △      A R C H I V E   I N D E X   . . .   OK          │
│ KERBEROS KORP EST. 2001  •  GULF COAST FIELD UNIT  •  REV 2.077   │
└───────────────────────────────────────────────────────────────────┘
kerberos@tm-2026a:/dossier$ tree -L 2 --dirsfirst
```

</div>

### What this is

Curated archive distilled from `ProjectPortfolio`, `A32Termux`, and scattered coursework — one reference dossier, less clutter, clearer navigation. Structured for **recruiters, collaborators, and future-me** who needs to find a cert, a lab, or a code sample in under 30 seconds.

> Full profile lives at **[@Tometri](https://github.com/Tometri)** — this repo is the filing cabinet, that one is the dossier cover.

### ◯ Quick index

| Path | What's inside | For |
|------|---------------|-----|
| [`Documents/Certificates/`](Documents/Certificates/) | CompTIA Security+, ISC2 CC, AZ-900, Cato AI — PDFs + domain breakdowns | Verify creds |
| [`Documents/Resume/Archive/`](Documents/Resume/Archive/) | `Tristen_McDuff_Resume_IT_2026*.docx` — base + enhanced, pre-2001 to present | Hiring |
| [`Documents/AzureTemplates/`](Documents/AzureTemplates/) | `SecureVM.json` + `AzureFirewalledVNet.zip` — VNet + Firewall + TrustedLaunch VM | Cloud / infra review |
| [`Documents/Notes/`](Documents/Notes/) | `AD_DS.md`, `CiscoNetworkingBasics.md`, `AWS_*.md`, `CIAT_Sec+`, `assembly.md`, `GitCommands.md` — condensed study notes | Reference |
| [`CiscoPacketTracer/`](CiscoPacketTracer/) | `.pka` activities — wireless router + simple network + quizzes | Networking labs |
| [`Python/`](Python/) | `Codedex` (50+ scripts) + `PythonCrashCourse` — code samples | Reference |
| [`PowerShell/`](PowerShell/) | `PortEnumeratorPS5.ps1`, `PortEnumeratorPS7.ps1` — port enumeration scripts | Reference |
| [`ObsidianVault/`](ObsidianVault/) | Cross-device notes, incl. `ComputerForensics/` | Reference |
| [`ProfileREADMEs/`](ProfileREADMEs/) | Profile README drafts (80s + CyberPunk, V2) | Reference |
| [`HTML/`](HTML/) | `codedex/` — ~30 hand-built pages | Frontend basics |
| [`HTML/codedex/`](HTML/codedex/) | `Elements` / `Forms` / `Structure` — ~30 hand-built pages | Frontend basics |

### × Featured — start here

**1. [`it_support_bot`](https://github.com/Tometri/it_support_bot) — IT Support Chatbot (Python)** — scored retrieval over a curated KB (password resets, VPN, error codes) with cited sources + deterministic fallback; `http.server` UI + CLI. The most recruiter-relevant project in this dossier.

  How it works: a curated knowledge base is chunked and scored against the user's question; the best-matching chunk grounds the answer with a cited source. If no chunk scores high enough — or no LLM key is present — it falls back deterministically to a safe, scripted answer instead of guessing, with escalation paths for out-of-scope and sensitive requests. Entry points are the CLI and a lightweight `http.server` web UI on `127.0.0.1:8000`. See [`it_support_bot.md`](it_support_bot.md) for the architecture summary.

**2. Azure VNet + Firewall + SecureVM** — `Documents/AzureTemplates/SecureVM.json` — Debian 12-gen2, Premium LRS, Secure Boot + vTPM, SSH-key auth, boot diagnostics. Deployed in Azure, template archived here.

**3. Packet Tracer — Wireless Router & Client / Simple Network** — `CiscoPacketTracer/Activities/` — CCNA 1 & 2 aligned.

```
┌─────────────────────────────────────────────────┐
│  CART  •  60-PIN  •  CHR / PRG  •  CIC LOCK     │
│  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
│  PCB REV: TM-2026A  •  REGION: NTSC-U  •  SAVE: BATTERY BACKED │
└─────────────────────────────────────────────────┘
```

### □ How to use

```bash
# clone
git clone https://github.com/Tometri/Dossier.git
cd Dossier

# browse certs
ls Documents/Certificates/CompTIA/
ls Documents/Certificates/ISC2_CC/

# deploy Azure template (example)
az deployment group create -g rg-lab --template-file Documents/AzureTemplates/SecureVM.json

# run a Python sample
python Python/Codedex/calculator.py
```

### △ Credentials at a glance

| Credential | Earned | Valid Thru |
|------------|--------|------------|
| CompTIA Security+ (SY0-701) | Jun 22, 2026 | Jun 22, 2029 |
| ISC2 Certified in Cybersecurity (CC) — ACE 3cr | Jul 13, 2026 | Jul 31, 2029 |
| Microsoft AZ-900 | 2026 | — |
| AWS Educate: Intro to Generative AI | May 20, 2026 | — |
| AI Literacy Professional (Pearson) | Feb 20, 2026 | — |
| AI in Cybersecurity (Cato) | Aug 24, 2026 | — |
| Cato SSE Expert Certification | Oct 31, 2026 | — |
| MongoDB Basics for Students | Oct 31, 2026 | — |
| SASE Business Impact and Strategy (Cato) | Oct 30, 2026 | — |
| SASE Advanced Security / Deployment and Management (Cato) | Oct 29, 2026 | — |
| SASE Expert Level 1 / Level 2 (Cato) | Oct 29, 2026 | — |
| Zero Trust Security Essentials (Cato) | Oct 28, 2026 | — |
| CompTIA Linux+ | In queue — voucher secured | — |

Verify: [credly.com/users/tristen-mcduff](https://credly.com/users/tristen-mcduff) · Full detail in [@Tometri profile](https://github.com/Tometri).

### ○ Notes

- **Resume:** Canonical files are `Documents/Resume/Archive/Tristen_McDuff_Resume_IT_2026*.docx` — enhanced build mirrors the profile.
- **Certificates:** Original PDFs retained by issuer folder; filenames are issuer-original.
- **Theme note:** the KERBEROS KORP framing, unit numbers, and serial numbers are a retro theme, not an official affiliation or identifier.
- **Naming:** `Dossier` is the curated set. `ProjectPortfolio` and `A32Termux` remain as raw sources — this repo is the signal, not the noise.

<div align="left">

```ansi
┌─────────────────────────────────────────────────────────────────────────┐
│  KERBEROS KORP  •  PANZER COP DIVISION  •  PROTECT GEAR UNIT  •  ©2001-2026  │
│  “Good technicians document. Great ones make the next tech’s job easier.”       │
└─────────────────────────────────────────────────────────────────────────┘
kerberos@tm-2026a:/dossier$ █
```

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0A0A,100:0A0A0A&height=70&section=footer&text=END%20OF%20LINE%20%E2%80%94%20%E6%9C%80%E7%B5%82%E8%A1%8C&fontSize=10&fontColor=4a5568&animation=fadeIn" width="100%" />
