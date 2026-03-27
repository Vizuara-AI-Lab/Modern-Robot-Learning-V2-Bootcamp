"""
VLA Lecture — Manim Animations
==============================
4 scenes for Lecture 2 Parts 1 & 2:
  Scene01: Bag of Words — sparse one-hot vectors for two synonymous sentences
  Scene02: Word2Vec — embedding space with clustering and analogy arrows
  Scene03: GRU — sequential processing with hidden state evolution
  Scene04: mini-VLA — full pipeline data flow (3 encoders → concat → fusion → diffusion)

Render all:  manim -qh --fps 30 -a vla_components.py
Render one:  manim -qh --fps 30 vla_components.py Scene01_BagOfWords
"""

from manim import *
import numpy as np

# ─────────────────────────────────────────────
# Colors (Vizuara Warm Palette)
# ─────────────────────────────────────────────
ACCENT = ManimColor("#D97757")
WARM   = ManimColor("#C4956A")
TEAL   = ManimColor("#7DA488")
BLUE   = ManimColor("#5B8CB8")
PURPLE = ManimColor("#9B7EC8")
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


def make_vector_bar(n, color, height=2.0, width=0.35, values=None):
    """Vertical bar of cells representing a vector."""
    bar = VGroup()
    if values is None:
        values = rng.random(n)
    cell_h = height / n
    for i, v in enumerate(values):
        c = interpolate_color(BLACK, color, 0.15 + 0.85 * abs(v))
        sq = Rectangle(
            width=width, height=cell_h,
            fill_color=c, fill_opacity=0.85,
            stroke_width=0.5, stroke_color=WHITE,
        )
        sq.move_to([0, (n / 2 - i - 0.5) * cell_h, 0])
        bar.add(sq)
    bar.move_to(ORIGIN)
    return bar


# ═══════════════════════════════════════════════════════════════
# Scene 01 — Bag of Words: Two synonymous sentences, sparse vectors
# ═══════════════════════════════════════════════════════════════
class Scene01_BagOfWords(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Bag of Words Encoding", font_size=34, color=ACCENT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)

        # --- Vocabulary ---
        vocab = ["pick", "up", "the", "red", "cup", "grab", "crimson", "mug", "a", "to"]
        vocab_group = VGroup()
        for i, w in enumerate(vocab):
            t = Text(w, font_size=18, color=WHITE)
            t.move_to([i * 1.2 - 5.4, 2.0, 0])
            vocab_group.add(t)

        vocab_label = Text("Vocabulary", font_size=20, color=WARM)
        vocab_label.next_to(vocab_group, LEFT, buff=0.4)

        self.play(FadeIn(vocab_group), FadeIn(vocab_label), run_time=1.5)
        self.wait(0.5)

        # --- Sentence 1 ---
        s1_text = Text('"pick up the red cup"', font_size=22, color=ACCENT)
        s1_text.move_to([-3.5, 0.6, 0])
        self.play(Write(s1_text), run_time=1)

        # Highlight matching words
        s1_indices = [0, 1, 2, 3, 4]  # pick, up, the, red, cup
        s1_cells = VGroup()
        for i in range(len(vocab)):
            val = "1" if i in s1_indices else "0"
            col = ACCENT if i in s1_indices else GREY_D
            cell = Square(side_length=0.5, fill_color=col,
                          fill_opacity=0.6 if i in s1_indices else 0.15,
                          stroke_width=1, stroke_color=GREY_B)
            cell.move_to([i * 1.2 - 5.4, -0.2, 0])
            num = Text(val, font_size=16, color=WHITE)
            num.move_to(cell.get_center())
            s1_cells.add(VGroup(cell, num))

        self.play(LaggedStart(*[FadeIn(c, shift=DOWN*0.2) for c in s1_cells],
                               lag_ratio=0.08), run_time=1.5)
        self.wait(0.5)

        # --- Sentence 2 ---
        s2_text = Text('"grab the crimson mug"', font_size=22, color=TEAL)
        s2_text.move_to([-3.5, -1.2, 0])
        self.play(Write(s2_text), run_time=1)

        s2_indices = [2, 5, 6, 7]  # the, grab, crimson, mug
        s2_cells = VGroup()
        for i in range(len(vocab)):
            val = "1" if i in s2_indices else "0"
            col = TEAL if i in s2_indices else GREY_D
            cell = Square(side_length=0.5, fill_color=col,
                          fill_opacity=0.6 if i in s2_indices else 0.15,
                          stroke_width=1, stroke_color=GREY_B)
            cell.move_to([i * 1.2 - 5.4, -2.0, 0])
            num = Text(val, font_size=16, color=WHITE)
            num.move_to(cell.get_center())
            s2_cells.add(VGroup(cell, num))

        self.play(LaggedStart(*[FadeIn(c, shift=DOWN*0.2) for c in s2_cells],
                               lag_ratio=0.08), run_time=1.5)
        self.wait(0.5)

        # --- Overlap highlight ---
        overlap_text = Text("Overlap: only 'the' → similarity ≈ 0.2", font_size=22, color=ManimColor("#D4543A"))
        overlap_text.move_to([0, -3.0, 0])

        # Circle the overlapping 'the' cells
        circle1 = Circle(radius=0.35, color=ManimColor("#D4543A"), stroke_width=3)
        circle1.move_to(s1_cells[2].get_center())
        circle2 = Circle(radius=0.35, color=ManimColor("#D4543A"), stroke_width=3)
        circle2.move_to(s2_cells[2].get_center())

        self.play(Create(circle1), Create(circle2), Write(overlap_text), run_time=1.5)
        self.wait(2)

        # --- Verdict ---
        verdict = Text("Same meaning → completely different vectors!", font_size=26, color=ACCENT)
        verdict.move_to([0, -3.5, 0])
        self.play(FadeOut(overlap_text), Write(verdict), run_time=1)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 02 — Word2Vec Embedding Space
# ═══════════════════════════════════════════════════════════════
class Scene02_Word2VecSpace(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("Word Embedding Space (Word2Vec)", font_size=34, color=ACCENT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)

        # Word positions (hand-designed for visual clarity)
        words = {
            # Actions cluster (orange)
            "pick":  ([-4.5, -0.5, 0], ACCENT),
            "grab":  ([-3.8, -1.0, 0], ACCENT),
            "grasp": ([-4.2,  0.2, 0], ACCENT),
            "lift":  ([-3.3, -0.2, 0], ACCENT),
            # Objects cluster (blue)
            "cup":   ([1.0,  -1.5, 0], BLUE),
            "mug":   ([1.8,  -1.0, 0], BLUE),
            "glass": ([1.5,  -2.0, 0], BLUE),
            # Colors cluster (teal)
            "red":     ([3.5, 1.0, 0], TEAL),
            "crimson": ([4.2, 0.5, 0], TEAL),
            "scarlet": ([3.8, 1.6, 0], TEAL),
            # Royalty (purple) for the analogy
            "king":   ([-1.0,  2.5, 0], PURPLE),
            "queen":  ([ 1.5,  2.5, 0], PURPLE),
            "man":    ([-1.0,  1.0, 0], WARM),
            "woman":  ([ 1.5,  1.0, 0], WARM),
        }

        # Plot all words
        dots = VGroup()
        labels = VGroup()
        for word, (pos, color) in words.items():
            dot = Dot(point=pos, radius=0.08, color=color)
            label = Text(word, font_size=16, color=color)
            label.next_to(dot, UR, buff=0.1)
            dots.add(dot)
            labels.add(label)

        self.play(LaggedStart(*[FadeIn(d, scale=2) for d in dots], lag_ratio=0.05),
                  LaggedStart(*[FadeIn(l) for l in labels], lag_ratio=0.05),
                  run_time=2.5)
        self.wait(1)

        # --- Cluster circles ---
        action_circle = Ellipse(width=2.5, height=2.0, color=ACCENT,
                                stroke_width=2, stroke_opacity=0.5)
        action_circle.move_to([-3.95, -0.35, 0])
        action_label = Text("Actions", font_size=18, color=ACCENT)
        action_label.next_to(action_circle, DOWN, buff=0.2)

        object_circle = Ellipse(width=2.0, height=2.0, color=BLUE,
                                stroke_width=2, stroke_opacity=0.5)
        object_circle.move_to([1.4, -1.5, 0])
        object_label = Text("Objects", font_size=18, color=BLUE)
        object_label.next_to(object_circle, DOWN, buff=0.2)

        color_circle = Ellipse(width=2.0, height=1.8, color=TEAL,
                               stroke_width=2, stroke_opacity=0.5)
        color_circle.move_to([3.8, 1.0, 0])
        color_label = Text("Colors", font_size=18, color=TEAL)
        color_label.next_to(color_circle, DOWN, buff=0.2)

        self.play(Create(action_circle), Create(object_circle), Create(color_circle),
                  FadeIn(action_label), FadeIn(object_label), FadeIn(color_label),
                  run_time=1.5)
        self.wait(1)

        # --- King-Queen analogy ---
        arrow_king_man = Arrow(
            start=words["king"][0], end=words["man"][0],
            color=WARM, stroke_width=3, buff=0.15,
        )
        arrow_queen_woman = Arrow(
            start=words["queen"][0], end=words["woman"][0],
            color=WARM, stroke_width=3, buff=0.15,
        )
        analogy_text = Text("king - man + woman ≈ queen", font_size=24, color=PURPLE)
        analogy_text.to_edge(DOWN, buff=0.6)

        self.play(GrowArrow(arrow_king_man), GrowArrow(arrow_queen_woman), run_time=1.5)
        self.play(Write(analogy_text), run_time=1)
        self.wait(1)

        insight = Text("Meaning lives in geometry!", font_size=26, color=ACCENT)
        insight.next_to(analogy_text, UP, buff=0.3)
        self.play(Write(insight), run_time=1)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 03 — GRU Sequential Processing
# ═══════════════════════════════════════════════════════════════
class Scene03_GRUProcessing(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("GRU: Reading a Sentence Word by Word", font_size=34, color=ACCENT)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)

        words = ["pick", "up", "the", "red", "cup"]
        n = len(words)
        spacing = 2.4
        start_x = -(n - 1) * spacing / 2

        # Build GRU cells
        gru_cells = VGroup()
        word_labels = VGroup()
        hidden_arrows = VGroup()
        input_arrows = VGroup()

        for i, word in enumerate(words):
            x = start_x + i * spacing
            # GRU cell
            cell = make_block("GRU", BLUE, width=1.4, height=0.9, font_size=18, opacity=0.3)
            cell.move_to([x, 0, 0])
            gru_cells.add(cell)

            # Word input from below
            w_label = Text(word, font_size=20, color=ACCENT)
            w_label.move_to([x, -1.5, 0])
            word_labels.add(w_label)

            # Input arrow
            inp_arr = Arrow(start=[x, -1.1, 0], end=[x, -0.5, 0],
                            color=ACCENT, stroke_width=2, buff=0.05)
            input_arrows.add(inp_arr)

            # Hidden state arrow to next cell
            if i < n - 1:
                nx = start_x + (i + 1) * spacing
                h_arr = Arrow(start=[x + 0.75, 0, 0], end=[nx - 0.75, 0, 0],
                              color=TEAL, stroke_width=3, buff=0.05)
                h_label = Text(f"h{i+1}", font_size=14, color=TEAL)
                h_label.next_to(h_arr, UP, buff=0.1)
                hidden_arrows.add(VGroup(h_arr, h_label))

        # Show cells
        self.play(LaggedStart(*[FadeIn(c, shift=UP*0.3) for c in gru_cells],
                               lag_ratio=0.15), run_time=2)
        self.wait(0.5)

        # Animate word-by-word processing
        for i in range(n):
            anims = [FadeIn(word_labels[i], shift=UP*0.3),
                     GrowArrow(input_arrows[i])]

            # Flash the GRU cell
            flash = gru_cells[i][0].copy()
            flash.set_fill(ACCENT, opacity=0.5)

            anims.append(FadeIn(flash))

            self.play(*anims, run_time=0.6)
            self.play(FadeOut(flash), run_time=0.3)

            # Show hidden state arrow
            if i < n - 1:
                self.play(GrowArrow(hidden_arrows[i][0]),
                          FadeIn(hidden_arrows[i][1]), run_time=0.5)

        # Final output
        final_x = start_x + (n - 1) * spacing
        out_arrow = Arrow(start=[final_x, 0.5, 0], end=[final_x, 1.5, 0],
                          color=TEAL, stroke_width=4, buff=0.05)

        # Vector bar for sentence embedding
        vec_bar = make_vector_bar(8, TEAL, height=1.2, width=0.6,
                                  values=[0.8, 0.3, 0.9, 0.5, 0.7, 0.2, 0.6, 0.4])
        vec_bar.move_to([final_x, 2.3, 0])
        vec_label = Text("Sentence\nEmbedding\n(128-d)", font_size=16, color=TEAL)
        vec_label.next_to(vec_bar, RIGHT, buff=0.3)

        self.play(GrowArrow(out_arrow), run_time=0.7)
        self.play(FadeIn(vec_bar, shift=UP*0.3), FadeIn(vec_label), run_time=1)
        self.wait(1)

        # Bottleneck warning
        warning = Text("⚠ Entire sentence compressed into ONE vector",
                        font_size=22, color=ManimColor("#D4543A"))
        warning.to_edge(DOWN, buff=0.6)
        self.play(Write(warning), run_time=1)
        self.wait(2)


# ═══════════════════════════════════════════════════════════════
# Scene 04 — mini-VLA Pipeline Data Flow
# ═══════════════════════════════════════════════════════════════
class Scene04_MiniVLAPipeline(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        title = Text("mini-VLA: The Duct-Tape Pipeline", font_size=34, color=ACCENT)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title), run_time=1)

        y_positions = [1.5, 0, -1.5]
        labels = ["Camera Image", '"push the cube"', "Joint Angles"]
        encoders = ["TinyCNN", "GRU", "State MLP"]
        colors = [BLUE, ACCENT, TEAL]
        vec_labels_text = ["128-d", "128-d", "128-d"]

        input_groups = VGroup()
        encoder_groups = VGroup()
        vec_groups = VGroup()
        all_arrows_in = VGroup()
        all_arrows_enc = VGroup()

        for i in range(3):
            y = y_positions[i]

            # Input label
            inp = Text(labels[i], font_size=18, color=colors[i])
            inp.move_to([-5.5, y, 0])
            input_groups.add(inp)

            # Encoder block
            enc = make_block(encoders[i], colors[i], width=1.8, height=0.7, font_size=17, opacity=0.35)
            enc.move_to([-2.5, y, 0])
            encoder_groups.add(enc)

            # Arrow: input → encoder
            arr1 = Arrow(start=[-4.3, y, 0], end=[-3.5, y, 0],
                         color=colors[i], stroke_width=2, buff=0.05)
            all_arrows_in.add(arr1)

            # Vector bar
            vec = make_vector_bar(6, colors[i], height=0.6, width=0.5,
                                  values=rng.random(6))
            vec.move_to([-0.3, y, 0])
            vec_lbl = make_dim_label(vec_labels_text[i])
            vec_lbl.next_to(vec, RIGHT, buff=0.15)
            vec_groups.add(VGroup(vec, vec_lbl))

            # Arrow: encoder → vector
            arr2 = Arrow(start=[-1.5, y, 0], end=[-0.7, y, 0],
                         color=colors[i], stroke_width=2, buff=0.05)
            all_arrows_enc.add(arr2)

        # Animate inputs and encoders
        self.play(LaggedStart(*[FadeIn(g) for g in input_groups], lag_ratio=0.2),
                  run_time=1.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in all_arrows_in], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(e, shift=RIGHT*0.3) for e in encoder_groups], lag_ratio=0.15),
                  run_time=1.5)
        self.play(LaggedStart(*[GrowArrow(a) for a in all_arrows_enc], lag_ratio=0.15),
                  LaggedStart(*[FadeIn(v, shift=RIGHT*0.3) for v in vec_groups], lag_ratio=0.15),
                  run_time=1.5)
        self.wait(0.5)

        # --- Concatenation ---
        concat_block = make_block("Concat", WARM, width=1.2, height=2.0, font_size=16, opacity=0.3)
        concat_block.move_to([1.5, 0, 0])

        concat_arrows = VGroup()
        for i in range(3):
            y = y_positions[i]
            arr = Arrow(start=[0.3, y, 0], end=[0.85, y * 0.3, 0],
                        color=WARM, stroke_width=2, buff=0.05)
            concat_arrows.add(arr)

        concat_dim = make_dim_label("384-d")
        concat_dim.next_to(concat_block, DOWN, buff=0.2)

        self.play(LaggedStart(*[GrowArrow(a) for a in concat_arrows], lag_ratio=0.1),
                  FadeIn(concat_block, shift=RIGHT*0.3),
                  FadeIn(concat_dim),
                  run_time=1.5)
        self.wait(0.5)

        # --- Fusion MLP ---
        fusion_block = make_block("Fusion MLP", WARM, width=1.6, height=0.8, font_size=16, opacity=0.35)
        fusion_block.move_to([3.3, 0, 0])
        fusion_arr = Arrow(start=[2.15, 0, 0], end=[2.45, 0, 0],
                           color=WARM, stroke_width=2, buff=0.05)
        fusion_dim = make_dim_label("128-d")
        fusion_dim.next_to(fusion_block, DOWN, buff=0.2)

        self.play(GrowArrow(fusion_arr),
                  FadeIn(fusion_block, shift=RIGHT*0.3),
                  FadeIn(fusion_dim),
                  run_time=1)
        self.wait(0.5)

        # --- Diffusion Head ---
        diff_block = make_block("Diffusion\nHead", PURPLE, width=1.6, height=0.8, font_size=16, opacity=0.35)
        diff_block.move_to([5.3, 0, 0])
        diff_arr = Arrow(start=[4.15, 0, 0], end=[4.45, 0, 0],
                         color=PURPLE, stroke_width=3, buff=0.05)

        actions_text = Text("Robot\nActions", font_size=18, color=PURPLE)
        actions_text.move_to([6.5, 0, 0])
        act_arr = Arrow(start=[6.15, 0, 0], end=[6.15, 0, 0],
                        color=PURPLE, stroke_width=2, buff=0.05)

        self.play(GrowArrow(diff_arr),
                  FadeIn(diff_block, shift=RIGHT*0.3),
                  run_time=1)
        self.wait(0.5)

        # "Duct tape" label with humor
        duct_tape = Text("← The 'duct tape'", font_size=16, color=ManimColor("#D4543A"))
        duct_tape.next_to(concat_block, UP, buff=0.4)
        self.play(Write(duct_tape), run_time=1)
        self.wait(0.5)

        # Show ~135K params
        params = Text("Total: ~135K parameters", font_size=20, color=WARM)
        params.to_edge(DOWN, buff=0.5)
        self.play(Write(params), run_time=1)
        self.wait(2)
