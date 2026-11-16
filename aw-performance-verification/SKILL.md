---
name: aw-performance-verification
description: Define and measure performance budgets, locate bottlenecks, and verify improvements under representative conditions; do not optimize from anecdote alone.
---

# Performance Verification

## Trigger and inputs
Use when latency, throughput, resource use, bundle/runtime cost, scalability, or a performance regression matters. Require a measurable target, exact revision, representative workload and environment, and relevant architecture/data context.

## Output and scope
Produce a baseline, methodology, results, bottleneck evidence, proposed or verified change, and limitations. Avoid unrelated micro-optimization and preserve correctness and accepted behavior.

## Method
1. Define user or system metric, percentile, load shape, budget, and variance controls.
2. Warm up and repeat measurements where needed; record environment differences.
3. Profile the dominant path before choosing an intervention.
4. Measure the same scenario after changes and check for shifted bottlenecks.
5. Run correctness and stability checks alongside performance verification.

## Evidence, exit, and handoff
Record revisions, workload, environment, samples, summaries, profiles, and confidence limits appropriate to the claim. Exit when the budget is met or an explicit risk decision exists. Hand bottlenecks to the owning engineer and capacity/release implications to reliability or release owners.
