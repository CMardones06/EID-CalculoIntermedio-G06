"""
EID - Calculo Intermedio

Grupo 6 - Integrales Definidas y Área Geométrica
Camila Mardones, Beatriz Martin, Patricio Salazar

"""

from manim import *

class AreasIntegral(Scene):
    def construct(self):

        titulo = Text("Integral definida y area geometrica", font_size=30)
        titulo.to_edge(UP)

        ejes = Axes(
            x_range=[-0.5, 3.5, 1],
            y_range=[-5, 6, 1],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False
        )
        ejes.shift(DOWN * 0.4)

        def funcion(x):
            return x**2 - 4

        grafica = ejes.plot(funcion, x_range=[0, 3], color=BLUE)
        etiqueta = MathTex("f(x)=x^2-4", font_size=32)
        etiqueta.to_corner(UR).shift(DOWN * 0.65)

        self.play(Write(titulo))
        self.play(Create(ejes))
        self.play(Create(grafica), Write(etiqueta))
        self.wait(2)

        punto = Dot(ejes.c2p(2, 0), color=YELLOW)
        marca = MathTex("x=2", color=YELLOW, font_size=27)
        marca.next_to(punto, UP, buff=0.2)
        self.play(FadeIn(punto), Write(marca))
        self.wait(2)

        negativa = ejes.get_area(grafica, x_range=[0, 2], color=RED, opacity=0.5)
        positiva = ejes.get_area(grafica, x_range=[2, 3], color=GREEN, opacity=0.5)

        valor_negativo = MathTex(r"-\frac{16}{3}", color=RED, font_size=30)
        valor_negativo.move_to(ejes.c2p(1, -2.2))
        valor_positivo = MathTex(r"+\frac{7}{3}", color=GREEN, font_size=25)
        valor_positivo.move_to(ejes.c2p(2.6, 1.5))

        self.play(FadeIn(negativa), Write(valor_negativo))
        self.wait(3)
        self.play(FadeIn(positiva), Write(valor_positivo))
        self.wait(3)

        elementos = VGroup(
            ejes, grafica, etiqueta, punto, marca,
            negativa, positiva, valor_negativo, valor_positivo
        )
        self.play(FadeOut(elementos))

        integral = MathTex(r"\int_0^3 (x^2-4)\,dx", font_size=42)
        antiderivada = MathTex(r"=\left[\frac{x^3}{3}-4x\right]_0^3", font_size=40)
        evaluacion = MathTex(r"=(9-12)-0", font_size=40)
        resultado_integral = MathTex(r"=-3", color=YELLOW, font_size=44)
        pasos = VGroup(integral, antiderivada, evaluacion, resultado_integral)
        pasos.arrange(DOWN, buff=0.35)

        self.play(Write(integral))
        self.wait(2)
        self.play(Write(antiderivada))
        self.wait(2)
        self.play(Write(evaluacion))
        self.wait(2)
        self.play(Write(resultado_integral))
        self.wait(3)
        self.play(FadeOut(pasos))

        self.play(FadeIn(elementos))
        self.wait(2)
        self.play(FadeOut(valor_negativo), FadeOut(valor_positivo), FadeOut(marca), FadeOut(punto))

        def valor_absoluto(x):
            return abs(x**2 - 4)

        grafica_nueva = ejes.plot(valor_absoluto, x_range=[0, 3], color=BLUE)
        area_nueva = ejes.get_area(
            grafica_nueva, x_range=[0, 2], color=TEAL, opacity=0.5
        )
        etiqueta_nueva = MathTex(r"y=|x^2-4|", font_size=32)
        etiqueta_nueva.move_to(etiqueta)

        
        explicacion = Text(
        "El valor absoluto convierte los valores negativos en positivos",
        font_size=23
        )
        explicacion.to_edge(DOWN)

        self.play(
            Transform(negativa, area_nueva),
            Transform(grafica, grafica_nueva),
            Transform(etiqueta, etiqueta_nueva),
            Write(explicacion),
            run_time=3
        )

        self.wait(3)

        self.play(FadeOut(explicacion))

        self.play(FadeOut(ejes), FadeOut(grafica), FadeOut(etiqueta),
                  FadeOut(negativa), FadeOut(positiva))

        formula = MathTex(r"A=\int_0^3 |x^2-4|\,dx", font_size=40)
        area_roja = MathTex(r"A_1=\left|-\frac{16}{3}\right|=\frac{16}{3}", font_size=39)
        area_verde = MathTex(r"A_2=\frac{7}{3}", font_size=39)
        suma = MathTex(r"A=\frac{16}{3}+\frac{7}{3}=\frac{23}{3}\approx 7.67",
                       font_size=39, color=TEAL)
        pasos_area = VGroup(formula, area_roja, area_verde, suma)
        pasos_area.arrange(DOWN, buff=0.4)

        self.play(Write(formula))
        self.wait(2)
        self.play(Write(area_roja))
        self.wait(2)
        self.play(Write(area_verde))
        self.wait(2)
        self.play(Write(suma))
        self.wait(3)
        self.play(FadeOut(pasos_area), FadeOut(titulo))

        titulo_final = Text("Comparacion de resultados", font_size=34)
        titulo_final.to_edge(UP)
        lado_izquierdo = VGroup(
            Text("Integral definida", font_size=26),
            MathTex("-3", color=RED, font_size=58)
        )
        lado_izquierdo.arrange(DOWN, buff=0.35).shift(LEFT * 3)
        lado_derecho = VGroup(
            Text("Area geometrica", font_size=26),
            MathTex("7.67", color=GREEN, font_size=58)
        )
        lado_derecho.arrange(DOWN, buff=0.35).shift(RIGHT * 3)
        comparacion = MathTex(r"-3 < 7.67", font_size=40, color=YELLOW)
        comparacion.shift(DOWN * 1.3)
        conclusion = Text("La integral suma aportes con signo", font_size=25)
        conclusion.to_edge(DOWN)

        self.play(Write(titulo_final))
        self.play(FadeIn(lado_izquierdo), FadeIn(lado_derecho))
        self.play(Write(comparacion))
        self.wait(2)
        self.play(Write(conclusion))
        self.wait(4)
