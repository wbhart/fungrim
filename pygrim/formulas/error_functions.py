# -*- coding: utf-8 -*-

from ..expr import *

def_Topic(
    Title("Error functions"),
    Section("Definitions"),
    Entries(
        "e46223",
        "7375c0",
        "d2914b",
    ),
    Section("Illustrations"),
    Entries(
        "3be335",
    ),
    Section("Integral representations"),
    Entries(
        "2aaba8",
        "36ef64",
        "622772",
    ),
    Section("Connection formulas"),
    Entries(
        "7f355d",
        "bfc86e",
        "01440f",
    ),
    Section("Functional equations"),
    Entries(
        "94db18",
        "603a49",
        "ec0205",
    ),
    Section("Hypergeometric representations"),
    Entries(
        "abadc7",
        "98688d",
        "cb93ea",
        "ae3110",
    ),
    Section("Derivatives"),
    Entries(
        "b5bd5d",
        "fae9d3",
    ),
)

make_entry(ID("e46223"),
    SymbolDefinition(Erf, Erf(z), "Error function"))

make_entry(ID("7375c0"),
    SymbolDefinition(Erfc, Erfc(z), "Complementary error function"))

make_entry(ID("d2914b"),
    SymbolDefinition(Erfi, Erfi(z), "Imaginary error function"))

make_entry(ID("3be335"),
    Image(Description("X-ray of", Erf(z), "on", Element(z, ClosedInterval(-4,4) + ClosedInterval(-4,4)*ConstI)),
        ImageSource("xray_erf")),
    description_xray,
    )

make_entry(ID("2aaba8"),
    Formula(Equal(Erf(z), 2/Sqrt(ConstPi) * Integral(Exp(-(t**2)), For(t, 0, z)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("36ef64"),
    Formula(Equal(Erfc(z), 2/Sqrt(ConstPi) * Integral(Exp(-(t**2)), For(t, z, Infinity)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("622772"),
    Formula(Equal(Erfi(z), 2/Sqrt(ConstPi) * Integral(Exp(t**2), For(t, 0, z)))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("94db18"),
    Formula(Equal(Erf(-z), -Erf(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("ec0205"),
    Formula(Equal(Erfc(-z), 2-Erfc(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("603a49"),
    Formula(Equal(Erfi(-z), -Erfi(z))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("abadc7"),
    Formula(Equal(Erf(z), (2*z)/Sqrt(ConstPi) * Hypergeometric1F1(Div(1,2), Div(3,2), -(z**2)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("98688d"),
    Formula(Equal(Erf(z), (2*z*Exp(-(z**2)))/Sqrt(ConstPi) * Hypergeometric1F1(1, Div(3,2), z**2))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("cb93ea"),
    Formula(Equal(Erf(z), z/Sqrt(z**2) - Exp(-(z**2))/(z*Sqrt(ConstPi)) * HypergeometricUStar(Div(1,2), Div(1,2), z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), Unequal(z, 0))))

make_entry(ID("ae3110"),
    Formula(Equal(Erfc(z), Exp(-(z**2))/(z*Sqrt(ConstPi)) * HypergeometricUStar(Div(1,2), Div(1,2), z**2))),
    Variables(z),
    Assumptions(And(Element(z, CC), Greater(Re(z), 0))))


make_entry(ID("7f355d"),
    Formula(Equal(Erf(z) + Erfc(z), 1)),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("bfc86e"),
    Formula(Equal(Erfc(z), 1 - Erf(z))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("01440f"),
    Formula(Equal(Erfi(z), -(ConstI*Erf(ConstI*z)))),
    Variables(z),
    Assumptions(Element(z, CC)))


make_entry(ID("b5bd5d"),
    Formula(Equal(ComplexDerivative(Erf(z), For(z, z, 1)), 2/Sqrt(ConstPi) * Exp(-(z**2)))),
    Variables(z),
    Assumptions(Element(z, CC)))

make_entry(ID("fae9d3"),
    Formula(Equal(ComplexDerivative(Erf(z), For(z, z, n)), 2/Sqrt(ConstPi) * (-1)**(n+1) * HermitePolynomial(n-1, z) * Exp(-(z**2)))),
    Variables(z, n),
    Assumptions(And(Element(z, CC), Element(n, ZZGreaterEqual(1)))))

