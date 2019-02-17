import time
import xbmc
import os
import xbmcgui
import urllib2
import webbrowser


def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
		function4,
		function5,
		function6,
		function7,
		function8,
		function9,
		function10,
		function11,
		function12,
		function13,
		function14,
		function15,
		function16,
		function17,
		function18
        )
        
    call = dialog.select('[COLORwhite]Pairing, ajuda, contato, Youtube[/COLOR]', [
	'[COLORwhite]  >>> [B]Pairing Sites[/B] <<<[/COLOR]',#1=0
	'[COLORlime]  - [B]Flashx.tv[/B][/COLOR] [COLORwhite](Login/Pair)[/COLOR]',#2 
	'[COLORlime]  - [B]Openload.co[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#3 
	'[COLORlime]  - [B]Streamango.com[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#4	
    '[COLORlime]  - [B]TheVideo.me[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#5
    '[COLORlime]  - [B]VidUp.me[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#6
	'[COLORlime]  - [B]vShare.eu[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#7
	'[COLORwhite]  >>> [B]Real Debrid[/B] <<<[/COLOR]',#8=0
	'[COLORblue]  - [B]Real Debrid[/B][/COLOR] [COLORwhite](Login)[/COLOR]',#9
	'[COLORblue]  - [B]Url Resolver[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#10
    '[COLORblue]  - [B]Resolve Url[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#11
    '[COLORwhite]  >>> [B]TRAKT[/B] <<<[/COLOR]',#12=0
    '[COLORred]  - [B]Trakt[/B][/COLOR] [COLORwhite](Login)[/COLOR]',#13
    '[COLORred]  - [B]Trakt[/B][/COLOR] [COLORwhite](Pair)[/COLOR]',#14
    '[COLORwhite]  >>> [B]Support, Youtube, donation[/B] <<<[/COLOR]',#15=0
	'[COLORaqua]  - [B]MilhanoSupport[/B][/COLOR] [COLORwhite]@ FB[/COLOR]',#16
	'[COLORwhite]  - [B]You[/B][/COLOR][COLORred][B]Tube[/B][/COLOR] [COLORwhite]Canal[/COLOR]',#17
	'[COLORblue]  - paypal.me/joaomilhano[/COLOR]',])#18
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-18]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def function1(): 0

def function2():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://flashx.tv/pair' ) )
    else:
        opensite = webbrowser . open('https://flashx.tv/pair')

def function3():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://olpair.com' ) )
    else:
        opensite = webbrowser . open('https://olpair.com')

def function4():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://streamango.com/pair' ) )
    else:
        opensite = webbrowser . open('https://streamango.com/pair')

def function5():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')
        
def function6():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://vidup.me/pair' ) )
    else:
        opensite = webbrowser . open('https://vidup.me/pair')
		
def function7():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://vshare.eu/pair' ) )
    else:
        opensite = webbrowser . open('http://vshare.eu/pair')		

def function8(): 0			
	
def function9():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://real-debrid.com' ) )
    else:
        opensite = webbrowser . open('https://real-debrid.com/')
		
def function10():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://real-debrid.com/device' ) )
    else:
        opensite = webbrowser . open('https://real-debrid.com/device')

def function11():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://real-debrid.com/device' ) )
    else:
        opensite = webbrowser . open('https://real-debrid.com/device')

def function12(): 0

def function13():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://trakt.tv/auth/signin' ) )
    else:
        opensite = webbrowser . open('https://trakt.tv/auth/signin')			
 
def function14():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://trakt.tv/activate' ) )
    else:
        opensite = webbrowser . open('https://trakt.tv/activate')
		
def function15(): 0		

def function16():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.facebook.com/joaomilhanofernandes' ) )
    else:
        opensite = webbrowser . open('https://www.facebook.com/joaomilhanofernandes')

def function17():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.youtube.com/user/j2mf4' ) )
    else:
        opensite = webbrowser . open('https://www.youtube.com/user/j2mf4')		

def function18():
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'paypal.me/joaomilhano' ) )
    else:
        opensite = webbrowser . open('paypal.me/joaomilhano')	
		
menuoptions()