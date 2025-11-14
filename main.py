from manim import *
import numpy as np

class LightInterference(Scene):
    def construct(self):
        # Presenter information (persistent on all slides)
        presenter_info = VGroup(
            Text("Aditya Bhattacharjee", font_size=16, color=GRAY),
            Text("Grade 8 | New Horizon Public School", font_size=14, color=GRAY),
            Text("Indiranagar, Bangalore", font_size=14, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        presenter_info.to_corner(DL, buff=0.3)
        self.add(presenter_info)
        
        # Title
        title = Text("Double-Slit Interference", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # INTRODUCTORY SLIDE: What is Interference?
        intro_title = Text("What is Interference?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(intro_title))
        self.wait(0.5)
        
        # Definition
        definition = VGroup(
            Text("Interference is the phenomenon where", font_size=24),
            Text("two or more light waves overlap and combine", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        
        self.play(Write(definition[0]))
        self.wait(0.8)
        self.play(Write(definition[1]))
        self.wait(1.5)
        
        # Key points
        key_points = VGroup(
            Text("• When two waves meet, they add together", font_size=20, color=BLUE),
            Text("• In phase (crests align) → Constructive", font_size=20, color=RED),
            Text("  Result: BRIGHT spots (amplitudes add)", font_size=18, color=RED),
            Text("• Out of phase (crest meets trough) → Destructive", font_size=20, color=BLUE_E),
            Text("  Result: DARK spots (waves cancel)", font_size=18, color=BLUE_E),
            Text("• Creates alternating bright and dark bands", font_size=20, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.5)
        
        self.play(LaggedStart(*[Write(point) for point in key_points], lag_ratio=0.4), run_time=5)
        self.wait(2)
        
        # Example text
        example = Text("Let's see it in action...", font_size=22, color=ORANGE).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(example))
        self.wait(1.5)
        
        # Clear intro slide
        self.play(
            *[FadeOut(mob) for mob in [intro_title, definition, key_points, example]]
        )
        self.wait(0.5)
        
        # Setup
        distance = 1.5  # Distance between sources
        
        # Create two point sources
        sources = [Dot(LEFT * distance/2 + DOWN * 2.5, color=YELLOW, radius=0.08),
                  Dot(RIGHT * distance/2 + DOWN * 2.5, color=YELLOW, radius=0.08)]
        
        # Add labels for sources
        source_labels = VGroup(
            Text("S1", font_size=20).next_to(sources[0], LEFT, buff=0.2),
            Text("S2", font_size=20).next_to(sources[1], RIGHT, buff=0.2)
        )
        
        # Create screen
        screen = Line(UP * 3 + LEFT * 4, UP * 3 + RIGHT * 4, color=WHITE, stroke_width=6)
        screen_label = Text("Screen", font_size=24).next_to(screen, UP, buff=0.2)
        
        # Add sources and screen to scene
        self.play(*[Create(s) for s in sources], Write(source_labels))
        self.wait(0.5)
        self.play(Create(screen), Write(screen_label))
        self.wait(0.5)
        
        # Show wave overlap to demonstrate interference
        explanation1 = Text("Waves from both sources overlap", font_size=22).to_edge(DOWN)
        self.play(Write(explanation1))
        
        # Create multiple wave fronts that remain visible to show interference
        all_waves = VGroup()
        num_wavefronts = 6
        
        for i in range(num_wavefronts):
            # Waves from source 1 (blue)
            wave1 = Circle(
                radius=0.3 + i * 0.9,
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.6
            ).move_to(sources[0].get_center())
            
            # Waves from source 2 (green)
            wave2 = Circle(
                radius=0.3 + i * 0.9,
                color=GREEN,
                stroke_width=2,
                stroke_opacity=0.6
            ).move_to(sources[1].get_center())
            
            all_waves.add(wave1, wave2)
        
        # Show all wave fronts simultaneously
        self.play(LaggedStart(*[Create(w) for w in all_waves], lag_ratio=0.15), run_time=3)
        self.wait(1)
        
        # DETAILED WAVE SUPERPOSITION DEMONSTRATION
        # Fade out everything except sources and screen
        self.play(
            FadeOut(all_waves),
            FadeOut(explanation1),
            FadeOut(source_labels),
            FadeOut(screen_label)
        )
        
        # Create a close-up demonstration area
        demo_title = Text("Wave Superposition", font_size=32).to_edge(UP)
        self.play(Write(demo_title))
        
        # Show wave profiles side by side
        wave_demo_area = Rectangle(width=7, height=3, color=WHITE).shift(LEFT * 0.5)
        self.play(Create(wave_demo_area))
        
        # Create sine wave representations with visible crests and troughs
        ax_left = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3,
            y_length=2,
            axis_config={"include_tip": False, "stroke_width": 1},
        ).shift(LEFT * 3.5 + UP * 0.3)
        
        # Wave 1 from source S1 (Blue)
        wave1_func = ax_left.plot(lambda x: np.sin(2 * PI * x), color=BLUE, stroke_width=3)
        wave1_label = Text("Wave from S1", font_size=18, color=BLUE).next_to(ax_left, UP, buff=0.2)
        
        # Mark crest and trough
        crest1 = Dot(ax_left.c2p(0.25, 1), color=RED, radius=0.08)
        crest1_label = Text("Crest", font_size=14, color=RED).next_to(crest1, UP, buff=0.1)
        trough1 = Dot(ax_left.c2p(0.75, -1), color=BLUE_E, radius=0.08)
        trough1_label = Text("Trough", font_size=14, color=BLUE_E).next_to(trough1, DOWN, buff=0.1)
        
        self.play(Create(ax_left), Create(wave1_func), Write(wave1_label))
        self.play(GrowFromCenter(crest1), Write(crest1_label))
        self.play(GrowFromCenter(trough1), Write(trough1_label))
        self.wait(1)
        
        # Wave 2 from source S2 (Green)
        ax_right = Axes(
            x_range=[0, 4, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=3,
            y_length=2,
            axis_config={"include_tip": False, "stroke_width": 1},
        ).shift(RIGHT * 2.5 + UP * 0.3)
        
        wave2_func = ax_right.plot(lambda x: np.sin(2 * PI * x), color=GREEN, stroke_width=3)
        wave2_label = Text("Wave from S2", font_size=18, color=GREEN).next_to(ax_right, UP, buff=0.2)
        
        crest2 = Dot(ax_right.c2p(0.25, 1), color=RED, radius=0.08)
        trough2 = Dot(ax_right.c2p(0.75, -1), color=BLUE_E, radius=0.08)
        
        self.play(Create(ax_right), Create(wave2_func), Write(wave2_label))
        self.play(GrowFromCenter(crest2), GrowFromCenter(trough2))
        self.wait(1)
        
        # Show CONSTRUCTIVE interference (crest + crest)
        construct_label = Text("CONSTRUCTIVE INTERFERENCE", font_size=22, color=RED).to_edge(DOWN).shift(UP * 0.3)
        construct_desc = Text("Crest + Crest = BRIGHT", font_size=18).next_to(construct_label, DOWN)
        self.play(Write(construct_label), Write(construct_desc))
        
        # Highlight crests meeting
        self.play(
            crest1.animate.set_color(YELLOW).scale(1.5),
            crest2.animate.set_color(YELLOW).scale(1.5),
        )
        
        # Show result: larger amplitude
        result_ax = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=3,
            y_length=2.5,
            axis_config={"include_tip": False, "stroke_width": 1},
        ).shift(DOWN * 2)
        
        result_wave1 = result_ax.plot(lambda x: 2 * np.sin(2 * PI * x), color=YELLOW, stroke_width=4)
        result_label1 = Text("Sum = 2× Amplitude", font_size=18, color=YELLOW).next_to(result_ax, DOWN, buff=0.2)
        plus_sign = Text("+", font_size=30).move_to(UP * 0.3)
        equals_sign = Text("=", font_size=30).next_to(result_ax, UP, buff=0.3)
        
        self.play(Write(plus_sign))
        self.play(Write(equals_sign), Create(result_ax), Create(result_wave1), Write(result_label1))
        self.wait(2)
        
        # Clear for destructive interference
        self.play(
            *[FadeOut(mob) for mob in [
                crest1, crest2, trough1, trough2, crest1_label, trough1_label,
                result_ax, result_wave1, result_label1, plus_sign, equals_sign,
                construct_label, construct_desc
            ]]
        )
        
        # Show DESTRUCTIVE interference (crest + trough)
        destruct_label = Text("DESTRUCTIVE INTERFERENCE", font_size=22, color=BLUE_E).to_edge(DOWN).shift(UP * 0.3)
        destruct_desc = Text("Crest + Trough = DARK (Cancel Out)", font_size=18).next_to(destruct_label, DOWN)
        self.play(Write(destruct_label), Write(destruct_desc))
        
        # Shift wave 2 by half wavelength to show out of phase
        wave2_shifted = ax_right.plot(lambda x: np.sin(2 * PI * x + PI), color=GREEN, stroke_width=3)
        crest2_shifted = Dot(ax_right.c2p(0.25, -1), color=BLUE_E, radius=0.08)
        crest2_label = Text("Trough", font_size=14, color=BLUE_E).next_to(crest2_shifted, DOWN, buff=0.1)
        crest1_new = Dot(ax_left.c2p(0.25, 1), color=RED, radius=0.08)
        crest1_label_new = Text("Crest", font_size=14, color=RED).next_to(crest1_new, UP, buff=0.1)
        
        self.play(
            Transform(wave2_func, wave2_shifted),
            GrowFromCenter(crest1_new),
            GrowFromCenter(crest2_shifted),
            Write(crest1_label_new),
            Write(crest2_label)
        )
        
        self.play(
            crest1_new.animate.set_color(PURPLE).scale(1.5),
            crest2_shifted.animate.set_color(PURPLE).scale(1.5),
        )
        
        # Show result: zero amplitude
        result_ax2 = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=3,
            y_length=2.5,
            axis_config={"include_tip": False, "stroke_width": 1},
        ).shift(DOWN * 2)
        
        zero_line = result_ax2.plot(lambda x: 0, color=GRAY, stroke_width=4)
        result_label2 = Text("Sum = 0 (Cancelled)", font_size=18, color=GRAY).next_to(result_ax2, DOWN, buff=0.2)
        plus_sign2 = Text("+", font_size=30).move_to(UP * 0.3)
        equals_sign2 = Text("=", font_size=30).next_to(result_ax2, UP, buff=0.3)
        
        self.play(Write(plus_sign2))
        self.play(Write(equals_sign2), Create(result_ax2), Create(zero_line), Write(result_label2))
        self.wait(2.5)
        
        # Clear demonstration and return to main view
        self.play(
            *[FadeOut(mob) for mob in [
                demo_title, wave_demo_area, ax_left, ax_right, wave1_func, wave2_func,
                wave1_label, wave2_label, result_ax2, zero_line, result_label2,
                plus_sign2, equals_sign2, destruct_label, destruct_desc,
                crest1_new, crest2_shifted, crest1_label_new, crest2_label
            ]]
        )
        
        # Bring back the sources and screen
        self.play(
            Write(source_labels),
            Write(screen_label)
        )
        
        # Recreate wave fronts
        all_waves = VGroup()
        for i in range(num_wavefronts):
            wave1 = Circle(
                radius=0.3 + i * 0.9,
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.6
            ).move_to(sources[0].get_center())
            
            wave2 = Circle(
                radius=0.3 + i * 0.9,
                color=GREEN,
                stroke_width=2,
                stroke_opacity=0.6
            ).move_to(sources[1].get_center())
            
            all_waves.add(wave1, wave2)
        
        self.play(FadeIn(all_waves))
        self.wait(0.5)
        
        # Highlight constructive interference (bright spots)
        explanation2 = Text("Where waves meet IN PHASE → Bright (Constructive)", 
                          font_size=20, color=RED).to_edge(DOWN)
        self.play(Write(explanation2))
        
        # Show some bright spots where constructive interference occurs
        bright_spots = VGroup()
        for i in [-2, 0, 2]:
            spot = Dot(UP * 3 + RIGHT * i * 1.5, color=RED, radius=0.15)
            bright_spots.add(spot)
        
        self.play(LaggedStart(*[GrowFromCenter(spot) for spot in bright_spots], lag_ratio=0.2))
        self.wait(1.5)
        
        # Highlight destructive interference (dark spots)
        self.play(FadeOut(explanation2))
        explanation3 = Text("Where waves meet OUT OF PHASE → Dark (Destructive)", 
                          font_size=20, color=BLUE).to_edge(DOWN)
        self.play(Write(explanation3))
        
        # Show dark spots
        dark_spots = VGroup()
        for i in [-0.75, 0.75]:
            spot = Dot(UP * 3 + RIGHT * i * 2, color=BLUE_E, radius=0.12)
            dark_spots.add(spot)
        
        self.play(LaggedStart(*[GrowFromCenter(spot) for spot in dark_spots], lag_ratio=0.2))
        self.wait(1.5)
        
        # Clear and show full pattern
        self.play(
            FadeOut(all_waves),
            FadeOut(bright_spots),
            FadeOut(dark_spots),
            FadeOut(explanation3)
        )
        
        explanation4 = Text("Complete Interference Pattern", font_size=24).to_edge(DOWN)
        self.play(Write(explanation4))
        
        # Create detailed interference pattern
        points = [screen.point_from_proportion(x/60) for x in range(61)]
        dots = []
        for i, point in enumerate(points):
            # Calculate actual path difference for realistic pattern
            x_pos = point[0]
            
            # Distance from each source to point on screen
            d1 = np.sqrt((x_pos - sources[0].get_center()[0])**2 + 
                        (point[1] - sources[0].get_center()[1])**2)
            d2 = np.sqrt((x_pos - sources[1].get_center()[0])**2 + 
                        (point[1] - sources[1].get_center()[1])**2)
            
            # Path difference determines interference
            path_diff = d1 - d2
            # Intensity based on path difference (wavelength = 0.8 for visible effect)
            intensity = (np.cos(2 * np.pi * path_diff / 0.8) + 1) / 2
            
            if intensity > 0.8:
                dot = Dot(point, color=RED, radius=0.12)
            elif intensity > 0.6:
                dot = Dot(point, color=ORANGE, radius=0.10)
            elif intensity > 0.4:
                dot = Dot(point, color=YELLOW, radius=0.08)
            elif intensity > 0.2:
                dot = Dot(point, color=BLUE, radius=0.06)
            else:
                dot = Dot(point, color=BLUE_E, radius=0.04)
            
            dot.set_opacity(0.3 + intensity * 0.7)
            dots.append(dot)
        
        self.play(LaggedStart(*[GrowFromCenter(dot) for dot in dots], lag_ratio=0.02), run_time=3)
        self.wait(3)

class LightDiffraction(Scene):
    def construct(self):
        # Presenter information (persistent on all slides)
        presenter_info = VGroup(
            Text("Aditya Bhattacharjee", font_size=16, color=GRAY),
            Text("Grade 8 | New Horizon Public School", font_size=14, color=GRAY),
            Text("Indiranagar, Bangalore", font_size=14, color=GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        presenter_info.to_corner(DL, buff=0.3)
        self.add(presenter_info)
        
        # Title
        title = Text("Single-Slit Diffraction", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # INTRODUCTORY SLIDE: What is Diffraction?
        intro_title = Text("What is Diffraction?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(intro_title))
        self.wait(0.5)
        
        # Definition
        definition = VGroup(
            Text("Diffraction is the bending of light waves", font_size=24),
            Text("around obstacles or through narrow openings", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP * 1.5)
        
        self.play(Write(definition[0]))
        self.wait(0.8)
        self.play(Write(definition[1]))
        self.wait(1.5)
        
        # Key points
        key_points = VGroup(
            Text("• Light doesn't always travel in straight lines", font_size=20, color=BLUE),
            Text("• When light passes through a small opening,", font_size=20, color=BLUE),
            Text("  it spreads out instead of staying narrow", font_size=20, color=BLUE),
            Text("• Creates a characteristic pattern on a screen", font_size=20, color=GREEN),
            Text("• Proves light behaves as a wave!", font_size=20, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.8)
        
        self.play(LaggedStart(*[Write(point) for point in key_points], lag_ratio=0.5), run_time=5)
        self.wait(2)
        
        # Example text
        example = Text("Let's see how it happens...", font_size=22, color=ORANGE).to_edge(DOWN).shift(UP * 0.5)
        self.play(Write(example))
        self.wait(1.5)
        
        # Clear intro slide
        self.play(
            *[FadeOut(mob) for mob in [intro_title, definition, key_points, example]]
        )
        self.wait(0.5)
        
        # Create barrier with single slit
        slit_width = 1.2
        barrier_top = Line(
            LEFT * 5 + UP * (slit_width/2),
            LEFT * 5 + UP * 3.5,
            color=GREY,
            stroke_width=12
        )
        barrier_bottom = Line(
            LEFT * 5 + DOWN * (slit_width/2),
            LEFT * 5 + DOWN * 3.5,
            color=GREY,
            stroke_width=12
        )
        
        barrier_label = Text("Single Slit", font_size=20).next_to(barrier_top, LEFT, buff=0.3)
        
        # Create screen
        screen = Line(UP * 3.5 + RIGHT * 4, DOWN * 3.5 + RIGHT * 4, color=WHITE, stroke_width=6)
        screen_label = Text("Screen", font_size=24).next_to(screen, RIGHT, buff=0.2)
        
        # Show barrier and screen
        self.play(Create(barrier_top), Create(barrier_bottom), Write(barrier_label))
        self.wait(0.3)
        self.play(Create(screen), Write(screen_label))
        self.wait(0.5)
        
        # Incoming plane waves
        explanation1 = Text("Incoming plane waves", font_size=22).to_edge(DOWN)
        self.play(Write(explanation1))
        
        incoming_waves = VGroup()
        for i in range(7):
            wave = Line(
                LEFT * 6.5 + UP * (i * 1.0 - 3),
                LEFT * 5.5 + UP * (i * 1.0 - 3),
                color=BLUE,
                stroke_width=2
            )
            incoming_waves.add(wave)
        
        self.play(LaggedStart(*[Create(w) for w in incoming_waves], lag_ratio=0.15), run_time=2)
        self.wait(1)
        
        # Huygens Principle: Each point in slit acts as source
        self.play(FadeOut(explanation1))
        explanation2 = Text("Each point in slit acts as a wave source (Huygens' Principle)", 
                          font_size=18).to_edge(DOWN)
        self.play(Write(explanation2))
        
        # Show point sources within the slit
        num_sources = 5
        slit_sources = VGroup()
        for i in range(num_sources):
            y_pos = (i - (num_sources-1)/2) * slit_width / (num_sources + 1)
            source = Dot(LEFT * 5 + UP * y_pos, color=YELLOW, radius=0.06)
            slit_sources.add(source)
        
        self.play(LaggedStart(*[GrowFromCenter(s) for s in slit_sources], lag_ratio=0.15))
        self.wait(1)
        
        # Show wavelets from each source
        self.play(FadeOut(incoming_waves), FadeOut(explanation2))
        explanation3 = Text("Wavelets spread and interfere", font_size=22).to_edge(DOWN)
        self.play(Write(explanation3))
        
        # Create wavelets from each slit source
        all_wavelets = VGroup()
        for source in slit_sources:
            for i in range(4):
                wavelet = Arc(
                    radius=0.4 + i * 1.5,
                    start_angle=-PI/2.5,
                    angle=PI/1.25,
                    color=interpolate_color(BLUE, GREEN, 
                                          slit_sources.submobjects.index(source) / len(slit_sources)),
                    stroke_width=1.5,
                    stroke_opacity=0.5
                )
                wavelet.move_arc_center_to(source.get_center())
                all_wavelets.add(wavelet)
        
        self.play(
            LaggedStart(*[Create(w) for w in all_wavelets], lag_ratio=0.05),
            run_time=4
        )
        self.wait(1.5)
        
        # Show the resulting wave pattern in space
        self.play(FadeOut(explanation3))
        explanation4 = Text("Interference creates intensity pattern", font_size=22).to_edge(DOWN)
        self.play(Write(explanation4))
        
        # Create wave intensity visualization between slit and screen
        wave_field = VGroup()
        for x in range(20):
            x_pos = -4 + x * 0.4
            for y in range(15):
                y_pos = -3 + y * 0.4
                
                # Calculate interference from all slit sources
                total_amplitude = 0
                for source in slit_sources:
                    dist = np.sqrt((x_pos - source.get_center()[0])**2 + 
                                  (y_pos - source.get_center()[1])**2)
                    # Simple wave equation
                    total_amplitude += np.cos(2 * PI * dist / 1.5)
                
                intensity = (total_amplitude / len(slit_sources) + 1) / 2
                
                if intensity > 0.6:
                    dot = Dot([x_pos, y_pos, 0], radius=0.03, 
                             color=interpolate_color(BLUE, RED, intensity))
                    dot.set_opacity(intensity * 0.4)
                    wave_field.add(dot)
        
        self.play(FadeIn(wave_field, run_time=2))
        self.wait(1.5)
        
        # Fade wave field and show final pattern on screen
        self.play(
            FadeOut(all_wavelets),
            FadeOut(slit_sources),
            FadeOut(wave_field),
            FadeOut(explanation4)
        )
        
        explanation5 = Text("Final Diffraction Pattern on Screen", font_size=24).to_edge(DOWN)
        self.play(Write(explanation5))
        
        # Create detailed intensity pattern on screen
        screen_dots = []
        num_points = 70
        for i in range(num_points):
            y_pos = 3.5 - (7 * i / (num_points - 1))
            
            # Realistic sinc function for single-slit diffraction
            theta = (i - num_points/2) / 8
            if abs(theta) < 0.1:
                intensity = 1.0
            else:
                intensity = abs(np.sin(3 * theta) / (3 * theta)) ** 2
            
            if intensity > 0.05:  # Only show visible points
                dot = Dot(
                    RIGHT * 4 + UP * y_pos,
                    radius=0.03 + intensity * 0.08,
                    color=interpolate_color(BLUE_E, RED, intensity)
                )
                dot.set_opacity(0.4 + intensity * 0.6)
                screen_dots.append(dot)
        
        self.play(LaggedStart(*[FadeIn(d) for d in screen_dots], lag_ratio=0.01), run_time=3)
        
        # Show central maximum label
        central_label = Text("Central Maximum", font_size=16, color=RED).next_to(
            screen, LEFT, buff=0.5
        ).shift(UP * 0.0)
        arrow = Arrow(central_label.get_right(), RIGHT * 4, buff=0.1, color=RED, stroke_width=2)
        
        self.play(Write(central_label), Create(arrow))
        
        # Add formula
        formula = MathTex(
            r"I(\theta) = I_0 \left(\frac{\sin(\beta)}{\beta}\right)^2",
            font_size=28
        ).to_edge(UP)
        self.play(Write(formula))
        
        self.wait(3)

class LightDemo(Scene):
    def construct(self):
        # Create a menu to select which demo to show
        title = Text("Light Physics Demos", font_size=40)
        options = VGroup(
            Text("1. Light Interference", font_size=30, color=BLUE),
            Text("2. Light Diffraction", font_size=30, color=GREEN),
            Text("3. Exit", font_size=30, color=RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(DOWN * 0.5)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(Create(options))
        self.wait(1)
        
        # These would be connected to actual scene transitions in a real implementation
        # For now, we'll just show the first demo
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
