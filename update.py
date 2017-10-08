from string import Template
import os

HEADER = \
"""#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "python3 update.py"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#"""

CYG_MIRROR = "http://mirror.pkill.info/cygwin/"

variants = {
    "windowsservercore": {
        "name": "windowsservercore",
        "archs": ["x86_64", "x86"],
    },
    "nanoserver": {
        "name": "nanoserver",
        "archs": ["x86_64"],
    },
}

archs = {
    "x86_64": {
        "name": "x86_64",
        "surfix": "64",
    },
    "x86": {
        "name": "x86",
        "surfix": "",
    },
}

for _, variant in variants.items():
    for arch in [archs[arch] for arch in variant["archs"]]:
        with open("Dockerfile-{}.template".format(variant["name"]), "r") as tmpl_file:
            tmpl = Template(tmpl_file.read())
            dockerfile_path = os.path.join(variant["name"], arch["name"], "Dockerfile")
            os.makedirs(os.path.dirname(dockerfile_path), exist_ok=True)
            with open(dockerfile_path, "w") as out_file:
                out_file.write(tmpl.safe_substitute(
                    HEADER=HEADER,
                    CYG_MIRROR=CYG_MIRROR,
                    CYG_ROOT="C:/cygwin{}".format(arch["surfix"]),
                    ARCH=arch["name"],
                    ARCH_SURFIX=arch["surfix"],
                ))
