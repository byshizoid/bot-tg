def get_weather_emoji(weather_description):
    """Возвращает эмодзи на основе описания погоды."""
    if "clear" in weather_description:
        return "☀️"  # Солнечно
    elif "cloud" in weather_description:
        return "☁️"  # Облачно
    elif "rain" in weather_description:
        return "🌧️"  # Дождливо
    elif "snow" in weather_description:
        return "❄️"  # Снежно
    else:
        return "🌍"  # Неопределенная погода
