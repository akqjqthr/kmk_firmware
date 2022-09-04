from kb import KMKKeyboard

from kmk.keys import KC, make_key
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()
keyboard.debug_enabled = False
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
keyboard.modules.append(MouseKeys())

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# MOTION = KC.MO(1)

# MT_BSPC = KC.MT(KC.BSPC, KC.MO(1))
MT_BSPC = KC.LT(1, KC.BSPC, prefer_hold=False, tap_interrupted=False, tap_time=120)
MT_SPC = KC.LT(2, KC.SPC, prefer_hold=False, tap_interrupted=False, tap_time=150)

# HOMEROW MODS
GUI_A = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=300)
ALT_S = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=200)
CTL_D = KC.MT(KC.D, KC.LCTRL, prefer_hold=False, tap_interrupted=True, tap_time=200)
SFT_F = KC.MT(KC.F, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=150)
SFT_J = KC.MT(KC.J, KC.LSFT, prefer_hold=True, tap_interrupted=True, tap_time=180)
CTL_K= KC.MT(KC.K, KC.LCTRL, prefer_hold=False, tap_interrupted=False, tap_time=200)
ALT_L = KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=250)


combos = Combos()
keyboard.modules.append(combos)

make_key(
    names=('MYKEY',),
    on_press=lambda: print('I pressed MYKEY'),
)

combos.combos = [
    Chord((KC.N, KC.M), KC.RALT),
    Sequence((KC.MINS, KC.MINS), KC.EQUAL, timeout=200, per_key_timeout=False),
    Sequence((KC.LBRC, KC.LBRC), KC.RBRC, timeout=200, per_key_timeout=False),
    Sequence((KC.SLSH, KC.SLSH), KC.BSLS, timeout=200, per_key_timeout=False),
    # Chord((KC.A, KC.B, KC.C), KC.LALT),
    # Sequence((KC.LEADER, KC.A, KC.B), KC.C),
    # Sequence((KC.E, KC.F) KC.MYKEY, timeout=500, per_key_timeout=False),
]


# TODO Comment one of these on each side
# Left is 0, Right is 1
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT

split = Split(
    split_side=split_side,
    split_type=SplitType.UART,
    split_flip=False,
    data_pin=keyboard.data_pin,
    data_pin2=keyboard.data_pin2,
    use_pio=True,
    debug_enabled=False
)

keyboard.modules.append(split)

#split = Split(split_type=SplitType.UART, split_side=split_side)

#keyboard.modules.append(split)
keyboard.keymap = [
    [  #QWERTY
        KC.GRV,         KC.N1,          KC.N2,          KC.N3,          KC.N4,           KC.N5,                                        KC.N6,          KC.N7,          KC.N8,          KC.N9,          KC.N0,          KC.MINS,\
        KC.LGUI,        KC.Q,           KC.W,           KC.E,           KC.R,            KC.T,                                         KC.Y,           KC.U,           KC.I,           KC.O,           KC.P,           KC.LBRC,\
        KC.LCTL,        GUI_A,          ALT_S,          CTL_D,          SFT_F,           KC.G,                                         KC.H,           SFT_J,          CTL_K,          ALT_L,          KC.SCLN,        KC.QUOT,\
        KC.LSFT,        KC.Z,           KC.X,           KC.C,           KC.V,            KC.B,                                         KC.N,           KC.M,           KC.COMM,        KC.DOT,         KC.SLSH,        KC.RSFT,\
                                        KC.LALT,        KC.ESC,         MT_BSPC,         KC.TAB,         KC.LEFT,       KC.RIGHT,      KC.ENT,         MT_SPC,         KC.DEL,         KC.RIGHT,
    ],
    [  #NAV
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        KC.EQUAL,\
        KC.TAB,         KC.Q,           KC.W,           KC.MB_RMB,      KC.MB_LMB,       KC.PGUP,                                      KC.MW_UP,       _______,        KC.MS_UP,       _______,        _______,        KC.RBRC,\
        KC.LCTL,        KC.LCTRL(KC.A), KC.LALT,        KC.LCTRL,       KC.LSFT,         KC.PGDN,                                      KC.MW_DOWN,     KC.MS_LEFT,     KC.MS_DOWN,     KC.MS_RIGHT,    KC.SCLN,        KC.BSLS,\
        KC.LSFT,        KC.LCTRL(KC.Z), KC.LCTRL(KC.X), KC.LCTRL(KC.C), KC.LCTRL(KC.V),  KC.B,                                         KC.HOME,        KC.LEFT,        KC.DOWN,        KC.UP,          KC.RIGHT,       KC.END,\
                                        _______,        KC.ESC,         KC.DF(0),        KC.TAB,         KC.N5,         KC.N6,         KC.MB_LMB,      KC.MB_RMB,      KC.DEL,         _______,
    ],
    [  #FUN
        _______,        KC.F1,          KC.F2,          KC.F3,          KC.F4,           KC.F5,                                        KC.F6,          KC.F7,          KC.F8,          KC.F9,          KC.F10,         KC.F11,\
        KC.PSCR,        KC.PAUSE,       KC.INSERT,      _______,        _______,         KC.PGUP,                                      _______,        _______,        _______,        _______,        _______,        KC.F12,\
        KC.CAPS,        _______,        _______,        _______,        _______,         KC.PGDN,                                      _______,        _______,        _______,        _______,        _______,        _______,\
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        _______,\
                                        _______,        _______,        KC.BSPC,         _______,       _______,       _______,        _______,        KC.DF(0),       _______,        _______,
    ],
    [  #test
        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,         XXXXXXX,                                      XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,\
        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,         XXXXXXX,                                      XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,\
        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,         XXXXXXX,                                      XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,\
        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,         XXXXXXX,                                      XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,\
                                        XXXXXXX,        XXXXXXX,        XXXXXXX,         XXXXXXX,       XXXXXXX,       XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,        XXXXXXX,
    ],
    [  #test
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        _______,\
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        _______,\
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        _______,\
        _______,        _______,        _______,        _______,        _______,         _______,                                      _______,        _______,        _______,        _______,        _______,        _______,\
                                        _______,        _______,        _______,         _______,       _______,       _______,        _______,        _______,        _______,        _______,
    ]
]

if __name__ == '__main__':
    keyboard.go()

# print("Starting")

# import board

# from kmk.kmk_keyboard import KMKKeyboard
# from kmk.keys import KC
# from kmk.scanners import DiodeOrientation

# keyboard = KMKKeyboard()

# keyboard.col_pins = (board.D5,)    # try D5 on Feather, keeboar
# keyboard.row_pins = (board.D6,)    # try D6 on Feather, keeboar
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

# keyboard.keymap = [
#     [KC.A,]
# ]

# if __name__ == '__main__':
#     keyboard.go()

