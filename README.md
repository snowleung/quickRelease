###HOW TO USE

1. modify index.py, set your own app file name and bundle id at AutoBuild(), just like this :

		APPS = AutoBuild([('jinziqi.ipa','home.jinziqi'), ('imagesC.ipa', 'home.ImagesC')])
	
2. modify core/appconf.py, set self.local_ip to your server ip address, just like this

		self.local_ip = '192.168.11.222'
	
3. copy your app file to QucikRelease/static/client/, and let the file name match 1.

4. run this command:

		sudo python index.py 80
		
5. use safari to visit http://your_ip/ than select what you need to install.

6. done

