<template>
  <div>
    <!-- Toolbar -->
    <div class="toolbar-buttons">
      <button @click="addSlide" class="tool-btn add-btn" title="Add blank slide after current">+</button>
      <button @click="copyDrawing" class="tool-btn copy-btn" title="Copy this slide's drawings">✂</button>
      <button v-if="copiedSlide > 0" @click="pasteDrawing" class="tool-btn paste-btn" title="Paste drawings into this slide">📋</button>
      <div v-if="toast" class="toast-msg">{{ toast }}</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      copiedSlide: 0,
      toast: '',
      toastTimer: null,
      pasteHandler: null,
    };
  },
  mounted() {
    this.pasteHandler = (e) => {
      if (this.copiedSlide <= 0) return;
      e.preventDefault();
      this.pasteDrawing();
    };
    document.addEventListener('paste', this.pasteHandler);
  },
  methods: {
    getPage() {
      return parseInt(window.location.pathname.replace(/\//g, '')) || 1;
    },
    showToast(msg, ms = 3000) {
      this.toast = msg;
      clearTimeout(this.toastTimer);
      this.toastTimer = setTimeout(() => { this.toast = ''; }, ms);
    },

    async addSlide() {
      const page = this.getPage();
      try {
        const res = await fetch(`http://localhost:3099/add-slide?after=${page}`);
        const data = await res.json();
        if (data.ok) {
          this.showToast('Slide added!');
          setTimeout(() => { window.location.pathname = `/${data.newSlide}`; }, 800);
        }
      } catch (e) { this.showToast('Add slide failed'); }
    },

    copyDrawing() {
      const page = this.getPage();
      this.copiedSlide = page;
      this.showToast(`Slide ${page} drawings copied! Go to target slide and click 📋 or Ctrl+V`, 4000);
    },

    async pasteDrawing() {
      if (this.copiedSlide <= 0) return;
      const page = this.getPage();
      if (page === this.copiedSlide) {
        this.showToast('Navigate to a different slide first');
        return;
      }
      try {
        const res = await fetch(`http://localhost:3099/copy-drawing?from=${this.copiedSlide}&to=${page}`);
        const data = await res.json();
        if (data.ok) {
          this.showToast(`Drawings from slide ${this.copiedSlide} pasted to slide ${page}!`);
          setTimeout(() => { window.location.reload(); }, 800);
        } else {
          this.showToast('Paste failed: ' + (data.error || 'unknown'));
        }
      } catch (e) {
        this.showToast('Paste failed — is the server running?');
      }
    },
  },
  beforeUnmount() {
    if (this.pasteHandler) document.removeEventListener('paste', this.pasteHandler);
  }
}
</script>

<style>
.toolbar-buttons {
  position: fixed;
  bottom: 70px; right: 24px;
  display: flex; flex-direction: column; gap: 8px;
  z-index: 200; align-items: center;
}
.tool-btn {
  width: 36px; height: 36px; border-radius: 50%;
  background: #c2785c; color: #fff;
  font-size: 18px; font-weight: 700;
  border: none; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  opacity: 0.5; transition: opacity 0.2s, background 0.2s;
  font-family: -apple-system, sans-serif;
  line-height: 1; padding: 0;
}
.tool-btn:hover { opacity: 1; }
.add-btn { font-size: 22px; }
.paste-btn { background: #5a7fa5; opacity: 0.7; }
.paste-btn:hover { opacity: 1; }

.toast-msg {
  position: fixed; bottom: 130px; right: 24px;
  background: rgba(58,48,37,0.9); color: #fff;
  padding: 8px 16px; border-radius: 8px;
  font-size: 13px; font-family: -apple-system, sans-serif;
  white-space: nowrap; pointer-events: none;
  animation: toast-in 0.2s ease-out;
}
@keyframes toast-in {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
