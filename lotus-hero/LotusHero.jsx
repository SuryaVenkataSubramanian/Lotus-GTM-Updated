// Lotus waitlist hero: white page with the React Bits GradientASCII animation behind the headline.
//
// 1. Add the component:   npx shadcn@latest add @react-bits/GradientASCII-JS-CSS
// 2. Drop this file next to it and render <LotusHero /> at the top of the waitlist page.
//
// Settings follow the animation prompt (colors, horizon shape, characters, cell size, density).
// lightMode keeps the page background white, and gradient/glyph opacity are lowered slightly
// so the headline and the email field stay easy to read over the animation.

import GradientASCII from './GradientASCII';

export default function LotusHero() {
  return (
    <section style={{ position: 'relative', overflow: 'hidden', background: '#ffffff', padding: '88px clamp(20px, 8vw, 120px) 104px' }}>
      <div aria-hidden="true" style={{ position: 'absolute', left: 0, right: 0, top: 0, height: 760, pointerEvents: 'none' }}>
        <GradientASCII
          colors={['#a855f7', '#f6f8ff']}
          shape="horizon"
          characters=" =+xX0S8#@"
          cellSize={18}
          density={0.8}
          lightMode
          gradientOpacity={0.6}
          glyphOpacity={0.7}
          grain={0.04}
        />
      </div>

      <div style={{ position: 'relative', zIndex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 28, textAlign: 'center' }}>
        <span>Document360 - Lotus · Docs as code</span>
        <h1>
          Docs as code, <span style={{ color: '#7f56d9' }}>synced both ways</span>
        </h1>
        <p>Your docs in GitHub. Your team in Document360. Always in sync.</p>
        {/* Waitlist form, chips and the Document360 ⟷ Lotus ⟷ GitHub visual follow, as in the design. */}
      </div>
    </section>
  );
}
