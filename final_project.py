#Library & Modul
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
jumlah = int(input("Jumlah penerima email = "))
for x in range(jumlah) :
    email = input("Masukkan email yang ke - {} = ". format(x+1))
    f = open("list_penerima.txt","a")
    f.write (email +"\n")
f.close()

penerima =[]
for i in range(jumlah) :
    penerima_file = open("list_penerima.txt","r")
    penerima_baca = penerima_file.readlines()
    penerima_email = penerima_baca[i-1] .strip()
    penerima.append(penerima_email)
    i = i+1
penerima_file.close()

#Isi email
judul = input("Masukkan Subject = ")
msg['From'] = pengirim
msg['To'] = ', '.join(penerima)
msg['Subject'] = judul
message = input("Isi pesan = ")
msg.attach(MIMEText(message,'plain'))

#Input Attechment
#https://www.youtube.com/watch?v=bXRYJEKjqIM
namafile = input("Masukkan nama file dan jenis file yang akan dikirim = ")
attachment = open(namafile,'rb')
part = MIMEBase('application','octet-stream')
part.set_payload ((attachment).read())
encoders.encode_base64(part)
part.add_header("Content-Disposition","attachment; filename = "+namafile)
msg.attach(part)
msg['Attachment'] = namafile

#Menyambungkan ke server
#https://www.youtube.com/watch?v=sXjpkcF7rPQ
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(msg['From'], password)
print ("Berhasil Login")

#Proses Mengirim
server.sendmail(pengirim, penerima, msg.as_string())
server.quit()
for i in range(len(penerima)) :
    print ("Email berhasil dikirim ke {}". format(penerima[i]))
import os
os.remove("list_penerima.txt")