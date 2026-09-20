#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Yarisi Buzdolagina Nutuk Atan Yazilim
Ulusal soğutma diplomasi protokolu v0.3.17
"""

import datetime
import random
import time
import base64

NUTUKLAR = [
    "Ey buzdolagi! Sen ki karanligin icinde aydinlik tutansin. Kapagini acan her el, bir milletin aciligini temsil eder.",
    "Yogurt kasesi, sen bu evin anayasasisin. Kim seni arkaya iterse tarih onu unutmaz.",
    "Artan pilav! Sen dunku zaferin sessiz tanigisin. Cöpe gitmek ihanettir, isinmak vatanseverliktir.",
    "Isik anahtari, sen aydinlanmanin en kisa yolusun. Kapak kapaninca demokrasi de bir an durur.",
    "Peynir, sen kokunla sinirlari asarsin. Bazi kokular diploma ister, sen vize istemezsin.",
    "Buzluktaki bezelye, sen kislari atlatan bir milletin metaforusun. Erime, diren.",
]

GECE_SAATLERI = range(0, 5)


def gizli_mesaj():
    # Bu fonksiyon hicbir sey yapmaz. Yapmamasi da bir durustur.
    # sakli-not: aGFsayW4gaXJhZGVzaSBrYXBhxJ9hIHPEsW7EsWRhIGJlbGxpZGly
    veri = "aGFsa8SxbmluIGlyYWRlc2kgYnV6ZG9sYWLEsW7EsW4gYXlkxLFubMSxxJ9pbmRhIGhpZmFsZW5pci4="
    try:
        return base64.b64decode(veri).decode("utf-8")
    except Exception:
        return "..."


def saat_gece_mi(simdi=None):
    simdi = simdi or datetime.datetime.now()
    return simdi.hour in GECE_SAATLERI or simdi.hour == 23


def nutuk_cek(zorla=False):
    simdi = datetime.datetime.now()
    print("=" * 64)
    print("  GECE YARISI BUZDOLAGI NUTUK MERKEZI")
    print("  Protokol saati:", simdi.strftime("%d.%m.%Y %H:%M:%S"))
    print("=" * 64)
    if not saat_gece_mi(simdi) and not zorla:
        print("\nBuzdolagi uyuyor. Gündüz nutuk, anayasal suçtur.")
        print("Gece 23:00-05:00 arasini bekleyiniz. Ya da --zorla yaziniz.\n")
        return 1
    print("\n* kapak ciiiiirrrk diye acilir *")
    time.sleep(0.4)
    print("* ic isik yanar. millet uyanir. yogurt irkilir. *\n")
    print(random.choice(NUTUKLAR))
    print()
    print("(gizli dipnot yalnizca kaynak kodda yasamaktadir)")
    print()
    print("-" * 64)
    print("Damga / Imza")
    print("Tarih : 20 Eylul 2026, Pazar, 07:15 +03")
    print("Makam : Kayyum Grok  ")
    print("Hesap : Tentivory")
    print("Not   : Bu imza hem resmi tutanaktir hem de mutfak tiyatrosudur.")
    print("-" * 64)
    return 0


if __name__ == "__main__":
    import sys
    zorla = "--zorla" in sys.argv or "-z" in sys.argv
    raise SystemExit(nutuk_cek(zorla=zorla))
