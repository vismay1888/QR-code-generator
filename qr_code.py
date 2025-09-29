import qrcode

#Taking upi id as input
upi_id = input("Enter your UPI ID = ")

#upi : //pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining payment url based on upi app
#you can modify url based on payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name%mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name%mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name%mc=1234'

#create qr codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Display the qr code (you may need to install PIL/Pillow Library)ld
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
