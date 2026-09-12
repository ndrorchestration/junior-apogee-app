# Persona-to-Role Migration Policy

**Status:** Current architecture direction / implementation migration not yet complete  
**Date:** 2026-09-12  
**Parent migration:** `ndrorchestration/DGAF-Framework#671`  
**Repository tracker:** issue #12

## Product architecture rule

The evaluation workbench must not depend on named personas as primitive runtime semantics.

Executable behavior should resolve through explicit **roles, capabilities, policies, contracts, and execution profiles**. Optional personas may be used for presentation, but changing a presentation alias must not change the semantics of the role it represents.

## Current state

The naming-boundary work through `main` commit `44e5780c62384369cd9a4a1aaf14dc45f1c3bdc6` is **phase 0** of this broader migration.

It successfully neutralized retired current-facing branding and converted the former primary orchestration display identity to the functional label `Evaluation Orchestrator`, while preserving legacy repository/package/import/CLI/env identifiers for compatibility.

However, the runtime and test model still includes identity-keyed `AgentName` semantics for multiple named roles. Those references require classification and controlled migration rather than another search-and-replace.

## Migration classifications

Each named reference must be classified before modification:

- `FD` — functional dependency: replace with a role/capability ID.
- `PP` — persona/presentation: move behind an optional presentation mapping.
- `FX` — fixture/demo identity: neutralize unless identity is specifically under test.
- `HP` — historical/provenance identity: preserve exactly and connect through lineage metadata.
- `UN` — undefined/conflicting: do not migrate until specified/adjudicated.

## Product capabilities to preserve

The following should survive as first-class product capabilities rather than persona-owned behavior:

- evaluation orchestration;
- evidence integrity and provenance checks;
- configurable rubrics;
- hard/non-compensatory gates;
- independent review and evaluator dissent;
- escalation and human review routing;
- comparison admissibility controls;
- replay/debugging and trace linkage;
- explicit tested-vs-NOT-TESTED coverage;
- evidence freshness and scope boundaries;
- governance-request packaging without self-authorization.

## Persona behavior rule

If a named persona contains prompts, heuristics, memory behavior, routing decisions, or other logic that materially changes execution, that logic must be extracted into an explicit object such as:

- execution profile;
- behavior policy;
- prompt strategy;
- interaction policy.

It must not remain hidden inside presentation identity.

## Compatibility rule

Legacy aliases and technical identifiers remain until active consumers have migrated and semantic/cross-repository compatibility checks pass. Alias retirement is evidence-based rather than calendar-based.

## Verification requirements

Every implementation wave must show:

- tests equal or stronger than before;
- no silent change in evaluation semantics;
- deterministic legacy-alias resolution;
- no historical evidence mutation;
- no authority or governance-state transfer by rename;
- rollback path;
- compatibility for active consumers.

## Separation from branding

The final commercial product name and the later repository/package/import/CLI/env technical rename are separate decisions. This architecture migration should not wait for final branding, and branding must not be allowed to redefine runtime semantics.

## Evidence boundary

This migration does not establish external certification, compliance, safety, production readiness, governance authorization, or validated efficacy. It is an architectural decomposition of how the workbench represents responsibilities and behavior.
