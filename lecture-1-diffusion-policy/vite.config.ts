import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [{
    name: 'passthrough-viz-assets',
    resolveId(source) {
      if (source.startsWith('/viz/')) {
        return { id: source, external: true }
      }
    }
  }]
})
