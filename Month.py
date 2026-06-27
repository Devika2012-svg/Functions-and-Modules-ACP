import calendar

print("\n🌟 MONTHS OF THE YEAR 🌟")
print("========================")

for i in range(1, 13):
    print(f"🌺 {i}. {calendar.month_name[i]}")

print("========================")
choice = input("\nDo you wish to print the calender of the entire year? (y/n): ").lower()
if choice == "y":
    year = int(input("Enter the year: "))
    print(f"🌟 Calender of {year} 🌟")
    print(calendar.calendar(year))
else:
    print("")
