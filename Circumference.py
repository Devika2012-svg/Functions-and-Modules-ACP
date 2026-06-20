print("📐 Welcome to the Circle Calculator! 📐")

def calculate_circumference(radius):
    return 2 * 3.14 * radius

while True:

    radius = float(input("\n🔵 Enter the radius of your circle: "))    

    circumference = calculate_circumference(radius)

    print("✨ - Results - ✨")
    print(f"📏 The circumference of your circle is: {circumference:.2f}")

    again = input("🎉 Do you wish to use it again?! (y/n) 🎉 ").lower()

    if again == "n":
        print("🏁 The program has successfully ended!")
        break
