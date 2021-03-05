#import smtplib
#https://code.tutsplus.com/id/tutorials/sending-emails-in-python-with-smtp--cms-29975
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

#email pengirim
pengirim = "denisealdianto2@gmail.com"
password = "qwertyuiop18"

#Input email penerima
#https://www.youtube.com/watch?v=sXjpkcF7rPQ
msg = MIMEMultipart()
list_email = [] 
jumlah = int(input("Jumlah penerima email = "))
for x in range(jumlah) :
    email = input("Masukkan email yang ke - {} = ". format(x+1))
    list_email.append(email)
judul = input("Masukkan Subject = ")

#Input Attechment
#https://www.youtube.com/watch?v=bXRYJEKjqIM
namafile = input("Masukkan nama file dan jenis file yang akan dikirim = ")
attachment = open(namafile,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload ((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; namafile = "+namafile)

msg.attach(part)
#Isi email
msg['From'] = pengirim
msg['To'] = ', '.join(list_email)
msg['Subject'] = judul
msg['Attachment'] = namafile
message = input("Isi pesan = ")
msg.attach(MIMEText(message,'plain'))

#Menyambungkan ke server
#https://www.youtube.com/watch?v=sXjpkcF7rPQ
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
print ("Berhasil Login")

#Proses Mengirim
server.sendmail(pengirim, list_email, msg.as_string())
server.quit()
for i in range(len(list_email)) :
    print ("Email berhasil dikirim ke {}". format(list_email[i]))