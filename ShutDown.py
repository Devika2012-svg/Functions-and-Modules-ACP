def shutdown():

    print("...SHUTTING DOWN IN PROGRESS....")

    apps_closed = input("Are all applications closed? (yes/no): ").strip().lower()
    if apps_closed == "no":
        print("⚠️ Sorry, shut down is not possible. Applications are still open.")
        return
    elif apps_closed != "yes":
        print("😞 Invalid input. Please enter (yes/no) only.")
        return

    files_saved = input("Are all files saved? (yes/no): ").strip().lower()
    if files_saved == "no":
        print("⚠️ Sorry, shut down is not possible. Some files are not saved.")
        return
    elif files_saved != "yes":
        print("😞 Invalid input. Please enter (yes/no) only.")
        return

    download_in_progress = input("Is a download in progress? (yes/no): ").strip().lower()
    if download_in_progress == "yes":
        print("⚠️ Sorry, shut down is not possible. A download is in progress.")
        return
    elif download_in_progress != "no":
        print("😞 Invalid input. Please enter (yes/no) only.")
        return

    software_update = input("Is a software update running? (yes/no): ").strip().lower()
    if software_update == "yes":
        print("⚠️ Sorry, shut down is not possible. A software update is running.")
        return
    elif software_update != "no":
        print("😞 Invalid input. Please enter (yes/no) only.")
        return

    choice = input("All checks passed. Do you want to shut down? (yes/no): ").strip().lower()

    if choice == "yes":
        print("✔️ Shutting down...")
    elif choice == "no":
        print("⛔ Shutdown cancelled.")
    else:
        print("😞 Invalid input.")

shutdown()
