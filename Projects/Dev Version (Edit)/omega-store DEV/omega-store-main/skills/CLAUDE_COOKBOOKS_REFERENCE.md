# CLAUDE COOKBOOKS REFERENCE

> **Source:** https://github.com/anthropics/claude-cookbooks
> **Authority:** Anthropic Official (MIT License)
> **Status:** TIER 1 Reference for Claude Implementations
> **Last Updated:** 2026-02-28

---

## PURPOSE

This document catalogs the official Anthropic Claude Cookbooks - production-ready patterns and implementations for Claude capabilities. When building Claude-powered features, **ALWAYS check this reference first** before implementing custom solutions.

---

## COOKBOOK CATALOG

### CORE CAPABILITIES

| Cookbook | Path | Use Case |
|----------|------|----------|
| **Classification** | `capabilities/` | Text/data classification, categorization, labeling |
| **RAG** | `capabilities/` | Retrieval Augmented Generation with external knowledge |
| **Summarization** | `capabilities/` | Text summarization, distillation, key point extraction |

### TOOL USE & INTEGRATION

| Cookbook | Path | Use Case |
|----------|------|----------|
| **Customer Service Agent** | `tool_use/customer_service_agent.ipynb` | Building customer service bots |
| **Calculator Integration** | `tool_use/calculator_tool.ipynb` | Math/calculation tool binding |
| **SQL Queries** | `misc/how_to_make_sql_queries.ipynb` | Database query generation |

### THIRD-PARTY INTEGRATIONS

| Cookbook | Path | Use Case |
|----------|------|----------|
| **Pinecone RAG** | `third_party/Pinecone/rag_using_pinecone.ipynb` | Vector database RAG |
| **Wikipedia Search** | `third_party/Wikipedia/wikipedia-search-cookbook.ipynb` | Knowledge base integration |
| **Web Page Processing** | `misc/read_web_pages_with_haiku.ipynb` | Web scraping, content extraction |
| **Voyage AI Embeddings** | `third_party/VoyageAI/how_to_create_embeddings.md` | Text embeddings |

### MULTIMODAL (VISION)

| Cookbook | Path | Use Case |
|----------|------|----------|
| **Getting Started with Vision** | `multimodal/getting_started_with_vision.ipynb` | Image processing basics |
| **Vision Best Practices** | `multimodal/best_practices_for_vision.ipynb` | Image analysis optimization |
| **Charts & Graphs** | `multimodal/reading_charts_graphs_powerpoints.ipynb` | Visual data interpretation |
| **Form Extraction** | `multimodal/how_to_transcribe_text.ipynb` | Document/form OCR |
| **Image Generation** | `misc/illustrated_responses.ipynb` | Stable Diffusion integration |

### ADVANCED PATTERNS

| Cookbook | Path | Use Case |
|----------|------|----------|
| **Sub-agents** | `multimodal/using_sub_agents.ipynb` | Haiku as sub-agent with Opus |
| **PDF Processing** | `misc/pdf_upload_summarization.ipynb` | PDF parsing and summarization |
| **Automated Evals** | `misc/building_evals.ipynb` | Prompt evaluation systems |
| **JSON Mode** | `misc/how_to_enable_json_mode.ipynb` | Consistent JSON output |
| **Content Moderation** | `misc/building_moderation_filter.ipynb` | Moderation filter patterns |
| **Prompt Caching** | `misc/prompt_caching.ipynb` | Efficient caching techniques |

### SPECIALIZED DIRECTORIES

| Directory | Purpose |
|-----------|---------|
| `coding/` | Code generation and analysis |
| `extended_thinking/` | Extended reasoning capabilities |
| `finetuning/` | Model fine-tuning guides |
| `patterns/agents/` | Agent design patterns |
| `observability/` | Monitoring and logging |
| `skills/` | Skill implementations |
| `tool_evaluation/` | Tool evaluation frameworks |

---

## INTEGRATION PATTERNS

### Pattern 1: RAG Implementation
```
1. Check: third_party/Pinecone/rag_using_pinecone.ipynb
2. Check: third_party/VoyageAI/how_to_create_embeddings.md
3. Apply to: omega-claw vector operations
```

### Pattern 2: Tool Use
```
1. Check: tool_use/customer_service_agent.ipynb
2. Check: tool_use/calculator_tool.ipynb
3. Apply to: omega-claw skill handlers
```

### Pattern 3: Multi-Agent
```
1. Check: multimodal/using_sub_agents.ipynb
2. Check: patterns/agents/
3. Apply to: omega-claw orchestrator
```

### Pattern 4: Vision Features
```
1. Check: multimodal/getting_started_with_vision.ipynb
2. Check: multimodal/best_practices_for_vision.ipynb
3. Apply to: phantom_agent image processing
```

---

## OMEGA SKILL MAPPINGS

| Omega Skill | Relevant Cookbook |
|-------------|-------------------|
| `analyst-agent` | Classification, RAG, Summarization |
| `classifier-agent` | Classification |
| `guardian-agent` | Content Moderation Filter |
| `orchestrator-agent` | Sub-agents, Agent Patterns |
| `writer-agent` | Summarization, JSON Mode |

---

## USAGE RULES

1. **ALWAYS CHECK COOKBOOKS FIRST** before implementing Claude features
2. **PREFER cookbook patterns** over custom implementations
3. **CITE the cookbook** in code comments when using a pattern
4. **UPDATE this reference** when new cookbooks are added

---

## QUICK ACCESS

```bash
# Clone the cookbooks locally
git clone https://github.com/anthropics/claude-cookbooks.git

# Or access directly
https://github.com/anthropics/claude-cookbooks
```

---

## REPOSITORY STATS

- **Stars:** 33.7k+
- **Forks:** 3.5k+
- **Contributors:** 64+
- **License:** MIT
- **Primary Language:** Jupyter Notebook (95.9%)

---

*This reference is part of the Omega Store and is governed by SOURCES.xml Tier 3: Validated Knowledge.*
