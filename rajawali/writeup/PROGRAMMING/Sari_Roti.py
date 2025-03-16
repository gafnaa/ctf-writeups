#CTFRST
bukan_rahasia = "r%u#$%LDcC:0C_f`0Ccd2r~z=c%N"

# Refrensi
char = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def sari_roti(rahasia):
    """Saya Suka Sari Roti"""

    # putaran
    putaran = 47
    decoded = ""

    # decode
    for c in rahasia:
        index = char.find(c)
        ori = (index + putaran) % len(char)
        decoded = decoded + char[ori]

    print(decoded)


sari_roti(bukan_rahasia)

 
