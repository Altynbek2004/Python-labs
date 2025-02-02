import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def spoofing_simulyatsiyasy():
    # Жіберуші және алушы (тек мысал үшін жалған мекенжайлар)
    zhiberushi = "hacker@example.com"
    alushy = "kurban@example.com"

    # Электрондық поштаның тақырыптарын жасау (бұзу үшін)
    tema = "Маңызды: Сіздің аккаунтыңыз бұзылды"
    jalghan_zhiberushi = "support@bank.kz"  # Жалған жіберуші мекенжайы
    jalghan_zhauap_mekenjaiy = "fake-support@bank.kz"  # Жалған жауап мекенжайы

    # Электрондық поштаның мазмұны
    mazmuny = """
    Құрметті тұтынушы,

    Сіздің аккаунтыңызда күмәнді әрекет анықталды. Аккаунтыңызды қауіпсіз ету үшін төмендегі сілтемеге өтіңіз:

    http://fake-bank-login.kz

    Егер бұл әрекетті орындамасаңыз, аккаунтыңыз бұғатталуы мүмкін.

    Құрметпен,
    Жалған банк қолдау қызметі
    """

    # Электрондық пошта хабарламасын құру
    hat = MIMEMultipart()
    hat['From'] = jalghan_zhiberushi
    hat['To'] = alushy
    hat['Subject'] = tema
    hat['Reply-To'] = jalghan_zhauap_mekenjaiy  # Жалған жауап мекенжайы

    # Электрондық поштаның мәтінін тіркеу
    hat.attach(MIMEText(mazmuny, 'plain'))

    # SMTP серверінің параметрлері (бұл жерде хат жіберілмейді)
    smtp_server = "smtp.example.com"  # SMTP сервері (мысал үшін)
    smtp_port = 587  # SMTP порты
    smtp_user = "username"  # Логин (мысал үшін)
    smtp_password = "password"  # Құпиясөз (мысал үшін)

    # Хат жіберу процесін модельдеу
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Қауіпсіз байланыс үшін TLS қосу
        server.login(smtp_user, smtp_password)  # Серверге қосылу
        server.sendmail(zhiberushi, alushy, hat.as_string())  # Хатты жіберу
        server.quit()  # Байланысты жабу
        print("Жалған хат сәтті жіберілді (симуляция).")
    except Exception as e:
        print(f"Қате: {e}")


if __name__ == "__main__":
    spoofing_simulyatsiyasy()
