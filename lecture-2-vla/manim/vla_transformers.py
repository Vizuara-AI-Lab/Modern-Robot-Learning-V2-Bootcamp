"""
VLA Lecture — Manim Animations (Parts 3 & 4)
=============================================
4 scenes for Lecture 2 Parts 3 & 4:
  Scene05: Self-Attention — Q·K scores, softmax heatmap, weighted sum of Values
  Scene06: Multi-Head Attention — 4 heads with different patterns, merge outputs
  Scene07: Next-Token Prediction — causal mask, autoregressive generation
  Scene08: VLM Processing — image patches + text tokens, cross-modal attention

Render all:  manim -qh --fps 30 -a vla_transformers.py
Render one:  manim -qh --fps 30 vla_transformers.py Scene05_AttentionScores
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# Colors (Vizuara Warm Palette — same as Part 1/2)
# ─────────────────────────────────────────────
ACCENT = ManimColor("#D97757")
WARM   = ManimColor("#C4956A")
TEAL   = ManimColor("#7DA488")
BLUE   = ManimColor("#5B8CB8")
PURPLE = ManimColor("#9B7EC8")
RED    = ManimColor("#D4543A")
TEXT_DIM = GREY_B
BG_COLOR = ManimColor("#1A1915")

rng = np.random.RandomState(42)


def make_block(label, color, width=1.6, height=0.8, font_size=20, opacity=0.35):
    rect = RoundedRectangle(
        corner_radius=0.12, width=width, height=height,
        fill_color=color, fill_opacity=opacity,
        stroke_color=color, stroke_width=2,
    )
    txt = Text(label, font_size=font_size, color=WHITE)
    txt.move_to(rect.get_center())
    if txt.width > rect.width - 0.2:
        txt.scale_to_fit_width(rect.width - 0.2)
    return VGroup(rect, txt)


def make_dim_label(text, font_size=16):
    return Text(text, font_size=font_size, color=GREY_B, font="JetBrains Mono")


# ═══════════════════════════════════════════════════════════════
# Scene 05 — Self-Attention: Q·K Scores and Weighted Sum
# ═══════════════════════════════════════════════════════════════
class Scene05_AttentionScores(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Self-Attention: Every Word Sees Every Word", font_size=32, color=ACCENT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        words = ["picked", "up", "the", "red", "cup"]
        n = len(words)
        spacing = 1.8
        start_x = -(n - 1) * spacing / 2

        # ── Word boxes at bottom ──
        word_boxes = VGroup()
        for i, w in enumerate(words):
            x = start_x + i * spacing
            box = RoundedRectangle(
                corner_radius=0.08, width=1.3, height=0.5,
                fill_color=BLUE, fill_opacity=0.25,
                stroke_color=BLUE, stroke_width=1.5,
            )
            box.move_to([x, -2.5, 0])
            label = Text(w, font_size=18, color=WHITE)
            label.move_to(box.get_center())
            word_boxes.add(VGroup(box, label))

        self.play(LaggedStart(*[FadeIn(wb, shift=UP * 0.2) for wb in word_boxes],
                               lag_ratio=0.1), run_time=1.5)
        self.wait(0.5)

        # ── Q, K, V arrows ──
        qkv_label = Text("Each word → Q, K, V projections", font_size=18, color=WARM)
        qkv_label.move_to([0, -1.6, 0])
        self.play(FadeIn(qkv_label), run_time=0.8)

        q_dots = VGroup()
        k_dots = VGroup()
        v_dots = VGroup()
        for i in range(n):
            x = start_x + i * spacing
            q = Dot([x - 0.3, -1.1, 0], radius=0.06, color=ACCENT)
            k = Dot([x, -1.1, 0], radius=0.06, color=TEAL)
            v = Dot([x + 0.3, -1.1, 0], radius=0.06, color=PURPLE)
            q_dots.add(q)
            k_dots.add(k)
            v_dots.add(v)

        q_lbl = Text("Q", font_size=14, color=ACCENT).move_to([-5.0, -1.1, 0])
        k_lbl = Text("K", font_size=14, color=TEAL).move_to([-4.6, -1.1, 0])
        v_lbl = Text("V", font_size=14, color=PURPLE).move_to([-4.2, -1.1, 0])

        self.play(FadeIn(q_dots), FadeIn(k_dots), FadeIn(v_dots),
                  FadeIn(q_lbl), FadeIn(k_lbl), FadeIn(v_lbl), run_time=1)
        self.wait(0.5)

        # ── Attention heatmap ──
        # Simulated scores (hand-designed for pedagogical clarity)
        raw_scores = np.array([
            [0.1, 0.8, 0.0, 0.2, 0.9],  # picked attends to: up, cup
            [0.7, 0.1, 0.0, 0.1, 0.3],  # up attends to: picked
            [0.0, 0.0, 0.1, 0.4, 0.6],  # the → red, cup
            [0.1, 0.0, 0.1, 0.1, 0.9],  # red → cup (strongly!)
            [0.2, 0.1, 0.3, 0.7, 0.1],  # cup → red
        ])
        # Softmax per row
        def softmax(x):
            e = np.exp(x - x.max(axis=-1, keepdims=True))
            return e / e.sum(axis=-1, keepdims=True)
        weights = softmax(raw_scores * 3)

        cell_size = 0.6
        heatmap_group = VGroup()
        hm_x0 = -(n - 1) * cell_size / 2
        hm_y0 = 0.8

        # Row/col labels
        for i, w in enumerate(words):
            row_label = Text(w, font_size=13, color=ACCENT)
            row_label.move_to([hm_x0 - cell_size * 0.8, hm_y0 - i * cell_size, 0])
            col_label = Text(w, font_size=13, color=TEAL)
            col_label.move_to([hm_x0 + i * cell_size, hm_y0 + cell_size * 0.7, 0])
            col_label.rotate(PI / 6)
            heatmap_group.add(row_label, col_label)

        cells = VGroup()
        for i in range(n):
            for j in range(n):
                w = weights[i, j]
                cell_color = interpolate_color(ManimColor("#1A1915"), ACCENT, min(w * 2, 1.0))
                cell = Square(
                    side_length=cell_size * 0.9,
                    fill_color=cell_color, fill_opacity=0.8,
                    stroke_width=0.5, stroke_color=GREY_B,
                )
                cell.move_to([hm_x0 + j * cell_size, hm_y0 - i * cell_size, 0])
                val_text = Text(f"{w:.2f}", font_size=10, color=WHITE)
                val_text.move_to(cell.get_center())
                cells.add(VGroup(cell, val_text))

        heatmap_title = Text("Attention Weights (softmax of Q·Kᵀ / √d)", font_size=18, color=WARM)
        heatmap_title.move_to([0, hm_y0 + cell_size * 1.5, 0])

        self.play(FadeOut(qkv_label), run_time=0.3)
        self.play(FadeIn(heatmap_title), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c, scale=0.8) for c in cells], lag_ratio=0.02),
                  FadeIn(heatmap_group), run_time=2.5)
        self.wait(1)

        # ── Highlight "red" → "cup" ──
        red_cup_idx = 3 * n + 4  # row 3 (red), col 4 (cup)
        highlight = SurroundingRectangle(cells[red_cup_idx], color=WHITE, stroke_width=3, buff=0.04)
        hl_text = Text('"red" → "cup": 0.54', font_size=18, color=WHITE)
        hl_text.move_to([3.5, 0.8, 0])

        self.play(Create(highlight), Write(hl_text), run_time=1)
        self.wait(1)

        # ── Output ──
        output_text = Text(
            "Each word's output = weighted sum of all Values",
            font_size=20, color=TEAL
        )
        output_text.to_edge(DOWN, buff=0.4)
        self.play(Write(output_text), run_time=1)
        self.wait(0.5)

        insight = Text("No bottleneck — direct connections between any two words!",
                        font_size=22, color=ACCENT)
        insight.next_to(output_text, UP, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 06 — Multi-Head Attention: 4 Heads with Different Patterns
# ═══════════════════════════════════════════════════════════════
class Scene06_MultiHeadAttention(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Multi-Head Attention: Different Perspectives", font_size=32, color=ACCENT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        words = ["picked", "up", "the", "red", "cup"]
        n = len(words)

        head_names = ["Head 1\nSubject-Verb", "Head 2\nAdj-Noun", "Head 3\nVerb-Object", "Head 4\nSpatial"]
        head_colors = [ACCENT, TEAL, BLUE, PURPLE]

        # Key connections each head focuses on (from_idx, to_idx)
        head_connections = [
            [(0, 0)],        # Head 1: picked self-attends (subject-verb)
            [(3, 4)],        # Head 2: red → cup (adjective-noun)
            [(0, 4)],        # Head 3: picked → cup (verb-object)
            [(2, 4)],        # Head 4: the → cup (determiner)
        ]

        # Draw 4 mini heatmaps in a 2×2 grid
        positions = [[-3.0, 0.5], [0.5, 0.5], [-3.0, -2.2], [0.5, -2.2]]
        cell_sz = 0.38

        all_head_groups = VGroup()

        for h in range(4):
            cx, cy = positions[h]
            head_group = VGroup()

            # Head label
            h_label = Text(head_names[h], font_size=14, color=head_colors[h])
            h_label.move_to([cx + (n - 1) * cell_sz / 2, cy + n * cell_sz / 2 + 0.4, 0])
            head_group.add(h_label)

            # Mini heatmap — mostly dim, bright on key connections
            for i in range(n):
                for j in range(n):
                    is_key = (i, j) in head_connections[h]
                    opacity = 0.85 if is_key else 0.12
                    fill_c = head_colors[h] if is_key else ManimColor("#2a2a25")
                    cell = Square(
                        side_length=cell_sz * 0.88,
                        fill_color=fill_c, fill_opacity=opacity,
                        stroke_width=0.3, stroke_color=GREY_B,
                    )
                    cell.move_to([cx + j * cell_sz, cy + (n - 1 - i) * cell_sz, 0])
                    head_group.add(cell)

            # Row labels (words)
            for i, w in enumerate(words):
                lbl = Text(w, font_size=10, color=GREY_B)
                lbl.move_to([cx - cell_sz * 0.7, cy + (n - 1 - i) * cell_sz, 0])
                head_group.add(lbl)

            all_head_groups.add(head_group)

        # Animate heads one by one
        for h in range(4):
            self.play(FadeIn(all_head_groups[h]), run_time=1.2)
            self.wait(0.4)

        # ── Merge arrow ──
        merge_block = make_block("Concat +\nProject", WARM, width=1.8, height=1.0,
                                  font_size=16, opacity=0.35)
        merge_block.move_to([4.5, -0.8, 0])

        merge_arrows = VGroup()
        for h in range(4):
            cx, cy = positions[h]
            arr = Arrow(
                start=[cx + n * cell_sz, cy + (n - 1) * cell_sz / 2, 0],
                end=merge_block.get_left() + LEFT * 0.05,
                color=head_colors[h], stroke_width=2, buff=0.1,
            )
            merge_arrows.add(arr)

        output_label = Text("128-d output\n(all perspectives\ncombined)", font_size=14, color=WARM)
        output_label.next_to(merge_block, RIGHT, buff=0.3)

        self.play(LaggedStart(*[GrowArrow(a) for a in merge_arrows], lag_ratio=0.1),
                  FadeIn(merge_block, shift=RIGHT * 0.3), run_time=1.5)
        self.play(FadeIn(output_label), run_time=0.8)
        self.wait(1)

        insight = Text("4 heads × 32-d each = 128-d total — richer than one big head",
                        font_size=20, color=ACCENT)
        insight.to_edge(DOWN, buff=0.4)
        self.play(Write(insight), run_time=1)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 07 — Next-Token Prediction with Causal Mask
# ═══════════════════════════════════════════════════════════════
class Scene07_NextTokenPrediction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Next-Token Prediction (How GPT/Gemma Learn)", font_size=32, color=ACCENT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        tokens = ["The", "robot", "picked", "up", "the", "red", "?"]
        n = len(tokens)
        spacing = 1.5
        start_x = -(n - 1) * spacing / 2

        # ── Token boxes ──
        token_boxes = VGroup()
        for i, t in enumerate(tokens):
            x = start_x + i * spacing
            color = ACCENT if t == "?" else BLUE
            box = RoundedRectangle(
                corner_radius=0.08, width=1.0, height=0.45,
                fill_color=color, fill_opacity=0.25 if t != "?" else 0.5,
                stroke_color=color, stroke_width=1.5,
            )
            box.move_to([x, 1.5, 0])
            label = Text(t, font_size=16, color=WHITE)
            label.move_to(box.get_center())
            token_boxes.add(VGroup(box, label))

        self.play(LaggedStart(*[FadeIn(tb, shift=DOWN * 0.2) for tb in token_boxes[:-1]],
                               lag_ratio=0.08), run_time=1.5)
        self.wait(0.5)

        # ── Causal attention mask ──
        mask_title = Text("Causal Attention Mask", font_size=20, color=WARM)
        mask_title.move_to([0, 0.5, 0])
        self.play(FadeIn(mask_title), run_time=0.5)

        cell_sz = 0.5
        mask_x0 = -(n - 2) * cell_sz / 2  # exclude '?' from mask display
        mask_y0 = -0.5
        mask_n = n - 1  # 6 tokens (without ?)

        mask_cells = VGroup()
        mask_labels = VGroup()
        for i in range(mask_n):
            # Row label
            rl = Text(tokens[i], font_size=10, color=GREY_B)
            rl.move_to([mask_x0 - cell_sz * 0.8, mask_y0 - i * cell_sz, 0])
            mask_labels.add(rl)
            # Col label
            cl = Text(tokens[i], font_size=10, color=GREY_B)
            cl.move_to([mask_x0 + i * cell_sz, mask_y0 + cell_sz * 0.7, 0])
            cl.rotate(PI / 6)
            mask_labels.add(cl)

            for j in range(mask_n):
                can_attend = j <= i  # causal: can only see past + self
                fill_c = TEAL if can_attend else ManimColor("#2a2a25")
                opacity = 0.6 if can_attend else 0.1
                cell = Square(
                    side_length=cell_sz * 0.88,
                    fill_color=fill_c, fill_opacity=opacity,
                    stroke_width=0.3, stroke_color=GREY_B,
                )
                cell.move_to([mask_x0 + j * cell_sz, mask_y0 - i * cell_sz, 0])
                mask_cells.add(cell)

        self.play(LaggedStart(*[FadeIn(c, scale=0.9) for c in mask_cells], lag_ratio=0.01),
                  FadeIn(mask_labels), run_time=2)
        self.wait(1)

        mask_note = Text("Lower triangle = each token only sees past tokens (no peeking!)",
                          font_size=16, color=TEAL)
        mask_note.move_to([0, mask_y0 - mask_n * cell_sz - 0.3, 0])
        self.play(FadeIn(mask_note), run_time=0.7)
        self.wait(0.5)

        # ── Prediction ──
        predict_label = Text("Predict →", font_size=20, color=ACCENT)
        predict_label.next_to(token_boxes[-2], RIGHT, buff=0.15)
        predict_label.shift(UP * 0.0)

        self.play(FadeIn(token_boxes[-1], scale=1.3), Write(predict_label), run_time=1)
        self.wait(0.5)

        # Show prediction
        answer = Text('"cup"', font_size=28, color=ACCENT)
        answer.move_to(token_boxes[-1].get_center() + UP * 0.8)
        answer_arrow = Arrow(
            start=answer.get_bottom(), end=token_boxes[-1].get_top(),
            color=ACCENT, stroke_width=2, buff=0.1,
        )

        self.play(Write(answer), GrowArrow(answer_arrow), run_time=1)
        self.wait(1)

        # ── Scale insight ──
        insight = Text(
            "Train on trillions of tokens → model learns grammar, semantics, world knowledge",
            font_size=18, color=ACCENT,
        )
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1.2)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 08 — VLM Processing: Image Patches + Text in One Transformer
# ═══════════════════════════════════════════════════════════════
class Scene08_VLMProcessing(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("VLM: Vision + Language in One Transformer", font_size=32, color=ACCENT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        # ── Image patches (left side) ──
        img_label = Text("Camera Image", font_size=18, color=BLUE)
        img_label.move_to([-5.0, 2.0, 0])
        self.play(FadeIn(img_label), run_time=0.5)

        # 4×4 grid representing image patches (simplified from 14×14)
        patch_grid = VGroup()
        grid_n = 4
        patch_sz = 0.4
        grid_x0, grid_y0 = -5.5, 0.8
        patch_colors = [BLUE, ManimColor("#4A7A9B"), ManimColor("#6B9BBB"), ManimColor("#3A6A8B")]
        for r in range(grid_n):
            for c in range(grid_n):
                p = Square(
                    side_length=patch_sz,
                    fill_color=patch_colors[(r + c) % len(patch_colors)],
                    fill_opacity=0.5,
                    stroke_width=0.5, stroke_color=GREY_B,
                )
                p.move_to([grid_x0 + c * patch_sz, grid_y0 - r * patch_sz, 0])
                patch_grid.add(p)

        self.play(FadeIn(patch_grid), run_time=1)
        self.wait(0.3)

        # SigLIP encoder
        siglip = make_block("SigLIP\n(Frozen)", BLUE, width=1.6, height=0.7, font_size=14, opacity=0.35)
        siglip.move_to([-3.2, 0.5, 0])
        arr_to_siglip = Arrow(
            start=[-4.2, 0.5, 0], end=[-4.05, 0.5, 0],
            color=BLUE, stroke_width=2, buff=0.05,
        )
        self.play(GrowArrow(arr_to_siglip), FadeIn(siglip, shift=RIGHT * 0.2), run_time=0.8)

        # Visual tokens
        vis_tokens = VGroup()
        for i in range(6):
            tok = Square(
                side_length=0.3,
                fill_color=BLUE, fill_opacity=0.5,
                stroke_width=0.5, stroke_color=BLUE,
            )
            tok.move_to([-1.5 + i * 0.35, 0.5, 0])
            vis_tokens.add(tok)

        vis_label = Text("196 visual tokens", font_size=12, color=BLUE)
        vis_label.move_to([-0.4, 0.1, 0])

        arr_siglip_out = Arrow(
            start=siglip.get_right(), end=[-1.8, 0.5, 0],
            color=BLUE, stroke_width=2, buff=0.05,
        )
        self.play(GrowArrow(arr_siglip_out),
                  LaggedStart(*[FadeIn(t, scale=0.5) for t in vis_tokens], lag_ratio=0.05),
                  FadeIn(vis_label), run_time=1.2)
        self.wait(0.3)

        # ── Text tokens (left side, below) ──
        text_input = Text('"pick up the red cup"', font_size=16, color=TEAL)
        text_input.move_to([-5.0, -1.0, 0])
        self.play(FadeIn(text_input), run_time=0.5)

        tokenizer = make_block("Tokenizer\n+ Embed", TEAL, width=1.4, height=0.6, font_size=13, opacity=0.35)
        tokenizer.move_to([-3.2, -1.0, 0])
        arr_to_tok = Arrow(
            start=[-4.0, -1.0, 0], end=[-3.95, -1.0, 0],
            color=TEAL, stroke_width=2, buff=0.05,
        )
        self.play(GrowArrow(arr_to_tok), FadeIn(tokenizer, shift=RIGHT * 0.2), run_time=0.7)

        txt_tokens = VGroup()
        txt_words = ["pick", "up", "the", "red", "cup"]
        for i, w in enumerate(txt_words):
            tok = RoundedRectangle(
                corner_radius=0.04, width=0.5, height=0.3,
                fill_color=TEAL, fill_opacity=0.4,
                stroke_width=0.5, stroke_color=TEAL,
            )
            tok.move_to([-1.5 + i * 0.55, -1.0, 0])
            lbl = Text(w, font_size=9, color=WHITE)
            lbl.move_to(tok.get_center())
            txt_tokens.add(VGroup(tok, lbl))

        txt_label = Text("5 text tokens", font_size=12, color=TEAL)
        txt_label.move_to([-0.2, -1.4, 0])

        arr_tok_out = Arrow(
            start=tokenizer.get_right(), end=[-1.8, -1.0, 0],
            color=TEAL, stroke_width=2, buff=0.05,
        )
        self.play(GrowArrow(arr_tok_out),
                  LaggedStart(*[FadeIn(t, scale=0.5) for t in txt_tokens], lag_ratio=0.06),
                  FadeIn(txt_label), run_time=1)
        self.wait(0.3)

        # ── Concatenation ──
        concat_label = Text("Concatenate into one sequence", font_size=16, color=WARM)
        concat_label.move_to([2.0, 1.5, 0])
        self.play(FadeIn(concat_label), run_time=0.5)

        # Combined sequence bar
        combined = VGroup()
        for i in range(6):
            tok = Square(side_length=0.28, fill_color=BLUE, fill_opacity=0.5,
                         stroke_width=0.4, stroke_color=BLUE)
            tok.move_to([1.0 + i * 0.32, 0.8, 0])
            combined.add(tok)
        sep = Text("|", font_size=16, color=GREY_B)
        sep.move_to([1.0 + 6 * 0.32 + 0.05, 0.8, 0])
        combined.add(sep)
        for i, w in enumerate(txt_words):
            tok = RoundedRectangle(corner_radius=0.03, width=0.45, height=0.28,
                                    fill_color=TEAL, fill_opacity=0.4,
                                    stroke_width=0.4, stroke_color=TEAL)
            tok.move_to([1.0 + (7 + i) * 0.32 + 0.15, 0.8, 0])
            lbl = Text(w, font_size=7, color=WHITE)
            lbl.move_to(tok.get_center())
            combined.add(VGroup(tok, lbl))

        self.play(FadeIn(combined, shift=DOWN * 0.2), run_time=1.2)
        self.wait(0.5)

        # ── Transformer block ──
        transformer = make_block("Gemma 2B Transformer\n(26 layers)", PURPLE,
                                  width=4.5, height=1.0, font_size=16, opacity=0.3)
        transformer.move_to([2.5, -0.5, 0])
        arr_to_tf = Arrow(
            start=[2.5, 0.5, 0], end=[2.5, -0.0, 0],
            color=PURPLE, stroke_width=3, buff=0.05,
        )

        self.play(GrowArrow(arr_to_tf), FadeIn(transformer, shift=DOWN * 0.3), run_time=1)
        self.wait(0.5)

        # ── Cross-attention highlight ──
        cross_attn_title = Text("Cross-Modal Attention", font_size=20, color=ACCENT)
        cross_attn_title.move_to([2.5, -1.8, 0])
        self.play(Write(cross_attn_title), run_time=0.7)

        # Draw attention arc: "red" (text) ↔ blue patch (visual)
        # "red" is token index ~10 in combined, a visual patch is ~index 2
        red_tok_pos = [1.0 + (7 + 3) * 0.32 + 0.15, 0.8, 0]  # "red" text token
        blue_patch_pos = [1.0 + 2 * 0.32, 0.8, 0]  # a visual patch

        arc = ArcBetweenPoints(
            start=blue_patch_pos, end=red_tok_pos,
            angle=-PI / 3, color=ACCENT, stroke_width=3,
        )
        arc_label = Text('"red" ↔ red pixels', font_size=14, color=ACCENT)
        arc_label.move_to([2.0, 1.3, 0])

        self.play(Create(arc), FadeIn(arc_label), run_time=1.5)
        self.wait(1)

        # ── Output ──
        output_text = Text("Fused Vision-Language Embeddings", font_size=18, color=PURPLE)
        output_text.move_to([2.5, -2.5, 0])
        out_arrow = Arrow(
            start=[2.5, -1.0, 0], end=[2.5, -2.2, 0],
            color=PURPLE, stroke_width=3, buff=0.1,
        )
        self.play(GrowArrow(out_arrow), Write(output_text), run_time=1)
        self.wait(0.5)

        insight = Text("No duct tape — modalities attend to each other at every layer!",
                        font_size=20, color=ACCENT)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)
