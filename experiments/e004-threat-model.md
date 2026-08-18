# AgentBait E004 Threat Model

## Attacker capability

The attacker can influence metadata or provenance information presented to an autonomous agent during tool discovery.

The attacker does not directly modify the model weights and does not need direct access to privileged resources.

## Victim capability

The victim agent can discover and invoke multiple tools.

At least one discovered capability provides access to a more sensitive resource.

## Vulnerable architecture

The agent's tool-selection decision is treated as sufficient authorization to execute the selected capability.

## Attack chain

1. Attacker-controlled or attacker-influenced provenance metadata is presented during tool discovery.
2. The autonomous agent interprets the metadata as evidence of trust.
3. The agent preferentially selects the signaled tool.
4. The selected tool has a privileged capability.
5. The architecture executes the capability without an independent authorization decision.
6. A protected resource becomes accessible.

## Secure architecture

Tool selection and authorization are separate decisions.

A model selecting a privileged tool does not itself authorize execution.

## Security impact

Potential impacts depend on the privileged capability:

- Confidentiality: unauthorized access to protected data.
- Integrity: unauthorized modification of protected resources.
- Availability: unauthorized destructive or disruptive actions.

## Root-cause hypothesis

The architectural root cause is conflation of autonomous tool selection with authorization, combined with insufficient trust separation for tool metadata.

## Candidate taxonomy

Primary:
- Agentic tool misuse / excessive agency.
- Agentic supply-chain / tool-discovery trust failure.

Potential CWE:
- CWE-1427 when the concrete implementation involves externally supplied content being incorporated into LLM prompting.

CWE mapping should be finalized only after validating a real affected product.
