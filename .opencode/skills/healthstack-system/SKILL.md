---
name: healthstack-system
description: HealthStack-System work (Django multi-hospital records platform, SQLite, DRF + Django channels). Use for ANY task under /home/fabiljayson/Projects/HealthStack-System-main — covers run command and the archival/university-project framing.
---

# HealthStack-System (main)

Multi-hospital platform: patient records sharing, appointments, online pharmacy, lab payments (SSLCommerz), doctor chat (Django channels). Stack: Django + DRF + Bootstrap + Ajax/JS + SQLite.

## Run

```bash
cd HealthStack-System-main && python manage.py runserver
```

## Framing

University Software-Engineering project (B.Sc. CSE, March–June 2025, team of multiple contributors incl. Bless Junior). Treat it as **semi-archival**: no active roadmap. Confirm with the user before refactoring; keep changes small and compatible with the existing 5-role model (Patient, Doctor, Hospital Admin, Lab Worker, Pharmacist).

## Pitfalls

- SQLite + Django channels in dev is fine, but don't promise production-grade chat performance from this stack.
- External services (MailTrap, SSLCommerz) use test/dev credentials — never hardcode or leak them in docs or commits.
- Don't confuse with `HealthStack-System-2.0` (empty sibling repo with no files).
