class Component extends DCLogic {
constructor(props) {
super(props);
this.asciiHost = null;
this.asciiCanvas = null;
this.setAsciiHost = (el) => { this.asciiHost = el; };
this.setAsciiCanvas = (el) => { this.asciiCanvas = el; };
this.ctaHost = null;
this.ctaCanvas = null;
this.setCtaHost = (el) => { this.ctaHost = el; };
this.setCtaCanvas = (el) => { this.ctaCanvas = el; };
}
componentDidMount() {
this.stops = [];
try { const a = this.startAscii(this.asciiHost, this.asciiCanvas, {}); if (a) this.stops.push(a); } catch (e) {}
try { const b = this.startAscii(this.ctaHost, this.ctaCanvas, { variation: 3, scale: 1.25, density: 0.7, gradientOpacity: 0.5, glyphOpacity: 0.6 }); if (b) this.stops.push(b); } catch (e) {}
}
componentWillUnmount() {
(this.stops || []).forEach((stop) => stop());
}
renderVals() {
return { setAsciiHost: this.setAsciiHost, setAsciiCanvas: this.setAsciiCanvas, setCtaHost: this.setCtaHost, setCtaCanvas: this.setCtaCanvas };
}
startAscii(hostEl, canvasEl, overrides) {
// Port of React Bits <GradientASCII /> (JS + CSS variant) with the hero settings:
// colors ["#a855f7","#f6f8ff"], shape "horizon", characters " =+xX0S8#@", cellSize 18, density 0.8, light mode on a white page.
const container = hostEl;
const canvas = canvasEl;
if (!container || !canvas) return null;
const S = {
colors: ['#a855f7', '#f6f8ff'], shape: 0, characters: ' =+xX0S8#@', cellSize: 18, density: 0.8,
glyphOpacity: 0.7, glow: 0.2, depthOfField: 0, flicker: 0.2, softness: 0.5, scale: 1, flow: 0.5, speed: 1,
gradientOpacity: 0.6, grain: 0.04, variation: 0, mouseInteraction: true, scrambleRadius: 0.1, clickEffect: 1,
intro: true, lightMode: true, fontFamily: '"IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace'
};
Object.assign(S, overrides || {});
const MAX_COLORS = 8, MAX_CLICKS = 4, MAX_TRAIL = 24, CLICK_LIFE = 1.2, TRAIL_LIFE = 0.7, TRAIL_STEP = 0.015, INTRO_SECONDS = 2.4;
const ATLAS_CELL_W = 60, ATLAS_CELL_H = 100, ATLAS_COLUMNS = 16, FONT_SCALE = 0.78;
const VERTEX = `#version 300 es
out vec2 vUv;
void main() {
  vec2 p = vec2(float((gl_VertexID << 1) & 2), float(gl_VertexID & 2));
  vUv = p;
  gl_Position = vec4(p * 2.0 - 1.0, 0.0, 1.0);
}`;
const COMMON = `
float hash12(vec2 p) {
  vec3 q = fract(vec3(p.xyx) * 0.1031);
  q += dot(q, q.yzx + 33.33);
  return fract((q.x + q.y) * q.z);
}
`;
const FIELD = `#version 300 es
precision highp float;
precision highp int;
uniform float uAspect;
uniform float uTime;
uniform int uShape;
uniform vec3 uRamp[8];
uniform int uCount;
uniform float uScale;
uniform float uSoftness;
uniform float uFlow;
uniform vec2 uSeed;
uniform vec4 uTrail[24];
uniform float uRadius;
uniform vec4 uClicks[4];
uniform int uClickEffect;
uniform float uIntro;
uniform float uFrame;
in vec2 vUv;
layout(location = 0) out vec4 outColor;
layout(location = 1) out vec4 outAux;
` + COMMON + `
vec2 hash22(vec2 p) {
  vec3 q = fract(vec3(p.xyx) * vec3(0.1031, 0.103, 0.0973));
  q += dot(q, q.yzx + 33.33);
  return fract((q.xx + q.yz) * q.zy) * 2.0 - 1.0;
}
float noise(vec2 p) {
  vec2 i = floor(p);
  vec2 f = fract(p);
  vec2 u = f * f * f * (f * (f * 6.0 - 15.0) + 10.0);
  float a = dot(hash22(i), f);
  float b = dot(hash22(i + vec2(1.0, 0.0)), f - vec2(1.0, 0.0));
  float c = dot(hash22(i + vec2(0.0, 1.0)), f - vec2(0.0, 1.0));
  float d = dot(hash22(i + vec2(1.0, 1.0)), f - vec2(1.0, 1.0));
  return 0.5 + 0.5 * mix(mix(a, b, u.x), mix(c, d, u.x), u.y);
}
vec3 labToRgb(vec3 lab) {
  float l = lab.x + 0.3963377774 * lab.y + 0.2158037573 * lab.z;
  float m = lab.x - 0.1055613458 * lab.y - 0.0638541728 * lab.z;
  float s = lab.x - 0.0894841775 * lab.y - 1.2914855480 * lab.z;
  l = l * l * l; m = m * m * m; s = s * s * s;
  return vec3(
    4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
    -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
    -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
  );
}
vec3 encode(vec3 c) {
  c = clamp(c, 0.0, 1.0);
  return mix(c * 12.92, 1.055 * pow(c, vec3(1.0 / 2.4)) - 0.055, step(0.0031308, c));
}
vec3 horizon(vec2 p, float time, out float order) {
  float span = 0.5 * max(uAspect, 1.0);
  float x = p.x / span;
  float arch = -0.17 - 0.2 * x * x + 0.02 * sin(time * 0.6);
  float soft = mix(0.05, 0.22, uSoftness);
  float edge = p.y - arch;
  float rim = 0.38 * smoothstep(-soft, 0.42, edge);
  vec2 sun = vec2(0.08 * sin(time * 0.31) * span, 0.58);
  float spread = length((p - sun) / vec2(0.95 * span, 0.75));
  float sky = mix(0.55, 1.0, smoothstep(0.2, 0.95, spread));
  order = clamp(edge * 1.3, 0.0, 1.0);
  return vec3(rim, sky, smoothstep(0.18, 0.62, edge));
}
vec4 tone(float t) {
  float x = smoothstep(0.3, 1.0, t) * float(uCount - 1);
  int index = int(floor(x));
  return vec4(mix(uRamp[index], uRamp[min(index + 1, uCount - 1)], fract(x)), smoothstep(0.0, 0.38, t));
}
void main() {
  vec2 p = (vUv - 0.5) * vec2(uAspect, 1.0);
  float time = uTime;
  vec2 q = p / uScale;
  vec2 warp = vec2(
    noise(q * 1.6 + uSeed + vec2(0.0, time * 0.3)),
    noise(q * 1.6 + uSeed.yx + vec2(4.3, -time * 0.24))
  ) - 0.5;
  q += warp * uFlow * 0.18;
  float order = 0.0;
  vec3 shape = horizon(q, time, order);
  float reveal = clamp((uIntro * 1.45 - order) / 0.45, 0.0, 1.0);
  reveal = reveal * reveal * (3.0 - 2.0 * reveal);
  float scramble = 0.0;
  for (int i = 0; i < 24; i++) {
    vec4 point = uTrail[i];
    if (point.z <= 0.0) continue;
    vec2 d = p - point.xy;
    scramble = max(scramble, point.z * exp(-dot(d, d) / (uRadius * uRadius)));
  }
  for (int i = 0; i < 4; i++) {
    vec4 c = uClicks[i];
    if (c.w <= 0.0) continue;
    float d = length(p - c.xy);
    if (uClickEffect == 1) {
      scramble = max(scramble, exp(-pow((d - c.z * 0.75) / 0.06, 2.0)) * c.w);
    } else if (uClickEffect == 2) {
      float size = 0.08 + 0.22 * (1.0 - exp(-c.z * 5.0));
      scramble = max(scramble, (1.0 - smoothstep(size * 0.6, size, d)) * c.w);
    }
  }
  vec2 t = clamp(shape.xy * mix(0.7, 1.0, reveal), 0.0, 1.0);
  vec4 mixed = mix(tone(t.x), tone(t.y), shape.z);
  vec3 color = encode(labToRgb(mixed.rgb));
  float alpha = mixed.a * reveal;
  float dither = (hash12(gl_FragCoord.xy + uFrame * 13.7) - 0.5) / 255.0;
  outColor = clamp(vec4(color * alpha + dither, alpha + dither), 0.0, 1.0);
  outAux = vec4(reveal, scramble, 0.0, 1.0);
}`;
const GLYPHS = `
uniform sampler2D uField;
uniform sampler2D uAux;
uniform sampler2D uAtlas;
uniform vec2 uResolution;
uniform vec2 uCell;
uniform vec2 uOffset;
uniform vec2 uAtlasGrid;
uniform float uCount;
uniform float uDensity;
uniform float uOpacity;
uniform float uFlicker;
uniform float uDepth;
uniform float uGlyphTime;
uniform float uSeedValue;
uniform float uLight;
` + COMMON + `
float sampleGlyph(float index, vec2 local, vec2 coord, float soft) {
  float column = mod(index, uAtlasGrid.x);
  float row = floor(index / uAtlasGrid.x);
  vec2 atlasUv = vec2((column + local.x) / uAtlasGrid.x, (row + 1.0 - local.y) / uAtlasGrid.y);
  vec2 continuous = coord / uAtlasGrid;
  float scale = exp2(soft);
  return textureGrad(uAtlas, atlasUv, dFdx(continuous) * scale, dFdy(continuous) * scale).a;
}
vec4 glyphAt(vec2 px) {
  vec2 coord = (px - uOffset) / uCell;
  vec2 cell = floor(coord);
  vec2 local = coord - cell;
  vec2 uv = clamp(((cell + 0.5) * uCell + uOffset) / uResolution, vec2(0.0), vec2(1.0));
  vec4 field = texture(uField, uv);
  vec4 aux = texture(uAux, uv);
  vec3 visible = uLight > 0.5 ? field.rgb + (1.0 - field.a) : field.rgb;
  float luma = dot(visible, vec3(0.2126, 0.7152, 0.0722));
  float value = uLight > 0.5 ? clamp((1.0 - luma) * 1.5, 0.0, 1.0) : luma;
  float pick = hash12(cell + uSeedValue * 7.31);
  float level = hash12(cell * 1.73 + 4.1 + uSeedValue);
  float tick = floor(uGlyphTime * 9.0 + level * 9.0);
  float wobble = (hash12(cell * 2.31 + tick * 17.7) - 0.5) * uFlicker * 0.4 + (level - 0.5) * 0.1;
  float tone = clamp(pow(value, 0.75) + wobble, 0.0, 1.0);
  float index = floor(tone * (uCount - 1.0) + 0.5);
  float decode = max(aux.g, 1.0 - aux.r);
  if (decode > 0.02) {
    float frame = floor(uGlyphTime * 20.0);
    if (hash12(cell * 3.7 + frame * 5.3) < decode * 1.25) index = 1.0 + floor(hash12(cell + frame * 1.37) * (uCount - 1.0));
  }
  float present = step(pick, uDensity * mix(1.0, 0.3 + tone * 1.1, 0.55));
  float cutoff = smoothstep(0.03, 0.1, value);
  float focus = step(hash12(cell * 0.71 + 9.2 + uSeedValue), uDepth);
  float coverage = sampleGlyph(index, local, coord, focus * 1.2);
  float alpha = uOpacity * present * cutoff * coverage * mix(1.0, 0.35 + 0.65 * level, 0.55) * (1.0 - focus * 0.5);
  if (uLight < 0.5) {
    vec3 light = field.rgb * 0.55 + vec3(0.03) * field.a;
    return vec4(light * alpha, 0.6 * field.a * alpha);
  }
  vec3 ink = visible * 0.8;
  return vec4(ink * alpha, alpha);
}
`;
const HALO = `#version 300 es
precision highp float;
uniform float uDownscale;
in vec2 vUv;
out vec4 outColor;
` + GLYPHS + `
void main() {
  outColor = glyphAt(gl_FragCoord.xy * uDownscale);
}`;
const BLUR = `#version 300 es
precision highp float;
uniform sampler2D uSource;
uniform vec2 uStep;
in vec2 vUv;
out vec4 outColor;
void main() {
  vec4 sum = texture(uSource, vUv) * 0.2270270270;
  sum += texture(uSource, vUv + uStep * 1.3846153846) * 0.3162162162;
  sum += texture(uSource, vUv - uStep * 1.3846153846) * 0.3162162162;
  sum += texture(uSource, vUv + uStep * 3.2307692308) * 0.0702702703;
  sum += texture(uSource, vUv - uStep * 3.2307692308) * 0.0702702703;
  outColor = sum;
}`;
const COMPOSITE = `#version 300 es
precision highp float;
uniform sampler2D uHalo;
uniform float uGlow;
uniform float uGradient;
uniform float uGrain;
uniform float uFrame;
in vec2 vUv;
out vec4 outColor;
` + GLYPHS + `
void main() {
  vec4 base = texture(uField, vUv) * uGradient;
  vec4 glyph = glyphAt(gl_FragCoord.xy);
  vec4 halo = texture(uHalo, vUv) * uGlow;
  vec4 color;
  if (uLight < 0.5) {
    color = base + glyph + halo;
  } else {
    color = glyph + base * (1.0 - glyph.a);
    color += halo * 0.6 * (1.0 - color.a);
  }
  float grain = (hash12(gl_FragCoord.xy + uFrame * vec2(17.0, 59.0)) + hash12(gl_FragCoord.xy * 1.31 + uFrame * 7.0) - 1.0) * uGrain;
  float body = clamp(color.a, 0.0, 1.0);
  color.rgb += grain * (0.25 + body) * 0.5;
  color.a = clamp(color.a, 0.0, 1.0);
  color.rgb = clamp(color.rgb, 0.0, color.a);
  outColor = color;
}`;
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const toLinear = (v) => (v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4));
const toLab = (rgb) => {
const lr = toLinear(rgb[0]), lg = toLinear(rgb[1]), lb = toLinear(rgb[2]);
const l = Math.cbrt(0.4122214708 * lr + 0.5363325363 * lg + 0.0514459929 * lb);
const m = Math.cbrt(0.2119034982 * lr + 0.6806995451 * lg + 0.1073969566 * lb);
const s = Math.cbrt(0.0883024619 * lr + 0.2817188376 * lg + 0.6299787005 * lb);
return [0.2104542553 * l + 0.793617785 * m - 0.0040720468 * s, 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s, 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s];
};
const hexRgb = (h) => [parseInt(h.slice(1, 3), 16) / 255, parseInt(h.slice(3, 5), 16) / 255, parseInt(h.slice(5, 7), 16) / 255];
const gl = canvas.getContext('webgl2', { alpha: true, premultipliedAlpha: true, antialias: false, depth: false, stencil: false });
if (!gl) return null;
const compile = (type, src) => { const sh = gl.createShader(type); if (!sh) return null; gl.shaderSource(sh, src); gl.compileShader(sh); return sh; };
const link = (frag) => {
const v = compile(gl.VERTEX_SHADER, VERTEX), f = compile(gl.FRAGMENT_SHADER, frag), pr = gl.createProgram();
if (!v || !f || !pr) return null;
gl.attachShader(pr, v); gl.attachShader(pr, f); gl.linkProgram(pr); gl.deleteShader(v); gl.deleteShader(f);
if (!gl.getProgramParameter(pr, gl.LINK_STATUS)) return null;
const item = { program: pr, uniforms: {} };
const n = gl.getProgramParameter(pr, gl.ACTIVE_UNIFORMS);
for (let i = 0; i < n; i++) { const info = gl.getActiveUniform(pr, i); if (!info) continue; const name = info.name.replace(/\[0\]$/, ''); item.uniforms[name] = gl.getUniformLocation(pr, name); }
return item;
};
const field = link(FIELD), halo = link(HALO), blur = link(BLUR), composite = link(COMPOSITE);
if (!field || !halo || !blur || !composite) return null;
const programs = [field, halo, blur, composite];
const createTarget = (count) => {
const textures = [];
for (let i = 0; i < count; i++) {
const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
textures.push(t);
}
return { textures, framebuffer: gl.createFramebuffer(), width: 0, height: 0 };
};
const sizeTarget = (target, w, h) => {
if (target.width === w && target.height === h) return;
target.width = w; target.height = h;
gl.bindFramebuffer(gl.FRAMEBUFFER, target.framebuffer);
target.textures.forEach((t, i) => { gl.bindTexture(gl.TEXTURE_2D, t); gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0 + i, gl.TEXTURE_2D, t, 0); });
gl.bindFramebuffer(gl.FRAMEBUFFER, null);
};
const buildAtlas = () => {
const list = Array.from(new Set(Array.from(S.characters)));
const columns = Math.min(ATLAS_COLUMNS, list.length), rows = Math.ceil(list.length / columns);
const c = document.createElement('canvas'); c.width = ATLAS_CELL_W * columns; c.height = ATLAS_CELL_H * rows;
const ctx = c.getContext('2d');
if (ctx) {
ctx.font = '300 ' + Math.round(ATLAS_CELL_H * FONT_SCALE) + 'px ' + S.fontFamily; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillStyle = '#fff';
list.forEach((ch, i) => { const col = i % columns, row = Math.floor(i / columns); ctx.fillText(ch, col * ATLAS_CELL_W + ATLAS_CELL_W / 2, row * ATLAS_CELL_H + ATLAS_CELL_H / 2 + 3); });
}
const tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex);
gl.pixelStorei(gl.UNPACK_PREMULTIPLY_ALPHA_WEBGL, false);
gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, gl.RGBA, gl.UNSIGNED_BYTE, c);
gl.generateMipmap(gl.TEXTURE_2D);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
return { texture: tex, count: list.length, grid: [columns, rows] };
};
const vao = gl.createVertexArray();
const fieldTarget = createTarget(2), haloA = createTarget(1), haloB = createTarget(1);
const ramp = new Float32Array(MAX_COLORS * 3);
S.colors.forEach((c, i) => ramp.set(toLab(hexRgb(c)), i * 3));
const reduce = window.matchMedia ? window.matchMedia('(prefers-reduced-motion: reduce)').matches : false;
const view = { width: 1, height: 1, ratio: 1 };
const clickData = new Float32Array(MAX_CLICKS * 4), clicks = [];
const trailData = new Float32Array(MAX_TRAIL * 4), trail = [];
const pointer = { x: 0, y: 0, inside: false };
let atlas = buildAtlas();
let time = 0, glyphTime = 0, introClock = S.intro && !reduce ? 0 : 1, frameSeed = 0, grainClock = 0, raf = 0, last = 0, visible = true, disposed = false;
if (document.fonts && document.fonts.load) {
document.fonts.load('300 64px ' + S.fontFamily, S.characters).then(() => { if (disposed) return; gl.deleteTexture(atlas.texture); atlas = buildAtlas(); draw(); }, () => {});
}
const bindGlyphs = (prog, width, height) => {
const u = prog.uniforms;
const cellH = S.cellSize * view.ratio, cellW = cellH * (ATLAS_CELL_W / ATLAS_CELL_H);
gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, fieldTarget.textures[0]); gl.uniform1i(u.uField, 0);
gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, fieldTarget.textures[1]); gl.uniform1i(u.uAux, 1);
gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D, atlas.texture); gl.uniform1i(u.uAtlas, 2);
gl.uniform2f(u.uResolution, width, height);
gl.uniform2f(u.uCell, cellW, cellH);
gl.uniform2f(u.uOffset, (width - Math.ceil(width / cellW) * cellW) / 2, (height - Math.ceil(height / cellH) * cellH) / 2);
gl.uniform2f(u.uAtlasGrid, atlas.grid[0], atlas.grid[1]);
gl.uniform1f(u.uCount, atlas.count); gl.uniform1f(u.uDensity, S.density); gl.uniform1f(u.uOpacity, S.glyphOpacity);
gl.uniform1f(u.uFlicker, reduce ? 0 : S.flicker); gl.uniform1f(u.uDepth, S.depthOfField); gl.uniform1f(u.uGlyphTime, glyphTime);
gl.uniform1f(u.uSeedValue, S.variation); gl.uniform1f(u.uLight, S.lightMode ? 1 : 0);
};
const draw = () => {
const aspect = view.width / view.height;
gl.bindVertexArray(vao); gl.disable(gl.BLEND);
gl.bindFramebuffer(gl.FRAMEBUFFER, fieldTarget.framebuffer);
gl.drawBuffers([gl.COLOR_ATTACHMENT0, gl.COLOR_ATTACHMENT1]);
gl.viewport(0, 0, fieldTarget.width, fieldTarget.height);
gl.useProgram(field.program);
const fu = field.uniforms;
gl.uniform1f(fu.uAspect, aspect); gl.uniform1f(fu.uTime, time); gl.uniform1i(fu.uShape, S.shape);
gl.uniform3fv(fu.uRamp, ramp); gl.uniform1i(fu.uCount, S.colors.length); gl.uniform1f(fu.uScale, S.scale);
gl.uniform1f(fu.uSoftness, S.softness); gl.uniform1f(fu.uFlow, S.flow); gl.uniform2f(fu.uSeed, S.variation * 3.17, S.variation * 1.91);
gl.uniform4fv(fu.uTrail, trailData); gl.uniform1f(fu.uRadius, S.scrambleRadius); gl.uniform4fv(fu.uClicks, clickData);
gl.uniform1i(fu.uClickEffect, S.clickEffect); gl.uniform1f(fu.uIntro, introClock); gl.uniform1f(fu.uFrame, frameSeed);
gl.drawArrays(gl.TRIANGLES, 0, 3);
gl.bindFramebuffer(gl.FRAMEBUFFER, haloA.framebuffer); gl.drawBuffers([gl.COLOR_ATTACHMENT0]);
gl.viewport(0, 0, haloA.width, haloA.height); gl.useProgram(halo.program);
bindGlyphs(halo, canvas.width, canvas.height); gl.uniform1f(halo.uniforms.uDownscale, canvas.width / haloA.width);
gl.drawArrays(gl.TRIANGLES, 0, 3);
gl.useProgram(blur.program); gl.activeTexture(gl.TEXTURE0); gl.uniform1i(blur.uniforms.uSource, 0);
gl.bindFramebuffer(gl.FRAMEBUFFER, haloB.framebuffer); gl.bindTexture(gl.TEXTURE_2D, haloA.textures[0]);
gl.uniform2f(blur.uniforms.uStep, 1 / haloA.width, 0); gl.drawArrays(gl.TRIANGLES, 0, 3);
gl.bindFramebuffer(gl.FRAMEBUFFER, haloA.framebuffer); gl.bindTexture(gl.TEXTURE_2D, haloB.textures[0]);
gl.uniform2f(blur.uniforms.uStep, 0, 1 / haloA.height); gl.drawArrays(gl.TRIANGLES, 0, 3);
gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, canvas.width, canvas.height);
gl.useProgram(composite.program); bindGlyphs(composite, canvas.width, canvas.height);
const cu = composite.uniforms;
gl.activeTexture(gl.TEXTURE3); gl.bindTexture(gl.TEXTURE_2D, haloA.textures[0]); gl.uniform1i(cu.uHalo, 3);
gl.uniform1f(cu.uGlow, S.glow); gl.uniform1f(cu.uGradient, S.gradientOpacity); gl.uniform1f(cu.uGrain, S.grain); gl.uniform1f(cu.uFrame, frameSeed);
gl.drawArrays(gl.TRIANGLES, 0, 3);
};
const resize = () => {
view.width = Math.max(1, container.clientWidth); view.height = Math.max(1, container.clientHeight);
view.ratio = Math.min(window.devicePixelRatio || 1, 2);
canvas.width = Math.max(1, Math.round(view.width * view.ratio)); canvas.height = Math.max(1, Math.round(view.height * view.ratio));
sizeTarget(fieldTarget, Math.max(1, Math.round(canvas.width / 2)), Math.max(1, Math.round(canvas.height / 2)));
const hw = Math.max(1, Math.round(canvas.width / 4)), hh = Math.max(1, Math.round(canvas.height / 4));
sizeTarget(haloA, hw, hh); sizeTarget(haloB, hw, hh);
draw(); wake();
};
const updateInput = (dt) => {
trail.forEach((p) => { p.age += dt; });
while (trail.length && trail[trail.length - 1].age > TRAIL_LIFE) trail.pop();
for (let i = 0; i < MAX_TRAIL; i++) { const p = trail[i]; if (!p) { trailData[i * 4 + 2] = 0; continue; } const k = 1 - p.age / TRAIL_LIFE; trailData.set([p.x, p.y, k * k, 0], i * 4); }
clicks.forEach((c) => { c.age += dt; });
while (clicks.length && clicks[clicks.length - 1].age > CLICK_LIFE) clicks.pop();
for (let i = 0; i < MAX_CLICKS; i++) { const c = clicks[i]; if (!c) { clickData[i * 4 + 3] = 0; continue; } const k = c.age / CLICK_LIFE; const env = Math.min(1, c.age / 0.08) * (1 - k) * (1 - k); clickData.set([c.x, c.y, c.age, env], i * 4); }
};
const frame = (now) => {
raf = 0;
if (disposed || !visible || document.hidden) return;
const dt = last ? clamp((now - last) / 1000, 0.001, 0.05) : 1 / 60;
last = now;
if (!reduce) { time += dt * S.speed * 0.5; glyphTime += dt * Math.max(S.speed, 0.15); }
if (introClock < 1) introClock = Math.min(1, introClock + dt / INTRO_SECONDS);
grainClock += dt;
if (!reduce && grainClock > 1 / 24) { grainClock = 0; frameSeed = (frameSeed + 1) % 97; }
updateInput(dt); draw();
const busy = !reduce || introClock < 1 || clicks.length > 0 || trail.length > 0;
if (busy) raf = requestAnimationFrame(frame); else last = 0;
};
function wake() { if (!raf && !disposed && visible && !document.hidden) raf = requestAnimationFrame(frame); }
const locate = (e) => {
const r = container.getBoundingClientRect();
const x = (e.clientX - r.left) / Math.max(1, r.width), y = 1 - (e.clientY - r.top) / Math.max(1, r.height);
pointer.inside = x >= 0 && x <= 1 && y >= 0 && y <= 1; pointer.x = (x - 0.5) * (r.width / Math.max(1, r.height)); pointer.y = y - 0.5;
};
const onMove = (e) => {
locate(e);
if (!pointer.inside || !S.mouseInteraction || reduce) return;
const head = trail[0];
const gap = head ? Math.hypot(pointer.x - head.x, pointer.y - head.y) : Infinity;
if (gap < TRAIL_STEP) return;
if (head && head.age < 0.1) { const steps = Math.min(6, Math.floor(gap / (TRAIL_STEP * 2))); for (let i = 1; i <= steps; i++) { const k = i / (steps + 1); trail.unshift({ x: head.x + (pointer.x - head.x) * k, y: head.y + (pointer.y - head.y) * k, age: 0 }); } }
trail.unshift({ x: pointer.x, y: pointer.y, age: 0 }); trail.length = Math.min(trail.length, MAX_TRAIL);
wake();
};
const onDown = (e) => { locate(e); if (!pointer.inside || !S.clickEffect || reduce) return; clicks.unshift({ x: pointer.x, y: pointer.y, age: 0 }); if (clicks.length > MAX_CLICKS) clicks.pop(); wake(); };
const onVis = () => { last = 0; wake(); };
const ro = new ResizeObserver(resize); ro.observe(container);
const io = new IntersectionObserver((entries) => { visible = entries.some((en) => en.isIntersecting); if (visible) { last = 0; wake(); } }); io.observe(container);
window.addEventListener('pointermove', onMove, { passive: true });
window.addEventListener('pointerdown', onDown, { passive: true });
document.addEventListener('visibilitychange', onVis);
resize();
return () => {
if (disposed) return; disposed = true; cancelAnimationFrame(raf);
ro.disconnect(); io.disconnect();
window.removeEventListener('pointermove', onMove); window.removeEventListener('pointerdown', onDown); document.removeEventListener('visibilitychange', onVis);
[fieldTarget, haloA, haloB].forEach((t) => { t.textures.forEach((x) => gl.deleteTexture(x)); gl.deleteFramebuffer(t.framebuffer); });
gl.deleteTexture(atlas.texture); gl.deleteVertexArray(vao);
programs.forEach((p) => gl.deleteProgram(p.program));
};
}
}
