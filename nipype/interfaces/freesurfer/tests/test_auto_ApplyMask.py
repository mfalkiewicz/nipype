# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import ApplyMask


def test_ApplyMask_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    invert_xfm=dict(argstr='-invert',
    ),
    keep_mask_deletion_edits=dict(argstr='-keep_mask_deletion_edits',
    ),
    mask_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    mask_thresh=dict(argstr='-T %.4f',
    ),
    out_file=dict(argstr='%s',
    hash_files=True,
    keep_extension=True,
    name_source=['in_file'],
    name_template='%s_masked',
    position=-1,
    ),
    subjects_dir=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    transfer=dict(argstr='-transfer %d',
    ),
    use_abs=dict(argstr='-abs',
    ),
    xfm_file=dict(argstr='-xform %s',
    ),
    xfm_source=dict(argstr='-lta_src %s',
    ),
    xfm_target=dict(argstr='-lta_dst %s',
    ),
    )
    inputs = ApplyMask.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ApplyMask_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = ApplyMask.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
