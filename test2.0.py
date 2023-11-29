import uiautomator2 as u2

def check_keywords(device_ip):
    device = u2.connect(device_ip)
    device.session("com.zhiliaoapp.musically")
    device.sleep(4)
    search = device.xpath('//*[@text="Discover"]')
    search.click()
    device.sleep(3)
    
    with open('my_keyword.txt', 'r') as file:
        keywords = [line.strip() for line in file]

    for keyword in keywords:
        try:
            search_box1 = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/k37"]')
            search_box1.set_text(keyword)
        except:
            search_box2 = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ck3"]')
            search_box2.set_text(keyword)
        device.press("ENTER")
        device.sleep(4)
        for _ in range(2):
            sponser = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/h80"]')
            if sponser.exists:
                print("Sponsor Found for the keyword:", keyword)
                with open("keywords.txt", "a") as file:
                    file.write(keyword + "\n")
                break
            device.swipe(276, 1738, 234, 57)
            device.sleep(2)
        else:
            print("No Sponsor Found for the keyword:", keyword)

def main():
    device_ip = "192.168.1.9:34347"
    check_keywords(device_ip)

if __name__ == "__main__":
    main()

