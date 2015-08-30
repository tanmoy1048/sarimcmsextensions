# Overview #

Writing Bangla is now getting easier and easier. And now, with web keyboards writing bangla is more easier. This mod adds a keyboard bar in the bottom of webpage.

# Supported Layouts #

  * **Bijoy**
> > Traditional Bijoy layout in unicode format.
  * **Unijoy**
> > Unijoy layout created by Ekeshey
  * **Probhat**
> > Probhat layout created by Ekeshey

  * **Phonetic**
> > Phonetic bangla layout created by Hasin Haydar

# How to install #
### To install this mod you will need to edit the template of your style/theme. ###
For Example here i demonstrate **_prosilver_** theme.
  1. **Edit _/styles/prosilver/template/overall\_header.html_ of your phpbb,**
> > Add the following lines in `<head>` section,
```
<script type="text/javascript" src="http://sarimcmsextensions.googlecode.com/files/key.js"></script>
<style type="text/css" media="screen">
#keypanel{border-color:none;margin:none;padding:none;left:5px;position:fixed;bottom:0;opacity:0.5;background-color:black;height:35px;width:98%;-moz-border-radius:30px 30px 0 0;-webkit-border-radius:30px 30px 0 0;font-family:SolaimanLipi, 'Siyam Rupali', AponaLohit, Vrinda, sans-serif;}
#keymenu{background-color:#ccffff;overflow:hidden;opacity:0.6;position:fixed;bottom:35px;right:30px;width:80px;-moz-border-radius:30px;-webkit-border-radius:30px;font-family:SolaimanLipi, 'Siyam Rupali', AponaLohit, Vrinda, sans-serif;}
.keyop{display:block;padding:5px;-moz-border-radius:30px;-webkit-border-radius:30px;font-family:SolaimanLipi, 'Siyam Rupali', AponaLohit, Vrinda, sans-serif;font-size:12pt;}
#keysel{position:fixed;bottom:5px;left:80%;color:white;font-family:SolaimanLipi, 'Siyam Rupali', AponaLohit, Vrinda, sans-serif;font-size:13pt;}
</style>
```
  1. **Edit _/styles/prosilver/template/overall\_footer.html_ of your phpbb,**
> > Add the following line after `</body>` tag,
```
<script type="text/javascript" src="http://sarimcmsextensions.googlecode.com/files/preload.js"></script>
```
  1. **Goto _STYLES_ section of your phpbb's _Administration Control Panel_**
  1. **In Left Side Bar Click _Templates_**
  1. **Click _Refresh_ beside your theme name.**

## Congrats!!! You have successfully installed bangla keyboard to your website ##

# How to use #
  1. **Click the _"কিবোর্ডঃ"_ section in the keyboard bar in the bottom of the page.**
  1. **Now click on your favorite bangla layout and start writing bangla**


# THANKS FOR READING and GOOD LUCK #
### Dont forget to comment for any query or suggestion ###