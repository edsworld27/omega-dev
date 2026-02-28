# Claude Superpower Extensions (Awesome Claude Skills)

**Purpose:** This skill acts as a direct bridge to the [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills) repository, granting the agent access to a curated list of superpowers, resources, and tools for customizing Claude AI workflows, specifically for Claude Code.

## Instructions
1. **Discover Skills:** When tasked with a problem that requires a specific workflow, tool, or integration that is not natively available in the Omega System, refer to the `Awesome Claude Skills` repository to find community or official skills that solve the problem.
2. **Review Skill Capabilities:** Access [https://github.com/travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) and browse the categories (Document Skills, Design & Creative, Development, Communication, etc.).
3. **Integration Phase:** Extrapolate the required instructions, prompts, or tools from the chosen skill and integrate them into your current context or propose a new Omega Skill based on that community skill.
4. **Follow Guidelines:** Always verify that the external skill complies with the Omega Constitution. If a skill conflicts with the Constitution (e.g., skips tests or bypasses security), the Constitution ALWAYS wins.

## Examples
*Input:* "I need to analyze a large PDF and extract technical specifications."
*Action:* The agent checks the `Awesome Claude Skills` repo for "Document Skills", finds an appropriate PDF analysis skill, and uses its methodologies to parse the document efficiently while adhering to Omega's active context.

## Constraints
- **Subservience:** These external skills are additive. They do NOT override any existing Omega protocols (like the `AUDIT_PROTOCOL` or `SECURITY.md`).
- **Validation:** Always validate the source code or prompts of any community skill before executing them in the Dev or Live environment.

## Quality Criteria
- The selected skill successfully accelerates the requested workflow.
- No constitutional laws were broken during the execution of the external skill.
