import segno

def create_qrcode():
    qrcode = segno.make("https://docs.google.com/forms/d/e/1FAIpQLSdhZcExx6LSIXxk0ub55mSu-WIh23WYdGG9HY5EZhLDo7P8eA/viewform?usp=sf_link", micro=False)
    qrcode.save("qr_code.png", scale=5)

create_qrcode()