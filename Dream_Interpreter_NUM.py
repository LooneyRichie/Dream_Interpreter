from datetime import datetime

def calculate_life_path_number(month, day, year):
    """
    Calculate the Life Path Number by summing the digits of the birthdate
    until a single digit is obtained.
    """
    def reduce_to_single_digit(num):
        while num > 9 and num != 11 and num != 22 and num != 33:  # Master numbers are exceptions
            num = sum(int(digit) for digit in str(num))
        return num

    total = sum(int(digit) for digit in f"{month}{day}{year}")
    return reduce_to_single_digit(total)

def calculate_destiny_number(full_name):
    """
    Calculate the Destiny Number by summing the numerical values of the letters
    in the full name and reducing to a single digit or master number.
    """
    def letter_to_number(letter):
        return ord(letter.upper()) - ord('A') + 1

    total = sum(letter_to_number(char) for char in full_name if char.isalpha())
    return calculate_life_path_number(0, 0, total)  # Reuse the reduce function

def calculate_soul_urge_number(full_name):
    """
    Calculate the Soul Urge Number by summing the numerical values of the vowels
    in the full name and reducing to a single digit or master number.
    """
    vowels = "AEIOU"
    def letter_to_number(letter):
        return ord(letter.upper()) - ord('A') + 1

    total = sum(letter_to_number(char) for char in full_name if char.upper() in vowels)
    return calculate_life_path_number(0, 0, total)  # Reuse the reduce function

def numerology_chart(month, day, year, full_name):
    life_path_number = calculate_life_path_number(month, day, year)
    destiny_number = calculate_destiny_number(full_name)
    soul_urge_number = calculate_soul_urge_number(full_name)

    print(f"Your Life Path Number is: {life_path_number}")
    print(f"Your Destiny Number is: {destiny_number}")
    print(f"Your Soul Urge Number is: {soul_urge_number}")
    print("\nNumerology Chart:")

    # Life Path Number descriptions
    if life_path_number == 1:
        print("1: Leader, independent, and ambitious.")
        print("   You are a natural-born leader with a strong sense of individuality. "
              "You thrive when taking charge and pursuing your goals.")
    elif life_path_number == 2:
        print("2: Diplomatic, sensitive, and cooperative.")
        print("   You are a peacemaker who values harmony and relationships. "
              "Your empathy and ability to work with others make you a great mediator.")
    elif life_path_number == 3:
        print("3: Creative, expressive, and optimistic.")
        print("   You are full of creative energy and love to express yourself. "
              "Your optimism and charisma inspire those around you.")
    elif life_path_number == 4:
        print("4: Practical, disciplined, and hardworking.")
        print("   You are grounded and reliable, with a strong work ethic. "
              "You excel at building solid foundations for long-term success.")
    elif life_path_number == 5:
        print("5: Adventurous, dynamic, and freedom-loving.")
        print("   You crave freedom and new experiences. "
              "Your adventurous spirit drives you to explore and embrace change.")
    elif life_path_number == 6:
        print("6: Caring, responsible, and family-oriented.")
        print("   You are a nurturer who values family and community. "
              "Your sense of responsibility and compassion make you a natural caregiver.")
    elif life_path_number == 7:
        print("7: Analytical, spiritual, and introspective.")
        print("   You are a seeker of truth and knowledge. "
              "Your introspective nature leads you to explore the deeper meanings of life.")
    elif life_path_number == 8:
        print("8: Ambitious, authoritative, and goal-oriented.")
        print("   You are driven by success and have a strong sense of authority. "
              "Your determination and leadership skills help you achieve your goals.")
    elif life_path_number == 9:
        print("9: Compassionate, humanitarian, and idealistic.")
        print("   You are a visionary who cares deeply about the world. "
              "Your compassion and idealism inspire you to help others and make a difference.")
    elif life_path_number == 11:
        print("11: Intuitive, visionary, and inspiring (Master Number).")
        print("   You possess heightened intuition and spiritual insight. "
              "Your visionary ideas and ability to inspire others make you a natural leader.")
    elif life_path_number == 22:
        print("22: Master builder, practical, and visionary (Master Number).")
        print("   You have the ability to turn dreams into reality. "
              "Your practical skills and visionary mindset allow you to achieve great things.")
    elif life_path_number == 33:
        print("33: Master teacher, compassionate, and spiritually uplifting (Master Number).")
        print("   You are a beacon of love and compassion. "
              "Your spiritual wisdom and ability to uplift others make you a true teacher.")
    else:
        print("Unknown Life Path Number.")

    # Destiny Number descriptions
    print("\nDestiny Number Descriptions:")
    if destiny_number == 1:
        print("1: You are destined to lead and inspire others with your determination and vision.")
    elif destiny_number == 2:
        print("2: You are destined to bring peace and harmony to the world through cooperation and diplomacy.")
    elif destiny_number == 3:
        print("3: You are destined to bring joy and creativity to the world through your talents.")
    elif destiny_number == 4:
        print("4: You are destined to build a strong foundation in life through discipline and hard work.")
    elif destiny_number == 5:
        print("5: You are destined to embrace freedom and change, inspiring others with your adventurous spirit.")
    elif destiny_number == 6:
        print("6: You are destined to nurture and care for others, creating harmony in your community.")
    elif destiny_number == 7:
        print("7: You are destined to seek knowledge and spiritual understanding, guiding others with your wisdom.")
    elif destiny_number == 8:
        print("8: You are destined to achieve material success and lead others with your ambition and authority.")
    elif destiny_number == 9:
        print("9: You are destined to serve humanity with compassion and make a positive impact on the world.")
    elif destiny_number == 11:
        print("11: You are destined to inspire others with your intuition and visionary ideas (Master Number).")
    elif destiny_number == 22:
        print("22: You are destined to turn dreams into reality and create lasting achievements (Master Number).")
    elif destiny_number == 33:
        print("33: You are destined to uplift others with your compassion and spiritual wisdom (Master Number).")
    else:
        print("Unknown Destiny Number.")

    # Soul Urge Number descriptions
    print("\nSoul Urge Number Descriptions:")
    if soul_urge_number == 1:
        print("1: Your soul craves independence and the freedom to express your individuality.")
    elif soul_urge_number == 2:
        print("2: Your soul seeks harmony and meaningful connections with others.")
    elif soul_urge_number == 3:
        print("3: Your soul desires creative expression and the joy of sharing your talents.")
    elif soul_urge_number == 4:
        print("4: Your soul yearns for stability, order, and a sense of purpose.")
    elif soul_urge_number == 5:
        print("5: Your soul craves freedom, adventure, and the thrill of new experiences.")
    elif soul_urge_number == 6:
        print("6: Your soul seeks love, harmony, and the opportunity to care for others.")
    elif soul_urge_number == 7:
        print("7: Your soul desires spiritual growth, introspection, and deeper understanding.")
    elif soul_urge_number == 8:
        print("8: Your soul craves success, power, and the ability to make a difference.")
    elif soul_urge_number == 9:
        print("9: Your soul seeks to serve humanity and make the world a better place.")
    elif soul_urge_number == 11:
        print("11: Your soul desires to inspire others with your intuition and spiritual insight (Master Number).")
    elif soul_urge_number == 22:
        print("22: Your soul craves the ability to create lasting achievements and make a global impact (Master Number).")
    elif soul_urge_number == 33:
        print("33: Your soul seeks to uplift others with love, compassion, and spiritual wisdom (Master Number).")
    else:
        print("Unknown Soul Urge Number.")

def main():
    print("Welcome to the Numerology Chart Generator!")
    birthdate = input("Enter your birthdate (mm dd yyyy): ")
    full_name = input("Enter your full name: ")
    try:
        # Validate the date format and check if it's a valid date
        valid_date = datetime.strptime(birthdate, "%m %d %Y")
        month, day, year = valid_date.month, valid_date.day, valid_date.year
        numerology_chart(month, day, year, full_name)
    except ValueError:
        print("Invalid input. Please enter a valid date in the format mm dd yyyy.")

if __name__ == "__main__":
    main()
