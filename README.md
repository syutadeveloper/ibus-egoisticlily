# ibus-egoisticlily
This project join Input Method IBus and kanakanji converter EgoisticLily.<br>
Caution: State is sample. Do not production use.

# Requirement
* IBus
* [EgoisticLilyPy][1]
* autotools
* python3

# Install
## build
    run command below.
    1. autoreconf
    2. ./configure --with-egoisticlily-model=<<egoisticlily-model path>> --datadir=<<data dir>>
    3. make
    4. sudo make install
    * <<egoisticlily-madel path>> path to EgoisticLily Model path. this sould be abs path.
    * <<data dir>> ibus and glib-2.0 parent path. In openSUSE it is /usr/share. Default is /usr/local/share.

## Use
Restart ibus. and add [EgoisticLily] in [設定] - [入力メソッド] - [追加] - [日本語].<br>
Then [日本語 - EgoisticLily] is shown in list of IBus. Select it.<br>

## Convert
Select [Input mode] - [Hiragana].<br>
Input any key and press [SPACE].

[1]:https://github.com/E-Lily/EgoisticLilyPy
