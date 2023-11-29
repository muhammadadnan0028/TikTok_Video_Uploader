import uiautomator2 as u2


def read_keywords_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines from the file and strip any leading/trailing whitespace
            lines = [line.strip() for line in file.readlines()]

            # Convert the list of lines to a tuple
            keywords_tuple = tuple(lines)

            return keywords_tuple
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None




def check_keywords(device_ip, keywords):
    device = u2.connect(device_ip)
    device.session("com.zhiliaoapp.musically")
    device.sleep(4)
    search = device.xpath('//*[@text="Discover"]')
    search.click()
    device.sleep(3)
    for keyword in keywords:
        try:
            search_box1 = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/k37"]')
            search_box1.set_text(keyword)
        except:
            search_box2 = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ck3"]')
            search_box2.set_text(keyword)
        device.press("ENTER")
        device.sleep(4)
        attempts = 2
        while attempts > 0:
            sponser = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/h80"]')
            if sponser.exists:
                print("Sponsor Found for the keyword:", keyword)
                with open("keywords.txt", "a") as file:
                    file.write(keyword + "\n")
                break  # Exit the loop if sponsor is found
            else:
                # Scroll down
                device.swipe(276, 1738, 234, 57)
                device.sleep(2)  # Wait for the content to load
                attempts -= 1
                if sponser.exists:
                    print("Sponsor Found for the keyword:", keyword)
                    with open("keywords.txt", "a") as file:
                        file.write(keyword + "\n")
                    break  # Exit the loop if sponsor is found
        else:
            print("No Sponsor Found for the keyword:",keyword)




def main():

    device_Ip = "192.168.1.9:34347"
    
    file_path = 'keywords.txt'  # Replace with the path to your file
    keywords = read_keywords_from_file(file_path)
    check_keywords(device_Ip, keywords)

if __name__ == "__main__":
    main()

