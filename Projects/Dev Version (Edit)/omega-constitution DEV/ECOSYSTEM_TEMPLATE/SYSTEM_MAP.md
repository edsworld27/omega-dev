# OMEGA SYSTEM FLOW MAP

```
User drops files     →  00 User/00_Drop_Zone/
                              ↓
AI reads constitution →  (from GitHub)
                              ↓
Work happens         →  Projects/
                              ↓
Finished products    →  00 User/01_Send_Off/
```

## The Flow

1. **User** drops project files in `00 User/00_Drop_Zone/`
2. **AI** reads the constitution from GitHub
3. **AI** follows INSTRUCTOR.xml rules
4. **Work** happens in `Projects/`
5. **Output** goes to `00 User/01_Send_Off/`

## Key Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Drop Zone | `00 User/00_Drop_Zone/` | User input |
| Send Off | `00 User/01_Send_Off/` | User output |
| Control Panel | `Omega Control/00 Rules/` | Python scripts |
| Context | `Omega Control/00 Rules/03_Context/` | Session state |
| Constitution | GitHub | Rules (fetched on demand) |

## Quick Start

```bash
python RUN.py --onboard    # First-time setup
python RUN.py              # Run the system
```
