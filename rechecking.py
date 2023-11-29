import uiautomator2 as u2
import time

def check_keywords(device_ip, keywords_file):
    found_keywords = set()  # Set to store found keywords

    while True:  # Keep running the app until manually stopped
        device = u2.connect(device_ip)
        try:
            device.session("com.zhiliaoapp.musically")
            device.sleep(6)
            search = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/gia"]/android.widget.ImageView[2]')
            search.click()
            device.sleep(3)

            with open(keywords_file, "r",encoding="utf-8") as file:
                keywords_to_check = file.read().splitlines()

            for keyword in keywords_to_check:
                try:
                    search_box = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/c8z"]')
                    search_box.set_text(keyword)
                except:
                    search_box = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ck3"]')
                    search_box.set_text(keyword)

                search = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/grr"]')
                search.click()
                device.sleep(4)

                attempts = 5  # Number of attempts to scroll and check for sponsor
                while attempts > 0:
                    sponsor = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ger"]')
                    if sponsor.exists:
                        if keyword not in found_keywords:
                            found_keywords.add(keyword)
                            print("Sponsor Found for the keyword:", keyword)
                            with open("ad_found_keywords.txt", "a") as file:
                                file.write(keyword + "\n")
                        else:
                            print("Duplicate found for the keyword:", keyword)
                        break
                    else:
                        device.swipe(276, 1738, 234, 57)
                        device.sleep(2)
                        attempts -= 1
                else:
                    print("No Sponsor Found for the keyword:", keyword)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Restarting the app...")
            device.app_stop("com.zhiliaoapp.musically")
            time.sleep(5)  # Sleep for a few seconds before restarting
            continue

def main():
    #Running on Emulator 103 colombia-pin-ooamanda1o and TikTok version 28.1.3
    device_ip = "emulator-5760"
    keywords_file = "keywords.txt"
    
    # Clear the existing content of the file and write the heading
    with open("ad_found_keywords.txt", "w") as file:
        file.write("Keywords with sponsors\n")
    
    check_keywords(device_ip, keywords_file)

if __name__ == "__main__":
    main()