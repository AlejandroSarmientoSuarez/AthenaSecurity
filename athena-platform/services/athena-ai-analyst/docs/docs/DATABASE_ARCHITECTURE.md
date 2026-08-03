# Database Architecture

# Athena AI Analyst

**Version:** 1.0

**Status:** Draft

---

# 1. Purpose

This document defines the logical data architecture for Athena AI Analyst.

The database stores:

- Security alerts.
- Investigations.
- Evidence.
- Threat mappings.
- Reports.
- Recommendations.
- Audit information.

The design prioritizes:

- Traceability.
- Explainability.
- Extensibility.
- Security.

---

# 2. Database Strategy

Primary Database:

PostgreSQL

Reasoning:

- ACID compliance.
- JSON support.
- Mature ecosystem.
- Excellent Python integration.
- Enterprise adoption.

Future complementary databases:

- Redis (cache)
- Elasticsearch (search)
- Object Storage (reports)
- Vector Database (RAG)

---

# 3. Core Entities

The MVP persists:

Alert

↓

Investigation

↓

Evidence

↓

Risk Assessment

↓

Recommendation

↓

Report

---

# 4. Entity Relationship

```
Alert
 │
 │ 1:N
 ▼
Investigation
 │
 ├──────────────┐
 ▼              ▼
Evidence     Recommendation
 │              │
 └──────┬───────┘
        ▼
 Risk Assessment
        │
        ▼
     Report
```

---

# 5. Tables

## alerts

Purpose:

Stores every security alert received.

Fields:

- id
- source
- event_type
- severity
- status
- raw_event
- created_at

---

## investigations

Purpose:

Stores investigation lifecycle.

Fields:

- id
- alert_id
- status
- hypothesis
- confidence
- started_at
- completed_at

---

## evidence

Purpose:

Stores evidence collected during investigation.

Fields:

- id
- investigation_id
- type
- source
- value
- relevance

---

## recommendations

Purpose:

Stores AI recommendations.

Fields:

- id
- investigation_id
- priority
- description
- requires_approval

---

## reports

Purpose:

Stores final investigation reports.

Fields:

- id
- investigation_id
- summary
- technical_findings
- recommendations
- generated_at

---

# 6. Future Tables

Future versions may include:

- users
- teams
- organizations
- assets
- incidents
- playbooks
- connectors
- threat_feeds
- ai_sessions

---

# 7. Relationships

Alert

1

↓

N

Investigation

↓

1

↓

N

Evidence

↓

1

↓

N

Recommendation

↓

1

↓

1

Report

---

# 8. Audit Strategy

Every investigation should be traceable.

Audit information includes:

- Creation time.
- Update time.
- AI version.
- Prompt version.
- Analyst actions.

---

# 9. Security Requirements

The database must support:

- Encryption at rest.
- Encrypted connections.
- Least privilege access.
- Immutable audit history.
- Secure backups.

---

# 10. Future Data Layer

Future architecture:

```
                Athena API

                     │

               PostgreSQL

        ┌────────┴────────┐

     Redis          Elasticsearch

        │                 │

        └──────┬──────────┘

               ▼

        Vector Database

               ▼

        AI Knowledge Layer
```

---

# 11. Design Principles

- Normalize operational data.
- Store immutable security evidence.
- Preserve investigation history.
- Keep AI outputs explainable.
- Support future RAG integration.

---

# 12. Long-Term Vision

Athena's database should evolve from a simple operational datastore into a security knowledge platform capable of supporting enterprise-scale investigations and AI-assisted reasoning.