# Lloyds Banking Group (incl. Lloyds, Halifax, Bank of Scotland, Scottish Widows, Lloyds Wealth / ex-Schroders Personal Wealth): AI Products and Achievements Inventory (as of Sept 2026)

Research scope note: roughly 30 search/fetch calls. Primary sources (lloydsbankinggroup.com, scottishwidows.co.uk, Microsoft/Google press rooms) are preferred. Items that rest only on one secondary source are marked **[single secondary source]**. The sources do not always agree on dates and figures. Those conflicts are listed where they come up.

## Q1: Lloyds' GenAI / AI strategy (Athena, financial assistant, Google Cloud, platforms, CoE, leadership)

### Takeaway
Lloyds runs a platform-led AI strategy with three main vendors. Google Cloud provides Vertex AI for the ML/GenAI platform and co-built the Envoy agent platform. Microsoft provides M365 Copilot, GitHub Copilot and the M365 E7 / Agent 365 suite. Aveni, in which Lloyds has invested, provides FinLLM. Lloyds says GenAI delivered about £50m of value in 2025 from about 50+ use cases, and it targets more than £100m from GenAI and agentic AI in 2026. Under "Accelerate 2030" (launched 30 July 2026), it says AI will support every customer interaction and every colleague by 2030. The two flagship items are Athena, a colleague knowledge assistant, and the agentic AI Financial Assistant in the app. The Financial Assistant was announced in November 2025 and had more than 500k Bank of Scotland users by mid-2026.

### Cited Findings — Itemised inventory

**1. Athena (GenAI colleague knowledge assistant). Colleague tools / retail operations. Live.**
- Announced 15 July 2025. Customer service colleagues in telephone and online banking use it to search about 13,000 internal knowledge articles. Average search time fell from 59 seconds to about 20 seconds, a 66% reduction. Telephone banking is projected to save about 4,000 hours a year. 21,000 colleagues ran 2.1m searches in early 2025, and the group projected 40m searches by year-end. The release names no vendor — [LBG press release, 15 Jul 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-accelerates-with-athena.html)
- Athena uses RAG grounded in approved internal content and runs on the group's Vertex AI-based ML/GenAI platform — [AI at LBG Medium blog, Jun 2026](https://medium.com/ai-at-lloyds-banking-group/athena-building-an-ai-powered-knowledge-platform-at-lloyds-banking-group-6b18107e23c9) (Vertex AI detail from search summary; the blog was not fetched directly)
- The 2026 figure is 20,000 colleagues with 66% faster search — [LBG press release, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html). The LBG AI hub page says 30,000+ customer-facing colleagues and 4m LLM-enabled searches a month — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html). **Conflict:** user numbers differ by source and date: 20k, 21k, 30k+, and 35k daily in one search summary.

**2. AI Financial Assistant (agentic AI, in the mobile app). Retail and wealth-adjacent. Announced, then pilot, then rolling out.**
- Announced 6 November 2025 as "the UK's first multi-feature AI-powered financial assistant", with launch set for early 2026 to the 21m app customers. The first two "hero" features are conversational spending insights and a savings-and-investments tool. It is also described as offering 24/7 personalised coaching, and it will expand to mortgages, car finance and protection. It hands customers over to human experts when needed and uses agentic AI with guardrails. Named executives are Ranil Boteju (Chief Data & Analytics Officer) and Helen Bierton (Chief Digital Officer) — [LBG press release, 6 Nov 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-unveils-uks-first-ai-powered-financial-assistant.html)
- About 7,000 employees tested it pre-launch, running 12,000 trials; it can query a payment and carry out the transaction — [The Paypers](https://thepaypers.com/fintech/news/lloyds-banking-group-to-launch-its-agentic-ai-financial-assistant) / [Fintech Futures](https://www.fintechfutures.com/ai-in-fintech/lloyds-banking-group-to-launch-ai-financial-assistant-in-2026) (secondary sources; the LBG release as fetched did not give the test numbers)
- By 22 June 2026 it had been deployed to more than 500,000 Bank of Scotland customers — [LBG press release, 22 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/1000-new-ai-roles.html); [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html). The rollout used Bank of Scotland first; full customer rollout is a 2026 milestone — [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html)
- The Q4 2025 results call described in-app AI agents in colleague beta, a conversational interface for everyday banking and spending insights, and an AI investment advice service in colleague testing — [Investing.com transcript, FY2025 results (Jan 2026)](https://www.investing.com/news/transcripts/earnings-call-transcript-lloyds-banking-q4-2025-sees-strong-income-growth-93CH-4472475)

**3. Google Cloud / Vertex AI ML and GenAI platform. Enterprise platform. Live.**
- Announced 9 April 2025 at Google Cloud Next. Lloyds moved 15 modelling systems, covering hundreds of models, from on-premise to Vertex AI. More than 300 data scientists and AI developers use the platform. The move saved 27 tonnes of CO2 in operational emissions. Since the move there have been 80+ new ML use cases and 18 GenAI systems in production, with 12 more due by end of June 2025. The platform supports third-party, open-source and Gemini LLMs. The release also announced an agentic AI prototype built with Google Cloud and an algorithm that cuts mortgage income verification from days to seconds — [LBG press release, 9 Apr 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-accelerates-ai-innovation-with-google-cloud.html); [Google Cloud press corner](https://www.googlecloudpresscorner.com/2025-04-09-Lloyds-Banking-Group-Accelerates-AI-Innovation-with-Google-Cloud)

**4. Envoy (enterprise AI-agent platform). Enterprise platform. Live.**
- Unveiled 1 May 2026 as a secure internal platform to build, deploy and govern AI agents. It was built with Google Cloud and integrates with LBG's LLM platform. Features: an Agent Marketplace for reuse, templates, built-in safety checks and risk monitoring, full audit trails, conversation memory with privacy controls, and behavioural monitoring. Ron van Kemenade (COO) is quoted. No agent counts were given — [LBG press release, 1 May 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-banking-group-unveils-envoy.html); [Medium blog](https://medium.com/ai-at-lloyds-banking-group/envoy-moving-ai-agents-from-concept-to-scaled-production-and-beyond-5ba18abecc54)

**5. Microsoft 365 Copilot. Colleague tools. Live.**
- 21 October 2025: nearly 30,000 M365 Copilot licences with 93% active usage, saving an average of 46 minutes a day per user. The same release reported 4,000+ data and tech hires since 2022, an AI Centre of Excellence of 200+ specialists, and 90,000 registrations for the Data Science Summer School 2025 — [LBG press release, 21 Oct 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-scales-adoption-of-copilot.html)
- By June 2026: 40,000 licences, with 97% of licence holders active — [LBG press release, 4 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/microsoft-365-frontier-suite.html)

**6. GitHub Copilot (code assistant). Engineering. Live.**
- Nearly 5,000 engineers use it. A code conversion of 11,000 lines across 83 files finished in half the expected time — [LBG, 21 Oct 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-scales-adoption-of-copilot.html). Lloyds reports a 50% improvement in converting code for established systems — [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html). The agreement extends it to more than 10,000 engineers — [LBG, 4 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/microsoft-365-frontier-suite.html)

**7. Microsoft 365 E7 "Frontier Suite" + Agent 365 + group-wide colleague assistant. Colleague tools. Deploying.**
- 4 June 2026: LBG is among the first UK organisations to deploy M365 E7 company-wide. E7 bundles E5, Copilot, Agent 365 with Work IQ, Entra Suite, Defender, Intune and Purview. Agent 365 will orchestrate multiple specialised agents. A single self-service "colleague assistant" agent is planned to give colleagues systems, information and answers in one place — [LBG press release, 4 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/microsoft-365-frontier-suite.html); [Microsoft UK Stories](https://ukstories.microsoft.com/features/lloyds-banking-group-rolls-out-microsoft-365-frontier-suite-to-power-its-agentic-future/)

**8. AI HR assistant / "Prosper". Colleague tools / HR. Live.**
- The AI HR assistant resolves about 90% of HR queries at first contact — [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html). "Prosper" is an HR solution credited with saving 4,000 working days — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html). It is uncertain whether Prosper is the same product as the AI HR assistant.

**9. Merlin (AI complaint summaries). Operations / complaints. Live.**
- Merlin produces AI-enabled summaries of customer complaints. Only the LBG AI hub page names it, and no launch date or metrics were found — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)

**10. Commercial Real Estate GenAI (tenancy schedule processing). Commercial banking. Live.**
- It processes complex tenancy documents in about 5 minutes — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html); [Medium blog](https://medium.com/ai-at-lloyds-banking-group/commercial-real-estate-artificial-intelligence-transforming-schedule-processing-with-generative-ai-fb3721920a0f)

**11. Mortgage income verification algorithm. Retail mortgages (Halifax, Lloyds). Announced April 2025.**
- It cuts the income verification step from days to seconds — [LBG, 9 Apr 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-accelerates-ai-innovation-with-google-cloud.html). At the H1 2026 strategy update, management said "agentic AI will make it easier than ever for customers to get advice" on mortgages — [Q2 2026 call transcript, 30 Jul 2026](https://stockanalysis.com/quote/lon/LLOY/transcripts/546825-q2-2026-strategy-update/)
- **Flag:** a search summary said Lloyds plans to deploy Oracle AI agents across retail, corporate, payments and insurance by mid-2026, and linked the mortgage algorithm to a "Gemini Enterprise Agent Platform". No primary source confirmed either claim, so both are excluded as unverified.

**12. AI Centre of Excellence and leadership.**
- The AI CoE had 200+ specialists as of October 2025 — [LBG, 21 Oct 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-scales-adoption-of-copilot.html). The AI page says 300+ AI specialists and 800+ AI models in production — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)
- **Sameer Gupta** was appointed Chief Data & AI Officer on 16 April 2026 and started in June 2026. He was previously Chief Analytics Officer at DBS and reports to COO Ron van Kemenade — [LBG, 16 Apr 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/sameer-gupta-chief-data-ai-officer.html). Ranil Boteju was Group Chief Data & Analytics Officer through 2025 — [LBG, 9 Apr 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-accelerates-ai-innovation-with-google-cloud.html). The April 2026 release does not say whom Gupta replaces.
- **Rohit Dhawan** is Group Head of AI and formerly AWS APAC Head of Data & AI Strategy. **Trystan Davies** is Group Head of Data & AI Science — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)
- On 21 January 2026, Dhawan's article "2026: The year of Agentic AI" set out five agentic focus areas: customer interactions, back-office work (fraud investigation, complaints, credit), frontline relationship-manager tools, a "colleague super-agent", and engineering (code conversion, test scripts) — [LBG insight](https://www.lloydsbankinggroup.com/insights/2026-the-year-of-agentic-ai-and-a-new-era-for-finance.html)

**13. Aveni investment / FinLLM. Partnership and investment.**
- Lloyds took part in Aveni's £11m Series A, led by Puma Private Equity with Nationwide and Scottish Enterprise, to develop FinLLM, an LLM for UK financial services, with Lloyds and Nationwide — [Aveni](https://aveni.ai/blog/aveni-secures-11m-investment-to-drive-ai-revolution-in-financial-services/). In a later £12m round in June 2026, led by PXN Ventures, LBG is listed as an existing investor — [Finextra](https://www.finextra.com/newsarticle/47859/lloyds-and-nationwide-backed-ai-fintech-aveni-raises-12-million); [FinTech Global, 4 Jun 2026](https://fintech.global/2026/06/04/lloyds-and-nationwide-backed-aveni-raises-12m/). University partners are Edinburgh, Bristol and Leeds — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)

### Inferences
- Lloyds uses different vendors for different layers. Google Cloud supplies the model and agent infrastructure (Vertex AI, Envoy). Microsoft supplies colleague productivity tools and agent orchestration (Copilot, E7/Agent 365). Aveni is a domain-LLM investment. HSBC benchmarks should compare at each of these layers.
- The Financial Assistant rollout started with Bank of Scotland, the smaller brand, before Lloyds and Halifax. This looks like a controlled launch sequence, but that is an inference.

### Gaps
- No primary source gives the LLM vendor or model inside the Financial Assistant. Vertex AI/Gemini is plausible but not confirmed.
- No count of agents live on Envoy was found.
- The Computer Weekly article on AI supporting all interactions by 2030 returned a 403 and could not be read.

## Q2: AI in wealth (Lloyds Wealth / ex-SPW, Scottish Widows, targeted support, InvestAI)

### Takeaway
The main wealth AI product is **InvestAI**, an AI investment agent inside the Scottish Widows app. Lloyds describes it as a "satnav for investments" that gives guidance rather than advice. It was piloted in H1 2026 through the FCA's AI Live Testing cohort and is being positioned for the FCA's new targeted-support regime. Lloyds plans to extend it as a simplified-advice service under the Lloyds Wealth brand, aiming for 1m new retail investors. SPW, now Lloyds Wealth, has used Aveni Detect for AI/NLP compliance monitoring of advice since 2023. No AI tools for Lloyds Wealth advisers, such as meeting-note or planning copilots, were found in public sources.

### Cited Findings
**14. Lloyds Wealth (formerly Schroders Personal Wealth), the corporate context.**
- On 9 October 2025, LBG agreed to buy Schroders' 49.9% of SPW in exchange for LBG's 19.1% stake in Cazenove Capital, with no cash paid, and to rebrand SPW as Lloyds Wealth. SPW then had about £17bn AuA, about 60k clients and about £45m operating profit in H1 2025. Schroders continues to manage assets under a multi-year agreement — [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-09/lloyds-takes-control-of-schroders-personal-wealth-joint-venture); [City AM](https://www.cityam.com/lloyds-banking-group-acquires-remaining-stake-in-schroders-personal-wealth/); [Investegate RNS](https://www.investegate.co.uk/announcement/rns/lloyds-banking-group--lloy/schroders-personal-wealth-acquisition/9160785)
- The rebrand was formally completed around May 2026; Calastone details changed on 5 May 2026 — [TheWealthNet](https://www.paminsight.com/twn/article/spw-formally-rebrands-to-lloyds-wealth); [Distributor Portal](https://distributorportal.co.uk/news/entry/spw-rebrand-announcement)
- **Conflict:** Financial Planning Today reports Lloyds Wealth AuA of £9.4bn at Q2 2026, down 5% since the buyout, against the widely cited £17bn — [Financial Planning Today, 30 Jul 2026](https://www.financialplanningtoday.co.uk/news/lloyds-wealth-launches-ai-simplified-advice-service). The figures may be measured on different bases. Separately, the Investing.com FY2025 transcript says SPW was acquired in "H2 2024", which conflicts with the October 2025 announcement and looks like a transcription error.

**15. InvestAI (AI investment agent / simplified advice). Wealth / Scottish Widows / Lloyds Wealth. Pilot, then rolling out.**
- InvestAI is embedded in the Scottish Widows app and is designed to "build both confidence and capability, opening up investing to those who've felt it's not for them" — [Scottish Widows press release, Aug 2026](https://www.scottishwidows.co.uk/about-us/media-centre/press-releases/expert-backed-ai-earns-pension-savers-trust.html)
- It launched in H1 2026 and has since supported 8,000+ conversations with pension scheme members — search summary of [Scottish Widows](https://www.scottishwidows.co.uk/about-us/media-centre/press-releases/expert-backed-ai-earns-pension-savers-trust.html) / [Professional Pensions](https://www.professionalpensions.com/news/4534174/trust-ai-tools-pension-guidance-scottish-widows). **[The 8,000 figure was not confirmed in the fetched primary text.]**
- On 22 April 2026, Reuters (via Resultsense) reported that Lloyds was the first UK lender to pilot an AI investment-decision tool, through Scottish Widows, with a small customer group and wider rollout later in 2026. Scottish Widows CEO Chira Barua called it "like a satnav for investments": it offers guidance, not regulated advice. Lloyds is one of eight firms in the FCA's second AI Live Testing cohort, and Advai is the FCA's technical partner — [Resultsense, 22 Apr 2026](https://www.resultsense.com/news/2026-04-22-lloyds-scottish-widows-ai-investment-guidance/); [Finimize](https://finimize.com/content/lloyds-tests-an-ai-tool-to-guide-everyday-investors)
- On 30 July 2026 (H1 results / Accelerate 2030), Lloyds said "Invest AI" is a new AI-enabled service to "bring simple advice to all" through Lloyds Wealth. It will form an "integrated lifetime proposition" running from execution-only D2C investing to full-advice financial planning. A version is already running in the Scottish Widows app, with targeted support planned — [Financial Planning Today, 30 Jul 2026](https://www.financialplanningtoday.co.uk/news/lloyds-wealth-launches-ai-simplified-advice-service)
- The strategy call said InvestAI launched in the Scottish Widows app sandbox using the targeted-support framework. It set a target of 1 million new retail investors through the AI-enabled offer, and said agentic "coaching agents" will extend wealth support across the retail banking app. Open-book wealth AuA is £110bn across D2C, intermediary and Lloyds Wealth. There are 22m app users and 5m workplace pension customers — [Q2 2026 call transcript](https://stockanalysis.com/quote/lon/LLOY/transcripts/546825-q2-2026-strategy-update/)
- Regulatory context: the FCA's targeted-support rules are set out in PS25/22 and are expected to apply from 6 April 2026 — [FCA PS25/22](https://www.fca.org.uk/publications/policy-statements/ps25-22-consumer-pensions-investment-decisions-rules-targeted-support); [FCA AGBR](https://www.fca.org.uk/firms/advice-guidance-boundary-review)

**16. Financial Assistant savings and investments feature. Retail and wealth. Pilot.**
- One of the two launch "hero" features is a savings and investment tool to help customers plan their financial futures — [LBG, 6 Nov 2025](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-unveils-uks-first-ai-powered-financial-assistant.html)

**17. Aveni Detect at SPW (AI/NLP advice compliance monitoring). Wealth / advice QA. Live since 2023.**
- Announced 7 March 2023. SPW adopted Aveni Detect, which uses NLP and GenAI, as a "Machine Line of Defence". It monitors all client interactions for conduct, complaints and vulnerability risk, ahead of Consumer Duty. Quotes from CEO Joseph Twigg and CRO Ray Milne — [Aveni](https://aveni.ai/blog/schroders-personal-wealth-spw/); [Money Marketing](https://www.moneymarketing.co.uk/news/schroders-adopts-ai-based-aveni-platform-to-transform-its-advice-offering/); [Finextra](https://www.finextra.com/pressarticle/95993/schroders-personal-wealth-adopts-ai-based-aveni-detect-platform)

**18. Scottish Widows research and positioning on AI (thought leadership).**
- The Retirement Report 2026 (August 2026) found that 30% would trust AI for pension guidance, and four in five of those would trust AI most if backed by a provider or regulated expert. 42% are comfortable using AI to explain jargon. Scottish Widows has more than 6.5m customers and says it is "building new AI-powered assistants" — [Scottish Widows](https://www.scottishwidows.co.uk/about-us/media-centre/press-releases/expert-backed-ai-earns-pension-savers-trust.html); [Retirement Report](https://expertise.scottishwidows.co.uk/retirement-report/technology-and-ai-in-retirement-decision-making/ai-in-retirement-decision-making)

### Inferences
- InvestAI is the direct competitor to any HSBC mass-affluent AI guidance offer. Lloyds is moving its AI towards regulated targeted support and then simplified advice, using Scottish Widows' 5m workplace pension base as its distribution channel. Resultsense also reports that HSBC is studying similar AI deployments for customers with £15k–£37.5k in liquid assets [single secondary source].
- Lloyds' wealth AI emphasis is on customers who don't yet invest and on the hybrid funnel from D2C to simplified advice to full advice. It is not an adviser-copilot strategy.

### Gaps
- No public information was found on AI tools used by Lloyds Wealth advisers beyond Aveni Detect, such as note-taking or suitability-report generation.
- InvestAI's vendor, model and pricing were not disclosed. It is unclear whether InvestAI in Scottish Widows and "Invest AI" under Lloyds Wealth are the same product.
- No confirmed information was found on Embark or on AI in Scottish Widows direct investing beyond InvestAI.
- There is no dedicated robo/ready-made investments AI announcement. Lloyds' "Ready-Made Investments" is not publicly described as AI-driven.

## Q3: Fraud/scam AI, call-centre, complaints, mortgage, code, training

### Takeaway
Fraud is Lloyds' most visible customer-protection use of AI. It runs an ML Dynamic Risk Engine, used agentic multi-agent tools on fraud calls from June 2026, and is launching an image-analysis "Scam Check". Lloyds reports that it prevented £1bn of attempted fraud in 2025 and has invested £100m in fraud technology since 2023. Colleague training is delivered through the AI Academy, launched January 2026, together with apprenticeships and a summer school.

### Cited Findings
**19. Agentic AI fraud protection (on calls). Fraud / contact centre. Live from June 2026.**
- Announced 8 June 2026. Multiple AI agents run during customer calls to verify identity, analyse transactions and assess scam risk in real time. Colleagues stay accountable and can override the agents. It is built on the Envoy platform, and no external vendors are named. Lloyds reports £1bn of fraud prevented in 2025 and £100m invested in fraud technology since 2023 — [LBG press release, 8 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-banking-group-deploys-agentic-ai-to-strengthen-real-time-.html); [Finextra](https://www.finextra.com/newsarticle/47884/lloyds-deploys-ai-agents-to-check-for-payment-scams-in-real-time)

**20. Scam Check (ML and image analysis for purchase scams). Retail payments. Announced June 2026, "coming soon".**
- When Lloyds flags a new-payee purchase as a possible scam, the customer answers questions and uploads screenshots of the item. ML and image analysis then look for scam indicators such as unrealistic prices, new seller accounts and deposit demands. 68% of customer fraud reports are shopping scams, many starting on Meta platforms. Lloyds says its systems monitor about 23,551 transactions a minute — [Lloyds press release, 8 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds/lloyds-to-launch-scam-check-to-help-customers-dodge-online-shop.html). Secondary coverage says it will cover Halifax, Bank of Scotland and Lloyds payment journeys — [Business Chief](https://businesschief.com/news/lloyds-unveils-ai-driven-strategy-to-combat-finance-fraud). **Note:** the primary page describes the Lloyds app only.

**21. Dynamic Risk Engine (ML fraud detection). Fraud. Live.**
- It identified £30m of previously unknown high-value risk — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html); [Medium blog](https://medium.com/ai-at-lloyds-banking-group/outsmarting-fraudsters-at-scale-lloyds-banking-groups-dynamic-risk-engine-story-f7316a795174)

**22. AI Academy and skills programmes. Colleague training. Live since January 2026.**
- The AI Academy launched in 2026 for all 67,000 colleagues and includes mandatory responsible-AI training — [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html); [LBG insight](https://www.lloydsbankinggroup.com/insights/2026-the-year-of-agentic-ai-and-a-new-era-for-finance.html)
- By 22 June 2026, colleagues had completed 400k+ courses, and 65k+ had finished responsible-AI modules. Lloyds had 700+ colleagues working on AI use cases and was targeting 1,000+ AI roles in 2026, including about 300 agentic roles. It launched a Level 6 AI Engineering apprenticeship with 33 apprentices, and the Data & AI Summer School grew to 250+ sessions — [LBG, 22 Jun 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/1000-new-ai-roles.html)
- Other programmes: AI for Leaders, the Gen AI Assurance Programme, an Understanding Bias in Data Bootcamp and a Responsible GenAI Toolkit — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)

### Inferences
- The contact-centre AI stack is Athena for knowledge, agentic fraud agents on live calls, and Merlin for complaint summaries. Together they point to AI across the full service journey, though only Athena has published metrics.

### Gaps
- No metrics were found for Merlin or complaints AI.
- **Flag:** Fintech Garden said "AI-powered customer complaints processing generated £50m benefit in 2025". This looks like a misreading of the group-wide £50m GenAI figure and should not be used.
- No customer-facing AI chatbot history was verified in this pass, for example the older Lloyds/Halifax virtual assistants.

## Q4: AI achievements, value quantification, awards, Responsible AI governance

### Takeaway
Lloyds puts numbers on AI value: about £50m from GenAI in 2025 and more than £100m targeted in 2026. It says digital and AI account for about 70% of upgraded strategic initiatives. Accelerate 2030 adds £2bn of gross cost savings for 2027–2030, with AI as a key enabler. Lloyds ranked 15th in the 2025 Evident AI Index, up 12 places. It was second among UK banks behind HSBC (8th) and tied with UBS for top place in Responsible AI leadership.

### Cited Findings
- 2025: about £50m of value from GenAI and 50+ use cases in production; more than £100m targeted for 2026 — [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html). The AI page says 57 GenAI use cases went live in 2025 — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)
- The £50m is a P&L benefit. Digital and AI initiatives make up about 70% of upgraded strategic initiatives and more than 60% of cost savings since 2021 — [FY2025 call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-lloyds-banking-q4-2025-sees-strong-income-growth-93CH-4472475)
- Accelerate 2030 (30 July 2026): £2bn of gross savings over 2027–2030, a cost-to-income ratio below 45% and RoTE of about 20%. AI investment is split 50% revenue/differentiation and 50% productivity. AI is to support every customer interaction and every colleague by 2030 — [Q2 2026 call transcript](https://stockanalysis.com/quote/lon/LLOY/transcripts/546825-q2-2026-strategy-update/); [Yahoo Finance](https://uk.finance.yahoo.com/news/lloyds-banking-group-reports-strong-072011589.html). Fintech Garden reports "£13bn total investment over four years" **[single secondary source; unverified]** — [Fintech Garden](https://fintech.garden/news/2026-07-30-lloyds-sets-2bn-savings-target-under-new-accelerate-2030-ai-strategy-as-half-yea/)
- 2025 Evident AI Index: Lloyds ranked 15th, up 12 places, the strongest improvement of any UK bank. HSBC was 8th, NatWest 16th and Barclays 23rd. Lloyds had the 6th-most AI use cases with outcomes and tied with UBS at the top of RAI Leadership — [Evident AI Index 2025](https://evidentinsights.com/bankingbrief/heres-the-2025-evident-ai-index/); [LBG, 29 Jan 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html) (the rankings of other banks come from search summaries of Evident coverage)
- Euromoney Global Digital Banking Report 2025 rated Lloyds "Outstanding" — [LBG press release](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/outstanding-in-euromoney-report.html)
- Responsible AI governance: 7 AI ethics principles, a Data & AI Ethics Committee (DAIEC), and an AI Assurance Framework covering the Plan, Develop and Live stages, aligned to the EU AI Act, UK AI assurance guidance and ISO 42001 — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html). On 20 April 2026, Lloyds announced 9 Responsible AI hires under Head of Responsible AI Dr Suzanne Brink, who joined in 2025. The team sits in the AI CoE and has three workstreams: Framework, R&D and Mobilisation. One hire is a GenAI Guardrails Product Owner — [LBG, 20 Apr 2026](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds/responsible-ai-expertise.html)
- 60+ AI researchers publish research, including on synthetic data and quantum — [LBG AI page](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)
- Other 2026 AI press releases found: 18 August 2026, "more than half of UK businesses say AI has created new jobs" (Lloyds Business Barometer); 25 August 2026, "Britain's most AI-savvy generation has a financial confidence gap" — [LBG AI page listing](https://www.lloydsbankinggroup.com/who-we-are/group-overview/artificial-intelligence.html)

### Inferences
- In 2025, HSBC was ahead of Lloyds in the Evident Index, 8th against 15th. But Lloyds is moving up faster and matches the leaders on responsible-AI disclosure. Lloyds' quantified value (about £50m, rising to more than £100m) is a disclosure benchmark HSBC can be compared against.

### Gaps
- No 2026 Evident AI Index result for Lloyds was found. The 2026 index may have come out in or after October 2026.
- No AI-specific industry awards were verified, such as Banking Tech Awards or FStech Awards.
- The full H1 2026 results PDF was not read, so there may be more AI KPIs in it, for example Financial Assistant usage at June 2026.

## Q5: 2025–2026 AI announcement timeline (summary)

### Takeaway
Announcement pace picked up sharply from April 2025 onwards, and 2026 is framed as "the year of agentic AI".

### Cited Findings
- 7 Mar 2023: SPW adopts Aveni Detect — [Aveni](https://aveni.ai/blog/schroders-personal-wealth-spw/)
- 9 Apr 2025: Vertex AI migration with Google Cloud; mortgage income-verification algorithm — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-accelerates-ai-innovation-with-google-cloud.html)
- 15 Jul 2025: Athena — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-accelerates-with-athena.html)
- 9 Oct 2025: full ownership of SPW and rebrand to Lloyds Wealth — [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-09/lloyds-takes-control-of-schroders-personal-wealth-joint-venture)
- 21 Oct 2025: M365 Copilot at about 30k licences; GitHub Copilot — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-scales-adoption-of-copilot.html)
- 6 Nov 2025: agentic AI Financial Assistant announced — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2025/lloyds-banking-group-2025/lloyds-banking-group-unveils-uks-first-ai-powered-financial-assistant.html)
- Jan 2026: AI Academy launched — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/1000-new-ai-roles.html)
- 21 Jan 2026: "Year of Agentic AI" article by Rohit Dhawan — [LBG](https://www.lloydsbankinggroup.com/insights/2026-the-year-of-agentic-ai-and-a-new-era-for-finance.html)
- 29 Jan 2026: £50m value delivered, more than £100m targeted; Evident Index rise — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/ai-driven-benefits-2026.html)
- 16 Apr 2026: Sameer Gupta appointed CDAO — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/sameer-gupta-chief-data-ai-officer.html)
- 20 Apr 2026: Responsible AI team expanded — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds/responsible-ai-expertise.html)
- 22 Apr 2026: InvestAI pilot in Scottish Widows through the FCA AI Live Testing cohort, reported by Reuters — [Resultsense](https://www.resultsense.com/news/2026-04-22-lloyds-scottish-widows-ai-investment-guidance/)
- 1 May 2026: Envoy agent platform (Google Cloud) — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-banking-group-unveils-envoy.html)
- About May 2026: SPW formally rebranded as Lloyds Wealth — [TheWealthNet](https://www.paminsight.com/twn/article/spw-formally-rebrands-to-lloyds-wealth)
- 4 Jun 2026: Microsoft 365 E7 Frontier Suite and Agent 365 — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/microsoft-365-frontier-suite.html)
- Jun 2026: Aveni £12m round with LBG participating — [Finextra](https://www.finextra.com/newsarticle/47859/lloyds-and-nationwide-backed-ai-fintech-aveni-raises-12-million)
- 8 Jun 2026: agentic fraud agents and Scam Check — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/lloyds-banking-group-deploys-agentic-ai-to-strengthen-real-time-.html); [Lloyds](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds/lloyds-to-launch-scam-check-to-help-customers-dodge-online-shop.html)
- 22 Jun 2026: 1,000+ AI roles; Financial Assistant at 500k+ Bank of Scotland customers — [LBG](https://www.lloydsbankinggroup.com/media/press-releases/2026/lloyds-banking-group/1000-new-ai-roles.html)
- 30 Jul 2026: Accelerate 2030 strategy; Invest AI under Lloyds Wealth; target of 1m new investors — [Financial Planning Today](https://www.financialplanningtoday.co.uk/news/lloyds-wealth-launches-ai-simplified-advice-service); [transcript](https://stockanalysis.com/quote/lon/LLOY/transcripts/546825-q2-2026-strategy-update/)
- Aug 2026: Scottish Widows Retirement Report on AI and InvestAI — [Scottish Widows](https://www.scottishwidows.co.uk/about-us/media-centre/press-releases/expert-backed-ai-earns-pension-savers-trust.html)

### Inferences
- The Financial Assistant rollout to Lloyds and Halifax customers and the targeted-support rollout of InvestAI are the likely next milestones to watch in Q4 2026.

### Gaps
- No AI announcements dated September 2026 were found.
