#!/usr/bin/python

import os,sys

args = sys.argv[1:]
images = ['search','login','signup','corners_body','corners_main','tab','corners_submenu','overtab','overtab_active']

options = {
    'css':False,
    'files':[]
}

for arg in args:
    if arg == 'css':
        options['css'] = True
    elif arg == 'all':
        options['files'] = images[:]
    elif arg in images:
        options['files'].append(arg)
    else:
        print "Unrecognized option: '%s'" % arg

options['files'] = set(options['files'])

colors = [
  ['yellowgreen', 'yg', 0x6F2F9E, 0x421466, 0x210A33],		#	Std NW purple
  ['blue',        'bl', 0x666666, 0x333333, 0x000000],		#	Dark gray
  ['purple',      'pu', 0x915EBA, 0x6F2F9E, 0x421466],		#	Lighter purple
  ['red',         're', 0x999999, 0x666666, 0x333333],		#	Lighter gray
  ['orange',      'or', 0xC8ADDE, 0x915EBA, 0x6F2F9E],		#	Lighter purple
  ['yellow',      'ye', 0xCCCCCC, 0x999999, 0x666666],		#	Lighter gray
  ['lightgreen',  'lg', 0xE3D3F2, 0xC8ADDE, 0x915EBA],		#	Lighter purple
  ['darkgreen',   'dg', 0xE6E6E6, 0xCCCCCC, 0x999999],		#	Lighter gray
  ['grey',        'gr', 0xD14B56, 0x82151E, 0x000000],		#	Dark Red
  ['black',       'bk', 0x5B57BA, 0x211464, 0x000000]		#	Dark Blue
  ]

if options['css']:
    css = open('build/theme.css','w')

for name,short,fore,back,accent in colors:
    os.system(
        ''.join([
                'cat %s.svg | sed "s/FORE/%06x/;s/BACK/%06x/;s/ACCENT/%06x/" > build/%s_%s.svg;' % (image, fore, back, accent, short, image) +
                #'inkscape -z -f build/%s_%s.svg -e build/%s_%s.png' % (short, image, short, image)
                #'rsvg-convert build/%s_%s.svg -o build/%s_%s.png;' % (short, image, short, image)
                'convert build/%s_%s.svg build/%s_%s.png;' % (short, image, short, image)
            for image in options['files']
        ]))
    if options['css']:
        css.write(
            '\n'.join([
                '/* %s %s #%06x #%06x #%06x */' % (name, short, fore, back, accent),
                '#page.%s .forecolor { color: #%06x; }' % (name, fore),
                '#page.%s .backcolor { color: #%06x; }' % (name, back),
                '#page.%s .accentcolor { color: #%06x; }' % (name, accent),
                '#page.%s #main > .corners div { background-image: url(/media/images/theme/gen/%s_corners_main.png); }' % (name, short),
                '#page.%s #body { background: #%06x; }' % (name, fore),
                '.%s a { color: #%06x; }' % (name, accent), # boosting this with an id reference overrides *every* link on the page
                '#page.%s #body > .corners div { background-image: url(/media/images/theme/gen/%s_corners_body.png); }' % (name, short),
                '#page.%s #search_box { background: #fff url(/media/images/theme/gen/%s_search.png) no-repeat 0% 0% scroll; }' % (name, short),
                '#page.%s #login_submit { background: #fff url(/media/images/theme/gen/%s_login.png) no-repeat 0% 0% scroll; }' % (name, short),
                '#page.%s #login_signup { background: #fff url(/media/images/theme/gen/%s_signup.png) no-repeat 0% 0% scroll; }' % (name, short),
                #'li.%s { background: #fff; background-image: url(/media/images/theme/gen/%s_tab.png); }' % (name, short),
                'li.%s a { background-color: #%06x; background-image: url(/media/images/theme/gen/%s_tab.png); }' % (name, fore, short),
                #'li.%s a { background: #%06x; background-image: url(/media/images/theme/gen/%s_tab.png); }' % (name, fore, short),
                '#page.%s #menu li.%s { margin-left: 0; width: 130px }' % (name, name),
                '#page.%s #submenu { background: #%06x; }' % (name, accent),
                '#page.%s #content_header { background: #%06x; }' % (name, back),
                '#page.%s #content_header > .corners div { background-image: url(/media/images/theme/gen/%s_corners_submenu.png); }' % (name, short),
                #'#page.%s #submenu a { color: #%06x; }' % (name, fore),
                '#page.%s #cross_link .inactive a { background-image: url(/media/images/theme/gen/%s_overtab.png); }' % (name, short),
                '#page.%s #cross_link a { background-image: url(/media/images/theme/gen/%s_overtab_active.png); }' % (name, short),
                '\n'
                ])
            )

if options['css']:
    css.close();