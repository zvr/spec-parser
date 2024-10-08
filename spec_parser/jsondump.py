# saving the model as JSON

# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import jsonpickle


def gen_jsondump(model, outdir, cfg):
    p = Path(outdir) / "jsondump"
    p.mkdir()

    f = p / "model.json"
    f.write_text(jsonpickle.encode(model, indent=2, warn=True))
