"""Aplicación mínima para la gestión de cobranzas en campo."""


def determinar_prioridad(dias_mora: int, valor_pendiente: float) -> str:
    """Determina la prioridad de una cobranza."""
    if dias_mora >= 60 or valor_pendiente >= 1000:
        return "ALTA"
    if dias_mora >= 30 or valor_pendiente >= 500:
        return "MEDIA"
    return "BAJA"


def main() -> None:
    prioridad = determinar_prioridad(45, 750.00)
    print("Gestión de Cobranzas Dermafreya - Baseline v1.0")
    print(f"Prioridad de la cobranza: {prioridad}")


if __name__ == "__main__":
    main()