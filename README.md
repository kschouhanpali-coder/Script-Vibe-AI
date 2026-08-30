<div align="center">

# ⚡ ScriptVibe AI
### Viral YouTube Script Studio & Teleprompter

**An AI-powered script generation studio that creates ready-to-record viral YouTube scripts in seconds.**

Configure your niche, tone, audience, and hook style — then let Google Gemini do the writing.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://script-vibe-ai-mwtqtjlp27532narmb4mua.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini](https://img.shields.io/badge/Google_Gemini-Powered-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)

![System Online](https://img.shields.io/badge/●_SYSTEM-ONLINE-00FF88?style=flat-square)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Live Demo](#-live-demo)
- [Why ScriptVibe AI?](#-why-scriptvibe-ai)
- [Features](#-features)
- [Studio Workspace](#️-studio-workspace)
- [Configuration Parameters](#️-configuration-parameters)
- [How It Works](#-how-it-works)
- [Getting Started](#-getting-started)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Use Cases](#-use-cases)
- [Roadmap](#️-roadmap)
- [FAQ](#-faq)

---

## 🎯 Overview

**ScriptVibe AI** takes the blank-page problem out of YouTube content creation. Instead of staring at an empty document, describe your video concept, pick a few configuration options, and get a fully structured, ready-to-record script back in seconds — complete with a hook, a teleprompter-ready format, and SEO-optimized metadata. It's built for creators who want to spend less time writing and more time recording.

Writing a good YouTube script isn't just about putting words on a page — it's about nailing the first five seconds, pacing the content for retention, and matching tone to audience. ScriptVibe AI bakes those principles directly into the generation pipeline, so every script it produces is already structured around what actually keeps viewers watching, not just what sounds nice on paper.

---

## 💡 Why ScriptVibe AI?

- **Speed** — go from idea to a full, structured script in seconds instead of hours
- **Retention-first design** — every script is built around a strong hook and paced for watch time, not just written prose
- **Fully configurable** — niche, tone, length, audience, hook style, and language are all adjustable per script
- **Recording-ready output** — the built-in teleprompter means you can go straight from generation to filming
- **SEO baked in** — auto-generated titles, descriptions, and tags mean you're not starting from scratch on the upload page either
- **No local setup required** — the hosted version runs entirely in your browser with just a Gemini API key

---

## 🌐 Live Demo

<div align="center">

### 👉 [**Launch ScriptVibe AI**](https://script-vibe-ai-mwtqtjlp27532narmb4mua.streamlit.app)

*No installation needed — open the link, add your Gemini API key, describe your video concept, and generate a viral script instantly.*

</div>

---

## ✨ Features

<table>
<tr>
<td valign="top" width="50%">

### ⚡ Script Generation
- **Viral Script Generation** — AI-crafted scripts optimized for engagement and retention
- **Niche Targeting** — Tech & AI, Finance, Lifestyle, and more
- **Script Tone Control** — Engaging & Fast-paced, Educational, Storytelling, and more
- **Video Length Targeting** — scripts for 1–2 min, 5–7 min, or 10+ min videos
- **First 5s Hook Styles** — shocking fact, bold question, controversial statement, story hook

</td>
<td valign="top" width="50%">

### 🎬 Production Ready
- **Audience Selection** — Tech Enthusiasts, General Audience, Students, and more
- **Multi-language Support** — generate scripts in English and other languages
- **Teleprompter Mode** — read your script hands-free with a built-in scrolling teleprompter
- **Raw Markdown View** — copy the raw script for editing in any tool
- **Video Metadata** — auto-generated titles, descriptions, and tags for YouTube SEO

</td>
</tr>
</table>

---

## 🖥️ Studio Workspace

The **Script Studio Workspace** has four views:

| View | Description |
|---|---|
| 🎬 **Studio View** | Formatted, section-by-section script view |
| 📺 **Teleprompter** | Auto-scrolling teleprompter for recording |
| 📝 **Raw Markdown** | Raw script text for copy-paste editing |
| 📊 **Video Metadata** | YouTube title, description, tags & thumbnail ideas |

---

## ⚙️ Configuration Parameters

| Parameter | Options |
|---|---|
| **Niche** | Tech & AI, Finance, Health, Lifestyle, Gaming, Education… |
| **Script Tone** | Engaging & Fast-paced, Educational, Storytelling, Motivational… |
| **Video Length** | 1–2 Minutes, 3–5 Minutes, 5–7 Minutes, 10+ Minutes |
| **Target Audience** | Tech Enthusiasts & Developers, General Audience, Students… |
| **First 5s Hook Style** | Shocking fact or statistic, Bold question, Controversial statement… |
| **Language** | English, Hindi, Spanish, French, and more |

---

## ⚙️ How It Works

1. **Describe your concept** — enter a short description of what your video is about, in plain language
2. **Set your configuration** — choose niche, tone, target length, audience, hook style, and language
3. **Prompt engineering pipeline** — ScriptVibe AI assembles a structured prompt combining your concept and configuration, tuned to produce a retention-optimized script
4. **Gemini generation** — Google Gemini generates the full script, broken into a hook, body sections, and a closing call-to-action
5. **Post-processing** — the raw output is formatted into the Studio View, converted into teleprompter-friendly pacing, and used to generate matching video metadata
6. **Review & record** — switch between Studio, Teleprompter, Raw Markdown, and Metadata views to refine and prepare for filming

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Google Gemini API Key — [get one free here](https://aistudio.google.com/app/apikey)

**1. Clone the repository**
```bash
git clone https://github.com/your-username/scriptvibe-ai.git
cd scriptvibe-ai
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

### Usage

| Step | Action |
|---|---|
| 1️⃣ | Open the app (local or via the [Live Demo](https://script-vibe-ai-mwtqtjlp27532narmb4mua.streamlit.app)) |
| 2️⃣ | Enter your **Gemini API Key** in the Studio Configuration panel |
| 3️⃣ | Describe your **Video Concept / Topic** |
| 4️⃣ | Select your **Niche, Tone, Length, Audience, Hook Style & Language** |
| 5️⃣ | Click **⚡ GENERATE VIRAL SCRIPT** |
| 6️⃣ | Switch to **Teleprompter** view and start recording! |

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Frontend** | Streamlit |
| **LLM** | Google Gemini |
| **Script Engine** | Custom prompt engineering pipeline |
| **Teleprompter** | Streamlit custom components |
| **Deployment** | Streamlit Cloud |

---

## 📁 Project Structure

```bash
scriptvibe-ai/
├── app.py                  # Main Streamlit app
├── utils/
│   ├── generator.py         # Gemini script generation logic
│   ├── teleprompter.py      # Teleprompter component
│   └── metadata.py          # YouTube metadata generator
├── requirements.txt
└── README.md
```

---

## 🎥 Use Cases

- **Solo creators** who need to produce scripts quickly without a writing team
- **Faceless YouTube channels** looking for consistent, structured scripts across a niche
- **Content agencies** generating first-draft scripts for multiple clients or niches at once
- **Non-native English speakers** who want polished scripts in their preferred language
- **New creators** learning what a well-structured, retention-focused script actually looks like

---

## 🗺️ Roadmap

- [ ] Support for additional LLM providers beyond Gemini
- [ ] Script versioning and history so you can compare past generations
- [ ] Team/collaboration mode for shared script libraries
- [ ] Direct export to video editing tools
- [ ] AI-suggested B-roll and visual cues alongside the script
- [ ] Voice-over generation option for full audio drafts

---

## ❓ FAQ

**Do I need my own Gemini API key?**
Yes — ScriptVibe AI uses your own Google Gemini API key so you control usage and costs directly. You can get one for free from Google AI Studio.

**Can I edit the generated script?**
Yes. The Raw Markdown view gives you the full script as plain text, ready to paste into any editor for further refinement.

**Is the teleprompter speed adjustable?**
The teleprompter is designed for hands-free reading during recording — check the Teleprompter view in the Studio Workspace for available pacing controls.

**Does it support languages other than English?**
Yes — you can select from multiple languages including Hindi, Spanish, and French when configuring your script.

**Is my API key stored anywhere?**
Your Gemini API key is used only to make requests during your session — always review the app's current data handling behavior before entering sensitive credentials.

---
