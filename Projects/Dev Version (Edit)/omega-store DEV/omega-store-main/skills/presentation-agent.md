# Presentation Maker (Gamma API)

**Purpose:** This skill equips the agent to autonomously define, outline, and generate high-fidelity presentations using the Gamma API, while adhering to strict brand guidelines and quality standards.

## Instructions
1. **Gather Requirements:** Before creating any presentation, you MUST ask the pilot or extract the following 6 requirements: Topic/Objective, Number of Slides (5, 8-10, 12-15), Target Audience, Text Density, Visual Style, and Logo Placement.
2. **Confirm Requirements:** Summarize the requirements and explicitly ask the user "Ready to create? (yes/no)". You MUST wait for confirmation.
3. **Generate Content:** Structure the slides according to the standard templates (e.g. 5-Slide Pitch vs 10-Slide Standard).
4. **API Execution:** Formulate the JSON payload for the Gamma API (`/v1.0/generations`) incorporating the text, theme ID, text options, image options (DALL-E-3), and card options. Once triggered, output both the `gammaUrl` and `exportUrl`.
5. **Fireflies MCP:** If meeting notes are needed as the base for the presentation, utilize the Fireflies MCP via the configured API keys.

## Examples
*Input:* "Create a 5-slide quick pitch for executives about our new AI tool, keep it minimalistic and corporate."
*Action:* The agent summarizes the 6 requirements for the user. Once approved, it drafts an outline (Hook -> Problem -> Solution -> Proof -> CTA), configures the Gamma JSON payload, and returns the generation links.

## Constraints
- **Brand Consistency:** Always ensure the generated theme matches the local brand guidelines (Primary Color, Logo URL).
- **Communication:** NEVER skip the 6 questions or generate a presentation without final confirmation from the pilot.

## Quality Criteria
- The presentation exactly matches the confirmed slide count and text density.
- The visual style is detailed and professional, adhering strictly to the extracted parameters.
- Both the `gammaUrl` (View Online) and `exportUrl` (Download PDF) are provided in the final output.
