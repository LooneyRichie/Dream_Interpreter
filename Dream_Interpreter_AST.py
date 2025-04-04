import swisseph as swe
from datetime import datetime
from geopy.geocoders import Nominatim
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            print("Form submitted")  # Debugging log
            birth_date = request.form["birth_date"]
            hour = int(request.form["hour"])
            minute = int(request.form["minute"])
            city = request.form["city"]
            country = request.form["country"]

            print(f"Received data: {birth_date}, {hour}:{minute}, {city}, {country}")  # Debugging log

            # Parse the birth date
            month, day, year = map(int, birth_date.split())
            birth_datetime = datetime(year, month, day, hour, minute)

            # Get coordinates
            latitude, longitude = get_coordinates(city, country)
            print(f"Coordinates: {latitude}, {longitude}")  # Debugging log

            # Calculate natal chart
            result = calculate_natal_chart(birth_datetime, latitude, longitude)
            print(f"Natal chart result: {result}")  # Debugging log

            return render_template("result.html", result=result)
        except Exception as e:
            print(f"Error occurred: {e}")  # Log the error to the console
            return render_template("index.html", error=str(e))
    return render_template("index.html")

def get_user_input():
    print("Enter your birth details (MM DD YYYY):")
    birth_date = input("Birthdate (e.g., 12 25 1990): ")
    month, day, year = map(int, birth_date.split())
    hour = int(input("Hour (0-23): "))
    minute = int(input("Minute (0-59): "))
    city = input("City of birth: ")
    country = input("Country of birth: ")
    return datetime(year, month, day, hour, minute), city, country

def get_coordinates(city, country):
    geolocator = Nominatim(user_agent="natal_chart_calculator")
    try:
        location = geolocator.geocode(f"{city}, {country}")
        if location:
            return location.latitude, location.longitude
        else:
            raise ValueError("Location not found")
    except Exception as e:
        print(f"Error in get_coordinates: {e}")  # Log the error
        raise ValueError("Could not find the location. Please check the city and country names.")

# Add Venus sign details
venus_sign_details = {
    "Aries": "You express love boldly and passionately. You value excitement and spontaneity in relationships.",
    "Taurus": "You express love steadily and sensually. You value stability, comfort, and physical affection.",
    "Gemini": "You express love playfully and intellectually. You value communication and mental stimulation in relationships.",
    "Cancer": "You express love emotionally and protectively. You value deep emotional connections and nurturing relationships.",
    "Leo": "You express love dramatically and generously. You value admiration, loyalty, and grand gestures in relationships.",
    "Virgo": "You express love practically and thoughtfully. You value acts of service and attention to detail in relationships.",
    "Libra": "You express love harmoniously and romantically. You value balance, beauty, and partnership in relationships.",
    "Scorpio": "You express love intensely and passionately. You value deep emotional bonds and transformative relationships.",
    "Sagittarius": "You express love adventurously and optimistically. You value freedom, exploration, and shared experiences in relationships.",
    "Capricorn": "You express love responsibly and traditionally. You value commitment, stability, and long-term goals in relationships.",
    "Aquarius": "You express love uniquely and independently. You value intellectual connection and individuality in relationships.",
    "Pisces": "You express love compassionately and dreamily. You value emotional depth, creativity, and spiritual connection in relationships."
}

# Add Mars sign details
mars_sign_details = {
    "Aries": "You are assertive, energetic, and bold. You take initiative and thrive in competitive situations.",
    "Taurus": "You are steady, determined, and patient. You pursue your goals with persistence and practicality.",
    "Gemini": "You are curious, adaptable, and quick-witted. You channel your energy into communication and learning.",
    "Cancer": "You are protective, emotional, and tenacious. You fight for what you care about and value security.",
    "Leo": "You are confident, passionate, and dramatic. You pursue your goals with creativity and enthusiasm.",
    "Virgo": "You are analytical, precise, and hardworking. You focus your energy on improving and organizing.",
    "Libra": "You are diplomatic, charming, and cooperative. You prefer to take action in a balanced and fair way.",
    "Scorpio": "You are intense, determined, and resourceful. You channel your energy into transformation and deep focus.",
    "Sagittarius": "You are adventurous, optimistic, and enthusiastic. You pursue your goals with freedom and exploration.",
    "Capricorn": "You are disciplined, ambitious, and practical. You focus your energy on long-term achievements.",
    "Aquarius": "You are innovative, independent, and unconventional. You channel your energy into unique and humanitarian causes.",
    "Pisces": "You are compassionate, intuitive, and creative. You pursue your goals with imagination and emotional depth."
}

# Add Jupiter sign details
jupiter_sign_details = {
    "Aries": "You are optimistic and enthusiastic about taking bold actions. You grow through courage and leadership.",
    "Taurus": "You find growth and abundance through stability, patience, and appreciating the finer things in life.",
    "Gemini": "You expand your horizons through learning, communication, and intellectual curiosity.",
    "Cancer": "You grow through emotional connections, nurturing others, and creating a sense of security.",
    "Leo": "You find joy and growth through creativity, self-expression, and inspiring others.",
    "Virgo": "You grow through service, attention to detail, and improving yourself and the world around you.",
    "Libra": "You expand your life through relationships, harmony, and seeking balance in all areas.",
    "Scorpio": "You grow through transformation, deep emotional connections, and uncovering hidden truths.",
    "Sagittarius": "You thrive on adventure, exploration, and expanding your philosophical and spiritual beliefs.",
    "Capricorn": "You grow through discipline, ambition, and achieving long-term goals.",
    "Aquarius": "You expand your horizons through innovation, independence, and contributing to humanitarian causes.",
    "Pisces": "You grow through compassion, spirituality, and connecting with your imagination and intuition."
}

# Add Saturn sign details
saturn_sign_details = {
    "Aries": "You learn discipline and responsibility through taking initiative and developing courage.",
    "Taurus": "You grow through patience, persistence, and building a stable foundation for your life.",
    "Gemini": "You learn to focus your thoughts and communication, developing mental discipline and adaptability.",
    "Cancer": "You grow through emotional maturity, nurturing others, and creating a secure home environment.",
    "Leo": "You learn to balance self-expression with responsibility, developing confidence and leadership skills.",
    "Virgo": "You grow through hard work, attention to detail, and serving others in practical ways.",
    "Libra": "You learn to create balance and harmony in relationships, developing fairness and cooperation.",
    "Scorpio": "You grow through transformation, emotional depth, and learning to let go of control.",
    "Sagittarius": "You learn to balance freedom with responsibility, growing through philosophical and spiritual discipline.",
    "Capricorn": "You grow through ambition, discipline, and achieving long-term goals with perseverance.",
    "Aquarius": "You learn to balance individuality with responsibility, growing through innovation and humanitarian efforts.",
    "Pisces": "You grow through spiritual discipline, compassion, and learning to trust your intuition."
}

# Add Uranus sign details
uranus_sign_details = {
    "Aries": "You bring innovation and boldness to new ideas and actions. You thrive on independence and pioneering change.",
    "Taurus": "You revolutionize stability and material values. You bring innovation to finances, comfort, and traditions.",
    "Gemini": "You innovate through communication, learning, and intellectual pursuits. You thrive on curiosity and adaptability.",
    "Cancer": "You bring change to family, home, and emotional security. You innovate in nurturing and creating emotional bonds.",
    "Leo": "You express creativity and individuality in bold and unique ways. You thrive on inspiring others through innovation.",
    "Virgo": "You bring innovation to work, health, and service. You thrive on improving systems and creating practical solutions.",
    "Libra": "You revolutionize relationships, balance, and harmony. You bring innovation to partnerships and social justice.",
    "Scorpio": "You transform through deep emotional and psychological change. You bring innovation to power and transformation.",
    "Sagittarius": "You bring innovation to philosophy, travel, and higher learning. You thrive on exploring new ideas and beliefs.",
    "Capricorn": "You revolutionize structures, authority, and discipline. You bring innovation to long-term goals and traditions.",
    "Aquarius": "You embody innovation, independence, and humanitarian ideals. You thrive on creating a better future for all.",
    "Pisces": "You bring innovation to spirituality, creativity, and compassion. You thrive on connecting with the collective unconscious."
}

# Add Neptune sign details
neptune_sign_details = {
    "Aries": "You dream of bold new beginnings and thrive on pioneering spiritual and creative paths.",
    "Taurus": "You find inspiration in stability, beauty, and the material world. You dream of creating lasting comfort.",
    "Gemini": "You are inspired by communication, learning, and intellectual exploration. You dream of connecting ideas and people.",
    "Cancer": "You dream of emotional security and nurturing connections. You are deeply inspired by family and home.",
    "Leo": "You are inspired by creativity, self-expression, and recognition. You dream of leaving a lasting legacy.",
    "Virgo": "You find inspiration in service, practicality, and improving the world. You dream of creating order and healing.",
    "Libra": "You dream of harmony, balance, and beauty. You are inspired by relationships and social justice.",
    "Scorpio": "You are inspired by transformation, emotional depth, and uncovering hidden truths. You dream of profound change.",
    "Sagittarius": "You dream of adventure, exploration, and expanding your spiritual and philosophical horizons.",
    "Capricorn": "You are inspired by discipline, ambition, and achieving long-term goals. You dream of building a lasting legacy.",
    "Aquarius": "You dream of innovation, independence, and humanitarian ideals. You are inspired by creating a better future.",
    "Pisces": "You are deeply inspired by compassion, spirituality, and creativity. You dream of connecting with the collective unconscious."
}

# Add Pluto sign details
pluto_sign_details = {
    "Aries": "You transform through bold actions and pioneering change. You thrive on initiating new beginnings.",
    "Taurus": "You transform through stability, material values, and persistence. You thrive on creating lasting security.",
    "Gemini": "You transform through communication, learning, and adaptability. You thrive on exchanging ideas and knowledge.",
    "Cancer": "You transform through emotional depth, family, and nurturing connections. You thrive on creating emotional security.",
    "Leo": "You transform through creativity, self-expression, and leadership. You thrive on inspiring others and leaving a legacy.",
    "Virgo": "You transform through service, practicality, and attention to detail. You thrive on improving systems and healing.",
    "Libra": "You transform through relationships, balance, and harmony. You thrive on creating fairness and justice.",
    "Scorpio": "You transform through intensity, emotional depth, and uncovering hidden truths. You thrive on profound change.",
    "Sagittarius": "You transform through exploration, philosophy, and spiritual growth. You thrive on expanding your horizons.",
    "Capricorn": "You transform through discipline, ambition, and achieving long-term goals. You thrive on building a lasting legacy.",
    "Aquarius": "You transform through innovation, independence, and humanitarian efforts. You thrive on creating a better future.",
    "Pisces": "You transform through spirituality, compassion, and creativity. You thrive on connecting with the collective unconscious."
}

# Corrected Sun sign details
sun_sign_details = {
    "Aries": "You are bold, energetic, and pioneering. You thrive on taking initiative and being a leader.",
    "Taurus": "You are steady, reliable, and value comfort. You thrive on stability and material security.",
    "Gemini": "You are curious, adaptable, and communicative. You thrive on learning and sharing ideas.",
    "Cancer": "You are nurturing, emotional, and protective. You thrive on creating a sense of home and security.",
    "Leo": "You are confident, creative, and charismatic. You thrive on self-expression and inspiring others.",
    "Virgo": "You are analytical, practical, and detail-oriented. You thrive on helping others and improving systems.",
    "Libra": "You are diplomatic, charming, and value harmony. You thrive on relationships and creating balance.",
    "Scorpio": "You are intense, passionate, and transformative. You thrive on deep emotional connections.",
    "Sagittarius": "You are adventurous, optimistic, and philosophical. You thrive on exploring new ideas and places.",
    "Capricorn": "You are disciplined, ambitious, and practical. You thrive on achieving long-term goals.",
    "Aquarius": "You are innovative, independent, and humanitarian. You thrive on creating a better future.",
    "Pisces": "You are compassionate, intuitive, and creative. You thrive on connecting with the collective unconscious."
}

# Add Moon sign details
moon_sign_details = {
    "Aries": "You are emotionally bold and spontaneous. You thrive on excitement and independence.",
    "Taurus": "You are emotionally steady and value comfort. You thrive on security and physical affection.",
    "Gemini": "You are emotionally curious and communicative. You thrive on mental stimulation and variety.",
    "Cancer": "You are deeply emotional and nurturing. You thrive on creating a sense of home and belonging.",
    "Leo": "You are emotionally expressive and dramatic. You thrive on admiration and loyalty.",
    "Virgo": "You are emotionally practical and detail-oriented. You thrive on helping others and being useful.",
    "Libra": "You are emotionally balanced and value harmony. You thrive on relationships and beauty.",
    "Scorpio": "You are emotionally intense and transformative. You thrive on deep emotional connections.",
    "Sagittarius": "You are emotionally adventurous and optimistic. You thrive on freedom and exploration.",
    "Capricorn": "You are emotionally disciplined and practical. You thrive on achieving stability and goals.",
    "Aquarius": "You are emotionally independent and innovative. You thrive on intellectual connections.",
    "Pisces": "You are emotionally compassionate and intuitive. You thrive on creativity and spirituality."
}

# Add Mercury sign details
mercury_sign_details = {
    "Aries": "You think and communicate boldly and directly. You thrive on quick decisions and action.",
    "Taurus": "You think and communicate steadily and practically. You thrive on clear and reliable information.",
    "Gemini": "You think and communicate quickly and adaptively. You thrive on learning and sharing ideas.",
    "Cancer": "You think and communicate emotionally and intuitively. You thrive on nurturing and protecting others.",
    "Leo": "You think and communicate creatively and confidently. You thrive on inspiring and leading others.",
    "Virgo": "You think and communicate analytically and precisely. You thrive on solving problems and organizing.",
    "Libra": "You think and communicate diplomatically and harmoniously. You thrive on creating balance and fairness.",
    "Scorpio": "You think and communicate intensely and deeply. You thrive on uncovering hidden truths.",
    "Sagittarius": "You think and communicate optimistically and philosophically. You thrive on exploring new ideas.",
    "Capricorn": "You think and communicate practically and ambitiously. You thrive on achieving long-term goals.",
    "Aquarius": "You think and communicate innovatively and independently. You thrive on unique and humanitarian ideas.",
    "Pisces": "You think and communicate intuitively and compassionately. You thrive on creativity and spirituality."
}

# Ensure the planet_details dictionary includes all corrected details
planet_details = {
    "Sun": sun_sign_details,
    "Moon": moon_sign_details,
    "Mercury": mercury_sign_details,
    "Venus": venus_sign_details,
    "Mars": mars_sign_details,
    "Jupiter": jupiter_sign_details,
    "Saturn": saturn_sign_details,
    "Uranus": uranus_sign_details,
    "Neptune": neptune_sign_details,
    "Pluto": pluto_sign_details
}

def calculate_natal_chart(birth_datetime, latitude, longitude):
    try:
        # Convert datetime to Julian Day
        julian_day = swe.julday(
            birth_datetime.year,
            birth_datetime.month,
            birth_datetime.day,
            birth_datetime.hour + birth_datetime.minute / 60.0
        )

        # List of planets to calculate
        planets = [
            swe.SUN, swe.MOON, swe.MERCURY, swe.VENUS, swe.MARS,
            swe.JUPITER, swe.SATURN, swe.URANUS, swe.NEPTUNE, swe.PLUTO
        ]
        planet_names = [
            "Sun", "Moon", "Mercury", "Venus", "Mars",
            "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"
        ]

        # Zodiac signs
        zodiac_signs = [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ]

        result = []
        for i, planet in enumerate(planets):
            position, _ = swe.calc_ut(julian_day, planet)
            degree = position[0]
            sign_index = int(degree // 30)
            sign = zodiac_signs[sign_index]
            planet_name = planet_names[i]

            # Add basic planet position
            result.append(f"{planet_name}: {degree:.2f}° in {sign}")

            # Add detailed information if available
            if planet_name in planet_details:
                details = planet_details[planet_name].get(sign, "No details available.")
                result.append(f"  - {details}")

        return "\n".join(result)
    except Exception as e:
        print(f"Error in calculate_natal_chart: {e}")  # Log the error
        raise ValueError("Error calculating natal chart.")

if __name__ == "__main__":
    app.run(debug=True)
