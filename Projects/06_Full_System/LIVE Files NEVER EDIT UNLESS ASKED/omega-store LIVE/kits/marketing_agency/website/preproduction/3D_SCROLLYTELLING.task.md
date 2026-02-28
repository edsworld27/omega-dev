# 3D SCROLLYTELLING.task.md

## FOR THE USER
This task implements a world-class, Awwwards-level 3D scrollytelling experience. It uses a high-performance HTML5 Canvas to playback an image sequence (120+ frames) that is linked to the user's scroll progress.

**Instructions:**
1. Drop your 120-frame image sequence into `/public/sequence/` (naming: `frame_0.webp` to `frame_119.webp`).
2. Run this task to generate the `ScrollyCanvas` component and integrate it into your landing page.
3. Ensure your background is set to `#050505` for a seamless floating effect.

---

## FOR THE AI

### OBJECTIVE
Build a premium scrollytelling experience using Next.js 14, Framer Motion, and Canvas.

### TECHNICAL REQUIREMENTS
1.  **Framework**: Next.js 14 (App Router), Tailwind CSS.
2.  **Animation**: Framer Motion `useScroll` and `useSpring`.
3.  **Canvas**: Dedicated `ScrollyCanvas.tsx` component.
4.  **Loading**: Preload all images and show a progress-indexed loading state.
5.  **Performance**: 120fps smooth interpolation with `stiffness: 100`, `damping: 30`.

### IMPLEMENTATION STEPS
1.  **Canvas Wrapper**:
    - `height: 400vh` for scroll duration.
    - Sticky `top-0` canvas covering the viewport.
2.  **Image Loading**:
    - Fetch and store images in a persistent `useRef` array.
    - Track load progress for the splash screen.
3.  **Scroll Mapping**:
    - Map `scrollYProgress` (0.0 to 1.0) to frame index `Math.floor(p * 120)`.
    - Apply `useSpring` to the progress value to eliminate scroll jitter.
4.  **Text Overlays (Beats)**:
    - Implement 4 narrative beats triggered at specific scroll ranges:
        - Beat A: 0.0 - 0.2
        - Beat B: 0.25 - 0.45
        - Beat C: 0.5 - 0.7
        - Beat D: 0.75 - 0.95
    - Each beat fades in/out using `useTransform`.

### SUCCESS CRITERIA
- Zero flicker between frames.
- Perfect blending with `#050505` background.
- Fully responsive canvas scaling (contain/cover logic).
- TypeScript types for all animation state.
