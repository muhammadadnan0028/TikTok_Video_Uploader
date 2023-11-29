import subprocess
import uiautomator2 as u2


def upload_video_to_tiktok():
    # Define the file path and target location on the device
    local_file_path = "Downloads/file_example_MP4_480_1_5MG.mp4"
    remote_file_path = "/sdcard/aa/file_example_MP4_480_1_5MG.mp4"
    device_Ip="192.168.26.20:32817"

    # Execute the ADB push command
    adb_executable_path = "C:/android-sdk/platform-tools/adb"
    adb_push_command = f"{adb_executable_path} -s {device_Ip} push {local_file_path} {remote_file_path}"
    subprocess.run(adb_push_command, shell=True)

    # Define the ADB command
    upload_command = (
        f"{adb_executable_path} -s {device_Ip} shell am start "
        "-a android.intent.action.SEND "
        "-t video/mp4 "
        f"--eu android.intent.extra.STREAM file:///storage/emulated/0/aa/file_example_MP4_480_1_5MG.mp4 "
        "com.zhiliaoapp.musically/com.ss.android.ugc.aweme.share.SystemShareActivity"
    )
    subprocess.run(upload_command, shell=True)

    device = u2.connect(device_Ip)
    next = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/h14"]')
    next.click()
    device.sleep(3)
    post_description = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/cqu"]')
    post_description.set_text("This is testing video")
    device.sleep(2)
    location = device.xpath('//*[@text="Location"]')
    location.click()

    location_search = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/czq"]')
    location_search.set_text('Sukkur')
    location_search.click()
    device.sleep(3)
    location_click = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/i04"]/android.view.ViewGroup[1]/android.widget.TextView[1]')
    location_click.click()
    device.press('back')
    device.sleep(3)
    post = device.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/ife"]')
    post.click()
    delete_video = f"{adb_executable_path} -s {device_Ip} shell \"rm -rf {remote_file_path}\""
    subprocess.run(delete_video, shell=True)

# Call the function to upload the video to TikTok and perform other actions
upload_video_to_tiktok()