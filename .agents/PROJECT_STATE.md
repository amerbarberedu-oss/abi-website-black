# ABI Website — Project State

## Last Updated
- **Date:** 2026-07-11 (July 11, 2026)
- **Agent:** Antigravity
- **Branch:** `main`
- **Latest Commit:** `aecf3bf` — Fix CSP: Google country TLDs + unsafe-eval
- **Status:** ✅ DEPLOYED TO PRODUCTION (abi.edu)

## Deployment
- **Vercel Account:** amerbarberedu-oss-projects (Alex)
- **Git Remote:** `origin` → amerbarberedu-oss/abi-website-black
- **Domain:** www.abi.edu / abi.edu

## Stable Baseline
- **Production commit:** `aecf3bf`
- **Rollback point:** `2d34130` (pre v0.4.0)

## Current Versions
- `landing.css?v=153`
- `campus.js?v=5`
- `funnels.css?v=59`
- `analytics.js?v=6` (abi.edu) — NOT MODIFIED (Arhum's domain)

## What's Deployed
- Campus-specific phone number system (Manhattan 2+1, Bronx 1+1)
- Gold theme (109 bx-gold override rules)
- SEO/AEO audit passing (17/17)
- CSP fully configured for all analytics services
- Clean codebase: no dead code, no unused images, no stale files
