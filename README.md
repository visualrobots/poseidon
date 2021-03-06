# [Poseidon](https://sidus-dev.github.io/projects/poseidon/index.html)
A fast, minimal and lightweight browser

### Screenshot

![Alt text](http://m-net.arbornet.org/~sidus/images/gscreenshot_2016-09-09-150033.png "Poseidon on Arch Linux")

### Requirements

* Requires [WebKit](https://webkitgtk.org/) 2.12.3 or higher

### Dependencies

* Arch Linux

`# pacman -S python3 python-gobject python-decorator python-six python-requests python-pillow python-cairo pyopenssl gtk3 gtksourceview3 webkit2gtk`

Optionally:

```
gst-libav: HTML5 H264 videos support
gst-plugins-base: HTML5 OGG videos support
gst-plugins-good: HTML5 H264 and WebM videos support
evince: Embed PDFs support
vte3: Embed terminal support
flashplugin: Adobe Flash Player
icedtea-web: Free web browser plugin to run applets written in Java and an implementation of Java Web Start
```

Full command:

`# pacman -S gst-libav gst-plugins-base gst-plugins-good evince vte3 flashplugin icedtea-web`

* Ubuntu/Mint

`# apt-get install gir1.2-evince-3.0 gir1.2-webkit2-4.0 python3-decorator python3-openssl libgtksourceview-3.0-dev`

Optional: [evince-browser-plugin](http://packages.ubuntu.com/en/yakkety/browser-plugin-evince)

If your WebKit version is too old, upgrade it from [here](https://launchpad.net/~webkit-team/+archive/ubuntu/ppa):

`# add-apt-repository ppa:webkit-team/ppa && apt-get update && apt-get upgrade`

* Fedora

`# dnf install python3-pyOpenSSL.noarch`

* FreeBSD (10.3*)

`# pkg install python3 py34-gobject3 py34-sqlite3 py34-pillow gtksourceview3`

then (ignore the first two lines if you already have pip3 installed):

```
python3.4 -m ensurepip
pip3.4 install --upgrade pip
pip3 install six decorator pyopenssl
rehash
```

[Compile](https://trac.webkit.org/wiki/BuildingGtk) [WebKitGTK](https://webkit.org/getting-the-code/) manually if the one provided by the ports is obsolete, viceversa:

`# pkg install webkit2-gtk3`

### Shortcuts

In the main entry, type:

* `about:plugins` to get a list of loaded plugins
* `about:bookmarks` to open bookmarks tab
* `about:history` to open history tab
* `about:cookies` to open cookies manager tab
* `about:settings` to open settings tab

### Settings

Edit settings directly from `include/settings.py`. `AdKiller`, `Javascript` and other plugins like `Flash` are activable/deactivable with a switch in the browser menu.

### Languages

Available languages:

* English (`en_US`)
* German (`de_DE`)
* Italian (`it_IT`)

### Themes

Any image can become a theme, right click on a image and click `Apply as theme`.

### Evince

If [evince](https://wiki.gnome.org/Apps/Evince) and `evince-browser-plugin` are installed, Poseidon will read PDF's directly in the WebKit2.WebView.

Note: In [Arch Linux](https://www.archlinux.org/) you just need to install `evince` as it's plugin comes together with the package.

### Defcon Mode (aka. Incognito)

If set `True` in `include/settings.py`, Poseidon will disable cache, ignore history and cookies independently from their policies.

### Tor

To use Poseidon with Tor, you need [torsocks](https://github.com/dgoulet/torsocks) or alternatively [proxychains](https://github.com/haad/proxychains).

Once Tor is started, through [arm](https://www.torproject.org/projects/arm.html.en) or the discontinued [vidalia](https://en.wikipedia.org/wiki/Vidalia_(software)), you can launch Poseidon in these ways:

* `$ torsocks(or proxychains) ./poseidon` (default mode)
* `$ torsocks(or proxychains) ./poseidon -i` (defcon mode)

### AdKiller

The switch `AdKiller` can be enabled/disabled via browser menu or permanently disabled in the settings panel.
Since version 0.3.7, AdKiller also blocks pop-ups in a very aggressive way so remember to disable it when needed.

### Code snippets, examples, icons, inspirations, peace to:

* https://gist.github.com/kklimonda/890640 (pybrowser.py)
* https://github.com/kvesteri/validators (validators)
* https://github.com/aperezdc/webkit2gtk-python-webextension-example (WebKit2GTK+ Python WebExtension loader)
* https://www.gnome-look.org/p/1012545/ (Faenza)
* http://www.gnome.org (Adwaita)

### Donations

If you enjoy [Poseidon](https://github.com/sidus-dev/poseidon)
consider to buy me a beer!

`BTC: 1Ki95pCN6drymSUY7sS45MLVDkfiKTC8t9`
